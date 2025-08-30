# Create the popup JavaScript
popup_js = """// YouTube Shorts Limiter Popup Script
document.addEventListener('DOMContentLoaded', async () => {
    const currentCountEl = document.getElementById('currentCount');
    const currentLimitEl = document.getElementById('currentLimit');
    const progressFillEl = document.getElementById('progressFill');
    const limitInputEl = document.getElementById('limitInput');
    const actionSelectEl = document.getElementById('actionSelect');
    const saveBtn = document.getElementById('saveBtn');
    const resetBtn = document.getElementById('resetBtn');

    // Load current settings and stats
    await loadStats();

    // Event listeners
    saveBtn.addEventListener('click', saveSettings);
    resetBtn.addEventListener('click', resetCount);
    limitInputEl.addEventListener('input', updateProgressBar);

    async function loadStats() {
        try {
            const result = await chrome.storage.sync.get(['maxShorts', 'actionType', 'shortsCount']);
            
            const maxShorts = result.maxShorts || 10;
            const actionType = result.actionType || 'block';
            const shortsCount = result.shortsCount || 0;

            // Update UI elements
            currentCountEl.textContent = shortsCount;
            currentLimitEl.textContent = maxShorts;
            limitInputEl.value = maxShorts;
            actionSelectEl.value = actionType;

            // Update progress bar
            updateProgressBar();
        } catch (error) {
            console.error('Error loading stats:', error);
        }
    }

    function updateProgressBar() {
        const current = parseInt(currentCountEl.textContent);
        const limit = parseInt(limitInputEl.value) || parseInt(currentLimitEl.textContent);
        const percentage = Math.min((current / limit) * 100, 100);

        progressFillEl.style.width = percentage + '%';

        // Change color based on progress
        progressFillEl.classList.remove('warning', 'danger');
        if (percentage >= 100) {
            progressFillEl.classList.add('danger');
        } else if (percentage >= 75) {
            progressFillEl.classList.add('warning');
        }
    }

    async function saveSettings() {
        try {
            const maxShorts = parseInt(limitInputEl.value);
            const actionType = actionSelectEl.value;

            if (maxShorts < 1 || maxShorts > 100) {
                alert('Please enter a limit between 1 and 100');
                return;
            }

            await chrome.storage.sync.set({
                maxShorts: maxShorts,
                actionType: actionType
            });

            // Update UI
            currentLimitEl.textContent = maxShorts;
            updateProgressBar();

            // Show success message
            showSuccessMessage('Settings saved successfully!');

        } catch (error) {
            console.error('Error saving settings:', error);
            alert('Error saving settings. Please try again.');
        }
    }

    async function resetCount() {
        try {
            await chrome.storage.sync.set({ shortsCount: 0 });
            
            // Update UI
            currentCountEl.textContent = '0';
            updateProgressBar();
            
            // Show success message
            showSuccessMessage('Count reset successfully!');

        } catch (error) {
            console.error('Error resetting count:', error);
            alert('Error resetting count. Please try again.');
        }
    }

    function showSuccessMessage(message) {
        // Create success message element
        const successDiv = document.createElement('div');
        successDiv.className = 'success-message';
        successDiv.textContent = message;
        
        // Insert after header
        const header = document.querySelector('.header');
        header.parentNode.insertBefore(successDiv, header.nextSibling);
        
        // Show with animation
        setTimeout(() => {
            successDiv.classList.add('show');
        }, 10);
        
        // Remove after 3 seconds
        setTimeout(() => {
            successDiv.classList.remove('show');
            setTimeout(() => {
                if (successDiv.parentNode) {
                    successDiv.parentNode.removeChild(successDiv);
                }
            }, 300);
        }, 3000);
    }

    // Update progress bar when limit input changes
    limitInputEl.addEventListener('input', () => {
        currentLimitEl.textContent = limitInputEl.value;
        updateProgressBar();
    });
});
"""

# Save popup.js
with open('popup.js', 'w') as f:
    f.write(popup_js)

print("Created popup.js")