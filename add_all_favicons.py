import os

pages = ['snapseat.html', 'nutrivision.html', 'paper-compsac.html', 'certifications.html']
for page in pages:
    path = os.path.join('pages', page)
    if os.path.exists(path):
        with open(path, 'r') as f:
            content = f.read()
        if 'rel="icon"' not in content:
            content = content.replace('</head>', '    <link rel="icon" type="image/svg+xml" href="../favicon.svg">\n    <link rel="alternate icon" type="image/png" href="../favicon.png">\n</head>')
            with open(path, 'w') as f:
                f.write(content)
            print(f"Added favicon to {path}")
