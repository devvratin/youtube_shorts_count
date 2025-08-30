# Create simple SVG icons for the extension
# Since we can't create actual PNG files easily, I'll create SVG icons and instructions for conversion

# 16x16 icon (for toolbar)
icon16_svg = """<svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
  <rect width="16" height="16" fill="#FF0000" rx="2"/>
  <circle cx="8" cy="8" r="4" fill="#FFF"/>
  <text x="8" y="11" font-family="Arial" font-size="6" fill="#FF0000" text-anchor="middle" font-weight="bold">S</text>
</svg>"""

# 48x48 icon (for extension management page)
icon48_svg = """<svg width="48" height="48" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
  <rect width="48" height="48" fill="#FF0000" rx="6"/>
  <circle cx="24" cy="24" r="16" fill="#FFF"/>
  <text x="24" y="30" font-family="Arial" font-size="14" fill="#FF0000" text-anchor="middle" font-weight="bold">STOP</text>
  <circle cx="24" cy="24" r="20" fill="none" stroke="#FFF" stroke-width="2" stroke-dasharray="3,3"/>
</svg>"""

# 128x128 icon (for Chrome Web Store)
icon128_svg = """<svg width="128" height="128" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FF0000;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#CC0000;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="128" height="128" fill="url(#grad1)" rx="16"/>
  <circle cx="64" cy="64" r="45" fill="#FFF" opacity="0.95"/>
  <text x="64" y="52" font-family="Arial" font-size="16" fill="#FF0000" text-anchor="middle" font-weight="bold">YouTube</text>
  <text x="64" y="70" font-family="Arial" font-size="20" fill="#FF0000" text-anchor="middle" font-weight="bold">SHORTS</text>
  <text x="64" y="88" font-family="Arial" font-size="16" fill="#FF0000" text-anchor="middle" font-weight="bold">LIMITER</text>
  <circle cx="64" cy="64" r="50" fill="none" stroke="#FFF" stroke-width="4" stroke-dasharray="8,8"/>
</svg>"""

# Save SVG files
with open('icon16.svg', 'w') as f:
    f.write(icon16_svg)

with open('icon48.svg', 'w') as f:
    f.write(icon48_svg)

with open('icon128.svg', 'w') as f:
    f.write(icon128_svg)

print("Created SVG icon files (icon16.svg, icon48.svg, icon128.svg)")
print("\nNOTE: The manifest.json expects PNG files. You'll need to:")
print("1. Convert these SVG files to PNG using an online converter")
print("2. Or create PNG icons using any image editor")
print("3. Or update manifest.json to use SVG files instead")