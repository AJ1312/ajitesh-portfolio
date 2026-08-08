import os

# 1. Update pages/patents.html
with open('pages/patents.html', 'r') as f:
    p_html = f.read()

p_html = p_html.replace('Published (Indian Patent Office)', 'Filed (Indian Patent Office)')
p_html = p_html.replace('PATENT 1 &middot; PUBLISHED', 'PATENT 1 &middot; FILED')
p_html = p_html.replace('PATENT 2 &middot; PUBLISHED', 'PATENT 2 &middot; FILED')
p_html = p_html.replace('PATENT 3 &middot; PUBLISHED', 'PATENT 3 &middot; FILED')

with open('pages/patents.html', 'w') as f:
    f.write(p_html)
print("Updated pages/patents.html to FILED status!")

# 2. Update index.html
with open('index.html', 'r') as f:
    idx_html = f.read()

# Only change the patent badges in the patents list, keeping IEEE Compsac as ACCEPTED
old_patents_block = """              <ul style="list-style: none; padding: 0">
                <li
                  style="
                    margin-bottom: 20px;
                    border-bottom: 1px solid var(--rule);
                    padding-bottom: 15px;
                  "
                >
                  <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 6px;">
                    <span
                      class="meta"
                      style="
                        color: var(--stamp);
                        border: 1px solid var(--stamp);
                        padding: 2px 6px;
                        font-size: 11px;
                        font-weight: bold;
                      "
                      >PUBLISHED</span
                    >
                    <span class="meta" style="font-weight: bold; color: var(--ink-soft);">App No: 202641072750 &middot; 2026</span>
                  </div>
                  <p class="body-lg bold" style="margin-top: 4px; line-height: 1.4;">
                    Cognitive-State-Aware Adaptive Information Security Enforcement System
                  </p>
                </li>
                <li
                  style="
                    margin-bottom: 20px;
                    border-bottom: 1px solid var(--rule);
                    padding-bottom: 15px;
                  "
                >
                  <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 6px;">
                    <span
                      class="meta"
                      style="
                        color: var(--stamp);
                        border: 1px solid var(--stamp);
                        padding: 2px 6px;
                        font-size: 11px;
                        font-weight: bold;
                      "
                      >PUBLISHED</span
                    >
                    <span class="meta" style="font-weight: bold; color: var(--ink-soft);">App No: 202541027783 &middot; 2026</span>
                  </div>
                  <p class="body-lg bold" style="margin-top: 4px; line-height: 1.4;">
                    Multi-Domain Feature Fusion Based Deep Learning System for Audio Deepfake Detection
                  </p>
                </li>
                <li style="margin-bottom: 20px">
                  <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 6px;">
                    <span
                      class="meta"
                      style="
                        color: var(--stamp);
                        border: 1px solid var(--stamp);
                        padding: 2px 6px;
                        font-size: 11px;
                        font-weight: bold;
                      "
                      >PUBLISHED</span
                    >
                    <span class="meta" style="font-weight: bold; color: var(--ink-soft);">App No: 2025411318 &middot; 2025</span>
                  </div>
                  <p class="body-lg bold" style="margin-top: 4px; line-height: 1.4;">
                    System for Lip-Sync Authenticity Detection Using Spatial, Spectral, and Feature Fusion
                  </p>
                </li>
              </ul>"""

new_patents_block = """              <ul style="list-style: none; padding: 0">
                <li
                  style="
                    margin-bottom: 20px;
                    border-bottom: 1px solid var(--rule);
                    padding-bottom: 15px;
                  "
                >
                  <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 6px;">
                    <span
                      class="meta"
                      style="
                        color: var(--stamp);
                        border: 1px solid var(--stamp);
                        padding: 2px 6px;
                        font-size: 11px;
                        font-weight: bold;
                      "
                      >FILED</span
                    >
                    <span class="meta" style="font-weight: bold; color: var(--ink-soft);">App No: 202641072750 &middot; 2026</span>
                  </div>
                  <p class="body-lg bold" style="margin-top: 4px; line-height: 1.4;">
                    Cognitive-State-Aware Adaptive Information Security Enforcement System
                  </p>
                </li>
                <li
                  style="
                    margin-bottom: 20px;
                    border-bottom: 1px solid var(--rule);
                    padding-bottom: 15px;
                  "
                >
                  <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 6px;">
                    <span
                      class="meta"
                      style="
                        color: var(--stamp);
                        border: 1px solid var(--stamp);
                        padding: 2px 6px;
                        font-size: 11px;
                        font-weight: bold;
                      "
                      >FILED</span
                    >
                    <span class="meta" style="font-weight: bold; color: var(--ink-soft);">App No: 202541027783 &middot; 2026</span>
                  </div>
                  <p class="body-lg bold" style="margin-top: 4px; line-height: 1.4;">
                    Multi-Domain Feature Fusion Based Deep Learning System for Audio Deepfake Detection
                  </p>
                </li>
                <li style="margin-bottom: 20px">
                  <div style="display: flex; gap: 8px; align-items: center; margin-bottom: 6px;">
                    <span
                      class="meta"
                      style="
                        color: var(--stamp);
                        border: 1px solid var(--stamp);
                        padding: 2px 6px;
                        font-size: 11px;
                        font-weight: bold;
                      "
                      >FILED</span
                    >
                    <span class="meta" style="font-weight: bold; color: var(--ink-soft);">App No: 2025411318 &middot; 2025</span>
                  </div>
                  <p class="body-lg bold" style="margin-top: 4px; line-height: 1.4;">
                    System for Lip-Sync Authenticity Detection Using Spatial, Spectral, and Feature Fusion
                  </p>
                </li>
              </ul>"""

idx_html = idx_html.replace(old_patents_block, new_patents_block)

with open('index.html', 'w') as f:
    f.write(idx_html)
print("Updated index.html patents to FILED status!")
