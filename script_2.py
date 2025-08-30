# Create the background script
background_js = """
// Background script for YouTube Shorts Limiter
chrome.runtime.onInstalled.addListener((details) => {
    if (details.reason === 'install') {
        // Set default values on first install
        chrome.storage.sync.set({
            maxShorts: 10,
            actionType: 'block',
            shortsCount: 0
        });
    }
});

// Listen for messages from content script or popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'resetCount') {
        chrome.storage.sync.set({ shortsCount: 0 }, () => {
            sendResponse({ success: true });
        });
        return true; // Will respond asynchronously
    }
    
    if (request.action === 'getStats') {
        chrome.storage.sync.get(['maxShorts', 'actionType', 'shortsCount'], (result) => {
            sendResponse(result);
        });
        return true; // Will respond asynchronously
    }
});

// Reset count daily at midnight
function scheduleReset() {
    const now = new Date();
    const tomorrow = new Date(now);
    tomorrow.setDate(now.getDate() + 1);
    tomorrow.setHours(0, 0, 0, 0);
    
    const msUntilMidnight = tomorrow.getTime() - now.getTime();
    
    setTimeout(() => {
        chrome.storage.sync.set({ shortsCount: 0 });
        scheduleReset(); // Schedule next reset
    }, msUntilMidnight);
}

// Start the daily reset scheduler
scheduleReset();
"""

# Save background.js
with open('background.js', 'w') as f:
    f.write(background_js)

print("Created background.js")