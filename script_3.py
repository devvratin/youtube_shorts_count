# Create the popup HTML
popup_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Shorts Limiter</title>
    <link rel="stylesheet" href="popup.css">
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="icon">🎯</div>
            <h1>Shorts Limiter</h1>
        </div>
        
        <div class="stats">
            <div class="stat-item">
                <span class="stat-label">Today's Count:</span>
                <span class="stat-value" id="currentCount">0</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">Daily Limit:</span>
                <span class="stat-value" id="currentLimit">10</span>
            </div>
        </div>
        
        <div class="progress-bar">
            <div class="progress-fill" id="progressFill"></div>
        </div>
        
        <div class="settings">
            <h2>Settings</h2>
            
            <div class="setting-group">
                <label for="limitInput">Daily Shorts Limit:</label>
                <input type="number" id="limitInput" min="1" max="100" value="10">
            </div>
            
            <div class="setting-group">
                <label for="actionSelect">Action when limit reached:</label>
                <select id="actionSelect">
                    <option value="block">Block further shorts</option>
                    <option value="loop">Loop current short</option>
                </select>
            </div>
        </div>
        
        <div class="actions">
            <button id="saveBtn" class="btn btn-primary">Save Settings</button>
            <button id="resetBtn" class="btn btn-secondary">Reset Count</button>
        </div>
        
        <div class="footer">
            <p>Stay focused and productive! 💪</p>
        </div>
    </div>
    
    <script src="popup.js"></script>
</body>
</html>"""

# Save popup.html
with open('popup.html', 'w') as f:
    f.write(popup_html)

print("Created popup.html")