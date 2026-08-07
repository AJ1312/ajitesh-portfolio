import re

html_start = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ajitesh Sharma — Software Engineer · Systems Security · Applied AI/ML</title>
    
    <meta name="description" content="The Sharma Dispatch: Editorial portfolio of Ajitesh Sharma. Software Engineer specializing in Systems, Security, and Applied AI/ML based in Vellore, India.">
    <meta name="keywords" content="Ajitesh Sharma, Software Engineer, Systems Builder, C++, Deep Packet Inspection, Machine Learning, Applied AI/ML, VIT Vellore">
    <meta name="author" content="Ajitesh Sharma">
    
    <meta property="og:title" content="Ajitesh Sharma — The Engineering Record of a Systems Builder">
    <meta property="og:description" content="Portfolio of Ajitesh Sharma: Systems Security, C++17 DPI engines, and AI safety research.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://ajiteshsharma.com">
    <meta property="og:image" content="images/portrait.jpg">
    
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>A</text></svg>">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400;1,700&display=swap" rel="stylesheet">
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
    
    <link rel="stylesheet" href="css/styles.css">
</head>
<body class="newspaper-theme">
    
    <div class="container">
        <!-- SECTION 1: MASTHEAD HEADER -->
        <header class="masthead section-rule--double" style="margin-top: 20px;">
            <!-- Top Utility -->
            <div class="newspaper-grid" style="border-bottom: 1px solid var(--rule); padding: 5px 0;">
                <div class="col-span-12 meta uppercase" style="display:flex; justify-content: space-between;">
                    <span>BY THE ENGINEERING DESK &middot; REPORTING FROM VELLORE, BETWEEN LABS AND TERMINALS</span>
                    <span><a href="#projects">Read the Dispatches &rarr;</a> &nbsp;&nbsp; <a href="#contact">Get in Touch</a></span>
                </div>
            </div>
            
            <!-- Title -->
            <div class="text-center" style="padding: 40px 0 20px 0; border-bottom: 1px solid var(--rule);">
                <h1 class="display-xl rv" style="margin-bottom: 5px;">Ajitesh Sharma</h1>
                <p class="meta rv">THE ENGINEERING RECORD OF A SYSTEMS BUILDER</p>
            </div>
            
            <!-- Dateline -->
            <div class="newspaper-grid" style="border-bottom: 1px solid var(--rule); padding: 10px 0;">
                <div class="col-span-4 meta text-left">THURSDAY 7 AUGUST 2026 &middot; VOL. I</div>
                <div class="col-span-4 meta text-center">SELECTED WORKS &amp; NOTES</div>
                <div class="col-span-4 meta text-right">PRICE: ONE SSH SESSION</div>
            </div>
            
            <!-- Nav -->
            <nav class="nav" id="main-nav" style="border-bottom: 4px solid var(--rule-dark); padding: 15px 0;">
                <div class="newspaper-grid" style="align-items: center;">
                    <div class="col-span-6 heading-md" style="margin:0;">Ajitesh Sharma</div>
                    <div class="col-span-6" style="display: flex; justify-content: flex-end; gap: 25px; align-items: center;">
                        <a href="#projects" class="meta bold">WORK</a>
                        <a href="#stack" class="meta bold">STACK</a>
                        <a href="#contact" class="meta bold">CONTACT</a>
                        <a href="#contact" style="background: var(--ink); color: var(--paper); padding: 6px 16px;" class="meta bold">HIRE HIM</a>
                    </div>
                </div>
            </nav>
        </header>

        <main class="dispatch-content">
            
            <!-- SECTION 2: HERO / FRONT PAGE -->
            <section id="front-page" class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 40px 0;">
                <div class="newspaper-grid">
                    <!-- Left side (headline) - 6 columns -->
                    <div class="col-span-6 column-bordered">
                        <div style="display:flex; justify-content: space-between; border-bottom: 1px solid var(--rule); padding-bottom: 10px; margin-bottom: 30px;">
                            <span class="meta uppercase">FRONT PAGE</span>
                            <span class="meta uppercase">FILED UNDER: OPEN INVESTIGATIONS</span>
                        </div>
                        
                        <p class="kicker-label rv">CASE NO. 43 &mdash; FINDINGS PUBLISHED</p>
                        <h2 class="display-lg rv" style="margin-bottom: 30px; letter-spacing: -1.5px; line-height: 1.05;">
                            A systems engineer<br>who builds things &mdash;<br><i class="italic">kernel to cloud.</i>
                        </h2>
                        
                        <div class="newspaper-grid" style="margin-top: 40px;">
                            <div class="col-span-6">
                                <p class="body-lg italic rv" style="border-left: 2px solid var(--ink); padding-left: 15px; margin-bottom: 20px;">
                                    Three years in: Ajitesh Sharma builds high-throughput DPI engines, and deploys streaming anomaly detectors.
                                </p>
                                <p class="meta rv" style="border-bottom: 1px solid var(--rule); padding-bottom: 15px; margin-bottom: 15px;">BY THE ENGINEERING DESK &middot; REPORTING FROM VELLORE</p>
                                <div class="rv" style="display: flex; gap: 10px;">
                                    <a href="#projects" class="meta bold" style="background: var(--ink); color: var(--paper); padding: 12px 16px; border: 1px solid var(--ink);">READ THE WORK &rarr;</a>
                                    <a href="#contact" class="meta bold" style="background: transparent; color: var(--ink); padding: 12px 16px; border: 1px solid var(--ink);">GET IN TOUCH</a>
                                </div>
                            </div>
                            <div class="col-span-6 rv">
                                <p class="body">Currently completing his B.Tech in Computer Science (Information Security) at VIT Vellore.</p>
                                <p class="body" style="margin-top: 15px;">He interned at Hindalco Industries (Aditya Birla Group), digitizing workforce scheduling for 1,200+ site personnel.</p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Right side (image and text) - 6 columns -->
                    <div class="col-span-6" style="padding-left: 30px;">
                        <figure class="rv" style="border: 1px solid var(--rule-dark); padding: 5px; background: var(--paper-bright);">
                            <img src="images/portrait.jpg" alt="Ajitesh Sharma Portrait" style="width: 100%; height: auto; border: 1px solid var(--rule-dark); filter: grayscale(100%) contrast(1.1);">
                        </figure>
                        <p class="meta rv" style="margin-top: 8px;">PICTURED: the subject, in his natural habitat.</p>
                        
                        <div style="margin-top: 30px;" class="newspaper-grid">
                            <div class="col-span-12">
                                <p class="body rv">
                                    <span class="dropcap">H</span>e builds things that inspect, detect, and protect. His work spans C++17 deep packet inspection engines, O(1)-memory streaming anomaly detectors, and containerized microservices platforms.
                                </p>
                                <p class="body rv" style="margin-top: 15px;">
                                    When he's not writing lock-free code, he's publishing on AI safety at IEEE or filing Indian patent applications for systems that don't exist yet.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
"""

with open('index.html', 'r') as f:
    orig = f.read()

# We'll just replace the <header> and <section id="front-page">
import re
new_html = re.sub(r'<header class="masthead">.*?</header>\s*<main class="dispatch-content">\s*<!-- SECTION 2: HERO / FRONT PAGE -->\s*<section id="front-page".*?</section>', html_start, orig, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(new_html)
