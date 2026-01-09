#!/bin/bash
# Quick Setup Script for Lunaro AI
# Run this in Termux to set everything up automatically

echo "🌙 Lunaro AI - Quick Setup"
echo "=================================="
echo ""

# Check if running in Termux
if [ ! -d "$PREFIX" ]; then
    echo "❌ Error: This script must be run in Termux!"
    exit 1
fi

echo "📦 Step 1: Updating packages..."
pkg update -y && pkg upgrade -y

echo ""
echo "📦 Step 2: Installing dependencies..."
echo "This will take 10-20 minutes. Please be patient!"
pkg install -y python git clang cmake ninja openjdk-17

echo ""
echo "🐍 Step 3: Installing Python packages..."
pip install --upgrade pip
pip install buildozer cython kivy

echo ""
echo "📁 Step 4: Setting up storage access..."
termux-setup-storage

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Edit chat_ai.py and add your Firebase config (if using Firebase)"
echo "2. Test the app: python main.py"
echo "3. Build APK: buildozer android debug"
echo ""
echo "📖 For detailed instructions, read README.md"
echo ""
echo "🎉 Happy building!"
