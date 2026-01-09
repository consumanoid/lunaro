#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lunaro AI App - Main Interface
Complete login system, themes, chat memory, and admin panel
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image as KivyImage
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.animation import Animation
import json
import os
from datetime import datetime
from chat_ai import ConversationalAI

# Theme definitions with emojis
THEMES = {
    'Black': {
        'bg': (0, 0, 0, 1),
        'text': (1, 1, 1, 1),
        'input_bg': (0.1, 0.1, 0.1, 1),
        'button': (0.2, 0.2, 0.2, 1),
        'user_bubble': (0.15, 0.15, 0.15, 1),
        'ai_bubble': (0.25, 0.25, 0.25, 1),
        'emoji': '⬛'
    },
    'Dark': {
        'bg': (0.15, 0.15, 0.15, 1),
        'text': (0.9, 0.9, 0.9, 1),
        'input_bg': (0.2, 0.2, 0.2, 1),
        'button': (0.3, 0.3, 0.3, 1),
        'user_bubble': (0.25, 0.25, 0.25, 1),
        'ai_bubble': (0.35, 0.35, 0.35, 1),
        'emoji': '🌙'
    },
    'Blossom': {
        'bg': (1, 0.9, 0.95, 1),
        'text': (0.4, 0.2, 0.3, 1),
        'input_bg': (1, 0.85, 0.9, 1),
        'button': (1, 0.7, 0.85, 1),
        'user_bubble': (1, 0.8, 0.9, 1),
        'ai_bubble': (0.95, 0.75, 0.85, 1),
        'emoji': '🌸'
    },
    'Code': {
        'bg': (0, 0.1, 0, 1),
        'text': (0, 1, 0, 1),
        'input_bg': (0, 0.15, 0, 1),
        'button': (0, 0.2, 0, 1),
        'user_bubble': (0, 0.2, 0, 1),
        'ai_bubble': (0, 0.3, 0, 1),
        'emoji': '💻'
    },
    'Ocean': {
        'bg': (0, 0.2, 0.4, 1),
        'text': (0.8, 0.95, 1, 1),
        'input_bg': (0, 0.25, 0.45, 1),
        'button': (0, 0.3, 0.5, 1),
        'user_bubble': (0, 0.3, 0.5, 1),
        'ai_bubble': (0, 0.4, 0.6, 1),
        'emoji': '🌊'
    },
    'Sunset': {
        'bg': (0.2, 0.1, 0.3, 1),
        'text': (1, 0.9, 0.7, 1),
        'input_bg': (0.25, 0.15, 0.35, 1),
        'button': (0.3, 0.2, 0.4, 1),
        'user_bubble': (0.4, 0.2, 0.3, 1),
        'ai_bubble': (0.5, 0.3, 0.4, 1),
        'emoji': '🌅'
    }
}

class ChatApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_user = None
        self.current_theme = 'Black'
        self.ai = ConversationalAI()
        self.users_file = 'users.json'
        self.admin_password = 'madebyconsumanoid:3'
        self.chat_history = []
        self.max_history = 100
        
    def build(self):
        self.title = '🌙 Lunaro AI'
        self.load_users()
        # Show splash screen first
        return self.create_splash_screen()
    
    def create_splash_screen(self):
        """Create splash screen with Lunaro branding"""
        layout = FloatLayout()
        
        # Dark blue background
        with layout.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(0.1, 0.16, 0.25, 1)  # Dark blue
            self.splash_bg = Rectangle(size=Window.size, pos=(0, 0))
        
        # Center container
        center_box = BoxLayout(
            orientation='vertical',
            size_hint=(None, None),
            size=(400, 300),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            spacing=20
        )
        
        # Moon + UNARO text (moon replaces L)
        title_box = BoxLayout(orientation='horizontal', size_hint_y=0.4, spacing=5)
        title_box.add_widget(Label(size_hint_x=0.1))  # Spacer
        
        # Moon emoji/icon
        moon_label = Label(
            text='🌙',
            font_size='80sp',
            size_hint_x=0.2,
            color=(0.62, 0.72, 0.94, 1)
        )
        
        # UNARO text (without L)
        text_label = Label(
            text='UNARO',
            font_size='80sp',
            size_hint_x=0.7,
            bold=True,
            color=(0.49, 0.72, 0.94, 1)
        )
        
        title_box.add_widget(moon_label)
        title_box.add_widget(text_label)
        title_box.add_widget(Label(size_hint_x=0.1))  # Spacer
        
        # Tagline (no AI subtitle)
        tagline = Label(
            text='Where Intelligence Meets Innovation',
            font_size='16sp',
            size_hint_y=0.2,
            color=(0.43, 0.69, 1, 0.7)
        )
        
        # Loading animation
        loading_label = Label(
            text='• • •',
            font_size='24sp',
            size_hint_y=0.1,
            color=(0.29, 1, 1, 1)
        )
        
        # Animate loading dots
        def animate_dots(dt):
            current = loading_label.text
            if current == '•':
                loading_label.text = '• •'
            elif current == '• •':
                loading_label.text = '• • •'
            else:
                loading_label.text = '•'
        
        Clock.schedule_interval(animate_dots, 0.5)
        
        center_box.add_widget(title_box)
        center_box.add_widget(tagline)
        center_box.add_widget(Label(size_hint_y=0.2))  # Spacer
        center_box.add_widget(loading_label)
        
        layout.add_widget(center_box)
        
        # Transition to login after 3 seconds
        Clock.schedule_once(self.transition_to_login, 3)
        
        return layout
    
    def transition_to_login(self, dt):
        """Transition from splash to login screen"""
        self.root.clear_widgets()
        self.root.add_widget(self.create_login_screen())
    
    def load_users(self):
        """Load user data from JSON file"""
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r', encoding='utf-8') as f:
                    self.users_data = json.load(f)
            except:
                self.users_data = {}
        else:
            self.users_data = {}
    
    def save_users(self):
        """Save user data to JSON file"""
        try:
            with open(self.users_file, 'w', encoding='utf-8') as f:
                json.dump(self.users_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving users: {e}")
    
    def create_login_screen(self):
        """Create login interface"""
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        layout.canvas.before.clear()
        
        with layout.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(*THEMES['Black']['bg'])
            self.login_bg = Rectangle(size=layout.size, pos=layout.pos)
        
        layout.bind(size=self._update_login_bg, pos=self._update_login_bg)
        
        # Title
        title = Label(
            text='🌙 Welcome to Lunaro AI',
            font_size='24sp',
            size_hint_y=0.2,
            color=THEMES['Black']['text']
        )
        
        # Instructions
        instructions = Label(
            text='Enter your username to login or create account',
            font_size='14sp',
            size_hint_y=0.1,
            color=THEMES['Black']['text']
        )
        
        # Username input
        self.username_input = TextInput(
            hint_text='Username',
            multiline=False,
            size_hint_y=0.1,
            font_size='18sp',
            background_color=THEMES['Black']['input_bg']
        )
        self.username_input.bind(on_text_validate=self.login)
        
        # Login button
        login_btn = Button(
            text='Login / Create Account',
            size_hint_y=0.1,
            background_color=THEMES['Black']['button'],
            font_size='16sp'
        )
        login_btn.bind(on_press=self.login)
        
        layout.add_widget(Label(size_hint_y=0.2))  # Spacer
        layout.add_widget(title)
        layout.add_widget(instructions)
        layout.add_widget(self.username_input)
        layout.add_widget(login_btn)
        layout.add_widget(Label(size_hint_y=0.3))  # Spacer
        
        return layout
    
    def _update_login_bg(self, instance, value):
        """Update login background"""
        self.login_bg.size = instance.size
        self.login_bg.pos = instance.pos
    
    def login(self, instance):
        """Handle login/account creation"""
        username = self.username_input.text.strip()
        
        if not username:
            self.show_popup('Error', 'Please enter a username!')
            return
        
        self.current_user = username
        
        # Create new user or load existing
        if username not in self.users_data:
            self.users_data[username] = {
                'created': datetime.now().isoformat(),
                'theme': 'Black',
                'chat_history': [],
                'message_count': 0
            }
            self.save_users()
            welcome = True
        else:
            welcome = False
        
        # Load user preferences
        self.current_theme = self.users_data[username].get('theme', 'Black')
        self.chat_history = self.users_data[username].get('chat_history', [])[-10:]  # Load last 10
        
        # Switch to chat screen
        self.root.clear_widgets()
        self.root.add_widget(self.create_chat_screen(welcome))
    
    def create_chat_screen(self, welcome=False):
        """Create main chat interface"""
        layout = BoxLayout(orientation='vertical', padding=5, spacing=5)
        
        # Apply theme background
        with layout.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(*THEMES[self.current_theme]['bg'])
            self.chat_bg = Rectangle(size=layout.size, pos=layout.pos)
        
        layout.bind(size=self._update_chat_bg, pos=self._update_chat_bg)
        
        # Top bar with buttons
        top_bar = BoxLayout(size_hint_y=0.08, spacing=5)
        
        # Theme button
        theme_btn = Button(
            text=f"🎨 {THEMES[self.current_theme]['emoji']}",
            size_hint_x=0.2,
            background_color=THEMES[self.current_theme]['button']
        )
        theme_btn.bind(on_press=self.show_theme_picker)
        
        # Username display
        user_label = Label(
            text=f"👤 {self.current_user}",
            color=THEMES[self.current_theme]['text'],
            size_hint_x=0.6
        )
        
        # Admin button
        admin_btn = Button(
            text='📊',
            size_hint_x=0.1,
            background_color=THEMES[self.current_theme]['button']
        )
        admin_btn.bind(on_press=self.show_admin_login)
        
        # Logout button
        logout_btn = Button(
            text='🚪',
            size_hint_x=0.1,
            background_color=THEMES[self.current_theme]['button']
        )
        logout_btn.bind(on_press=self.logout)
        
        top_bar.add_widget(theme_btn)
        top_bar.add_widget(user_label)
        top_bar.add_widget(admin_btn)
        top_bar.add_widget(logout_btn)
        
        # Chat display area
        self.chat_scroll = ScrollView(size_hint_y=0.82)
        self.chat_layout = GridLayout(cols=1, spacing=10, size_hint_y=None, padding=10)
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))
        self.chat_scroll.add_widget(self.chat_layout)
        
        # Input area
        input_box = BoxLayout(size_hint_y=0.1, spacing=5)
        
        self.message_input = TextInput(
            hint_text='Type your message...',
            multiline=False,
            background_color=THEMES[self.current_theme]['input_bg'],
            foreground_color=THEMES[self.current_theme]['text'],
            size_hint_x=0.85
        )
        self.message_input.bind(on_text_validate=self.send_message)
        
        send_btn = Button(
            text='▶',
            size_hint_x=0.15,
            background_color=THEMES[self.current_theme]['button']
        )
        send_btn.bind(on_press=self.send_message)
        
        input_box.add_widget(self.message_input)
        input_box.add_widget(send_btn)
        
        layout.add_widget(top_bar)
        layout.add_widget(self.chat_scroll)
        layout.add_widget(input_box)
        
        # Load previous messages
        for msg in self.chat_history:
            self.add_message_bubble(msg['sender'], msg['text'], save=False)
        
        # Welcome message
        if welcome:
            self.add_message_bubble('AI', f"Hey {self.current_user}! 👋 I'm Lunaro, your AI assistant. I'll learn from our conversations to help you better!")
        elif self.chat_history:
            self.add_message_bubble('AI', f"Welcome back {self.current_user}! 🌙 I remember our previous chats!")
        
        return layout
    
    def _update_chat_bg(self, instance, value):
        """Update chat background"""
        self.chat_bg.size = instance.size
        self.chat_bg.pos = instance.pos
    
    def add_message_bubble(self, sender, text, save=True):
        """Add message bubble to chat"""
        bubble_layout = BoxLayout(size_hint_y=None, height=40, padding=5)
        
        if sender == 'User':
            # User message (right side)
            bubble_layout.add_widget(Label(size_hint_x=0.2))  # Spacer
            
            bubble = Label(
                text=f"👤 {text}",
                size_hint=(0.8, None),
                height=40,
                color=THEMES[self.current_theme]['text'],
                halign='right',
                valign='middle'
            )
            bubble.bind(size=bubble.setter('text_size'))
            
            with bubble.canvas.before:
                from kivy.graphics import Color, RoundedRectangle
                Color(*THEMES[self.current_theme]['user_bubble'])
                bubble.rect = RoundedRectangle(
                    size=bubble.size,
                    pos=bubble.pos,
                    radius=[10]
                )
            
            bubble.bind(size=lambda i, v: setattr(bubble.rect, 'size', v),
                       pos=lambda i, v: setattr(bubble.rect, 'pos', v))
            
            bubble_layout.add_widget(bubble)
        else:
            # AI message (left side)
            bubble = Label(
                text=f"🤖 {text}",
                size_hint=(0.8, None),
                height=40,
                color=THEMES[self.current_theme]['text'],
                halign='left',
                valign='middle'
            )
            bubble.bind(size=bubble.setter('text_size'))
            
            with bubble.canvas.before:
                from kivy.graphics import Color, RoundedRectangle
                Color(*THEMES[self.current_theme]['ai_bubble'])
                bubble.rect = RoundedRectangle(
                    size=bubble.size,
                    pos=bubble.pos,
                    radius=[10]
                )
            
            bubble.bind(size=lambda i, v: setattr(bubble.rect, 'size', v),
                       pos=lambda i, v: setattr(bubble.rect, 'pos', v))
            
            bubble_layout.add_widget(bubble)
            bubble_layout.add_widget(Label(size_hint_x=0.2))  # Spacer
        
        self.chat_layout.add_widget(bubble_layout)
        
        # Auto-scroll to bottom
        Clock.schedule_once(lambda dt: setattr(self.chat_scroll, 'scroll_y', 0), 0.1)
        
        # Save to history
        if save:
            msg_data = {
                'sender': sender,
                'text': text,
                'timestamp': datetime.now().isoformat()
            }
            self.chat_history.append(msg_data)
            
            # Keep only last 100 messages
            if len(self.chat_history) > self.max_history:
                self.chat_history = self.chat_history[-self.max_history:]
            
            # Save to user data
            self.users_data[self.current_user]['chat_history'] = self.chat_history
            self.users_data[self.current_user]['message_count'] = \
                self.users_data[self.current_user].get('message_count', 0) + 1
            self.save_users()
    
    def send_message(self, instance):
        """Send message and get AI response"""
        user_message = self.message_input.text.strip()
        
        if not user_message:
            return
        
        # Clear input
        self.message_input.text = ''
        
        # Add user message
        self.add_message_bubble('User', user_message)
        
        # Get AI response (auto-learning happens inside)
        ai_response = self.ai.get_response(user_message, self.current_user)
        
        # Add AI response
        self.add_message_bubble('AI', ai_response)
    
    def show_theme_picker(self, instance):
        """Show theme selection popup"""
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        for theme_name, theme_data in THEMES.items():
            btn = Button(
                text=f"{theme_data['emoji']} {theme_name}",
                size_hint_y=None,
                height=50,
                background_color=theme_data['button']
            )
            btn.bind(on_press=lambda x, t=theme_name: self.change_theme(t))
            content.add_widget(btn)
        
        popup = Popup(
            title='🎨 Choose Theme',
            content=content,
            size_hint=(0.8, 0.8)
        )
        
        self.theme_popup = popup
        popup.open()
    
    def change_theme(self, theme_name):
        """Change app theme"""
        self.current_theme = theme_name
        self.users_data[self.current_user]['theme'] = theme_name
        self.save_users()
        
        # Rebuild chat screen
        self.root.clear_widgets()
        self.root.add_widget(self.create_chat_screen())
        
        self.theme_popup.dismiss()
    
    def show_admin_login(self, instance):
        """Show admin login popup"""
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        label = Label(text='🔒 Enter Admin Password:', size_hint_y=0.3)
        
        password_input = TextInput(
            password=True,
            multiline=False,
            size_hint_y=0.2,
            hint_text='Password'
        )
        
        btn_box = BoxLayout(size_hint_y=0.2, spacing=5)
        
        login_btn = Button(text='Login')
        cancel_btn = Button(text='Cancel')
        
        btn_box.add_widget(login_btn)
        btn_box.add_widget(cancel_btn)
        
        content.add_widget(label)
        content.add_widget(password_input)
        content.add_widget(btn_box)
        
        popup = Popup(
            title='Admin Access',
            content=content,
            size_hint=(0.8, 0.4)
        )
        
        login_btn.bind(on_press=lambda x: self.check_admin_password(password_input.text, popup))
        cancel_btn.bind(on_press=popup.dismiss)
        
        popup.open()
    
    def check_admin_password(self, password, popup):
        """Verify admin password"""
        if password == self.admin_password:
            popup.dismiss()
            self.show_admin_panel()
        else:
            self.show_popup('Error', '❌ Wrong password!')
    
    def show_admin_panel(self):
        """Show admin statistics panel"""
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Stats
        total_users = len(self.users_data)
        total_messages = sum(u.get('message_count', 0) for u in self.users_data.values())
        
        stats_text = f"""
📊 Admin Statistics

👥 Total Users: {total_users}
💬 Total Messages: {total_messages}
🧠 AI Learning Status: Active
🔥 Current User: {self.current_user}
📅 App Version: 1.0.0

💡 Training Info:
- Auto-learning: ON
- Manual training available
- Firebase sync: Ready
        """
        
        stats_label = Label(
            text=stats_text,
            size_hint_y=0.7,
            halign='left',
            valign='top'
        )
        stats_label.bind(size=stats_label.setter('text_size'))
        
        close_btn = Button(text='Close', size_hint_y=0.1)
        
        content.add_widget(stats_label)
        content.add_widget(close_btn)
        
        popup = Popup(
            title='📊 Admin Panel',
            content=content,
            size_hint=(0.9, 0.8)
        )
        
        close_btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def logout(self, instance):
        """Logout current user"""
        self.current_user = None
        self.chat_history = []
        self.root.clear_widgets()
        self.root.add_widget(self.create_login_screen())
    
    def show_popup(self, title, message):
        """Show simple popup message"""
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        label = Label(text=message)
        btn = Button(text='OK', size_hint_y=0.3)
        
        content.add_widget(label)
        content.add_widget(btn)
        
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.4))
        btn.bind(on_press=popup.dismiss)
        popup.open()


if __name__ == '__main__':
    ChatApp().run()
