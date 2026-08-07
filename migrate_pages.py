import os
import re

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | The Sharma Dispatch</title>
    <meta name="description" content="Portfolio of Ajitesh Sharma">
    
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>A</text></svg>">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400;1,700&display=swap" rel="stylesheet">
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
    
    <link rel="stylesheet" href="../css/styles.css">
</head>
<body class="newspaper-theme">
    <div class="container">
        
        <!-- SUBPAGE HEADER -->
        <header class="masthead section-rule--double" style="margin-top: 20px;">
            <nav class="nav" id="main-nav" style="border-bottom: 4px solid var(--rule-dark); padding: 15px 0;">
                <div class="newspaper-grid" style="align-items: center;">
                    <div class="col-span-6 heading-md" style="margin:0;"><a href="../index.html" style="text-decoration: none; color: inherit;">&larr; THE SHARMA DISPATCH</a></div>
                    <div class="col-span-6" style="display: flex; justify-content: flex-end; gap: 25px; align-items: center;">
                        <a href="../index.html#projects" class="meta bold">WORK</a>
                        <a href="../index.html#contact" class="meta bold">CONTACT</a>
                        <a href="mailto:hello@ajiteshsharma.dev" style="background: var(--ink); color: var(--paper); padding: 6px 16px;" class="meta bold">HIRE HIM</a>
                    </div>
                </div>
            </nav>
        </header>

        <main class="dispatch-content">
            {content}
        </main>
        
        <!-- FOOTER -->
        <footer class="section" style="border-top: 4px solid var(--rule-dark); padding: 40px 0;">
            <div class="newspaper-grid">
                <div class="col-span-12 text-center rv">
                    <p class="meta uppercase">&copy; 2026 Ajitesh Sharma &middot; The Sharma Dispatch &mdash; Vol. I</p>
                </div>
            </div>
        </footer>
    </div>
    
    <script src="../js/main.js" defer></script>
    <script src="../js/animations.js" defer></script>
    <script src="../js/simulations.js" defer></script>
</body>
</html>
"""

def process_file(filepath):
    with open(filepath, 'r') as f:
        html = f.read()

    # Extract title
    title_match = re.search(r'<title>(.*?)\s*\|', html)
    title = title_match.group(1) if title_match else "Dispatch"

    # Extract Hero info
    hero_kicker = re.search(r'<div class="hero-kicker[^>]*>(.*?)</div>', html, re.DOTALL)
    kicker_text = hero_kicker.group(1).strip() if hero_kicker else "DISPATCH"
    
    hero_title = re.search(r'<h1 class="hero-title[^>]*>(.*?)</h1>', html, re.DOTALL)
    title_text = hero_title.group(1).strip() if hero_title else title
    
    hero_sub = re.search(r'<h2 class="hero-subtitle[^>]*>(.*?)</h2>', html, re.DOTALL)
    sub_text = hero_sub.group(1).strip() if hero_sub else ""

    content = f"""
            <!-- HERO -->
            <section class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <p class="kicker-label rv">{kicker_text}</p>
                        <h1 class="display-xl rv" style="margin-bottom: 20px;">{title_text}</h1>
                        <p class="display-sm rv" style="max-width: 800px;">{sub_text}</p>
                    </div>
                </div>
            </section>
    """

    # Extract Incident/Description if any
    incident = re.search(r'<section class="project-incident[^>]*>.*?<p class="drop-cap">(.*?)</p>', html, re.DOTALL)
    if incident:
        content += f"""
            <!-- DETAILS -->
            <section class="section" style="border-bottom: 1px solid var(--rule); padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <h3 class="heading-lg" style="margin-bottom: 20px;">The Incident</h3>
                        <p class="body-lg rv"><span class="dropcap">{incident.group(1)[0]}</span>{incident.group(1)[1:]}</p>
                    </div>
                </div>
            </section>
        """

    # Add terminal if present
    terminal = re.search(r'<div class="simulation-wrapper.*?>(.*?)</div>\s*<script>', html, re.DOTALL)
    if terminal:
        content += f"""
            <!-- SIMULATION -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12 rv" style="background: var(--ink); color: var(--paper); padding: 20px;">
                        <h3 class="meta" style="margin-bottom: 20px;">LIVE TELEMETRY</h3>
                        {terminal.group(1)}
                    </div>
                </div>
            </section>
        """

    # Write new file
    new_html = PAGE_TEMPLATE.replace("{title}", title).replace("{content}", content)
    
    with open(filepath, 'w') as f:
        f.write(new_html)

for filename in os.listdir('pages'):
    if filename.endswith('.html'):
        process_file(os.path.join('pages', filename))
