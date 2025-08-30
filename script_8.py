# Create a detailed installation guide
installation_guide = """# 📦 INSTALLATION GUIDE - YouTube Shorts Limiter Extension

Follow these step-by-step instructions to install and test your YouTube Shorts Limiter extension.

## 🚀 Quick Start (5 minutes)

### Step 1: Prepare Your Files
1. Create a new folder called `youtube-shorts-limiter`
2. Save all the provided files in this folder:
   - ✅ `manifest.json`
   - ✅ `content.js`
   - ✅ `background.js`
   - ✅ `popup.html`
   - ✅ `popup.css`
   - ✅ `popup.js`

### Step 2: Handle Icons
**Option A - Use Placeholder Icons:**
1. Create simple 16x16, 48x48, and 128x128 pixel PNG files
2. Name them `icon16.png`, `icon48.png`, and `icon128.png`
3. You can use any red circular icons or create simple colored squares

**Option B - Skip Icons Temporarily:**
1. Remove the "icons" section from `manifest.json`
2. Delete lines 19-23 in the manifest file

### Step 3: Install in Chrome/Edge

1. **Open Extensions Page:**
   - Type `chrome://extensions/` in your address bar
   - Or click Menu (⋮) → More Tools → Extensions

2. **Enable Developer Mode:**
   - Toggle the "Developer mode" switch in the top-right corner
   - You should see new buttons appear

3. **Load Your Extension:**
   - Click "Load unpacked" button
   - Navigate to your `youtube-shorts-limiter` folder
   - Click "Select Folder"

4. **Verify Installation:**
   - Your extension should appear with a green "Enabled" status
   - You'll see "YouTube Shorts Limiter" in your extensions list

### Step 4: Test the Extension

1. **Pin the Extension:**
   - Click the puzzle piece icon (🧩) in your browser toolbar
   - Click the pin icon next to "YouTube Shorts Limiter"

2. **Configure Settings:**
   - Click the extension icon in your toolbar
   - Set your daily limit (try 3 for testing)
   - Choose "Block" mode
   - Click "Save Settings"

3. **Test on YouTube:**
   - Go to `youtube.com`
   - Search for shorts or go directly to the Shorts section
   - Watch a few shorts and check the counter in the extension popup
   - After reaching your limit, you should see the block screen

## 🔧 Troubleshooting

### Extension Won't Load
**Error: "Manifest file is missing or unreadable"**
- Make sure `manifest.json` is in your folder and properly formatted
- Check for any extra characters or formatting issues

**Error: "Could not load icon"**
- Either add icon files or remove the icons section from manifest.json
- Icons are not required for the extension to work

### Extension Doesn't Count Shorts
**If the counter stays at 0:**
1. Make sure you're watching actual YouTube Shorts (URLs with `/shorts/`)
2. Refresh the YouTube page after installing the extension
3. Check the browser console (F12) for any error messages

**If settings won't save:**
1. Make sure you clicked "Save Settings"
2. Try disabling and re-enabling the extension
3. Check that Chrome has storage permissions

### Block Screen Doesn't Appear
**If you reach the limit but don't see the block screen:**
1. Make sure you selected "Block" mode in settings
2. Refresh the YouTube page
3. Check that your limit is set correctly

## 🛠️ Advanced Configuration

### Customize the Block Message
Edit the `blockMessage` section in `content.js` around line 85 to change:
- The motivational text
- Button text and colors
- Background styling

### Change Default Settings
Edit the default values in `background.js` around line 4:
- `maxShorts: 10` - Default daily limit
- `actionType: 'block'` - Default action type

### Modify the Popup Interface
- Edit `popup.html` for structure changes
- Edit `popup.css` for styling/colors
- Edit `popup.js` for functionality changes

## 📱 Testing Checklist

Before daily use, test these features:

- [ ] Extension loads without errors
- [ ] Popup opens and displays correctly
- [ ] Settings can be saved and persist after browser restart
- [ ] Counter increases when watching shorts
- [ ] Reset button works
- [ ] Block screen appears at limit (if using block mode)
- [ ] Loop functionality works (if using loop mode)
- [ ] Extension works after page refresh

## 🔄 Updating the Extension

When you make changes to any files:

1. Go to `chrome://extensions/`
2. Find your extension
3. Click the refresh icon (🔄) next to your extension
4. Refresh any open YouTube pages

## 📤 Sharing Your Extension

To share with others:
1. Zip your entire extension folder
2. Share the zip file
3. Recipients follow the same installation steps

## 🌐 Publishing to Chrome Web Store (Optional)

For permanent installation and sharing:

1. Create a Google Developer account ($5 one-time fee)
2. Package your extension as a `.zip` file
3. Upload to Chrome Web Store Developer Dashboard
4. Fill out store listing details
5. Submit for review (usually takes 3-7 days)

## 💡 Usage Tips

- **Start High**: Begin with a higher limit and gradually reduce it
- **Morning Setup**: Configure your settings each morning
- **Block Mode**: More effective for breaking habits
- **Loop Mode**: Less disruptive but still creates awareness
- **Reset Strategically**: Use manual reset for special occasions

## 🚨 Important Notes

- Extension only works on `youtube.com` domain
- Requires manual installation (not from Chrome store yet)
- Count resets automatically at midnight
- Settings are saved locally in your browser
- No data is transmitted externally

---

**Need Help?** Check the main README.md file for more detailed information about features and customization options.

**Ready to stay productive?** 🎯 Install your extension and take control of your YouTube Shorts habit!
"""

# Save the installation guide
with open('INSTALLATION_GUIDE.md', 'w') as f:
    f.write(installation_guide)

print("Created comprehensive INSTALLATION_GUIDE.md")
print("\n" + "="*60)
print("✅ YOUTUBE SHORTS LIMITER EXTENSION COMPLETE!")
print("="*60)
print("\nFiles created:")
files = [
    "manifest.json - Extension configuration",
    "content.js - Main functionality script", 
    "background.js - Background service worker",
    "popup.html - Settings interface",
    "popup.css - Interface styling", 
    "popup.js - Settings functionality",
    "README.md - Comprehensive documentation",
    "INSTALLATION_GUIDE.md - Step-by-step installation",
    "icon16.svg, icon48.svg, icon128.svg - Extension icons (convert to PNG)"
]

for i, file in enumerate(files, 1):
    print(f"{i:2d}. {file}")

print(f"\n🚀 Next Steps:")
print("1. Create a folder called 'youtube-shorts-limiter'")
print("2. Save all files to that folder") 
print("3. Convert SVG icons to PNG (optional)")
print("4. Follow INSTALLATION_GUIDE.md to install in Chrome")
print("5. Test on YouTube Shorts!")

print(f"\n🎯 Your extension will:")
print("• Track YouTube Shorts viewed daily")
print("• Block access or loop shorts when limit reached")  
print("• Provide a clean settings interface")
print("• Reset count automatically at midnight")
print("• Help you stay productive!")