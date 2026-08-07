import os, glob

for file in glob.glob("pages/*.html"):
    with open(file, "r") as f:
        content = f.read()
    
    # Remove old inline data svg favicons if any
    import re
    content = re.sub(r'<link rel="icon" href="data:image/svg\+xml.*?>', '', content)
    
    # Insert clean SVG and PNG favicon tags before </head>
    if 'href="../favicon.svg"' not in content:
        content = content.replace('</head>', '    <link rel="icon" type="image/svg+xml" href="../favicon.svg">\n    <link rel="alternate icon" type="image/png" href="../favicon.png">\n</head>')
    
    with open(file, "w") as f:
        f.write(content)
    print(f"Standardized {file}")

# Also check index.html
with open("index.html", "r") as f:
    idx = f.read()
if 'href="favicon.svg"' not in idx:
    idx = idx.replace('</head>', '    <link rel="icon" type="image/svg+xml" href="favicon.svg">\n    <link rel="alternate icon" type="image/png" href="favicon.png">\n</head>')
    with open("index.html", "w") as f:
        f.write(idx)
    print("Standardized index.html")
