#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lunaro AI Engine
Auto-learning, grammar correction, personality adaptation
"""

import json
import os
import random
import re
from datetime import datetime
from collections import defaultdict, Counter

class ConversationalAI:
    def __init__(self):
        self.learning_file = 'ai_learning.json'
        self.responses_file = 'ai_responses.json'
        
        # Firebase config (EDIT THIS!)
        self._firebase_config = {
            'database_url': "https://YOUR-PROJECT.firebaseio.com",
            'api_key': "YOUR_API_KEY",
            'project_id': "YOUR_PROJECT_ID"
        }
        
        # Load learning data
        self.load_learning_data()
        
        # Grammar patterns for correction
        self.grammar_rules = {
            r'\bi\b': 'I',
            r'\bim\b': "I'm",
            r'\bur\b': 'your',
            r'\bu\b': 'you',
            r'\br\b': 'are',
            r'\bthx\b': 'thanks',
            r'\bpls\b': 'please',
            r'\bbc\b': 'because',
            r'\bcuz\b': 'because',
        }
        
        # Personality traits learned from user
        self.user_personalities = {}
        
        # Word associations
        self.word_associations = defaultdict(Counter)
        
        # Response patterns
        self.response_patterns = {
            'greeting': ['hey', 'hi', 'hello', 'sup', 'yo', 'wassup'],
            'farewell': ['bye', 'goodbye', 'see you', 'later', 'cya'],
            'thanks': ['thanks', 'thank you', 'thx', 'tysm'],
            'question': ['what', 'when', 'where', 'why', 'how', 'who'],
            'positive': ['good', 'great', 'awesome', 'nice', 'cool', 'love'],
            'negative': ['bad', 'terrible', 'hate', 'sucks', 'awful'],
        }
        
        # Base responses
        self.base_responses = {
            'greeting': [
                "Hey! How's it going? 😊",
                "Hi there! What's up?",
                "Hello! How can I help you today?",
                "Hey! Good to see you! 👋",
            ],
            'farewell': [
                "See you later! 👋",
                "Bye! Have a great day!",
                "Catch you later! 😊",
                "Take care! See you soon!",
            ],
            'thanks': [
                "You're welcome! 😊",
                "No problem! Happy to help!",
                "Anytime! 🙌",
                "Glad I could help!",
            ],
            'positive': [
                "That's awesome! 🎉",
                "Great to hear! 😄",
                "Love the positive vibes! ✨",
                "That's really cool! 👍",
            ],
            'negative': [
                "I'm sorry to hear that 😔",
                "That's rough... Want to talk about it?",
                "Aw man, that sucks 😕",
                "I hope things get better soon!",
            ],
            'question': [
                "That's a good question! Let me think...",
                "Hmm, interesting question!",
                "Great question! 🤔",
            ],
            'default': [
                "Tell me more about that!",
                "Interesting! Go on...",
                "I see! What else?",
                "That's cool! 😊",
                "I hear you!",
                "Got it! What do you think?",
            ]
        }
    
    def load_learning_data(self):
        """Load AI learning data"""
        if os.path.exists(self.learning_file):
            try:
                with open(self.learning_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.learned_patterns = data.get('patterns', {})
                    self.learned_responses = data.get('responses', {})
                    self.conversation_history = data.get('history', [])
            except:
                self.learned_patterns = {}
                self.learned_responses = {}
                self.conversation_history = []
        else:
            self.learned_patterns = {}
            self.learned_responses = {}
            self.conversation_history = []
    
    def save_learning_data(self):
        """Save AI learning data"""
        try:
            data = {
                'patterns': self.learned_patterns,
                'responses': self.learned_responses,
                'history': self.conversation_history[-1000:],  # Keep last 1000
                'last_updated': datetime.now().isoformat()
            }
            with open(self.learning_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving learning data: {e}")
    
    def correct_grammar(self, text):
        """Basic grammar correction"""
        corrected = text
        for pattern, replacement in self.grammar_rules.items():
            corrected = re.sub(pattern, replacement, corrected, flags=re.IGNORECASE)
        
        # Capitalize first letter
        if corrected:
            corrected = corrected[0].upper() + corrected[1:]
        
        return corrected
    
    def detect_intent(self, message):
        """Detect user intent from message"""
        message_lower = message.lower()
        
        for intent, keywords in self.response_patterns.items():
            if any(keyword in message_lower for keyword in keywords):
                return intent
        
        return 'default'
    
    def learn_from_message(self, user_message, username):
        """Auto-learn from user message"""
        # Store conversation
        self.conversation_history.append({
            'user': username,
            'message': user_message,
            'timestamp': datetime.now().isoformat()
        })
        
        # Learn word associations
        words = user_message.lower().split()
        for i, word in enumerate(words):
            if i < len(words) - 1:
                next_word = words[i + 1]
                self.word_associations[word][next_word] += 1
        
        # Learn patterns
        intent = self.detect_intent(user_message)
        if intent not in self.learned_patterns:
            self.learned_patterns[intent] = []
        
        if user_message not in self.learned_patterns[intent]:
            self.learned_patterns[intent].append(user_message)
        
        # Learn user personality
        if username not in self.user_personalities:
            self.user_personalities[username] = {
                'message_count': 0,
                'avg_length': 0,
                'common_words': Counter(),
                'tone': 'neutral'
            }
        
        profile = self.user_personalities[username]
        profile['message_count'] += 1
        profile['avg_length'] = (
            (profile['avg_length'] * (profile['message_count'] - 1) + len(user_message))
            / profile['message_count']
        )
        
        # Update common words
        for word in words:
            if len(word) > 3:  # Only meaningful words
                profile['common_words'][word] += 1
        
        # Detect tone
        positive_count = sum(1 for word in words if word in self.response_patterns['positive'])
        negative_count = sum(1 for word in words if word in self.response_patterns['negative'])
        
        if positive_count > negative_count:
            profile['tone'] = 'positive'
        elif negative_count > positive_count:
            profile['tone'] = 'negative'
        
        # Save learning
        self.save_learning_data()
        
        # Try to sync to Firebase (silently fail if not configured)
        self.sync_to_firebase(user_message, username)
    
    def sync_to_firebase(self, message, username):
        """Sync data to Firebase (optional)"""
        try:
            # This is a placeholder - actual Firebase implementation
            # would use firebase-admin or requests
            # For now, just save to local file
            firebase_data_file = 'firebase_sync.json'
            
            if os.path.exists(firebase_data_file):
                with open(firebase_data_file, 'r', encoding='utf-8') as f:
                    firebase_data = json.load(f)
            else:
                firebase_data = {'conversations': []}
            
            firebase_data['conversations'].append({
                'message': message,
                'timestamp': datetime.now().isoformat(),
                'synced': False
            })
            
            with open(firebase_data_file, 'w', encoding='utf-8') as f:
                json.dump(firebase_data, f, indent=2)
        except:
            pass  # Silently fail
    
    def generate_response(self, user_message, username):
        """Generate intelligent response based on learning"""
        # Detect intent
        intent = self.detect_intent(user_message)
        
        # Check if we have learned responses for this intent
        if intent in self.learned_responses and self.learned_responses[intent]:
            response = random.choice(self.learned_responses[intent])
        elif intent in self.base_responses:
            response = random.choice(self.base_responses[intent])
        else:
            response = random.choice(self.base_responses['default'])
        
        # Personalize based on user personality
        if username in self.user_personalities:
            profile = self.user_personalities[username]
            
            # Match user's tone
            if profile['tone'] == 'positive' and random.random() > 0.5:
                response += " 😊"
            elif profile['tone'] == 'negative':
                response = response.replace("!", ".").replace("😊", "")
        
        return response
    
    def get_response(self, user_message, username):
        """Main method to get AI response"""
        # Learn from message (auto-learning)
        self.learn_from_message(user_message, username)
        
        # Generate response
        response = self.generate_response(user_message, username)
        
        return response
    
    def train_manually(self, pattern, response):
        """Manual training method (for admin use)"""
        intent = self.detect_intent(pattern)
        
        if intent not in self.learned_responses:
            self.learned_responses[intent] = []
        
        if response not in self.learned_responses[intent]:
            self.learned_responses[intent].append(response)
        
        self.save_learning_data()
        return True
    
    def get_stats(self):
        """Get AI statistics"""
        return {
            'total_conversations': len(self.conversation_history),
            'learned_patterns': sum(len(p) for p in self.learned_patterns.values()),
            'learned_responses': sum(len(r) for r in self.learned_responses.values()),
            'users_tracked': len(self.user_personalities),
            'word_associations': len(self.word_associations)
        }


if __name__ == '__main__':
    # Test the AI
    ai = ConversationalAI()
    
    print("🤖 AI Test Mode")
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        
        response = ai.get_response(user_input, "TestUser")
        print(f"AI: {response}\n")
    
    print(f"\nStats: {ai.get_stats()}")
