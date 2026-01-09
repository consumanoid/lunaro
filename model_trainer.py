#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Model Trainer
Manual training system with Firebase integration
"""

import json
import os
from datetime import datetime
from chat_ai import ConversationalAI

class ModelTrainer:
    def __init__(self):
        self.ai = ConversationalAI()
        self.training_log_file = 'training_log.json'
        self.load_training_log()
    
    def load_training_log(self):
        """Load training history"""
        if os.path.exists(self.training_log_file):
            try:
                with open(self.training_log_file, 'r', encoding='utf-8') as f:
                    self.training_log = json.load(f)
            except:
                self.training_log = []
        else:
            self.training_log = []
    
    def save_training_log(self):
        """Save training history"""
        try:
            with open(self.training_log_file, 'w', encoding='utf-8') as f:
                json.dump(self.training_log, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"❌ Error saving training log: {e}")
    
    def train_pattern(self, pattern, response):
        """Train AI with new pattern-response pair"""
        print(f"\n🧠 Training AI...")
        print(f"   Pattern: {pattern}")
        print(f"   Response: {response}")
        
        success = self.ai.train_manually(pattern, response)
        
        if success:
            # Log training
            log_entry = {
                'pattern': pattern,
                'response': response,
                'timestamp': datetime.now().isoformat(),
                'status': 'success'
            }
            self.training_log.append(log_entry)
            self.save_training_log()
            
            print("✅ Training successful!")
            return True
        else:
            print("❌ Training failed!")
            return False
    
    def train_from_file(self, filename):
        """Train from JSON file containing pattern-response pairs"""
        print(f"\n📂 Loading training data from {filename}...")
        
        if not os.path.exists(filename):
            print(f"❌ File not found: {filename}")
            return False
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                training_data = json.load(f)
            
            if not isinstance(training_data, list):
                print("❌ Invalid format! Expected list of objects with 'pattern' and 'response' keys")
                return False
            
            total = len(training_data)
            success_count = 0
            
            print(f"📊 Found {total} training examples\n")
            
            for i, item in enumerate(training_data, 1):
                pattern = item.get('pattern', '')
                response = item.get('response', '')
                
                if not pattern or not response:
                    print(f"⚠️  Skipping item {i}: Missing pattern or response")
                    continue
                
                print(f"[{i}/{total}] Training...", end=' ')
                
                if self.ai.train_manually(pattern, response):
                    success_count += 1
                    print("✅")
                else:
                    print("❌")
            
            # Log batch training
            log_entry = {
                'type': 'batch_training',
                'file': filename,
                'total': total,
                'successful': success_count,
                'timestamp': datetime.now().isoformat()
            }
            self.training_log.append(log_entry)
            self.save_training_log()
            
            print(f"\n✅ Batch training complete!")
            print(f"   Successful: {success_count}/{total}")
            print(f"   Failed: {total - success_count}/{total}")
            
            return True
            
        except json.JSONDecodeError:
            print("❌ Invalid JSON format!")
            return False
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def show_stats(self):
        """Show AI and training statistics"""
        print("\n" + "="*50)
        print("📊 AI STATISTICS")
        print("="*50)
        
        ai_stats = self.ai.get_stats()
        
        print(f"\n🤖 AI Learning:")
        print(f"   • Total conversations: {ai_stats['total_conversations']}")
        print(f"   • Learned patterns: {ai_stats['learned_patterns']}")
        print(f"   • Learned responses: {ai_stats['learned_responses']}")
        print(f"   • Users tracked: {ai_stats['users_tracked']}")
        print(f"   • Word associations: {ai_stats['word_associations']}")
        
        print(f"\n🎓 Training History:")
        print(f"   • Total training sessions: {len(self.training_log)}")
        
        if self.training_log:
            last_training = self.training_log[-1]
            print(f"   • Last training: {last_training.get('timestamp', 'Unknown')}")
        
        print("\n" + "="*50)
    
    def export_learning_data(self, output_file='exported_ai_data.json'):
        """Export all learning data to file"""
        print(f"\n💾 Exporting learning data to {output_file}...")
        
        try:
            export_data = {
                'ai_stats': self.ai.get_stats(),
                'learned_patterns': self.ai.learned_patterns,
                'learned_responses': self.ai.learned_responses,
                'training_log': self.training_log,
                'export_timestamp': datetime.now().isoformat()
            }
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Export successful! Saved to {output_file}")
            return True
            
        except Exception as e:
            print(f"❌ Export failed: {e}")
            return False
    
    def sync_with_firebase(self):
        """Sync learning data with Firebase"""
        print("\n☁️  Syncing with Firebase...")
        print("⚠️  Note: Firebase config must be set in chat_ai.py")
        
        # This is a placeholder for actual Firebase sync
        # In production, this would use firebase-admin SDK
        try:
            # Simulate sync
            firebase_sync_file = 'firebase_sync.json'
            
            sync_data = {
                'ai_learning': self.ai.learned_patterns,
                'responses': self.ai.learned_responses,
                'last_sync': datetime.now().isoformat(),
                'status': 'pending'
            }
            
            with open(firebase_sync_file, 'w', encoding='utf-8') as f:
                json.dump(sync_data, f, indent=2)
            
            print("✅ Data prepared for Firebase sync!")
            print(f"   File: {firebase_sync_file}")
            print("\n💡 To complete sync:")
            print("   1. Configure Firebase in chat_ai.py")
            print("   2. Install: pip install firebase-admin")
            print("   3. Upload this file to your Firebase database")
            
            return True
            
        except Exception as e:
            print(f"❌ Sync preparation failed: {e}")
            return False
    
    def interactive_training(self):
        """Interactive training mode"""
        print("\n" + "="*50)
        print("🎓 INTERACTIVE TRAINING MODE")
        print("="*50)
        print("\nTeach the AI new responses!")
        print("Type 'done' when finished\n")
        
        training_count = 0
        
        while True:
            print("-" * 50)
            pattern = input("Enter user pattern (or 'done'): ").strip()
            
            if pattern.lower() == 'done':
                break
            
            if not pattern:
                print("⚠️  Pattern cannot be empty!")
                continue
            
            response = input("Enter AI response: ").strip()
            
            if not response:
                print("⚠️  Response cannot be empty!")
                continue
            
            if self.train_pattern(pattern, response):
                training_count += 1
        
        print(f"\n✅ Training session complete!")
        print(f"   Trained {training_count} new patterns")
    
    def create_training_template(self, filename='training_template.json'):
        """Create a template file for batch training"""
        template = [
            {
                "pattern": "what's your name",
                "response": "I'm your AI assistant! You can call me whatever you'd like 😊"
            },
            {
                "pattern": "how are you",
                "response": "I'm doing great! Thanks for asking! How are you?"
            },
            {
                "pattern": "tell me a joke",
                "response": "Why don't scientists trust atoms? Because they make up everything! 😄"
            }
        ]
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(template, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Created training template: {filename}")
            print("\n💡 Edit this file with your own patterns and responses,")
            print("   then use 'train_from_file' to load them!")
            return True
            
        except Exception as e:
            print(f"❌ Failed to create template: {e}")
            return False


def main():
    """Main training interface"""
    trainer = ModelTrainer()
    
    print("\n" + "="*50)
    print("🤖 AI MODEL TRAINER")
    print("="*50)
    
    while True:
        print("\n📋 Options:")
        print("  1. Interactive training")
        print("  2. Train from file")
        print("  3. Show statistics")
        print("  4. Export learning data")
        print("  5. Sync with Firebase")
        print("  6. Create training template")
        print("  7. Exit")
        
        choice = input("\nEnter choice (1-7): ").strip()
        
        if choice == '1':
            trainer.interactive_training()
        
        elif choice == '2':
            filename = input("Enter training file path: ").strip()
            trainer.train_from_file(filename)
        
        elif choice == '3':
            trainer.show_stats()
        
        elif choice == '4':
            output = input("Enter output filename (or press Enter for default): ").strip()
            if output:
                trainer.export_learning_data(output)
            else:
                trainer.export_learning_data()
        
        elif choice == '5':
            trainer.sync_with_firebase()
        
        elif choice == '6':
            filename = input("Enter template filename (or press Enter for default): ").strip()
            if filename:
                trainer.create_training_template(filename)
            else:
                trainer.create_training_template()
        
        elif choice == '7':
            print("\n👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-7")


if __name__ == '__main__':
    main()
