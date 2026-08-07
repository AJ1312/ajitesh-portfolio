import os

with open('pages/sentinel-stream.html', 'r') as f:
    s_html = f.read()

# Fix LaTeX artifacts in sentinel-stream.html
s_html = s_html.replace("$pprox 4.2 ext{ KB}$", "approximately 4.2 KB")
s_html = s_html.replace("$O(N)$", "O(N)")
s_html = s_html.replace("$O(1)$", "O(1)")
s_html = s_html.replace("$O(M)$", "O(M)")
s_html = s_html.replace("$M$", "M")
s_html = s_html.replace("$s_{\\text{iso}}$", "s_iso")
s_html = s_html.replace("$s_{iso}$", "s_iso")
s_html = s_html.replace("$\\\\text{CoV}$", "CoV")

with open('pages/sentinel-stream.html', 'w') as f:
    f.write(s_html)

with open('pages/cipherpulse.html', 'r') as f:
    c_html = f.read()

# Fix LaTeX artifacts in cipherpulse.html
c_html = c_html.replace("$	ext{CoV} < 0.12$", "CoV &lt; 0.12")
c_html = c_html.replace("($	ext{CoV}$)", "(CoV)")
c_html = c_html.replace("($\\text{CoV}$)", "(CoV)")
c_html = c_html.replace("($\text{CoV}$)", "(CoV)")
c_html = c_html.replace("$O(1)$", "O(1)")
c_html = c_html.replace("($\\text{CoV} < 0.12$)", "(CoV &lt; 0.12)")

with open('pages/cipherpulse.html', 'w') as f:
    f.write(c_html)

print("Successfully fixed LaTeX artifacts and cleaned text across both pages!")
