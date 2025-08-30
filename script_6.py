# Create a comprehensive README file
readme_content = """# YouTube Shorts Limiter Browser Extension

A productivity-focused browser extension that helps you limit your YouTube Shorts consumption by tracking your daily viewing count and taking action when you reach your set limit.

## 🎯 Features

- **Track Shorts Consumption**: Automatically counts how many YouTube Shorts you've watched
- **Customizable Daily Limits**: Set your own daily limit (1-100 shorts)
- **Two Action Modes**:
  - **Block Mode**: Completely blocks access to more shorts with a motivational message
  - **Loop Mode**: Loops the current short indefinitely when limit is reached
- **Visual Progress Tracking**: See your daily progress with a color-coded progress bar
- **Daily Reset**: Automatically resets your count at midnight
- **Manual Reset**: Reset your count anytime through the popup
- **Clean Interface**: Modern, intuitive popup interface for settings and stats

## 📦 Installation

### For Chrome/Chromium Browsers:

1. **Download the Extension Files**
   - Save all the extension files to a folder on your computer
   - Make sure you have: `manifest.json`, `content.js`, `background.js`, `popup.html`, `popup.css`, `popup.js`

2. **Enable Developer Mode**
   - Open Chrome and go to `chrome://extensions/`
   - Toggle "Developer mode" in the top-right corner

3. **Load the Extension**
   - Click "Load unpacked"
   - Select the folder containing your extension files
   - The extension should now appear in your extensions list

4. **Pin the Extension** (Optional)
   - Click the puzzle piece icon in the toolbar
   - Pin "YouTube Shorts Limiter" for easy access

### For Firefox:

1. **Temporary Installation** (for testing):
   - Go to `about:debugging#/runtime/this-firefox`
   - Click "Load Temporary Add-on"
   - Select the `manifest.json` file

2. **Permanent Installation**:
   - Package the extension as a `.xpi` file
   - Submit to Firefox Add-ons store for review

## 🚀 How to Use

1. **Set Your Limit**
   - Click the extension icon in your browser toolbar
   - Set your daily shorts limit (default: 10)
   - Choose your preferred action: Block or Loop

2. **Save Settings**
   - Click "Save Settings" to apply your preferences

3. **Start Browsing**
   - Visit YouTube and watch shorts normally
   - The extension will track your count automatically

4. **When Limit is Reached**
   - **Block Mode**: You'll see a motivational screen preventing further shorts access
   - **Loop Mode**: The current short will loop indefinitely

5. **Reset if Needed**
   - Use "Reset Count" button to start fresh anytime
   - Count automatically resets daily at midnight

## 🛠️ Technical Details

- **Manifest Version**: 3 (latest Chrome extension standard)
- **Permissions**: 
  - `storage` - To save your settings and count
  - `activeTab` - To interact with YouTube pages
- **Host Permissions**: `*://*.youtube.com/*`
- **Content Script**: Monitors YouTube Shorts pages
- **Background Script**: Handles storage and daily resets

## 📁 File Structure

```
youtube-shorts-limiter/
├── manifest.json          # Extension configuration
├── content.js            # Main functionality script
├── background.js         # Background service worker
├── popup.html           # Settings interface
├── popup.css            # Interface styling
├── popup.js             # Settings functionality
└── README.md           # This file
```

## 🎨 Customization

You can customize the extension by modifying:

- **Limits**: Change the min/max values in the settings
- **Styling**: Edit `popup.css` for different colors/layout
- **Messages**: Modify the blocked content message in `content.js`
- **Icons**: Add your own 16x16, 48x48, and 128x128 pixel icons

## 🐛 Troubleshooting

**Extension not working?**
- Make sure you're on a YouTube Shorts page (`youtube.com/shorts/...`)
- Check that the extension is enabled in your browser
- Try refreshing the YouTube page

**Count not saving?**
- Check browser storage permissions
- Try resetting the count and setting it again

**Settings not applying?**
- Click "Save Settings" after making changes
- Refresh YouTube pages for changes to take effect

## 🔒 Privacy

This extension:
- ✅ Only works on YouTube pages
- ✅ Stores data locally in your browser
- ✅ Does not collect or transmit personal data
- ✅ Does not track your browsing outside YouTube

## 🤝 Contributing

Feel free to modify and improve this extension! Some ideas:
- Add weekly/monthly limits
- Statistics and usage charts
- Different blocking methods
- Custom motivational messages
- Time-based restrictions

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 💡 Tips for Productivity

- Start with a higher limit and gradually reduce it
- Use block mode for stronger willpower enforcement
- Set specific times when the extension is most needed
- Combine with other productivity tools for best results

Stay focused and productive! 🎯💪
"""

# Save README.md
with open('README.md', 'w') as f:
    f.write(readme_content)

print("Created README.md with comprehensive installation and usage instructions")