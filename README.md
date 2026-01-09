# 🌙 Lunaro AI - Complete Package

A learning AI chatbot with multi-user support, multiple themes, and auto-learning capabilities.

![Lunaro AI Logo](logo_preview.png)

## ✨ Features

### 👤 User System
- Individual user accounts
- Personal chat history (last 100 messages per user)
- Theme preferences saved per user
- No password required - just username

### 🎨 6 Beautiful Themes
- **⬛ Pure Black** - OLED friendly, battery saver
- **🌙 Dark Grey** - Classic dark mode
- **🌸 Cherry Blossom** - Pink aesthetic
- **💻 Matrix Code** - Green hacker style
- **🌊 Deep Ocean** - Blue underwater vibe
- **🌅 Sunset Glow** - Orange/purple warm tones

### 🧠 AI Learning
- **Auto-learning** from every conversation
- Grammar correction
- Personality adaptation per user
- Word associations
- Response improvement over time

### 🔒 Admin Panel
- Password protected (`madebyconsumanoid:3`)
- View user statistics
- Check AI learning status
- Access training tools

### 💾 Data Storage
- **Local storage** (users.json) - Private user data
- **Firebase sync** (optional) - Cloud learning backup
- Automatic saving

## 📱 Installation on Android (Termux)

### Step 1: Install Termux
1. Download **Termux** from F-Droid (NOT Google Play - it's outdated!)
   - Go to: https://f-droid.org/
   - Search for "Termux"
   - Install it

2. Open Termux

### Step 2: Setup Environment
Copy and paste these commands one by one into Termux:

```bash
# Update packages
pkg update && pkg upgrade -y

# Install required packages (this takes 5-10 minutes)
pkg install -y python git clang cmake ninja openjdk-17

# Install Python packages (this takes 10-15 minutes)
pip install --upgrade pip
pip install buildozer cython kivy

# Allow Termux to access phone storage
termux-setup-storage
```

**Note:** When `termux-setup-storage` runs, it will ask for permission - tap "Allow"!

### Step 3: Get the App Files
```bash
# Create a directory for the app
cd ~
mkdir LunaroAI
cd LunaroAI

# Copy all the files you downloaded here
# (Use a file manager to move: main.py, chat_ai.py, model_trainer.py, buildozer.spec)
```

Or if you have the files in your Downloads:
```bash
# Copy files from Downloads to Termux
cp /sdcard/Download/main.py ~/LunaroAI/
cp /sdcard/Download/chat_ai.py ~/LunaroAI/
cp /sdcard/Download/model_trainer.py ~/LunaroAI/
cp /sdcard/Download/buildozer.spec ~/LunaroAI/
```

### Step 4: Configure Firebase (IMPORTANT!)

Before building, edit the Firebase config in `chat_ai.py`:

```bash
# Open the file with nano editor
nano chat_ai.py
```

Find this section (around line 24):
```python
self._firebase_config = {
    'database_url': "https://YOUR-PROJECT.firebaseio.com",
    'api_key': "YOUR_API_KEY",
    'project_id': "YOUR_PROJECT_ID"
}
```

Replace with your Firebase credentials:
- `YOUR-PROJECT.firebaseio.com` → Your Firebase database URL
- `YOUR_API_KEY` → Your Firebase API key
- `YOUR_PROJECT_ID` → Your Firebase project ID

To save in nano:
- Press `Ctrl + X`
- Press `Y` (Yes)
- Press `Enter`

**Don't have Firebase?** That's okay! The app will still work locally. Firebase is only for cloud backup.

### Step 5: Test Locally First

Before building the APK, test if everything works:

```bash
# Make sure you're in the project folder
cd ~/LunaroAI

# Run the app
python main.py
```

If you see the login screen, great! Press `Ctrl + C` to stop it.

### Step 6: Build APK

**WARNING:** First build takes 30-60 minutes! Be patient and don't close Termux.

```bash
# Initialize buildozer (first time only)
buildozer android debug

# If it asks for Android SDK license, type 'y' and press Enter
```

**What happens during build:**
1. Downloads Android SDK (~500MB)
2. Downloads Android NDK (~500MB)
3. Compiles Python for Android
4. Packages your app
5. Creates APK file

**If build fails:**
```bash
# Clean and try again
buildozer android clean
buildozer android debug
```

### Step 7: Install the APK

```bash
# Find your APK
ls -lh bin/

# Copy to Downloads folder
cp bin/*.apk /sdcard/Download/

# Now open your file manager, go to Downloads, and install the APK
```

**Note:** You may need to enable "Install from Unknown Sources" in your Android settings!

## 🎯 How to Use

### First Time User
1. Open the app
2. Type any username (no spaces)
3. Press "Login / Create Account"
4. Click the 🎨 button to choose a theme
5. Start chatting!

### Returning User
1. Open the app
2. Type your username
3. Press "Login"
4. Your last 10 messages will load
5. Your theme preference is saved

### Changing Themes
1. Click the 🎨 button (top left)
2. Choose your favorite theme
3. Done! Theme is saved automatically

### Admin Access
1. Click the 📊 button (top right)
2. Enter password: `madebyconsumanoid:3`
3. View stats and learning data

### Logout
Click the 🚪 button (top right)

## 🔧 Manual Training (Advanced)

Want to teach the AI specific responses?

```bash
# Run the trainer
python model_trainer.py
```

Options:
1. **Interactive training** - Teach one pattern at a time
2. **Train from file** - Bulk training from JSON file
3. **Show statistics** - See AI learning progress
4. **Export data** - Backup learning data
5. **Sync Firebase** - Upload to cloud
6. **Create template** - Generate training file template

### Example Training File

Create `my_training.json`:
```json
[
  {
    "pattern": "what's your favorite color",
    "response": "I love all colors! But if I had to choose, I'd say blue 💙"
  },
  {
    "pattern": "can you help me code",
    "response": "Of course! I'd love to help you code. What are you working on?"
  }
]
```

Then train:
```bash
python model_trainer.py
# Choose option 2
# Enter: my_training.json
```

## 📊 File Structure

```
LunaroAI/
├── main.py              # Main app with UI
├── chat_ai.py           # AI engine with learning
├── model_trainer.py     # Training tool
├── buildozer.spec       # Build configuration
├── logo.svg             # Logo (vector)
├── icon.png             # App icon (512x512)
├── logo_preview.png     # Logo preview (256x256)
├── LICENSE              # MIT License
├── users.json          # User data (auto-created)
├── ai_learning.json    # AI learning data (auto-created)
├── training_log.json   # Training history (auto-created)
└── firebase_sync.json  # Firebase sync data (auto-created)
```

## 🐛 Troubleshooting

### "Command not found"
```bash
# Install missing package
pkg install python
```

### "Permission denied"
```bash
# Give execute permission
chmod +x main.py
```

### "Module not found: kivy"
```bash
# Reinstall kivy
pip install --upgrade --force-reinstall kivy
```

### Build takes forever
- **Normal!** First build takes 30-60 minutes
- Make sure you have good internet
- Don't close Termux during build
- Charge your phone (it uses lots of CPU)

### APK won't install
- Enable "Unknown Sources" in Android settings
- Try: Settings > Security > Unknown Sources > ON
- Or: Settings > Apps > Special Access > Install Unknown Apps > Your File Manager > Allow

### App crashes on open
- Make sure all Python files are in the same folder
- Check if `users.json` has correct permissions
- Try: `python main.py` to see error messages

### Firebase not working
- Firebase is optional!
- App works perfectly without it
- Firebase only needed for cloud backup

## 💡 Tips

### Battery Saving
- Use Pure Black theme (OLED screens save power with black)
- Close app when not in use

### Best Performance
- Clear chat history occasionally (logout and login)
- Train AI manually every 100 conversations for better responses

### Privacy
- Each user's chat is private (stored locally)
- Firebase sync is optional
- No data is sent without your permission

### Making It Better
- Chat more! AI learns from every message
- Use the manual trainer to teach specific responses
- Share with friends - more users = smarter AI

## 🔐 Admin Password

**Default password:** `madebyconsumanoid:3`

**To change it:** Edit line 27 in `main.py`
```python
self.admin_password = 'your_new_password_here'
```

Then rebuild the APK if you want the change on your phone.

## 📝 Building for Different Architectures

### For 32-bit devices (most compatible):
In `buildozer.spec`, use:
```
android.archs = armeabi-v7a
```

### For 64-bit devices (faster):
```
android.archs = arm64-v8a
```

### For both (universal, but larger APK):
```
android.archs = armeabi-v7a,arm64-v8a
```

**Current config:** 32-bit only (armeabi-v7a) ✅

## 🚀 Advanced: Deploying to Others

Want to share your app?

1. Build the APK (as shown above)
2. Copy APK from `bin/` folder
3. Share the APK file with friends
4. They just install it - no Termux needed!

**Note:** Each installation has separate user data. Firebase can sync learning data between installations if configured.

## 📧 Support

Found a bug? Want to add features?

1. Check the error messages when running `python main.py`
2. Make sure all files are in the same folder
3. Verify Firebase config if using cloud features
4. Try rebuilding: `buildozer android clean` then `buildozer android debug`

## 🎉 That's It!

You now have a fully functional AI chatbot that learns from you!

**Enjoy chatting with Lunaro! 🌙💬**

---

Made with ❤️ by Solo Dev (with help from Claude AI)
Password: `madebyconsumanoid:3` 🔐
