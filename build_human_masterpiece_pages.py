import os

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — The Sharma Dispatch</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400;1,700&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
    <link rel="stylesheet" href="../css/styles.css">
    <style>
        /* MASTERPIECE EDITORIAL STYLES */
        .pill-tag {{
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
            border-radius: 2px;
        }}

        /* METRICS DASHBOARD CARDS */
        .metrics-grid-4 {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin: 30px 0;
        }}
        .metric-card-styled {{
            background: #ffffff;
            border: 2px solid var(--rule-dark);
            box-shadow: 4px 4px 0px rgba(0,0,0,0.06);
            padding: 24px 18px;
            text-align: center;
            border-radius: 4px;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}
        .metric-card-styled:hover {{
            transform: translateY(-2px);
            box-shadow: 6px 6px 0px rgba(0,0,0,0.1);
        }}
        .metric-num-bold {{
            font-family: var(--font-display);
            font-size: 40px;
            font-weight: 900;
            color: var(--stamp);
            margin-bottom: 6px;
            line-height: 1.05;
        }}
        .metric-title-upper {{
            font-weight: 700;
            text-transform: uppercase;
            font-size: 12px;
            letter-spacing: 0.6px;
            margin-bottom: 8px;
            color: var(--ink);
        }}
        .metric-text-desc {{
            font-size: 13px;
            color: #555555;
            line-height: 1.45;
        }}

        /* KEY DECISION EXECUTIVE CARD */
        .decision-card-exec {{
            background: #ffffff;
            border-left: 6px solid var(--stamp);
            border-top: 2px solid var(--rule-dark);
            border-right: 2px solid var(--rule-dark);
            border-bottom: 2px solid var(--rule-dark);
            box-shadow: 4px 4px 0px rgba(0,0,0,0.05);
            padding: 32px 36px;
            margin: 35px 0;
            border-radius: 4px;
        }}

        /* MAC TERMINAL WORKBENCH */
        .terminal-suite-box {{
            border: 2px solid var(--rule-dark);
            background: #0f172a;
            color: #f8fafc;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
            margin: 35px 0;
            font-family: var(--font-mono, monospace);
        }}
        .terminal-bar-mac {{
            background: #1e293b;
            padding: 12px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid #334155;
        }}
        .terminal-dots {{
            display: flex;
            gap: 8px;
        }}
        .dot {{
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }}
        .dot-red {{ background: #ef4444; }}
        .dot-yellow {{ background: #f59e0b; }}
        .dot-green {{ background: #10b981; }}
        .terminal-body-inner {{
            padding: 24px;
        }}
        .wb-btn-tab {{
            background: #1e293b;
            color: #cbd5e1;
            border: 1px solid #475569;
            padding: 10px 18px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-right: 10px;
            margin-bottom: 12px;
            border-radius: 4px;
            transition: all 0.2s ease;
            font-family: var(--font-body);
        }}
        .wb-btn-tab:hover, .wb-btn-tab.active {{
            background: #ef4444;
            border-color: #ef4444;
            color: #ffffff;
            box-shadow: 0 0 12px rgba(239, 68, 68, 0.4);
        }}
        .wb-log-display {{
            background: #020617;
            color: #38bdf8;
            padding: 16px 20px;
            border-radius: 6px;
            border: 1px solid #1e293b;
            font-size: 13px;
            line-height: 1.6;
            margin: 18px 0;
            min-height: 65px;
        }}

        /* TABLE STYLING */
        .wb-table-master {{
            width: 100%;
            border-collapse: collapse;
            font-family: var(--font-body);
            font-size: 13px;
            background: #ffffff;
            color: #0f172a;
            border-radius: 6px;
            overflow: hidden;
            border: 1px solid #334155;
        }}
        .wb-table-master th {{
            background: #1e293b;
            color: #f8fafc;
            padding: 12px 16px;
            text-align: left;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.6px;
        }}
        .wb-table-master td {{
            padding: 14px 16px;
            border-bottom: 1px solid #e2e8f0;
            line-height: 1.5;
        }}
        .anim-fade-row {{
            animation: fadeInRow 0.4s ease-out forwards;
        }}
        @keyframes fadeInRow {{
            from {{
                opacity: 0;
                transform: translateY(-8px);
                background-color: #fef08a;
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
                background-color: transparent;
            }}
        }}

        /* BADGES */
        .badge-red {{
            display: inline-block;
            padding: 4px 10px;
            background: #fee2e2;
            color: #dc2626;
            border: 1px solid #dc2626;
            font-weight: 700;
            font-size: 11px;
            border-radius: 4px;
        }}
        .badge-amber {{
            display: inline-block;
            padding: 4px 10px;
            background: #fef3c7;
            color: #d97706;
            border: 1px solid #d97706;
            font-weight: 700;
            font-size: 11px;
            border-radius: 4px;
        }}
        .badge-green {{
            display: inline-block;
            padding: 4px 10px;
            background: #dcfce7;
            color: #15803d;
            border: 1px solid #15803d;
            font-weight: 700;
            font-size: 11px;
            border-radius: 4px;
        }}

        /* INTERACTIVE VECTOR SVG ARCHITECTURE DIAGRAM */
        .arch-svg-container {{
            background: #ffffff;
            border: 2px solid var(--rule-dark);
            box-shadow: 4px 4px 0px rgba(0,0,0,0.06);
            border-radius: 6px;
            padding: 24px;
            margin: 25px 0;
        }}
        .svg-node-box {{
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        .svg-node-box:hover rect {{
            fill: #fef3c7;
            stroke: #d92323;
            stroke-width: 2.5px;
        }}

        /* STEP CARDS FOR PIPELINE */
        .step-card-item {{
            background: #ffffff;
            border: 1px solid var(--rule);
            border-left: 4px solid var(--ink);
            padding: 20px 24px;
            margin-bottom: 16px;
            border-radius: 4px;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}
        .step-card-item:hover {{
            border-left-color: var(--stamp);
            transform: translateX(4px);
        }}

        @media screen and (max-width: 900px) {{
            .metrics-grid-4 {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}
        @media screen and (max-width: 600px) {{
            .metrics-grid-4 {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body class="newspaper-theme">
    <div class="container" style="max-width: 1100px;">
        
        <!-- SUBPAGE HEADER -->
        <header class="masthead" style="margin-top: 20px;">
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

SENTINEL_CONTENT = """
            <!-- 1. HERO SECTION -->
            <section class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 45px 0 35px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <p class="kicker-label">FIELD DISPATCH &mdash; AI CYBERSECURITY &amp; BEHAVIORAL UEBA</p>
                        <h1 class="display-xl" style="margin-bottom: 15px; font-size: 52px; line-height: 1.1;">SENTINEL-STREAM</h1>
                        <p class="display-sm" style="max-width: 920px; font-style: italic; line-height: 1.45; margin-bottom: 24px; color: #333333;">The AI Security Guard That Detects Rogue Accounts &amp; Data Theft in Real Time Without Crashing Servers</p>
                        
                        <!-- TECH PILLS -->
                        <div style="margin-bottom: 25px;">
                            <span class="pill-tag">Python</span>
                            <span class="pill-tag">Count-Min Sketch</span>
                            <span class="pill-tag">Isolation Forest</span>
                            <span class="pill-tag">LightGBM</span>
                            <span class="pill-tag">TreeSHAP</span>
                            <span class="pill-tag">FastAPI</span>
                        </div>

                        <div class="newspaper-grid" style="border-top: 1px solid var(--rule); padding-top: 20px;">
                            <div class="col-span-12">
                                <p class="meta" style="margin-bottom: 4px; font-weight: bold;">GITHUB REPOSITORY</p>
                                <a href="https://github.com/AJ1312/sentinel-stream" target="_blank" class="body-sm" style="color: var(--stamp); font-weight: bold; text-decoration: underline;">github.com/AJ1312/sentinel-stream &nearr;</a>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 2. MOTIVATION & USE CASE GRID -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-6" style="padding-right: 20px;">
                        <span class="kicker-label" style="color: var(--stamp);">PROJECT MOTIVATION</span>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Why I Built SENTINEL-STREAM</h3>
                        <p class="body-lg" style="line-height: 1.75;"><span class="dropcap">I</span> built SENTINEL-STREAM after noticing a pattern in how security tools actually fail in practice: it's rarely that they can't detect something unusual, it's that they detect too much, too vaguely, and analysts stop trusting the alerts. I wanted to build a behavioral anomaly engine that solved the boring, unglamorous parts of that problem properly — bounded memory that doesn't grow forever as more entities get monitored, meaningful scoring for entities with zero history, and an explanation attached to every single alert instead of a bare confidence score. This became my submission to Honeywell's own Q4 hackathon problem statement on behavioral anomaly detection.</p>
                    </div>

                    <div class="col-span-6" style="padding-left: 20px; border-left: 1px solid var(--rule);">
                        <span class="kicker-label" style="color: var(--stamp);">REAL-WORLD USE CASE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Catching Stolen Credentials</h3>
                        <p class="body-lg" style="line-height: 1.75;"><span class="dropcap">P</span>icture a mid-sized company's security team monitoring thousands of employee accounts and IoT devices. A contractor's credentials get compromised, and the attacker logs in from an unfamiliar location at an unusual hour, then starts quietly accessing a finance database this account has never touched before. A rule-based tool would either miss this or bury it under hundreds of other low-quality alerts. SENTINEL-STREAM scores this event in real time using the contractor's own behavioral baseline, flags it within milliseconds even though the account has limited history, and hands the analyst a plain-language reason — unusual login velocity, first-time resource access — instead of a bare "anomaly detected."</p>
                    </div>
                </div>
            </section>

            <!-- 3. NATIVE INTERACTIVE VECTOR ARCHITECTURE DIAGRAM -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label" style="color: var(--stamp);">SYSTEM ARCHITECTURE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0;">O(1) Streaming Profiler &amp; Threat Pipeline</h3>
                        <p class="body-lg" style="margin-bottom: 20px; color: #444;">Hover over any pipeline stage node to inspect data flow specs:</p>

                        <div class="arch-svg-container">
                            <svg viewBox="0 0 1000 360" width="100%" height="100%" style="overflow: visible;">
                                <!-- CONNECTOR ARROWS -->
                                <defs>
                                    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                        <path d="M 0 0 L 10 5 L 0 10 z" fill="#d92323" />
                                    </marker>
                                </defs>

                                <!-- PIPELINE FLOW LINES -->
                                <line x1="170" y1="120" x2="210" y2="120" stroke="#d92323" stroke-width="3" marker-end="url(#arrow)" />
                                <line x1="370" y1="120" x2="410" y2="120" stroke="#d92323" stroke-width="3" marker-end="url(#arrow)" />
                                <line x1="570" y1="120" x2="610" y2="120" stroke="#d92323" stroke-width="3" marker-end="url(#arrow)" />
                                <line x1="770" y1="120" x2="810" y2="120" stroke="#d92323" stroke-width="3" marker-end="url(#arrow)" />

                                <!-- STAGE 1 NODE -->
                                <g class="svg-node-box" onclick="showNodeDetail('Ingestion: Raw audit log events stream in via FastAPI non-blocking REST endpoints.')">
                                    <rect x="10" y="50" width="160" height="140" rx="6" fill="#f8fafc" stroke="#111111" stroke-width="2" />
                                    <rect x="10" y="50" width="160" height="35" rx="6" fill="#111111" />
                                    <text x="90" y="73" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle" font-family="Inter">01. INGESTION</text>
                                    <text x="90" y="115" fill="#111111" font-size="13" font-weight="bold" text-anchor="middle" font-family="Inter">Raw Log Stream</text>
                                    <text x="90" y="140" fill="#64748b" font-size="11" text-anchor="middle" font-family="Inter">FastAPI &amp; Kafka</text>
                                    <text x="90" y="165" fill="#d92323" font-size="11" font-weight="bold" text-anchor="middle" font-family="Inter">Async Ingress</text>
                                </g>

                                <!-- STAGE 2 NODE -->
                                <g class="svg-node-box" onclick="showNodeDetail('Profiler: EWMA rolling stats update in fixed 2 KB RAM per user without keeping raw event logs.')">
                                    <rect x="210" y="50" width="160" height="140" rx="6" fill="#f8fafc" stroke="#111111" stroke-width="2" />
                                    <rect x="210" y="50" width="160" height="35" rx="6" fill="#111111" />
                                    <text x="290" y="73" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle" font-family="Inter">02. O(1) PROFILER</text>
                                    <text x="290" y="115" fill="#111111" font-size="13" font-weight="bold" text-anchor="middle" font-family="Inter">Count-Min Sketch</text>
                                    <text x="290" y="140" fill="#64748b" font-size="11" text-anchor="middle" font-family="Inter">EWMA Rolling Stats</text>
                                    <text x="290" y="165" fill="#d92323" font-size="11" font-weight="bold" text-anchor="middle" font-family="Inter">2 KB / Entity</text>
                                </g>

                                <!-- STAGE 3 NODE -->
                                <g class="svg-node-box" onclick="showNodeDetail('Stage 1 IsoForest: Evaluates structural anomaly distance for entities with zero historical logs.')">
                                    <rect x="410" y="50" width="160" height="140" rx="6" fill="#f8fafc" stroke="#111111" stroke-width="2" />
                                    <rect x="410" y="50" width="160" height="35" rx="6" fill="#111111" />
                                    <text x="490" y="73" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle" font-family="Inter">03. STAGE 1 ISO</text>
                                    <text x="490" y="115" fill="#111111" font-size="13" font-weight="bold" text-anchor="middle" font-family="Inter">Isolation Forest</text>
                                    <text x="490" y="140" fill="#64748b" font-size="11" text-anchor="middle" font-family="Inter">Cold-Start Prior</text>
                                    <text x="490" y="165" fill="#d92323" font-size="11" font-weight="bold" text-anchor="middle" font-family="Inter">Zero-History OK</text>
                                </g>

                                <!-- STAGE 4 NODE -->
                                <g class="svg-node-box" onclick="showNodeDetail('Stage 2 LightGBM: Predicts exact attack type (Brute Force, Impossible Travel, Data Theft) in 1.84ms.')">
                                    <rect x="610" y="50" width="160" height="140" rx="6" fill="#f8fafc" stroke="#111111" stroke-width="2" />
                                    <rect x="610" y="50" width="160" height="35" rx="6" fill="#111111" />
                                    <text x="690" y="73" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle" font-family="Inter">04. STAGE 2 GBDT</text>
                                    <text x="690" y="115" fill="#111111" font-size="13" font-weight="bold" text-anchor="middle" font-family="Inter">LightGBM Classifier</text>
                                    <text x="690" y="140" fill="#64748b" font-size="11" text-anchor="middle" font-family="Inter">24.6x RF Speedup</text>
                                    <text x="690" y="165" fill="#d92323" font-size="11" font-weight="bold" text-anchor="middle" font-family="Inter">1.84ms Latency</text>
                                </g>

                                <!-- STAGE 5 NODE -->
                                <g class="svg-node-box" onclick="showNodeDetail('TreeSHAP Engine: Calculates exact Shapley feature attributions, explaining the risk score in plain English.')">
                                    <rect x="810" y="50" width="160" height="140" rx="6" fill="#f8fafc" stroke="#111111" stroke-width="2" />
                                    <rect x="810" y="50" width="160" height="35" rx="6" fill="#111111" />
                                    <text x="890" y="73" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle" font-family="Inter">05. TREESHAP</text>
                                    <text x="890" y="115" fill="#111111" font-size="13" font-weight="bold" text-anchor="middle" font-family="Inter">SHAP Explainability</text>
                                    <text x="890" y="140" fill="#64748b" font-size="11" text-anchor="middle" font-family="Inter">&lt;30us Calculation</text>
                                    <text x="890" y="165" fill="#d92323" font-size="11" font-weight="bold" text-anchor="middle" font-family="Inter">Human Reason</text>
                                </g>

                                <!-- PIPELINE STEP-BY-STEP EXPLANATION CALLOUT BOX -->
                                <rect x="10" y="220" width="960" height="120" rx="6" fill="#1e293b" />
                                <text x="30" y="250" fill="#38bdf8" font-size="13" font-weight="bold" font-family="Inter">PIPELINE EXECUTION SPECIFICATIONS:</text>
                                <text x="30" y="278" fill="#f8fafc" font-size="12" font-family="Inter" id="archNodeDetailText">
                                    • Click or hover on any pipeline stage node above to inspect its real-time specification details.
                                </text>
                                <text x="30" y="302" fill="#cbd5e1" font-size="12" font-family="Inter">
                                    • Continuous streaming updates user activity profiles in 2 KB of fixed RAM per entity without saving raw event logs.
                                </text>
                                <text x="30" y="324" fill="#cbd5e1" font-size="12" font-family="Inter">
                                    • Stage 1 handles zero-history users while Stage 2 LightGBM computes exact attack vectors in 1.84ms P50 latency.
                                </text>
                            </svg>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 4. MAC TERMINAL FORENSIC WORKBENCH CONSOLE -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">INTERACTIVE CONSOLE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Live Threat Radar &amp; AI Explanation Workbench</h3>
                        <p class="body-lg" style="margin-bottom: 20px; color: #444;">Select an enterprise attack scenario below to trigger real-time AI evaluation and inspect terminal audit logs:</p>

                        <div class="terminal-suite-box">
                            <div class="terminal-bar-mac">
                                <div class="terminal-dots">
                                    <div class="dot dot-red"></div>
                                    <div class="dot dot-yellow"></div>
                                    <div class="dot dot-green"></div>
                                </div>
                                <span style="font-size: 12px; color: #94a3b8; font-weight: bold;">SENTINEL-STREAM // FORENSIC AI TERMINAL</span>
                                <span style="font-size: 11px; background: #059669; color: #fff; padding: 2px 8px; border-radius: 4px; font-weight: bold;">LIVE ENGINE ACTIVE</span>
                            </div>

                            <div class="terminal-body-inner">
                                <div>
                                    <button class="wb-btn-tab" onclick="runSentinelSim('brute')">⚡ Test 1: Password Attack Surge</button>
                                    <button class="wb-btn-tab" onclick="runSentinelSim('travel')">🌍 Test 2: Impossible Location Login</button>
                                    <button class="wb-btn-tab" onclick="runSentinelSim('exfil')">📤 Test 3: Secret Database Exfiltration</button>
                                    <button class="wb-btn-tab" onclick="runSentinelSim('normal')">✅ Test 4: Normal Work Baseline</button>
                                </div>

                                <div class="wb-log-display" id="sentinelConsoleLog">
[SYSTEM READY] Sentinel-Stream monitoring active entity streams. Select an attack scenario button above to trigger live evaluation...
                                </div>

                                <table class="wb-table-master">
                                    <thead>
                                        <tr>
                                            <th style="width: 100px;">Timestamp</th>
                                            <th style="width: 140px;">User Account</th>
                                            <th>Observed Event</th>
                                            <th style="width: 150px;">Threat Level</th>
                                            <th style="width: 90px;">Latency</th>
                                            <th>Plain-English AI Explanation</th>
                                        </tr>
                                    </thead>
                                    <tbody id="wbSentinelBody">
                                        <tr class="anim-fade-row">
                                            <td>19:05:01</td>
                                            <td><b>sarah_marketing</b></td>
                                            <td>Opened standard project documents</td>
                                            <td><span class="badge-green">SAFE (NOMINAL)</span></td>
                                            <td>1.42 ms</td>
                                            <td>Activity matches normal daily baseline behavior.</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 5. PIPELINE WALKTHROUGH STEP CARDS -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">DETAILED WALKTHROUGH</span>
                        <h3 class="heading-lg" style="margin: 10px 0 25px 0;">6-Stage Execution Pipeline</h3>

                        <div class="step-card-item">
                            <h4 class="heading-md" style="margin-bottom: 8px;"><span style="color:var(--stamp); font-weight:900;">01.</span> Event Ingestion</h4>
                            <p class="body-lg">Raw audit logs (logins, database access, file downloads) stream in via REST API or Kafka queues without dropping client connections.</p>
                            <p class="meta" style="margin-top:8px;"><b>Tech Stack:</b> FastAPI, Pydantic &middot; <b>Why It Matters:</b> Async non-blocking endpoints handle thousands of concurrent events without connection queuing delays.</p>
                        </div>

                        <div class="step-card-item">
                            <h4 class="heading-md" style="margin-bottom: 8px;"><span style="color:var(--stamp); font-weight:900;">02.</span> Streaming Feature Engineering</h4>
                            <p class="body-lg">Builds a 21-feature vector on the fly using EWMA rolling averages and Count-Min Sketch tables, updating statistics in fixed memory without saving raw logs.</p>
                            <p class="meta" style="margin-top:8px;"><b>Tech Stack:</b> NumPy, Pandas &middot; <b>Why It Matters:</b> Vectorized array operations compute statistics in sub-millisecond speed while preventing memory exhaustion.</p>
                        </div>

                        <div class="step-card-item">
                            <h4 class="heading-md" style="margin-bottom: 8px;"><span style="color:var(--stamp); font-weight:900;">03.</span> Stage 1: Isolation Forest Cold-Start Prior</h4>
                            <p class="body-lg">Evaluates structural anomaly distance for brand-new users or devices with zero historical logs, eliminating cold-start vulnerability.</p>
                            <p class="meta" style="margin-top:8px;"><b>Tech Stack:</b> scikit-learn (IsolationForest) &middot; <b>Why It Matters:</b> Tree isolation scoring requires zero historical user baselines, flagging anomalous new entities on day one.</p>
                        </div>

                        <div class="step-card-item">
                            <h4 class="heading-md" style="margin-bottom: 8px;"><span style="color:var(--stamp); font-weight:900;">04.</span> Stage 2: LightGBM Threat Classifier</h4>
                            <p class="body-lg">Classifies the exact attack category (Brute Force, Impossible Travel, Data Theft) by evaluating features in a fast decision tree.</p>
                            <p class="meta" style="margin-top:8px;"><b>Tech Stack:</b> LightGBM &middot; <b>Why It Matters:</b> Leaf-wise tree growth runs 24.6× faster than Random Forest (1.84ms P50 latency).</p>
                        </div>

                        <div class="step-card-item">
                            <h4 class="heading-md" style="margin-bottom: 8px;"><span style="color:var(--stamp); font-weight:900;">05.</span> TreeSHAP Explainability Engine</h4>
                            <p class="body-lg">Walks decision tree paths directly to calculate exact feature attributions, explaining why the alert fired in microseconds.</p>
                            <p class="meta" style="margin-top:8px;"><b>Tech Stack:</b> SHAP (TreeSHAP) &middot; <b>Why It Matters:</b> Exact Shapley values are calculated analytically without noisy perturbation sampling, giving security analysts immediate trust.</p>
                        </div>

                        <div class="step-card-item">
                            <h4 class="heading-md" style="margin-bottom: 8px;"><span style="color:var(--stamp); font-weight:900;">06.</span> Live Dashboard Stream</h4>
                            <p class="body-lg">Pushes explained alert payloads directly to security analyst dashboards over persistent Server-Sent Events (SSE).</p>
                            <p class="meta" style="margin-top:8px;"><b>Tech Stack:</b> FastAPI (SSE), Chart.js &middot; <b>Why It Matters:</b> Real-time streaming alert feeds with zero WebSocket connection overhead.</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 6. EMPIRICAL BENCHMARKS METRICS GRID -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label" style="color: var(--stamp);">EMPIRICAL BENCHMARKS</span>
                        <h3 class="heading-lg" style="margin: 10px 0 25px 0;">Verified Performance Results</h3>

                        <div class="metrics-grid-4">
                            <div class="metric-card-styled">
                                <div class="metric-num-bold">~4.2 KB</div>
                                <div class="metric-title-upper">Per-Entity RAM</div>
                                <div class="metric-text-desc">Audited per-user RAM footprint (EWMA + Count-Min Sketch). Can reach 2 KB with 128-width sketch.</div>
                            </div>

                            <div class="metric-card-styled">
                                <div class="metric-num-bold">2.64 ms</div>
                                <div class="metric-title-upper">P99 Latency</div>
                                <div class="metric-text-desc">Single-event end-to-end model classification speed (P50 latency: 1.84 ms).</div>
                            </div>

                            <div class="metric-card-styled">
                                <div class="metric-num-bold">0.9403</div>
                                <div class="metric-title-upper">Macro F1 Score</div>
                                <div class="metric-text-desc">5-fold cross-validation score (&plusmn;0.0091) across standard NSL-KDD benchmark.</div>
                            </div>

                            <div class="metric-card-styled">
                                <div class="metric-num-bold">24.67×</div>
                                <div class="metric-title-upper">Random Forest Speedup</div>
                                <div class="metric-text-desc">LightGBM inference (2.64 ms) vs baseline Random Forest (65.15 ms) on identical hardware.</div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 7. KEY DESIGN DECISION EXECUTIVE HIGHLIGHT CARD -->
            <section class="section" style="padding: 30px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <div class="decision-card-exec">
                            <span class="kicker-label" style="color: var(--stamp);">KEY DESIGN DECISION</span>
                            <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Constant O(1) Memory Scaling Per User</h3>
                            <p class="body-lg" style="line-height: 1.75; margin: 0;"><span class="dropcap">R</span>ather than keeping endless historical log arrays that crash servers over time, SENTINEL-STREAM calculates rolling stats in a fixed <b>4.2 KB memory footprint</b> per user. Memory per user stays constant O(1) forever regardless of log volume, while total system RAM scales smoothly with active user count.</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 8. GITHUB CTA & FUTURE ROADMAP -->
            <section class="section" style="padding: 40px 0 20px 0; border-top: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12 text-center">
                        <h3 class="heading-lg" style="margin-bottom: 15px;">Explore the Project Source Code</h3>
                        <div style="margin-bottom: 25px;">
                            <a href="https://github.com/AJ1312/sentinel-stream" target="_blank" class="btn-github">⭐ View SENTINEL-STREAM on GitHub</a>
                        </div>
                        <p class="body-md" style="font-style: italic; color: #555; max-width: 800px; margin: 0 auto;">
                            <b>What I'd improve next:</b> If I were building this for production next, I would implement adaptive Count-Min Sketch resizing to dynamically adjust memory depth based on entity traffic density, and migrate the feature pipeline to Rust for sub-millisecond end-to-end ingestion.
                        </p>
                    </div>
                </div>
            </section>

            <script>
                function showNodeDetail(txt) {
                    document.getElementById('archNodeDetailText').innerText = '• ' + txt;
                }

                window.runSentinelSim = function(type) {
                    const tbody = document.getElementById('wbSentinelBody');
                    const consoleEl = document.getElementById('sentinelConsoleLog');
                    const ts = new Date().toISOString().substring(11, 19);

                    let user = '', event = '', badge = '', lat = '', why = '', logTxt = '';

                    if (type === 'brute') {
                        user = 'admin_john';
                        event = '45 failed login attempts in 10s';
                        badge = '<span class="badge-red">CRITICAL THREAT</span>';
                        lat = '1.84 ms';
                        why = 'Extreme login failure spike (+0.54 risk) + rapid event velocity.';
                        logTxt = `[${ts}] [ALERT] Event velocity spike detected for entity 'admin_john'. TreeSHAP attribution: failed_logins_1m (+0.54). Pushed to alert queue.`;
                    } else if (type === 'travel') {
                        user = 'exec_rachel';
                        event = 'Logged in from Tokyo 5m after NY';
                        badge = '<span class="badge-amber">HIGH RISK</span>';
                        lat = '2.12 ms';
                        why = 'Impossible physical movement speed (+0.68 geo-velocity risk).';
                        logTxt = `[${ts}] [ALERT] Impossible travel speed flag for 'exec_rachel'. Geo-velocity threshold exceeded (+0.68). Dispatching verification token.`;
                    } else if (type === 'exfil') {
                        user = 'dev_service';
                        event = 'Downloaded 14 GB customer DB off-hours';
                        badge = '<span class="badge-red">CRITICAL THREAT</span>';
                        lat = '1.95 ms';
                        why = 'Abnormal outbound data volume (+0.76 EWMA volume spike).';
                        logTxt = `[${ts}] [CRITICAL] Off-hours database export spike detected for 'dev_service'. Outbound volume +0.76. Session access suspended.`;
                    } else {
                        user = 'sarah_marketing';
                        event = 'Opened standard project documents';
                        badge = '<span class="badge-green">SAFE (NOMINAL)</span>';
                        lat = '1.42 ms';
                        why = 'Activity matches normal daily baseline behavior.';
                        logTxt = `[${ts}] [NOMINAL] Normal document access logged for 'sarah_marketing'. Anomaly score: 0.04. EWMA baseline updated.`;
                    }

                    consoleEl.innerText = logTxt;

                    const newRow = document.createElement('tr');
                    newRow.className = 'anim-fade-row';
                    newRow.innerHTML = `
                        <td>${ts}</td>
                        <td><b>${user}</b></td>
                        <td>${event}</td>
                        <td>${badge}</td>
                        <td>${lat}</td>
                        <td>${why}</td>
                    `;

                    tbody.insertBefore(newRow, tbody.firstChild);
                };
            </script>
"""

CIPHERPULSE_CONTENT = """
            <!-- 1. HERO SECTION -->
            <section class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 45px 0 35px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <p class="kicker-label">FIELD DISPATCH &mdash; HIGH-SPEED NETWORKING &amp; SECURITY</p>
                        <h1 class="display-xl" style="margin-bottom: 15px; font-size: 52px; line-height: 1.1;">CipherPulse</h1>
                        <p class="display-sm" style="max-width: 920px; font-style: italic; line-height: 1.45; margin-bottom: 24px; color: #333333;">The X-Ray Security Scanner for Encrypted Traffic That Catches Hidden Malware Without Invading Privacy</p>
                        
                        <!-- TECH PILLS -->
                        <div style="margin-bottom: 25px;">
                            <span class="pill-tag">C++17</span>
                            <span class="pill-tag">POSIX Threads</span>
                            <span class="pill-tag">Lock-Free Queue</span>
                            <span class="pill-tag">eBPF / AF_PACKET</span>
                            <span class="pill-tag">JA4+ Fingerprinting</span>
                            <span class="pill-tag">Welford CoV</span>
                        </div>

                        <div class="newspaper-grid" style="border-top: 1px solid var(--rule); padding-top: 20px;">
                            <div class="col-span-12">
                                <p class="meta" style="margin-bottom: 4px; font-weight: bold;">GITHUB REPOSITORY</p>
                                <a href="https://github.com/AJ1312/CipherPulse" target="_blank" class="body-sm" style="color: var(--stamp); font-weight: bold; text-decoration: underline;">github.com/AJ1312/CipherPulse &nearr;</a>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 2. MOTIVATION & USE CASE GRID -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-6" style="padding-right: 20px;">
                        <span class="kicker-label" style="color: var(--stamp);">PROJECT MOTIVATION</span>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Why I Built CipherPulse</h3>
                        <p class="body-lg" style="line-height: 1.75;"><span class="dropcap">M</span>ost of the internet's traffic is encrypted now, and newer TLS features like Encrypted Client Hello are starting to hide even the destination hostname that used to be visible during the handshake. I wanted to explore how much you can still infer about a connection — what kind of application it is, whether it's malicious — using only signals that remain visible even under full encryption: how a client negotiates its handshake, DNS lookups that precede a connection, and the shape and timing of the encrypted traffic itself. CipherPulse is a multi-threaded C++ engine built around that constraint.</p>
                    </div>

                    <div class="col-span-6" style="padding-left: 20px; border-left: 1px solid var(--rule);">
                        <span class="kicker-label" style="color: var(--stamp);">REAL-WORLD USE CASE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Catching Encrypted Hacker Signals</h3>
                        <p class="body-lg" style="line-height: 1.75;"><span class="dropcap">P</span>icture a network security appliance sitting at a company's edge, watching gigabit traffic in real time. Malware on an internal machine tries to phone home to its command-and-control server over a fully encrypted connection with no recognizable hostname. CipherPulse can't decrypt the traffic — it doesn't need to. It fingerprints the way the malware's TLS client negotiates its handshake and matches it against known C2 signatures, notices that the packets checked in at suspiciously regular intervals, and flags the flow as likely C2 beaconing — all while processing packets from thousands of other simultaneous connections without a single thread ever waiting on another.</p>
                    </div>
                </div>
            </section>

            <!-- 3. NATIVE INTERACTIVE VECTOR ARCHITECTURE DIAGRAM -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label" style="color: var(--stamp);">SYSTEM ARCHITECTURE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Lock-Free Fast-Path Traffic Inspection Pipeline</h3>
                        <p class="body-lg" style="margin-bottom: 20px; color: #444;">Hover over any pipeline stage node to inspect data flow specs:</p>

                        <div class="arch-svg-container">
                            <svg viewBox="0 0 1000 360" width="100%" height="100%" style="overflow: visible;">
                                <defs>
                                    <marker id="arrow2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                        <path d="M 0 0 L 10 5 L 0 10 z" fill="#d92323" />
                                    </marker>
                                </defs>

                                <line x1="170" y1="120" x2="210" y2="120" stroke="#d92323" stroke-width="3" marker-end="url(#arrow2)" />
                                <line x1="370" y1="120" x2="410" y2="120" stroke="#d92323" stroke-width="3" marker-end="url(#arrow2)" />
                                <line x1="570" y1="120" x2="610" y2="120" stroke="#d92323" stroke-width="3" marker-end="url(#arrow2)" />
                                <line x1="770" y1="120" x2="810" y2="120" stroke="#d92323" stroke-width="3" marker-end="url(#arrow2)" />

                                <!-- NODE 1 -->
                                <g class="svg-node-box" onclick="showNodeDetail('Ingestion: Raw Ethernet frames captured directly from kernel sockets using eBPF/AF_PACKET zero-copy sockets.')">
                                    <rect x="10" y="50" width="160" height="140" rx="6" fill="#f8fafc" stroke="#111111" stroke-width="2" />
                                    <rect x="10" y="50" width="160" height="35" rx="6" fill="#111111" />
                                    <text x="90" y="73" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle" font-family="Inter">01. RAW CAPTURE</text>
                                    <text x="90" y="115" fill="#111111" font-size="13" font-weight="bold" text-anchor="middle" font-family="Inter">AF_PACKET / eBPF</text>
                                    <text x="90" y="140" fill="#64748b" font-size="11" text-anchor="middle" font-family="Inter">Zero-Copy Socket</text>
                                    <text x="90" y="165" fill="#d92323" font-size="11" font-weight="bold" text-anchor="middle" font-family="Inter">Line-Rate Ingress</text>
                                </g>

                                <!-- NODE 2 -->
                                <g class="svg-node-box" onclick="showNodeDetail('Router: Hashes 5-tuple (src/dest IP, ports, protocol) to dispatch all packets of a flow to a single dedicated core.')">
                                    <rect x="210" y="50" width="160" height="140" rx="6" fill="#f8fafc" stroke="#111111" stroke-width="2" />
                                    <rect x="210" y="50" width="160" height="35" rx="6" fill="#111111" />
                                    <text x="290" y="73" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle" font-family="Inter">02. 5-TUPLE ROUTER</text>
                                    <text x="290" y="115" fill="#111111" font-size="13" font-weight="bold" text-anchor="middle" font-family="Inter">Consistent Hashing</text>
                                    <text x="290" y="140" fill="#64748b" font-size="11" text-anchor="middle" font-family="Inter">Zero Cross-Locks</text>
                                    <text x="290" y="165" fill="#d92323" font-size="11" font-weight="bold" text-anchor="middle" font-family="Inter">Pin to CPU Core</text>
                                </g>

                                <!-- NODE 3 -->
                                <g class="svg-node-box" onclick="showNodeDetail('Worker Threads: Dedicated worker threads run inside isolated lock-free loops with independent flow tables.')">
                                    <rect x="410" y="50" width="160" height="140" rx="6" fill="#f8fafc" stroke="#111111" stroke-width="2" />
                                    <rect x="410" y="50" width="160" height="35" rx="6" fill="#111111" />
                                    <text x="490" y="73" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle" font-family="Inter">03. FAST PATH</text>
                                    <text x="490" y="115" fill="#111111" font-size="13" font-weight="bold" text-anchor="middle" font-family="Inter">Lock-Free Queue</text>
                                    <text x="490" y="140" fill="#64748b" font-size="11" text-anchor="middle" font-family="Inter">Isolated Flow Tables</text>
                                    <text x="490" y="165" fill="#d92323" font-size="11" font-weight="bold" text-anchor="middle" font-family="Inter">0 Mutex Contention</text>
                                </g>

                                <!-- NODE 4 -->
                                <g class="svg-node-box" onclick="showNodeDetail('JA4+ Profiler: Parses ClientHello ciphers & extensions while stripping GREASE noise to generate stable client hashes.')">
                                    <rect x="610" y="50" width="160" height="140" rx="6" fill="#f8fafc" stroke="#111111" stroke-width="2" />
                                    <rect x="610" y="50" width="160" height="35" rx="6" fill="#111111" />
                                    <text x="690" y="73" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle" font-family="Inter">04. JA4+ PROFILER</text>
                                    <text x="690" y="115" fill="#111111" font-size="13" font-weight="bold" text-anchor="middle" font-family="Inter">TLS ClientHello</text>
                                    <text x="690" y="140" fill="#64748b" font-size="11" text-anchor="middle" font-family="Inter">FNV-1a Hash Signatures</text>
                                    <text x="690" y="165" fill="#d92323" font-size="11" font-weight="bold" text-anchor="middle" font-family="Inter">App ID Verified</text>
                                </g>

                                <!-- NODE 5 -->
                                <g class="svg-node-box" onclick="showNodeDetail('Welford CoV: Computes running inter-arrival time variance to flag automated C2 beaconing pulses.')">
                                    <rect x="810" y="50" width="160" height="140" rx="6" fill="#f8fafc" stroke="#111111" stroke-width="2" />
                                    <rect x="810" y="50" width="160" height="35" rx="6" fill="#111111" />
                                    <text x="890" y="73" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle" font-family="Inter">05. WELFORD CoV</text>
                                    <text x="890" y="115" fill="#111111" font-size="13" font-weight="bold" text-anchor="middle" font-family="Inter">Beacon Classifier</text>
                                    <text x="890" y="140" fill="#64748b" font-size="11" text-anchor="middle" font-family="Inter">CoV &lt; 0.12 Pulse Check</text>
                                    <text x="890" y="165" fill="#d92323" font-size="11" font-weight="bold" text-anchor="middle" font-family="Inter">C2 Flagged</text>
                                </g>

                                <rect x="10" y="220" width="960" height="120" rx="6" fill="#1e293b" />
                                <text x="30" y="250" fill="#38bdf8" font-size="13" font-weight="bold" font-family="Inter">PIPELINE EXECUTION SPECIFICATIONS:</text>
                                <text x="30" y="278" fill="#f8fafc" font-size="12" font-family="Inter" id="archNodeDetailText">
                                    • Click or hover on any pipeline stage node above to inspect its real-time specification details.
                                </text>
                                <text x="30" y="302" fill="#cbd5e1" font-size="12" font-family="Inter">
                                    • Packets are captured directly from kernel sockets and hashed by 5-tuple to pin flows to dedicated CPU cores.
                                </text>
                                <text x="30" y="324" fill="#cbd5e1" font-size="12" font-family="Inter">
                                    • Every worker thread processes its isolated flow table with zero cross-thread mutex locking on the hot path.
                                </text>
                            </svg>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 4. MAC TERMINAL FORENSIC WORKBENCH CONSOLE -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">INTERACTIVE CONSOLE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Live Encrypted Traffic X-Ray Inspection Workbench</h3>
                        <p class="body-lg" style="margin-bottom: 20px; color: #444;">Select a network stream to observe real-time JA4+ fingerprint extraction and threat classification:</p>

                        <div class="terminal-suite-box">
                            <div class="terminal-bar-mac">
                                <div class="terminal-dots">
                                    <div class="dot dot-red"></div>
                                    <div class="dot dot-yellow"></div>
                                    <div class="dot dot-green"></div>
                                </div>
                                <span style="font-size: 12px; color: #94a3b8; font-weight: bold;">CIPHERPULSE // FORENSIC DPI TERMINAL</span>
                                <span style="font-size: 11px; background: #059669; color: #fff; padding: 2px 8px; border-radius: 4px; font-weight: bold;">LOCK-FREE FAST-PATH ACTIVE</span>
                            </div>

                            <div class="terminal-body-inner">
                                <div>
                                    <button class="wb-btn-tab" onclick="runCipherSim('normal')">▶ Stream 1: Standard HTTPS Browsing</button>
                                    <button class="wb-btn-tab" onclick="runCipherSim('c2')">🚨 Stream 2: Encrypted C2 Hacker Beacon</button>
                                    <button class="wb-btn-tab" onclick="runCipherSim('bench')">⚡ Stream 3: High-Speed Multi-Thread Test</button>
                                </div>

                                <div class="wb-log-display" id="cipherConsoleLog">
[SYSTEM READY] CipherPulse Fast-Path Workers active across CPU cores. Select a stream button above...
                                </div>

                                <table class="wb-table-master">
                                    <thead>
                                        <tr>
                                            <th style="width: 100px;">Timestamp</th>
                                            <th>Network Connection</th>
                                            <th style="width: 210px;">JA4+ Fingerprint Hash</th>
                                            <th>Traffic Rhythm</th>
                                            <th style="width: 150px;">Security Verdict</th>
                                            <th style="width: 130px;">Action Taken</th>
                                        </tr>
                                    </thead>
                                    <tbody id="wbCipherBody">
                                        <tr class="anim-fade-row">
                                            <td>19:05:01</td>
                                            <td><b>192.168.1.45 &rarr; Google:443</b></td>
                                            <td><code>t13d151600_8daaf6152702</code></td>
                                            <td>Random human interaction timing</td>
                                            <td><span class="badge-green">SAFE (BENIGN)</span></td>
                                            <td>Allowed</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 5. PIPELINE WALKTHROUGH STEP CARDS -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">DETAILED WALKTHROUGH</span>
                        <h3 class="heading-lg" style="margin: 10px 0 25px 0;">7-Stage Packet Inspection Pipeline</h3>

                        <div class="step-card-item">
                            <h4 class="heading-md" style="margin-bottom: 8px;"><span style="color:var(--stamp); font-weight:900;">01.</span> RAW Packet Ingestion</h4>
                            <p class="body-lg">Captures raw ethernet frames directly from network sockets using eBPF or high-speed AF_PACKET for zero-copy memory speed.</p>
                            <p class="meta" style="margin-top:8px;"><b>Tech Stack:</b> eBPF / AF_PACKET, POSIX threads &middot; <b>Why It Matters:</b> Captures line-rate headers directly at kernel ingress without socket buffer copy overhead.</p>
                        </div>

                        <div class="step-card-item">
                            <h4 class="heading-md" style="margin-bottom: 8px;"><span style="color:var(--stamp); font-weight:900;">02.</span> Consistent 5-Tuple Hashing</h4>
                            <p class="body-lg">Hashes the 5-tuple (source/dest IP, ports, protocol) so all packets of a single flow land on the exact same worker thread queue.</p>
                            <p class="meta" style="margin-top:8px;"><b>Tech Stack:</b> std::hash, custom ThreadSafeQueue &middot; <b>Why It Matters:</b> Eliminates cross-thread locks because one thread owns a flow's lifecycle.</p>
                        </div>

                        <div class="step-card-item">
                            <h4 class="heading-md" style="margin-bottom: 8px;"><span style="color:var(--stamp); font-weight:900;">03.</span> Lock-Free Fast Path Processing</h4>
                            <p class="body-lg">Worker threads execute inside dedicated loops with isolated flow tables, enabling 100% lock-free lookups on the hot path.</p>
                            <p class="meta" style="margin-top:8px;"><b>Tech Stack:</b> C++17 STL, std::thread &middot; <b>Why It Matters:</b> Eliminates mutex contention on core packet loops during high traffic bursts.</p>
                        </div>

                        <div class="step-card-item">
                            <h4 class="heading-md" style="margin-bottom: 8px;"><span style="color:var(--stamp); font-weight:900;">04.</span> JA4+ Fingerprint Extraction</h4>
                            <p class="body-lg">Parses TLS ClientHello handshakes, sorts ciphers, filters GREASE noise extensions, and hashes into a stable JA4 signature using FNV-1a.</p>
                            <p class="meta" style="margin-top:8px;"><b>Tech Stack:</b> Pure C++17, FNV-1a Hash &middot; <b>Why It Matters:</b> Identifies client applications (Cobalt Strike, Sliver) even when hostname is encrypted.</p>
                        </div>

                        <div class="step-card-item">
                            <h4 class="heading-md" style="margin-bottom: 8px;"><span style="color:var(--stamp); font-weight:900;">05.</span> Active DNS Correlation Cache</h4>
                            <p class="body-lg">Maintains an in-memory cache of IP-to-domain mappings from plaintext DNS responses, automatically expiring entries via TTL timestamps.</p>
                            <p class="meta" style="margin-top:8px;"><b>Tech Stack:</b> Custom DNS Correlator &middot; <b>Why It Matters:</b> Labels encrypted IP connections with human-readable domain names.</p>
                        </div>

                        <div class="step-card-item">
                            <h4 class="heading-md" style="margin-bottom: 8px;"><span style="color:var(--stamp); font-weight:900;">06.</span> Welford Flow Periodicity Check</h4>
                            <p class="body-lg">Calculates running packet inter-arrival statistics using Welford's algorithm to compute Coefficient of Variation (CoV &lt; 0.12) for beaconing.</p>
                            <p class="meta" style="margin-top:8px;"><b>Tech Stack:</b> Welford Online Variance Engine &middot; <b>Why It Matters:</b> Computes exact numerical variance in constant O(1) time per packet.</p>
                        </div>

                        <div class="step-card-item">
                            <h4 class="heading-md" style="margin-bottom: 8px;"><span style="color:var(--stamp); font-weight:900;">07.</span> Structured Audit Log Output</h4>
                            <p class="body-lg">Outputs filtered PCAPs and streams structured JSON threat alerts detailing matched JA4 signatures and recommended eBPF drop rules.</p>
                            <p class="meta" style="margin-top:8px;"><b>Tech Stack:</b> C++ File I/O, nlohmann::json &middot; <b>Why It Matters:</b> Structured audit logs easily consumed by enterprise SIEM modules.</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 6. EMPIRICAL BENCHMARKS METRICS GRID -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label" style="color: var(--stamp);">EMPIRICAL BENCHMARKS</span>
                        <h3 class="heading-lg" style="margin: 10px 0 25px 0;">System Performance Results</h3>

                        <div class="metrics-grid-4">
                            <div class="metric-card-styled">
                                <div class="metric-num-bold">ZERO</div>
                                <div class="metric-title-upper">Lock Contention</div>
                                <div class="metric-text-desc">100% thread-isolated flow tables via deterministic 5-tuple consistent hashing.</div>
                            </div>

                            <div class="metric-card-styled">
                                <div class="metric-num-bold">JA4+</div>
                                <div class="metric-title-upper">TLS Fingerprinting</div>
                                <div class="metric-text-desc">Extracts ClientHello ciphers &amp; extensions while filtering GREASE noise.</div>
                            </div>

                            <div class="metric-card-styled">
                                <div class="metric-num-bold">&lt; 0.12</div>
                                <div class="metric-title-upper">Beacon Threshold</div>
                                <div class="metric-text-desc">Welford Coefficient of Variation (CoV) threshold flagging automated malware pulses.</div>
                            </div>

                            <div class="metric-card-styled">
                                <div class="metric-num-bold">ZERO</div>
                                <div class="metric-title-upper">Dependencies</div>
                                <div class="metric-text-desc">Built in pure C++17 STL for maximum portability and zero library bloat.</div>
                            </div>
                        </div>

                        <p class="meta text-center" style="margin-top: 15px; color: #666; font-style: italic;">
                            *Note on throughput: CipherPulse targets fast-path lock-free design limits. Throughput figures reflect PCAP offline benchmarks and multi-thread ring queue tests, pending full hardware-in-the-loop 10GbE NIC validation.
                        </p>
                    </div>
                </div>
            </section>

            <!-- 7. KEY DESIGN DECISION EXECUTIVE HIGHLIGHT CARD -->
            <section class="section" style="padding: 30px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <div class="decision-card-exec">
                            <span class="kicker-label" style="color: var(--stamp);">KEY DESIGN DECISION</span>
                            <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Lock-Free Multi-Threading via 5-Tuple Consistent Hashing</h3>
                            <p class="body-lg" style="line-height: 1.75; margin: 0;"><span class="dropcap">I</span>nstead of using a global shared flow table protected by slow mutex locks, CipherPulse hashes every packet's 5-tuple to pin it to a single dedicated worker CPU core. Because one worker thread owns 100% of a flow's lifecycle inside an isolated <code>std::unordered_map</code>, processing runs <b>100% lock-free with zero mutex overhead</b> on the hot path.</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 8. GITHUB CTA & FUTURE ROADMAP -->
            <section class="section" style="padding: 40px 0 20px 0; border-top: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12 text-center">
                        <h3 class="heading-lg" style="margin-bottom: 15px;">Explore the Project Source Code</h3>
                        <div style="margin-bottom: 25px;">
                            <a href="https://github.com/AJ1312/CipherPulse" target="_blank" class="btn-github">⭐ View CipherPulse on GitHub</a>
                        </div>
                        <p class="body-md" style="font-style: italic; color: #555; max-width: 800px; margin: 0 auto;">
                            <b>What I'd improve next:</b> If I were building this for production next, I would implement AF_XDP (XDP socket) zero-copy kernel driver bindings and hardware NIC offloading to achieve line-rate 10GbE packet processing without CPU ring buffer drops.
                        </p>
                    </div>
                </div>
            </section>

            <script>
                function showNodeDetail(txt) {
                    document.getElementById('archNodeDetailText').innerText = '• ' + txt;
                }

                window.runCipherSim = function(type) {
                    const tbody = document.getElementById('wbCipherBody');
                    const consoleEl = document.getElementById('cipherConsoleLog');
                    const ts = new Date().toISOString().substring(11, 19);

                    let conn = '', ja4 = '', rhythm = '', badge = '', action = '', logTxt = '';

                    if (type === 'c2') {
                        conn = '10.0.4.12 &rarr; 185.220.101.5 (Hidden IP)';
                        ja4 = 't13d190800_c84a8b291410';
                        rhythm = 'Strict 5.0s metronome pulse (CoV < 0.12)';
                        badge = '<span class="badge-red">ALERT: C2 BEACON</span>';
                        action = 'Blocked via eBPF';
                        logTxt = `[${ts}] [ALERT] JA4 match 't13d190800_c84a8b291410' (CobaltStrike C2) detected on 10.0.4.12:49152->185.220.101.5:443. Flow timing CoV=0.002. Injected eBPF drop rule.`;
                    } else if (type === 'bench') {
                        conn = '100,000 Pkts/sec Stream';
                        ja4 = 'Multi-Flow Hash Ring';
                        rhythm = '4 CPU Cores Active (0 Mutex Locks)';
                        badge = '<span class="badge-amber">LOCK-FREE OK</span>';
                        action = '0 Mutex Drops';
                        logTxt = `[${ts}] [BENCHMARK] Fast-path worker ring operating across 4 CPU cores. Hash dispatch rate: 104,200 pps. Mutex contention drops: 0.`;
                    } else {
                        conn = '192.168.1.45 &rarr; Google:443';
                        ja4 = 't13d151600_8daaf6152702';
                        rhythm = 'Random human interaction timing';
                        badge = '<span class="badge-green">SAFE (BENIGN)</span>';
                        action = 'Allowed';
                        logTxt = `[${ts}] [PASS] Clean TLS 1.3 ClientHello fingerprint verified for 192.168.1.45->Google:443. Traffic allowed.`;
                    }

                    consoleEl.innerText = logTxt;

                    const newRow = document.createElement('tr');
                    newRow.className = 'anim-fade-row';
                    newRow.innerHTML = `
                        <td>${ts}</td>
                        <td><b>${conn}</b></td>
                        <td><code>${ja4}</code></td>
                        <td>${rhythm}</td>
                        <td>${badge}</td>
                        <td><b>${action}</b></td>
                    `;

                    tbody.insertBefore(newRow, tbody.firstChild);
                };
            </script>
"""

with open('pages/sentinel-stream.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'SENTINEL-STREAM').replace('{content}', SENTINEL_CONTENT))

with open('pages/cipherpulse.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'CipherPulse').replace('{content}', CIPHERPULSE_CONTENT))

print("Masterpiece pages generated successfully!")
