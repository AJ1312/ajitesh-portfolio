with open('js/simulations.js', 'r') as f:
    text = f.read()

# Replace \` with `
text = text.replace('\\`', '`')
# Replace \$ with $
text = text.replace('\\$', '$')

with open('js/simulations.js', 'w') as f:
    f.write(text)
