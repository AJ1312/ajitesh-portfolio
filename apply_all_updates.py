import os

# 1. Update index.html
with open('index.html', 'r') as f:
    idx_html = f.read()

# Add favicon to index.html if not present
if 'rel="icon"' not in idx_html:
    idx_html = idx_html.replace('</head>', '    <link rel="icon" type="image/svg+xml" href="favicon.svg">\n    <link rel="alternate icon" type="image/png" href="favicon.png">\n</head>')

# Add Author's Note before <!-- SECTION 3: FIELD DISPATCHES (Projects) -->
authors_note = """        <!-- SECTION 2.5: AUTHOR'S NOTE -->
        <section
          id="authors-note"
          class="section"
          style="border-bottom: 4px solid var(--rule-dark); padding: 40px 0; background: var(--paper-warm);"
        >
          <div class="newspaper-grid">
            <div class="col-span-12">
              <div
                style="
                  border: 2px solid var(--rule-dark);
                  background: var(--paper-bright);
                  padding: 35px 40px;
                  box-shadow: 4px 4px 0px rgba(0, 0, 0, 0.06);
                "
              >
                <div style="border-bottom: 2px solid var(--rule-dark); padding-bottom: 12px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center;">
                  <span class="kicker-label" style="color: var(--stamp); font-size: 13px; letter-spacing: 1.5px; margin: 0;">EDITORIAL DISPATCH</span>
                  <span class="meta uppercase" style="font-weight: bold;">AUTHOR’S NOTE</span>
                </div>
                
                <h3 class="heading-lg" style="margin-bottom: 18px; font-size: 26px;">Author’s Note</h3>
                
                <p class="body-lg" style="line-height: 1.8; margin-bottom: 16px;">
                  I’m <b>Ajitesh Sharma</b>, a Computer Science student with a curiosity for understanding how technology works beneath the surface—and a habit of turning that curiosity into things I can build.
                </p>
                
                <p class="body-lg" style="line-height: 1.8; margin-bottom: 16px;">
                  My interests sit at the intersection of <b>software engineering, cybersecurity, and intelligent systems</b>. I enjoy working on problems where there is more to solve than simply writing code: designing systems, understanding how components interact, making them reliable, and figuring out what happens when things don’t go as planned.
                </p>
                
                <p class="body-lg" style="line-height: 1.8; margin-bottom: 16px;">
                  Along the way, I’ve built projects ranging from <b>behavioral anomaly detection</b> to <b>encrypted traffic analysis</b>, while gaining hands-on experience with backend development, system design, and security. Some of my work has also led to <b>patent filings and research in IEEE conferences</b>, giving me the opportunity to explore ideas beyond the classroom.
                </p>
                
                <p class="body-lg" style="line-height: 1.8; margin-bottom: 16px;">
                  This website is a collection of that journey—<b>the projects I’ve built, the problems I’ve explored, the things I’ve learned, and a few ideas still in progress.</b>
                </p>
                
                <p class="body-lg" style="line-height: 1.8; margin-bottom: 24px;">
                  I’m still early in the story, but that’s precisely what makes it interesting.
                </p>
                
                <div style="border-top: 1px solid var(--rule); padding-top: 18px; display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 10px;">
                  <div>
                    <p class="bold" style="font-family: var(--font-display); font-size: 20px; color: var(--ink); margin: 0 0 4px 0;">— Ajitesh Sharma</p>
                    <p class="meta" style="font-style: italic; color: #555; margin: 0;">Computer Science &middot; Builder &middot; Researcher &middot; Curious by default</p>
                  </div>
                  <span class="meta uppercase" style="background: var(--ink); color: var(--paper-bright); padding: 4px 10px; font-size: 10px; font-weight: bold; border-radius: 2px;">DISPATCH CERTIFIED</span>
                </div>
              </div>
            </div>
          </div>
        </section>

"""

if 'id="authors-note"' not in idx_html:
    idx_html = idx_html.replace('<!-- SECTION 3: FIELD DISPATCHES (Projects) -->', authors_note + '        <!-- SECTION 3: FIELD DISPATCHES (Projects) -->')

with open('index.html', 'w') as f:
    f.write(idx_html)

print("Updated index.html with Author's Note and favicon!")

# 2. Update pages/patents.html
with open('pages/patents.html', 'r') as f:
    p_html = f.read()

p_html = p_html.replace('Pending / Under Review (Indian Patent Office)', 'Published (Indian Patent Office)')
if 'rel="icon"' not in p_html:
    p_html = p_html.replace('</head>', '    <link rel="icon" type="image/svg+xml" href="../favicon.svg">\n    <link rel="alternate icon" type="image/png" href="../favicon.png">\n</head>')

with open('pages/patents.html', 'w') as f:
    f.write(p_html)

print("Updated pages/patents.html with Published status and favicon!")

# 3. Update pages/sentinel-stream.html
with open('pages/sentinel-stream.html', 'r') as f:
    s_html = f.read()

# Replace hackathon line with high-impact production description
old_honeywell_line = "This became my submission to Honeywell's own Q4 hackathon problem statement on behavioral anomaly detection."
new_impact_line = "Designed as a production-grade behavioral security engine capable of evaluating millions of high-velocity event streams with sub-millisecond classification latency and strict bounded memory."

s_html = s_html.replace(old_honeywell_line, new_impact_line)
if 'rel="icon"' not in s_html:
    s_html = s_html.replace('</head>', '    <link rel="icon" type="image/svg+xml" href="../favicon.svg">\n    <link rel="alternate icon" type="image/png" href="../favicon.png">\n</head>')

with open('pages/sentinel-stream.html', 'w') as f:
    f.write(s_html)

print("Updated pages/sentinel-stream.html with high-impact replacement line and favicon!")

# 4. Add favicon to all other subpages
subpages = ['cipherpulse.html', 'snapseat.html', 'nutrivision.html', 'internship.html', 'paper-compsac.html', 'certifications.html']
for page in subpages:
    path = os.path.join('pages', page)
    if os.path.exists(path):
        with open(path, 'r') as f:
            content = f.read()
        if 'rel="icon"' not in content:
            content = content.replace('</head>', '    <link rel="icon" type="image/svg+xml" href="../favicon.svg">\n    <link rel="alternate icon" type="image/png" href="../favicon.png">\n</head>')
            with open(path, 'w') as f:
                f.write(content)
            print(f"Added favicon to {path}")
