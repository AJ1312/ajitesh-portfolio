import os, glob, re

# 1. Clean all stray / malformed tags in <head> across all HTML files
all_html_files = ['index.html'] + glob.glob('pages/*.html')

for filepath in all_html_files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Remove any dangling text tags, svg tags, or malformed data-uri leftovers
    content = re.sub(r'\s*<text y=.*?A</text></svg>">\s*', '\n', content)
    content = re.sub(r'\s*href="data:image/svg\+xml.*?A</text></svg>">\s*', '\n', content)
    content = re.sub(r'\s*<link rel="icon" href="data:image/svg\+xml.*?>\s*', '\n', content)
    
    # Ensure clean standard favicons
    if filepath == 'index.html':
        fav_block = '    <link rel="icon" type="image/svg+xml" href="favicon.svg">\n    <link rel="alternate icon" type="image/png" href="favicon.png">'
    else:
        fav_block = '    <link rel="icon" type="image/svg+xml" href="../favicon.svg">\n    <link rel="alternate icon" type="image/png" href="../favicon.png">'
    
    # Clean duplicate favicon links if any
    content = re.sub(r'(\s*<link rel="(icon|alternate icon)"[^>]+>)+', '', content)
    content = content.replace('</head>', f'{fav_block}\n</head>')
    
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Cleaned head tags in {filepath}")

# 2. Update index.html
with open('index.html', 'r') as f:
    idx = f.read()

# Update SeatSnap -> SnapSeat in index.html
idx = idx.replace('SeatSnap', 'SnapSeat')

# Update Patents list in index.html with exact titles and App numbers
old_patents_list = """              <ul style="list-style: none; padding: 0">
                <li
                  style="
                    margin-bottom: 20px;
                    border-bottom: 1px solid var(--rule);
                    padding-bottom: 15px;
                  "
                >
                  <span
                    class="meta"
                    style="
                      color: var(--stamp);
                      border: 1px solid var(--stamp);
                      padding: 2px 6px;
                      font-size: 11px;
                    "
                    >PUBLISHED</span
                  >
                  <p class="body-lg bold" style="margin-top: 8px">
                    System and Method for O(1) Memory Streaming Anomaly
                    Detection
                  </p>
                </li>
                <li
                  style="
                    margin-bottom: 20px;
                    border-bottom: 1px solid var(--rule);
                    padding-bottom: 15px;
                  "
                >
                  <span
                    class="meta"
                    style="
                      color: var(--stamp);
                      border: 1px solid var(--stamp);
                      padding: 2px 6px;
                      font-size: 11px;
                    "
                    >PUBLISHED</span
                  >
                  <p class="body-lg bold" style="margin-top: 8px">
                    Audio Deepfake Detection via Shannon Entropy
                  </p>
                </li>
                <li style="margin-bottom: 20px">
                  <span
                    class="meta"
                    style="
                      color: var(--stamp);
                      border: 1px solid var(--stamp);
                      padding: 2px 6px;
                      font-size: 11px;
                    "
                    >PUBLISHED</span
                  >
                  <p class="body-lg bold" style="margin-top: 8px">
                    Real-time Lip-Sync Detection using Visual CNNs
                  </p>
                </li>
              </ul>"""

