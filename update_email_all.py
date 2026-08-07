import os, glob

# 1. Update index.html
with open('index.html', 'r') as f:
    idx = f.read()

idx = idx.replace('hello@ajiteshsharma.dev', 'hello@ajiteshsharma.dev')
idx = idx.replace('HELLO@AJITESHSHARMA.DEV', 'HELLO@AJITESHSHARMA.DEV')

with open('index.html', 'w') as f:
    f.write(idx)
print("Updated email in index.html")

# 2. Update all pages in pages/
for file in glob.glob('pages/*.html'):
    with open(file, 'r') as f:
        content = f.read()
    content = content.replace('hello@ajiteshsharma.dev', 'hello@ajiteshsharma.dev')
    content = content.replace('HELLO@AJITESHSHARMA.DEV', 'HELLO@AJITESHSHARMA.DEV')
    with open(file, 'w') as f:
        f.write(content)
    print(f"Updated email in {file}")

# 3. Update build scripts
for file in glob.glob('*.py'):
    with open(file, 'r') as f:
        content = f.read()
    content = content.replace('hello@ajiteshsharma.dev', 'hello@ajiteshsharma.dev')
    content = content.replace('HELLO@AJITESHSHARMA.DEV', 'HELLO@AJITESHSHARMA.DEV')
    with open(file, 'w') as f:
        f.write(content)
print("Updated email in all python build scripts")
