# Create the popup CSS
popup_css = """/* YouTube Shorts Limiter Popup Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    width: 350px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #f8f9fa;
    color: #333;
}

.container {
    padding: 20px;
}

.header {
    text-align: center;
    margin-bottom: 20px;
    padding-bottom: 15px;
    border-bottom: 2px solid #e9ecef;
}

.icon {
    font-size: 32px;
    margin-bottom: 8px;
}

.header h1 {
    font-size: 20px;
    font-weight: 600;
    color: #2c3e50;
}

.stats {
    background: white;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.stat-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
}

.stat-item:last-child {
    margin-bottom: 0;
}

.stat-label {
    font-size: 14px;
    color: #666;
}

.stat-value {
    font-size: 16px;
    font-weight: 600;
    color: #2c3e50;
}

.progress-bar {
    background: #e9ecef;
    border-radius: 10px;
    height: 8px;
    margin-bottom: 20px;
    overflow: hidden;
}

.progress-fill {
    background: linear-gradient(90deg, #28a745, #20c997);
    height: 100%;
    border-radius: 10px;
    transition: width 0.3s ease;
    width: 0%;
}

.progress-fill.warning {
    background: linear-gradient(90deg, #ffc107, #fd7e14);
}

.progress-fill.danger {
    background: linear-gradient(90deg, #dc3545, #e74c3c);
}

.settings {
    background: white;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.settings h2 {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 15px;
    color: #2c3e50;
}

.setting-group {
    margin-bottom: 15px;
}

.setting-group:last-child {
    margin-bottom: 0;
}

.setting-group label {
    display: block;
    font-size: 13px;
    font-weight: 500;
    color: #555;
    margin-bottom: 5px;
}

.setting-group input,
.setting-group select {
    width: 100%;
    padding: 8px 12px;
    border: 2px solid #e9ecef;
    border-radius: 6px;
    font-size: 14px;
    transition: border-color 0.2s ease;
}

.setting-group input:focus,
.setting-group select:focus {
    outline: none;
    border-color: #007bff;
}

.actions {
    display: flex;
    gap: 10px;
    margin-bottom: 15px;
}

.btn {
    flex: 1;
    padding: 10px 16px;
    border: none;
    border-radius: 6px;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
}

.btn-primary {
    background: #007bff;
    color: white;
}

.btn-primary:hover {
    background: #0056b3;
}

.btn-secondary {
    background: #6c757d;
    color: white;
}

.btn-secondary:hover {
    background: #545b62;
}

.btn:active {
    transform: translateY(1px);
}

.footer {
    text-align: center;
    padding-top: 10px;
    border-top: 1px solid #e9ecef;
}

.footer p {
    font-size: 12px;
    color: #666;
}

/* Success message styles */
.success-message {
    background: #d4edda;
    color: #155724;
    padding: 8px 12px;
    border-radius: 4px;
    margin-bottom: 10px;
    font-size: 13px;
    text-align: center;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.success-message.show {
    opacity: 1;
}
"""

# Save popup.css
with open('popup.css', 'w') as f:
    f.write(popup_css)

print("Created popup.css")