new_patents_list = """              <ul style="list-style: none; padding: 0">
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

if old_patents_list in idx:
    idx = idx.replace(old_patents_list, new_patents_list)
else:
    # Use regex or partial replace
    print("Replacing patents section in index.html...")
    idx = re.sub(r'<ul style="list-style: none; padding: 0">.*?</ul>', new_patents_list.strip(), idx, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(idx)
print("Updated index.html with SnapSeat and exact patent names!")

# 3. Update pages/snapseat.html
with open('pages/snapseat.html', 'r') as f:
    ss_content = f.read()

ss_content = ss_content.replace('SeatSnap', 'SnapSeat')
with open('pages/snapseat.html', 'w') as f:
    f.write(ss_content)
print("Updated pages/snapseat.html to SnapSeat!")

# 4. Update pages/patents.html with full rich details, exact titles, application numbers, and years
patents_html_full = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Filed Indian Patents | The Sharma Dispatch</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400;1,700&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
    <link rel="stylesheet" href="../css/styles.css">
    <style>
        .patent-badge-row {
            display: flex;
            gap: 12px;
            align-items: center;
            flex-wrap: wrap;
            margin-bottom: 12px;
        }
        .patent-tag-pill {
            background: var(--stamp);
            color: #ffffff;
            font-size: 11px;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 3px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .patent-app-pill {
            background: var(--ink);
            color: var(--paper-bright);
            font-family: var(--font-mono, monospace);
            font-size: 11px;
            font-weight: 600;
            padding: 3px 8px;
            border-radius: 3px;
        }
    </style>
    <link rel="icon" type="image/svg+xml" href="../favicon.svg">
    <link rel="alternate icon" type="image/png" href="../favicon.png">
</head>
<body class="newspaper-theme">
    <div class="container" style="max-width: 1100px;">
        
        <!-- SUBPAGE HEADER -->
        <header class="masthead" style="margin-top: 20px;">
            <nav class="nav" id="main-nav" style="border-bottom: 4px solid var(--rule-dark); padding: 15px 0;">
                <div class="newspaper-grid" style="align-items: center;">
                    <div class="col-span-6 heading-md" style="margin:0;"><a href="../index.html" style="text-decoration: none; color: inherit;">&larr; THE SHARMA DISPATCH</a></div>
                    <div class="col-span-6" style="display: flex; justify-content: flex-end; gap: 20px; align-items: center;">
                        <a href="../index.html#projects" class="meta bold">WORK</a>
                        <a href="../index.html#contact" class="meta bold">CONTACT</a>
                        <a href="mailto:hello@ajiteshsharma.dev" style="background: var(--ink); color: var(--paper); padding: 6px 16px; border-radius: 2px;" class="meta bold">HIRE HIM</a>
                    </div>
                </div>
            </nav>
        </header>

        <main class="dispatch-content">
            
            <!-- HERO -->
            <section class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <p class="kicker-label rv">ARCHITECTURAL DISCLOSURES</p>
                        <h1 class="display-xl rv" style="margin-bottom: 20px;">Filed Indian Patents</h1>
                        <p class="display-sm rv" style="max-width: 850px;">Public Technical Overviews of Cognitive Security Systems, Audio Deepfake Forensics, and Lip-Sync Verification.</p>
                        
                        <div class="newspaper-grid" style="margin-top: 30px; border-top: 1px solid var(--rule); padding-top: 20px;">
                            <div class="col-span-4 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">STATUS</p>
                                <p class="body-sm">Published (Indian Patent Office)</p>
                            </div>
                            <div class="col-span-4 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">DOMAIN</p>
                                <p class="body-sm">Information Security, Deepfake Detection, Adaptive UI</p>
                            </div>
                            <div class="col-span-4 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">DISCLAIMER</p>
                                <p class="body-sm">Visuals reflect high-level conceptual pipelines. Enabling equations, exact thresholds, and implementation internals are omitted.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- PATENT 1: COGNITIVE STATE -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12 rv">
                        <div class="patent-badge-row">
                            <span class="patent-tag-pill">PATENT 1 &middot; PUBLISHED</span>
                            <span class="patent-app-pill">App No: 202641072750 &middot; 2026</span>
                            <span class="meta" style="font-weight: bold;">Indian Patent Application (2026)</span>
                        </div>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0; font-size: 30px; line-height: 1.25;">Cognitive-State-Aware Adaptive Information Security Enforcement System</h3>
                        <p class="body-lg" style="margin-bottom: 30px; line-height: 1.7;">A non-biometric, content-agnostic middleware architecture that processes user interaction dynamics (typing, navigation, rhythm) to infer cognitive load and vulnerability state, dynamically escalating security friction.</p>
                    </div>
                    
                    <div class="col-span-12 rv">
                        <div class="featured-image rv" style="filter: grayscale(100%) contrast(1.1); border: 2px solid var(--rule-dark);"><img src="../images/cognitive_security_patent_1786102065871.jpg" alt="Cognitive-State-Aware Adaptive Information Security Architecture" style="width:100%;"></div>
                    </div>
                </div>
            </section>

            <!-- PATENT 2: AUDIO DEEPFAKE -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12 rv">
                        <div class="patent-badge-row">
                            <span class="patent-tag-pill">PATENT 2 &middot; PUBLISHED</span>
                            <span class="patent-app-pill">App No: 202541027783 &middot; 2026</span>
                            <span class="meta" style="font-weight: bold;">Indian Patent Application (2026)</span>
                        </div>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0; font-size: 30px; line-height: 1.25;">Multi-Domain Feature Fusion Based Deep Learning System for Audio Deepfake Detection</h3>
                        <p class="body-lg" style="margin-bottom: 30px; line-height: 1.7;">An architecture designed for robustness to acoustic noise and unseen manipulation conditions using multi-domain representation learning across Spectral, Cepstral, and Raw Temporal domains.</p>
                    </div>
                    
                    <div class="col-span-12 rv">
                        <div class="featured-image rv" style="filter: grayscale(100%) contrast(1.1); border: 2px solid var(--rule-dark);"><img src="../images/audio_deepfake_patent_1786102079124.jpg" alt="Audio Deepfake Detection Patent Architecture" style="width:100%;"></div>
                    </div>
                </div>
            </section>

            <!-- PATENT 3: LIP-SYNC -->
            <section class="section" style="padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12 rv">
                        <div class="patent-badge-row">
                            <span class="patent-tag-pill">PATENT 3 &middot; PUBLISHED</span>
                            <span class="patent-app-pill">App No: 2025411318 &middot; 2025</span>
                            <span class="meta" style="font-weight: bold;">Indian Patent Application (2025)</span>
                        </div>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0; font-size: 30px; line-height: 1.25;">System for Lip-Sync Authenticity Detection Using Spatial, Spectral, and Feature Fusion</h3>
                        <p class="body-lg" style="margin-bottom: 30px; line-height: 1.7;">A dual-path forensic architecture analyzing visual-only data (no audio required) by combining a learned visual attention CNN with handcrafted spatial and spectral forensic analysis to detect desynchronization artifacts.</p>
                    </div>
                    
                    <div class="col-span-12 rv">
                        <div class="featured-image rv" style="filter: grayscale(100%) contrast(1.1); border: 2px solid var(--rule-dark);"><img src="../images/lipsync_detection_patent_1786102092150.jpg" alt="Lip-Sync Authenticity Detection Patent Architecture" style="width:100%;"></div>
                    </div>
                </div>
            </section>

        </main>
        
        <!-- FOOTER -->
        <footer class="section" style="border-top: 4px solid var(--rule-dark); padding: 40px 0; margin-top: 40px;">
            <div class="newspaper-grid">
                <div class="col-span-12 text-center rv">
                    <p class="meta uppercase">&copy; 2026 Ajitesh Sharma &middot; The Sharma Dispatch &mdash; Vol. I</p>
                    <p class="body-sm" style="margin-top: 10px;">High-level architectures; implementation-specific patent details omitted for compliance.</p>
                </div>
            </div>
        </footer>
    </div>
    
    <script src="../js/main.js" defer></script>
    <script src="../js/animations.js" defer></script>
</body>
</html>
"""

with open('pages/patents.html', 'w') as f:
    f.write(patents_html_full)
print("Updated pages/patents.html with exact patent titles, application numbers, and years!")
