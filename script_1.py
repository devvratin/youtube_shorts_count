# Create the content script that monitors YouTube Shorts
content_js = """
// YouTube Shorts Limiter Content Script
class YouTubeShortsLimiter {
    constructor() {
        this.shortsCount = 0;
        this.maxShorts = 10; // Default limit
        this.actionType = 'block'; // 'block' or 'loop'
        this.currentShortUrl = '';
        this.isBlocked = false;
        this.originalContent = null;
        
        this.init();
    }

    async init() {
        // Load settings from storage
        await this.loadSettings();
        
        // Start monitoring
        this.startMonitoring();
        
        // Listen for URL changes (YouTube is a SPA)
        this.observeUrlChanges();
    }

    async loadSettings() {
        try {
            const result = await chrome.storage.sync.get(['maxShorts', 'actionType', 'shortsCount']);
            this.maxShorts = result.maxShorts || 10;
            this.actionType = result.actionType || 'block';
            this.shortsCount = result.shortsCount || 0;
        } catch (error) {
            console.log('Error loading settings:', error);
        }
    }

    async saveCount() {
        try {
            await chrome.storage.sync.set({ shortsCount: this.shortsCount });
        } catch (error) {
            console.log('Error saving count:', error);
        }
    }

    startMonitoring() {
        // Check if we're on a Shorts page
        setInterval(() => {
            this.checkShortsPage();
        }, 1000);
    }

    observeUrlChanges() {
        let lastUrl = location.href;
        new MutationObserver(() => {
            const url = location.href;
            if (url !== lastUrl) {
                lastUrl = url;
                this.handleUrlChange();
            }
        }).observe(document, { subtree: true, childList: true });
    }

    handleUrlChange() {
        if (this.isBlocked) {
            this.restoreOriginalContent();
            this.isBlocked = false;
        }
    }

    checkShortsPage() {
        const currentUrl = window.location.href;
        
        // Check if we're on YouTube Shorts
        if (currentUrl.includes('/shorts/')) {
            // New short detected
            if (currentUrl !== this.currentShortUrl) {
                this.currentShortUrl = currentUrl;
                this.handleNewShort();
            }
        }
    }

    async handleNewShort() {
        this.shortsCount++;
        await this.saveCount();
        
        console.log(`Shorts watched: ${this.shortsCount}/${this.maxShorts}`);
        
        // Check if limit reached
        if (this.shortsCount >= this.maxShorts) {
            if (this.actionType === 'block') {
                this.blockShorts();
            } else if (this.actionType === 'loop') {
                this.loopCurrentShort();
            }
        }
    }

    blockShorts() {
        if (this.isBlocked) return;
        
        this.isBlocked = true;
        this.originalContent = document.body.innerHTML;
        
        const blockMessage = `
            <div style="
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: #0f0f0f;
                color: white;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                font-family: 'Roboto', Arial, sans-serif;
                z-index: 10000;
            ">
                <div style="text-align: center; max-width: 600px; padding: 40px;">
                    <div style="font-size: 60px; margin-bottom: 20px;">🎯</div>
                    <h1 style="font-size: 32px; margin-bottom: 20px; font-weight: 300;">
                        Time to Focus!
                    </h1>
                    <p style="font-size: 18px; line-height: 1.5; margin-bottom: 30px; opacity: 0.8;">
                        You've watched <strong>${this.shortsCount} YouTube Shorts</strong> today.
                        <br>It's time to get back to being productive!
                    </p>
                    <div style="margin-bottom: 30px;">
                        <button onclick="window.location.href='https://youtube.com'" style="
                            background: #ff0000;
                            color: white;
                            border: none;
                            padding: 12px 24px;
                            border-radius: 24px;
                            font-size: 16px;
                            cursor: pointer;
                            margin: 0 10px;
                            transition: background 0.3s;
                        " onmouseover="this.style.background='#cc0000'" onmouseout="this.style.background='#ff0000'">
                            Go to YouTube Home
                        </button>
                        <button onclick="window.close()" style="
                            background: #333;
                            color: white;
                            border: none;
                            padding: 12px 24px;
                            border-radius: 24px;
                            font-size: 16px;
                            cursor: pointer;
                            margin: 0 10px;
                            transition: background 0.3s;
                        " onmouseover="this.style.background='#555'" onmouseout="this.style.background='#333'">
                            Close Tab
                        </button>
                    </div>
                    <div style="font-size: 14px; opacity: 0.6; margin-top: 20px;">
                        <p>You can reset your count in the extension popup</p>
                        <p>or change your limits in the settings</p>
                    </div>
                </div>
            </div>
        `;
        
        document.body.innerHTML = blockMessage;
    }

    loopCurrentShort() {
        // Find the video element and restart it
        const video = document.querySelector('video');
        if (video) {
            video.currentTime = 0;
            video.play();
        }
        
        // Show notification
        this.showNotification('Looping current short - you\\'ve reached your limit!');
    }

    restoreOriginalContent() {
        if (this.originalContent) {
            document.body.innerHTML = this.originalContent;
            this.originalContent = null;
        }
    }

    showNotification(message) {
        // Create notification overlay
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #ff0000;
            color: white;
            padding: 15px 20px;
            border-radius: 8px;
            font-family: Arial, sans-serif;
            font-size: 14px;
            z-index: 10000;
            max-width: 300px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        `;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        // Auto remove after 5 seconds
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 5000);
    }
}

// Initialize the limiter when the page loads
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        new YouTubeShortsLimiter();
    });
} else {
    new YouTubeShortsLimiter();
}
"""

# Save content.js
with open('content.js', 'w') as f:
    f.write(content_js)

print("Created content.js")