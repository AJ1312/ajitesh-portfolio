import os
import re

def replace_classes(filepath):
    with open(filepath, 'r') as f:
        html = f.read()

    # Nav Replacement
    nav_pattern = r'<nav class="site-nav.*?</nav>'
    new_nav = """<header class="masthead section-rule--double" style="margin-top: 20px;">
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
        </header>"""
    html = re.sub(nav_pattern, new_nav, html, flags=re.DOTALL)

    # Class mappings
    replacements = {
        r'class="editorial-theme page-transition"': 'class="newspaper-theme"',
        r'class="[^"]*font-serif text-6xl[^"]*"': 'class="display-xl rv"',
        r'class="[^"]*font-sans text-xl md:text-3xl font-medium text-ink[^"]*"': 'class="display-sm rv"',
        r'class="[^"]*font-mono text-sm uppercase tracking-widest muted[^"]*"': 'class="kicker-label rv"',
        r'class="[^"]*font-serif text-3xl[^"]*"': 'class="display-md"',
        r'class="[^"]*font-sans text-xl font-bold uppercase[^"]*"': 'class="heading-md"',
        r'class="[^"]*font-serif text-xl leading-relaxed text-ink[^"]*"': 'class="body-lg"',
        r'class="[^"]*font-sans text-base text-ink-muted[^"]*"': 'class="body"',
        r'class="[^"]*grid grid-cols-1 md:grid-cols-12[^"]*"': 'class="newspaper-grid"',
        r'class="[^"]*grid grid-cols-1 md:grid-cols-2[^"]*"': 'class="newspaper-grid"',
        r'class="[^"]*md:col-span-4[^"]*"': 'class="col-span-4 column-bordered"',
        r'class="[^"]*md:col-span-8[^"]*"': 'class="col-span-8"',
        r'class="[^"]*md:col-span-6[^"]*"': 'class="col-span-6 column-bordered"',
        r'bg-ink text-paper': 'style="background: var(--ink); color: var(--paper);"',
        r'bg-paper': '',
        r'border-bottom-double': 'section-rule--double',
        r'border-bottom-triple': 'section-rule--double',
        r'border-bottom border-ink': 'style="border-bottom: 1px solid var(--rule);"',
        r'border-top border-ink': 'style="border-top: 1px solid var(--rule);"',
        r'border-left border-right border-ink': 'style="border-left: 1px solid var(--rule); border-right: 1px solid var(--rule);"',
        r'border-right border-ink': 'style="border-right: 1px solid var(--rule);"',
        r'section-padding': 'style="padding: 40px 0;"',
        r'container wrapper-lg': '',
        r'container wrapper-md': '',
        r'container wrapper-xl': '',
    }
    
    for old, new in replacements.items():
        html = re.sub(old, new, html)

    # Footer Replacement
    footer_pattern = r'<footer class="site-footer.*?</footer\s*>'
    new_footer = """<footer class="section" style="border-top: 4px solid var(--rule-dark); padding: 40px 0;">
            <div class="newspaper-grid">
                <div class="col-span-12 text-center rv">
                    <p class="meta uppercase">&copy; 2026 Ajitesh Sharma &middot; The Sharma Dispatch &mdash; Vol. I</p>
                </div>
            </div>
        </footer>"""
    html = re.sub(footer_pattern, new_footer, html, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(html)

for filename in os.listdir('pages'):
    if filename.endswith('.html'):
        replace_classes(os.path.join('pages', filename))
