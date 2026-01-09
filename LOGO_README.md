# 🌙 Lunaro AI Logo & Branding

## Logo Files

This folder contains the official Lunaro AI logo:

### Files:
- **logo.svg** - Vector logo (scalable, best quality)
- **icon.png** - App icon (512x512 pixels) - Used for Android app
- **logo_preview.png** - Preview version (256x256 pixels)

## Logo Design

The Lunaro AI logo features:
- **Moon** - Represents "Lunaro" (lunar theme)
- **Neural Network Lines** - Represents AI and machine learning
- **Blue Color Scheme** - Tech-forward, calm, intelligent
- **Glowing Effects** - Modern, futuristic feel
- **Stars & Sparkles** - Magic and innovation

### Color Palette:
- **Primary Blue:** `#6fb1ff` - Main brand color
- **Cyan Accent:** `#4affff` - AI neural network nodes
- **Dark Background:** `#1a1a2e` - Professional, modern
- **Moon Blue:** `#6a9bd6` - Moon surface

## Usage

### For Android App:
The `icon.png` file is automatically used when you build the APK with buildozer.

### For Marketing/Social Media:
- Use `logo.svg` for print materials (scalable)
- Use `icon.png` for social media profile pictures
- Use `logo_preview.png` for smaller uses

### Variations:
You can modify the logo by editing `logo.svg` with any vector graphics editor:
- Inkscape (free)
- Adobe Illustrator
- Figma (online)

## Brand Guidelines

### Do's:
✅ Use the logo on dark backgrounds
✅ Keep adequate spacing around the logo
✅ Use the blue color palette
✅ Keep the moon and neural network together

### Don'ts:
❌ Don't stretch or distort the logo
❌ Don't change the colors dramatically
❌ Don't separate the moon from the text
❌ Don't use on light backgrounds without adjustments

## Creating Custom Sizes

If you need different sizes, use Python:

```python
from PIL import Image

# Open original
icon = Image.open('icon.png')

# Resize to custom size
custom = icon.resize((YOUR_SIZE, YOUR_SIZE), Image.Resampling.LANCZOS)
custom.save('icon_custom.png', 'PNG')
```

Common Android sizes:
- **48x48** - ldpi
- **72x72** - mdpi
- **96x96** - hdpi
- **144x144** - xhdpi
- **192x192** - xxhdpi
- **512x512** - xxxhdpi (our default)

## License

The Lunaro AI logo is covered under the MIT License (see LICENSE file).
You're free to use and modify it for your projects!

---

**Lunaro AI** 🌙 - Where Intelligence Meets Innovation
