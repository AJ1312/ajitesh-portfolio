import os

CSS_STYLES = """
        /* 10/10 MASTERPIECE CYBERSECURITY COCKPIT & EDITORIAL SYSTEM */
        .pill-tag {
            display: inline-block;
            background: var(--ink);
            color: var(--paper-bright);
            padding: 6px 14px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-right: 6px;
            margin-bottom: 8px;
            border-radius: 3px;
        }

        /* BENCHMARKS METRICS GRID */
        .metrics-grid-4 {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin: 25px 0;
        }
        .metric-card-styled {
            background: #ffffff;
            border: 2px solid var(--rule-dark);
            box-shadow: 4px 4px 0px rgba(0,0,0,0.06);
            padding: 24px 18px;
            text-align: center;
            border-radius: 4px;
            transition: transform 0.2s ease;
        }
        .metric-card-styled:hover {
            transform: translateY(-2px);
        }
        .metric-num-bold {
            font-family: var(--font-display);
            font-size: 42px;
            font-weight: 900;
            color: var(--stamp);
            margin-bottom: 6px;
            line-height: 1.05;
        }
        .metric-title-upper {
            font-weight: 700;
            text-transform: uppercase;
            font-size: 12px;
            letter-spacing: 0.6px;
            margin-bottom: 8px;
            color: var(--ink);
        }
        .metric-text-desc {
            font-size: 13px;
            color: #555555;
            line-height: 1.45;
        }

        /* KEY DECISION CALLOUT */
        .decision-card-exec {
            background: #ffffff;
            border-left: 6px solid var(--stamp);
            border-top: 2px solid var(--rule-dark);
            border-right: 2px solid var(--rule-dark);
            border-bottom: 2px solid var(--rule-dark);
            box-shadow: 4px 4px 0px rgba(0,0,0,0.05);
            padding: 30px 34px;
            margin: 35px 0;
            border-radius: 4px;
        }

        /* INTERACTIVE FORENSIC COCKPIT WORKBENCH */
        .cockpit-suite-box {
            border: 2px solid var(--rule-dark);
            background: #090d16;
            color: #f8fafc;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 12px 30px -5px rgba(0, 0, 0, 0.4);
            margin: 35px 0;
            font-family: var(--font-mono, monospace);
        }
        .cockpit-bar-mac {
            background: #111827;
            padding: 12px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid #1f2937;
        }
        .terminal-dots {
            display: flex;
            gap: 8px;
        }
        .dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }
        .dot-red { background: #ef4444; }
        .dot-yellow { background: #f59e0b; }
        .dot-green { background: #10b981; }
        .cockpit-body {
            padding: 24px;
        }
        .cockpit-btn-row {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
        }
        .cockpit-btn-action {
            background: #1e293b;
            color: #e2e8f0;
            border: 1px solid #334155;
            padding: 10px 18px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-radius: 4px;
            transition: all 0.2s ease;
            font-family: var(--font-body);
        }
        .cockpit-btn-action:hover, .cockpit-btn-action.active {
            background: #dc2626;
            border-color: #dc2626;
            color: #ffffff;
            box-shadow: 0 0 14px rgba(220, 38, 38, 0.5);
        }

        /* LIVE TELEMETRY DASHBOARD GRID */
        .telemetry-grid {
            display: grid;
            grid-template-columns: 2fr 3fr;
            gap: 18px;
            margin-bottom: 20px;
        }
        .telemetry-panel {
            background: #030712;
            border: 1px solid #1f2937;
            padding: 16px 20px;
            border-radius: 6px;
        }
        .telemetry-header {
            font-size: 11px;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            font-weight: bold;
            margin-bottom: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .gauge-number-big {
            font-size: 34px;
            font-weight: 900;
            line-height: 1;
            margin-bottom: 6px;
        }
        .gauge-bar-track {
            width: 100%;
            height: 8px;
            background: #1f2937;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 10px;
        }
        .gauge-bar-fill {
            height: 100%;
            transition: width 0.5s ease, background-color 0.5s ease;
        }
        .feature-bar-row {
            margin-bottom: 10px;
        }
        .feature-bar-label {
            display: flex;
            justify-content: space-between;
            font-size: 11px;
            margin-bottom: 4px;
            color: #cbd5e1;
        }
        .feature-bar-track {
            width: 100%;
            height: 6px;
            background: #1f2937;
            border-radius: 3px;
            overflow: hidden;
        }
        .feature-bar-fill {
            height: 100%;
            background: #38bdf8;
            transition: width 0.4s ease;
        }

        /* LIVE LOG CONSOLE */
        .cockpit-log-output {
            background: #020617;
            color: #38bdf8;
            padding: 14px 18px;
            border-radius: 6px;
            border: 1px solid #1e293b;
            font-size: 12px;
            line-height: 1.6;
            margin-bottom: 20px;
            min-height: 55px;
        }

        /* AUDIT TABLE */
        .cockpit-table {
            width: 100%;
            border-collapse: collapse;
            font-family: var(--font-body);
            font-size: 13px;
            background: #ffffff;
            color: #0f172a;
            border-radius: 6px;
            overflow: hidden;
            border: 1px solid #334155;
        }
        .cockpit-table th {
            background: #111827;
            color: #f8fafc;
            padding: 12px 14px;
            text-align: left;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.6px;
        }
        .cockpit-table td {
            padding: 12px 14px;
            border-bottom: 1px solid #e2e8f0;
            line-height: 1.45;
        }
        .anim-fade-row {
            animation: fadeInRow 0.4s ease-out forwards;
        }
        @keyframes fadeInRow {
            from {
                opacity: 0;
                transform: translateY(-8px);
                background-color: #fef08a;
            }
            to {
                opacity: 1;
                transform: translateY(0);
                background-color: transparent;
            }
        }

        /* INTERACTIVE STEPPER TABS FOR PIPELINE */
        .stepper-nav-row {
            display: flex;
            gap: 8px;
            overflow-x: auto;
            padding-bottom: 10px;
            margin-bottom: 20px;
            border-bottom: 2px solid var(--rule);
        }
        .stepper-tab-btn {
            background: var(--paper-warm);
            border: 2px solid var(--rule-dark);
            color: var(--ink);
            padding: 12px 18px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-radius: 4px;
            white-space: nowrap;
            transition: all 0.2s ease;
        }
        .stepper-tab-btn:hover, .stepper-tab-btn.active {
            background: var(--ink);
            color: var(--paper);
            border-color: var(--ink);
        }
        .stepper-detail-card {
            background: #ffffff;
            border: 2px solid var(--rule-dark);
            box-shadow: 4px 4px 0px rgba(0,0,0,0.06);
            padding: 28px 32px;
            border-radius: 6px;
            margin-bottom: 20px;
        }
        .algo-code-box {
            background: #0f172a;
            color: #38bdf8;
            padding: 16px 20px;
            border-radius: 4px;
            font-family: var(--font-mono, monospace);
            font-size: 13px;
            line-height: 1.6;
            margin: 16px 0;
            overflow-x: auto;
            border: 1px solid #1e293b;
        }

        /* BADGES */
        .badge-red {
            display: inline-block;
            padding: 3px 8px;
            background: #fee2e2;
            color: #dc2626;
            border: 1px solid #dc2626;
            font-weight: 700;
            font-size: 11px;
            border-radius: 3px;
        }
        .badge-amber {
            display: inline-block;
            padding: 3px 8px;
            background: #fef3c7;
            color: #d97706;
            border: 1px solid #d97706;
            font-weight: 700;
            font-size: 11px;
            border-radius: 3px;
        }
        .badge-green {
            display: inline-block;
            padding: 3px 8px;
            background: #dcfce7;
            color: #15803d;
            border: 1px solid #15803d;
            font-weight: 700;
            font-size: 11px;
            border-radius: 3px;
        }

        @media screen and (max-width: 900px) {
            .metrics-grid-4 {
                grid-template-columns: repeat(2, 1fr);
            }
            .telemetry-grid {
                grid-template-columns: 1fr;
            }
        }
        @media screen and (max-width: 600px) {
            .metrics-grid-4 {
                grid-template-columns: 1fr;
            }
        }
"""

def generate_page(title, content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — The Sharma Dispatch</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400;1,700&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
    <link rel="stylesheet" href="../css/styles.css">
    <style>
{CSS_STYLES}
    </style>
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
{content}
        </main>
        
        <!-- FOOTER -->
        <footer class="section" style="border-top: 4px solid var(--rule-dark); padding: 40px 0; margin-top: 60px;">
            <div class="newspaper-grid">
                <div class="col-span-12 text-center">
                    <p class="meta uppercase">&copy; 2026 Ajitesh Sharma &middot; The Sharma Dispatch &mdash; Vol. I</p>
                </div>
            </div>
        </footer>
    </div>
</body>
</html>
"""

# Now write the files using generate_page
from build_elite_workstations import SENTINEL_CONTENT, CIPHERPULSE_CONTENT

with open('pages/sentinel-stream.html', 'w') as f:
    f.write(generate_page('SENTINEL-STREAM', SENTINEL_CONTENT))

with open('pages/cipherpulse.html', 'w') as f:
    f.write(generate_page('CipherPulse', CIPHERPULSE_CONTENT))

print("Fixed CSS template and rebuilt Sentinel-Stream and CipherPulse pages!")
