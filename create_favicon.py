import os
from PIL import Image, ImageDraw, ImageFont

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="8" fill="#111111"/>
  <text x="32" y="47" dominant-baseline="middle" text-anchor="middle" font-family="'Playfair Display', Georgia, serif" font-size="44" font-weight="900" fill="#fcfaf7">A</text>
  <circle cx="48" cy="16" r="4" fill="#d92323"/>
</svg>
"""

with open("favicon.svg", "w") as f:
    f.write(svg_content)

# Also create high-res PNG favicon
img = Image.new('RGBA', (128, 128), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(img)
draw.rounded_rectangle([4, 4, 124, 124], radius=16, fill='#111111')

try:
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", 84)
except:
    font = ImageFont.load_default()

draw.text((36, 12), "A", fill='#fcfaf7', font=font)
draw.ellipse([92, 18, 110, 36], fill='#d92323')

img.save("favicon.png")
print("Favicons created successfully!")
