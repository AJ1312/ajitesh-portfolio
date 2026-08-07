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
    <link rel="stylesheet" href="../css/styles.css">
    <style>
        .sim-standalone-box {{
            border: 3px double var(--rule-dark);
            background: #fdfbf7;
            padding: 30px;
            margin: 40px 0;
            border-radius: 6px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.06);
            position: relative;
        }}
        .sim-box-header {{
            background: var(--ink);
            color: var(--paper-bright);
            padding: 12px 20px;
            margin: -30px -30px 25px -30px;
            border-radius: 3px 3px 0 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .sim-btn-action {{
            background: var(--ink);
            color: var(--paper);
            border: 2px solid var(--ink);
            padding: 10px 18px;
            font-size: 13px;
            font-weight: bold;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-right: 10px;
            margin-bottom: 10px;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            font-family: var(--font-body);
        }}
        .sim-btn-action:hover {{
            background: var(--stamp);
            border-color: var(--stamp);
            color: #fff;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(217, 35, 35, 0.2);
        }}
        .sim-btn-action:active {{
            transform: translateY(0);
        }}
        .sim-table {{
            width: 100%;
            border-collapse: collapse;
            font-family: var(--font-mono, monospace);
            font-size: 13px;
            margin-top: 20px;
            background: #fff;
            border: 1px solid var(--rule-dark);
        }}
        .sim-table th {{
            background: var(--paper-warm);
            color: var(--ink);
            padding: 12px;
            text-align: left;
            font-family: var(--font-body);
            font-size: 12px;
            text-transform: uppercase;
            border-bottom: 2px solid var(--rule-dark);
        }}
        .sim-table td {{
            padding: 12px;
            border-bottom: 1px solid var(--rule);
        }}
        .row-anim {{
            animation: slideFadeIn 0.5s ease-out forwards;
        }}
        @keyframes slideFadeIn {{
            from {{
                opacity: 0;
                transform: translateY(-12px);
                background-color: #fef08a;
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
                background-color: transparent;
            }}
        }}
        .pulse-critical {{
            display: inline-block;
            padding: 3px 8px;
            background: #fee2e2;
            color: #dc2626;
            border: 1px solid #f87171;
            font-weight: bold;
            border-radius: 3px;
            animation: pulseGlow 1.5s infinite;
        }}
        .pulse-high {{
            display: inline-block;
            padding: 3px 8px;
            background: #fef3c7;
            color: #d97706;
            border: 1px solid #fbbf24;
            font-weight: bold;
            border-radius: 3px;
        }}
        .pulse-safe {{
            display: inline-block;
            padding: 3px 8px;
            background: #dcfce7;
            color: #15803d;
            border: 1px solid #4ade80;
            font-weight: bold;
            border-radius: 3px;
        }}
        @keyframes pulseGlow {{
            0% {{ box-shadow: 0 0 0 0 rgba(220, 38, 38, 0.4); }}
            70% {{ box-shadow: 0 0 0 8px rgba(220, 38, 38, 0); }}
            100% {{ box-shadow: 0 0 0 0 rgba(220, 38, 38, 0); }}
        }}
        .risk-meter-container {{
            background: #fff;
            border: 1px solid var(--rule-dark);
            padding: 20px;
            margin-top: 20px;
        }}
        .meter-track {{
            background: #e2e8f0;
            height: 18px;
            border-radius: 3px;
            overflow: hidden;
            margin-top: 6px;
        }}
        .meter-fill {{
            height: 100%;
            width: 0%;
            background: var(--stamp);
            transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .summary-card {{
            background: var(--paper-bright);
            border: 2px solid var(--rule-dark);
            padding: 25px;
            margin-bottom: 25px;
        }}
        .outcome-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin: 30px 0;
        }}
        .outcome-card {{
            border: 1px solid var(--rule-dark);
            background: var(--paper-warm);
            padding: 20px;
            text-align: center;
        }}
        .outcome-number {{
            font-family: var(--font-display);
            font-size: 38px;
            font-weight: 900;
            color: var(--stamp);
            margin-bottom: 5px;
        }}
        .outcome-title {{
            font-weight: bold;
            text-transform: uppercase;
            font-size: 13px;
            letter-spacing: 0.5px;
            margin-bottom: 8px;
        }}
        .outcome-desc {{
            font-size: 14px;
            color: #444;
            line-height: 1.5;
        }}
        @media screen and (max-width: 768px) {{
            .outcome-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body class="newspaper-theme">
    <div class="container" style="max-width: 1100px;">
        <header class="masthead" style="margin-top: 20px;">
            <div class="newspaper-grid" style="border-bottom: 1px solid var(--rule); padding: 10px 0;">
                <div class="col-span-12 meta uppercase" style="display:flex; justify-content: space-between;">
                    <span>BY THE ENGINEERING DESK</span>
                    <span><a href="../index.html" style="font-weight:bold;">&larr; Back to Front Page</a></span>
                </div>
            </div>
        </header>

        <main class="dispatch-content">
{content}
        </main>
        
        <footer class="section" style="border-top: 4px solid var(--rule-dark); padding: 40px 0; text-align: center; margin-top: 60px;">
            <p class="meta">&copy; 2026 AJITESH SHARMA &middot; THE SHARMA DISPATCH &middot; VOL. I</p>
        </footer>
    </div>
</body>
</html>
"""

SENTINEL_CONTENT = """
            <!-- HEADER -->
            <section class="section" style="padding: 40px 0 20px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="project-badge" style="background:var(--ink); color:var(--paper); padding:4px 10px; font-weight:bold; font-size:12px;">AI CYBERSECURITY &amp; BEHAVIOR ANALYSIS</span>
                        <h1 class="display-lg" style="margin: 15px 0 10px 0; font-size: 42px;">Sentinel-Stream</h1>
                        <p class="tagline" style="font-size: 20px; font-style: italic; color: #444;">Real-Time AI Security Engine That Detects Insider Threats Without Crashing Servers</p>
                    </div>
                </div>
            </section>

            <!-- EXECUTIVE SUMMARY -->
            <section class="section" style="padding: 20px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-6 column-bordered">
                        <div class="summary-card">
                            <span class="kicker-label" style="color:var(--stamp);">THE PROBLEM</span>
                            <h3 class="heading-md" style="margin: 10px 0;">Server Crashes Under Heavy Traffic</h3>
                            <p class="body" style="font-size: 15px; line-height: 1.6;">
                                Traditional AI security tools try to remember every single user action in memory. When thousands of employees or users interact at once, security servers run out of RAM and crash—leaving company data exposed.
                            </p>
                        </div>
                    </div>

                    <div class="col-span-6">
                        <div class="summary-card" style="background: var(--paper-warm);">
                            <span class="kicker-label" style="color:var(--stamp);">THE SOLUTION</span>
                            <h3 class="heading-md" style="margin: 10px 0;">Fixed Memory AI Profiling</h3>
                            <p class="body" style="font-size: 15px; line-height: 1.6;">
                                <b>Sentinel-Stream</b> tracks user behavioral patterns using a smart mathematical technique that requires only <b>2 KB of RAM per user</b>. It spots abnormal behavior in under 3 milliseconds without overloading servers.
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- KEY OUTCOMES CARDS -->
            <section class="section" style="padding: 10px 0 30px 0; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); margin-bottom: 40px;">
                <span class="kicker-label">KEY PERFORMANCE RESULTS</span>
                <div class="outcome-grid">
                    <div class="outcome-card">
                        <div class="outcome-number">2.64 ms</div>
                        <div class="outcome-title">Lightning Speed</div>
                        <div class="outcome-desc">Detects suspicious activity 24× faster than traditional machine learning models.</div>
                    </div>

                    <div class="outcome-card">
                        <div class="outcome-number">2 KB</div>
                        <div class="outcome-title">Fixed Memory</div>
                        <div class="outcome-desc">Uses a tiny fixed RAM footprint per user, scaling to millions without server crashes.</div>
                    </div>

                    <div class="outcome-card">
                        <div class="outcome-number">94.0%</div>
                        <div class="outcome-title">Detection Accuracy</div>
                        <div class="outcome-desc">Accurately identifies brute-force attacks, impossible travel, and data theft.</div>
                    </div>
                </div>
            </section>

            <!-- STANDALONE ANIMATED SIMULATION CONTAINER BOX -->
            <section class="section" style="padding: 10px 0 30px 0;">
                <div class="sim-standalone-box">
                    <div class="sim-box-header">
                        <div style="font-weight:bold; font-size:14px; letter-spacing:0.5px;">
                            ⚡ LIVE ANIMATED THREAT INSPECTOR &amp; TREESHAP ENGINE
                        </div>
                        <div style="font-size:12px; opacity:0.8;">
                            PIPELINE: O(1) EWMA + LIGHTGBM
                        </div>
                    </div>

                    <p class="body" style="margin-bottom:20px; font-size:15px;">
                        Click any security test button below to trigger an <b>animated real-time threat evaluation</b> and watch the live attribution bars update dynamically:
                    </p>

                    <div>
                        <button class="sim-btn-action" onclick="runAnimatedScenario('brute')">⚡ Test 1: Password Attack Surge</button>
                        <button class="sim-btn-action" onclick="runAnimatedScenario('travel')">🌍 Test 2: Impossible Travel Location</button>
                        <button class="sim-btn-action" onclick="runAnimatedScenario('exfil')">📤 Test 3: Data Theft Exfiltration</button>
                        <button class="sim-btn-action" onclick="runAnimatedScenario('normal')">✅ Test 4: Normal Employee Work</button>
                    </div>

                    <!-- Live Animated Stream Table -->
                    <table class="sim-table">
                        <thead>
                            <tr>
                                <th>Timestamp</th>
                                <th>User Account</th>
                                <th>Observed Event</th>
                                <th>Threat Level</th>
                                <th>P99 Latency</th>
                                <th>Why Was This Alert Triggered?</th>
                            </tr>
                        </thead>
                        <tbody id="simAnimBody">
                            <tr class="row-anim">
                                <td>18:35:01</td>
                                <td><b>sarah_marketing</b></td>
                                <td>Opened standard project documents</td>
                                <td><span class="pulse-safe">SAFE (NOMINAL)</span></td>
                                <td>1.45 ms</td>
                                <td>Activity matches normal daily baseline behavior.</td>
                            </tr>
                        </tbody>
                    </table>

                    <!-- Live Dynamic TreeSHAP Risk Attribution Gauge -->
                    <div class="risk-meter-container">
                        <span class="meta bold uppercase" style="display:block; margin-bottom:15px; font-size:12px;">DYNAMIC TREESHAP FEATURE RISK ATTRIBUTION</span>

                        <div style="margin-bottom:14px;">
                            <div style="display:flex; justify-content:space-between; font-size:13px; font-weight:bold;">
                                <span>Failed Logins Rate (failed_logins_1m)</span>
                                <span id="txt_f1">+0.02</span>
                            </div>
                            <div class="meter-track"><div class="meter-fill" id="meter_f1" style="width:2%;"></div></div>
                        </div>

                        <div style="margin-bottom:14px;">
                            <div style="display:flex; justify-content:space-between; font-size:13px; font-weight:bold;">
                                <span>Event Velocity Spike (event_rate_delta)</span>
                                <span id="txt_f2">+0.04</span>
                            </div>
                            <div class="meter-track"><div class="meter-fill" id="meter_f2" style="width:4%;"></div></div>
                        </div>

                        <div>
                            <div style="display:flex; justify-content:space-between; font-size:13px; font-weight:bold;">
                                <span>Outbound Data Volume (outbound_bytes_ewma)</span>
                                <span id="txt_f3">+0.03</span>
                            </div>
                            <div class="meter-track"><div class="meter-fill" id="meter_f3" style="width:3%;"></div></div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- HOW IT WORKS (SIMPLE 3 STEPS) -->
            <section class="section" style="padding: 20px 0 40px 0; border-top: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">HOW IT WORKS</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0;">The 3-Step Detection Pipeline</h3>
                    </div>

                    <div class="col-span-4 rv column-bordered">
                        <h4 class="heading-md" style="margin-bottom: 10px;">1. Continuous Profiling</h4>
                        <p class="body" style="line-height: 1.6;">As user events stream in, the system continuously updates a lightweight rolling summary of each user's typical habits.</p>
                    </div>

                    <div class="col-span-4 rv column-bordered">
                        <h4 class="heading-md" style="margin-bottom: 10px;">2. Two-Stage AI Analysis</h4>
                        <p class="body" style="line-height: 1.6;">First, an Isolation Forest checks if the user is brand new. Then, a fast LightGBM model classifies the exact attack type.</p>
                    </div>

                    <div class="col-span-4 rv">
                        <h4 class="heading-md" style="margin-bottom: 10px;">3. Clear Explainability</h4>
                        <p class="body" style="line-height: 1.6;">Instead of a "black box" prediction, TreeSHAP explains exactly which factors contributed to the alert so security teams can act fast.</p>
                    </div>
                </div>

                <div style="margin-top: 40px; display:flex; gap:20px;">
                    <a href="https://github.com/AJ1312/sentinel-stream" target="_blank" class="btn-github">⭐ View Code on GitHub</a>
                    <a href="https://github.com/AJ1312/sentinel-stream-research" target="_blank" class="btn-research">🔬 View IEEE Research Paper</a>
                </div>
            </section>

            <script>
                function runAnimatedScenario(type) {
                    const tbody = document.getElementById('simAnimBody');
                    const ts = new Date().toISOString().substring(11, 19);

                    let user = '', activity = '', riskBadge = '', time = '', why = '', f1 = 0, f2 = 0, f3 = 0;

                    if (type === 'brute') {
                        user = 'admin_john';
                        activity = '45 failed login attempts in 10s';
                        riskBadge = '<span class="pulse-critical">CRITICAL THREAT</span>';
                        time = '1.84 ms';
                        why = 'Extreme login failure spike + high event velocity.';
                        f1 = 84; f2 = 62; f3 = 12;
                    } else if (type === 'travel') {
                        user = 'exec_rachel';
                        activity = 'Logged in from Tokyo 5m after NY';
                        riskBadge = '<span class="pulse-high">HIGH RISK</span>';
                        time = '2.12 ms';
                        why = 'Impossible physical movement speed (88% geo velocity).';
                        f1 = 14; f2 = 88; f3 = 25;
                    } else if (type === 'exfil') {
                        user = 'dev_service';
                        activity = 'Downloaded 14 GB customer DB off-hours';
                        riskBadge = '<span class="pulse-critical">CRITICAL THREAT</span>';
                        time = '1.95 ms';
                        why = 'Abnormal outbound data volume (94% volume spike).';
                        f1 = 12; f2 = 40; f3 = 94;
                    } else {
                        user = 'sarah_marketing';
                        activity = 'Opened standard project documents';
                        riskBadge = '<span class="pulse-safe">SAFE (NOMINAL)</span>';
                        time = '1.45 ms';
                        why = 'Activity matches normal daily baseline behavior.';
                        f1 = 2; f2 = 4; f3 = 3;
                    }

                    const newRow = document.createElement('tr');
                    newRow.className = 'row-anim';
                    newRow.innerHTML = `
                        <td>${ts}</td>
                        <td><b>${user}</b></td>
                        <td>${activity}</td>
                        <td>${riskBadge}</td>
                        <td>${time}</td>
                        <td>${why}</td>
                    `;

                    tbody.insertBefore(newRow, tbody.firstChild);

                    // Animate TreeSHAP progress bars
                    document.getElementById('meter_f1').style.width = f1 + '%';
                    document.getElementById('txt_f1').innerText = '+' + (f1 / 100).toFixed(2);

                    document.getElementById('meter_f2').style.width = f2 + '%';
                    document.getElementById('txt_f2').innerText = '+' + (f2 / 100).toFixed(2);

                    document.getElementById('meter_f3').style.width = f3 + '%';
                    document.getElementById('txt_f3').innerText = '+' + (f3 / 100).toFixed(2);
                }
            </script>
"""

CIPHERPULSE_CONTENT = """
            <!-- HEADER -->
            <section class="section" style="padding: 40px 0 20px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="project-badge" style="background:var(--ink); color:var(--paper); padding:4px 10px; font-weight:bold; font-size:12px;">HIGH-SPEED NETWORKING &amp; SECURITY</span>
                        <h1 class="display-lg" style="margin: 15px 0 10px 0; font-size: 42px;">CipherPulse</h1>
                        <p class="tagline" style="font-size: 20px; font-style: italic; color: #444;">High-Performance C++ Engine That Catches Hidden Encrypted Malware Without Violating Privacy</p>
                    </div>
                </div>
            </section>

            <!-- EXECUTIVE SUMMARY -->
            <section class="section" style="padding: 20px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-6 column-bordered">
                        <div class="summary-card">
                            <span class="kicker-label" style="color:var(--stamp);">THE PROBLEM</span>
                            <h3 class="heading-md" style="margin: 10px 0;">Encrypted Blindspots</h3>
                            <p class="body" style="font-size: 15px; line-height: 1.6;">
                                Today, 95%+ of web traffic is encrypted (HTTPS). Hackers take advantage of this by hiding malicious command-and-control signals inside encrypted channels. Traditional firewalls can't inspect encrypted data without decrypting it—which is slow, expensive, and invasive.
                            </p>
                        </div>
                    </div>

                    <div class="col-span-6">
                        <div class="summary-card" style="background: var(--paper-warm);">
                            <span class="kicker-label" style="color:var(--stamp);">THE SOLUTION</span>
                            <h3 class="heading-md" style="margin: 10px 0;">Fingerprint &amp; Rhythm Analysis</h3>
                            <p class="body" style="font-size: 15px; line-height: 1.6;">
                                <b>CipherPulse</b> analyzes encrypted network traffic <i>without decrypting user messages</i>. By looking at handshake digital fingerprints (JA4+) and connection timing rhythms, it detects hacker commands instantly at line-rate speed (100,000+ packets/sec).
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- KEY OUTCOMES CARDS -->
            <section class="section" style="padding: 10px 0 30px 0; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); margin-bottom: 40px;">
                <span class="kicker-label">KEY PERFORMANCE RESULTS</span>
                <div class="outcome-grid">
                    <div class="outcome-card">
                        <div class="outcome-number">100k+</div>
                        <div class="outcome-title">Packets / Second</div>
                        <div class="outcome-desc">Processes over 100,000 network packets every second on a single CPU core.</div>
                    </div>

                    <div class="outcome-card">
                        <div class="outcome-number">100%</div>
                        <div class="outcome-title">Privacy Preserved</div>
                        <div class="outcome-desc">Detects threats using connection fingerprints without decrypting personal user data.</div>
                    </div>

                    <div class="outcome-card">
                        <div class="outcome-number">0%</div>
                        <div class="outcome-title">Lock Overhead</div>
                        <div class="outcome-desc">Built in pure C++17 with lock-free data structures so processing threads never stall.</div>
                    </div>
                </div>
            </section>

            <!-- STANDALONE ANIMATED SIMULATION CONTAINER BOX -->
            <section class="section" style="padding: 10px 0 30px 0;">
                <div class="sim-standalone-box">
                    <div class="sim-box-header">
                        <div style="font-weight:bold; font-size:14px; letter-spacing:0.5px;">
                            ⚡ LIVE ANIMATED PACKET INSPECTOR &amp; JA4+ FORENSIC ENGINE
                        </div>
                        <div style="font-size:12px; opacity:0.8;">
                            ENGINE: C++17 RING BUFFER + eBPF
                        </div>
                    </div>

                    <p class="body" style="margin-bottom:20px; font-size:15px;">
                        Click any test stream button below to run an <b>animated live packet capture inspection</b>:
                    </p>

                    <div>
                        <button class="sim-btn-action" onclick="runAnimatedDpi('normal')">▶ Stream 1: Standard Web Browsing</button>
                        <button class="sim-btn-action" onclick="runAnimatedDpi('c2')">🚨 Stream 2: Encrypted Hacker Connection</button>
                        <button class="sim-btn-action" onclick="runAnimatedDpi('bench')">⚡ Stream 3: High-Speed Multi-Thread Test</button>
                    </div>

                    <!-- Live Animated Stream Table -->
                    <table class="sim-table">
                        <thead>
                            <tr>
                                <th>Timestamp</th>
                                <th>Network Connection</th>
                                <th>JA4+ Fingerprint Hash</th>
                                <th>Traffic Rhythm</th>
                                <th>Security Verdict</th>
                                <th>Action Taken</th>
                            </tr>
                        </thead>
                        <tbody id="simDpiBody">
                            <tr class="row-anim">
                                <td>18:35:01</td>
                                <td><b>192.168.1.45 &rarr; Google:443</b></td>
                                <td><code>t13d151600_8daaf6152702</code></td>
                                <td>Random human timing</td>
                                <td><span class="pulse-safe">SAFE (BENIGN)</span></td>
                                <td>Allowed</td>
                            </tr>
                        </tbody>
                    </table>

                    <!-- Dynamic Entropy & Flow Meter -->
                    <div class="risk-meter-container">
                        <span class="meta bold uppercase" style="display:block; margin-bottom:15px; font-size:12px;">ENCRYPTED PAYLOAD SHANNON ENTROPY &amp; FLOW METER</span>

                        <div style="margin-bottom:14px;">
                            <div style="display:flex; justify-content:space-between; font-size:13px; font-weight:bold;">
                                <span>Shannon Entropy Level (High = Encrypted Payload)</span>
                                <span id="txt_ent">5.42 / 8.0</span>
                            </div>
                            <div class="meter-track"><div class="meter-fill" id="meter_ent" style="width:67%;"></div></div>
                        </div>

                        <div>
                            <div style="display:flex; justify-content:space-between; font-size:13px; font-weight:bold;">
                                <span>Flow Periodicity Coefficient of Variation (CoV &lt; 0.12 = Hacker Beacon)</span>
                                <span id="txt_cov">0.686 (Normal)</span>
                            </div>
                            <div class="meter-track"><div class="meter-fill" id="meter_cov" style="width:85%;"></div></div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- HOW IT WORKS (SIMPLE 3 STEPS) -->
            <section class="section" style="padding: 20px 0 40px 0; border-top: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">HOW IT WORKS</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0;">The 3-Step Packet Inspection Pipeline</h3>
                    </div>

                    <div class="col-span-4 rv column-bordered">
                        <h4 class="heading-md" style="margin-bottom: 10px;">1. Kernel Packet Capture</h4>
                        <p class="body" style="line-height: 1.6;">Packets are captured directly from network interfaces using eBPF/AF_PACKET for zero-copy memory speed.</p>
                    </div>

                    <div class="col-span-4 rv column-bordered">
                        <h4 class="heading-md" style="margin-bottom: 10px;">2. JA4+ Fingerprinting</h4>
                        <p class="body" style="line-height: 1.6;">Extracts outer TLS handshake details to generate a unique digital signature without touching packet contents.</p>
                    </div>

                    <div class="col-span-4 rv">
                        <h4 class="heading-md" style="margin-bottom: 10px;">3. Rhythm &amp; Beaconing Check</h4>
                        <p class="body" style="line-height: 1.6;">Uses Welford's algorithm to spot automated, metronome-like beacon signals emitted by hacker tools (Cobalt Strike).</p>
                    </div>
                </div>

                <div style="margin-top: 40px;">
                    <a href="https://github.com/AJ1312/CipherPulse" target="_blank" class="btn-github">⭐ View Code on GitHub</a>
                </div>
            </section>

            <script>
                function runAnimatedDpi(type) {
                    const tbody = document.getElementById('simDpiBody');
                    const ts = new Date().toISOString().substring(11, 19);

                    let conn = '', ja4 = '', rhythm = '', verdictBadge = '', action = '', entPct = 0, covPct = 0, entTxt = '', covTxt = '';

                    if (type === 'c2') {
                        conn = '10.0.4.12 &rarr; 185.220.101.5 (Hidden IP)';
                        ja4 = 't13d190800_c84a8b291410';
                        rhythm = 'Strict 5.0s pulse (Metronome)';
                        verdictBadge = '<span class="pulse-critical">ALERT: MALICIOUS C2</span>';
                        action = 'Blocked at Kernel Level';
                        entPct = 99; covPct = 8;
                        entTxt = '7.94 / 8.0 (High Entropy)';
                        covTxt = '0.002 (Periodic C2 Beacon)';
                    } else if (type === 'bench') {
                        conn = '100,000 Packets / Sec Stream';
                        ja4 = 'Multi-Flow Hash Ring';
                        rhythm = '4 CPU Cores Active';
                        verdictBadge = '<span class="pulse-high">LOCK-FREE OK</span>';
                        action = '0 Mutex Drops';
                        entPct = 50; covPct = 100;
                        entTxt = '448,000 pps';
                        covTxt = '0 Mutex Contention';
                    } else {
                        conn = '192.168.1.45 &rarr; Google:443';
                        ja4 = 't13d151600_8daaf6152702';
                        rhythm = 'Random human timing';
                        verdictBadge = '<span class="pulse-safe">SAFE (BENIGN)</span>';
                        action = 'Allowed';
                        entPct = 67; covPct = 85;
                        entTxt = '5.42 / 8.0';
                        covTxt = '0.686 (Normal)';
                    }

                    const newRow = document.createElement('tr');
                    newRow.className = 'row-anim';
                    newRow.innerHTML = `
                        <td>${ts}</td>
                        <td><b>${conn}</b></td>
                        <td><code>${ja4}</code></td>
                        <td>${rhythm}</td>
                        <td>${verdictBadge}</td>
                        <td><b>${action}</b></td>
                    `;

                    tbody.insertBefore(newRow, tbody.firstChild);

                    document.getElementById('meter_ent').style.width = entPct + '%';
                    document.getElementById('txt_ent').innerText = entTxt;

                    document.getElementById('meter_cov').style.width = covPct + '%';
                    document.getElementById('txt_cov').innerText = covTxt;
                }
            </script>
"""

with open('pages/sentinel-stream.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'Sentinel-Stream').replace('{content}', SENTINEL_CONTENT))

with open('pages/cipherpulse.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'CipherPulse').replace('{content}', CIPHERPULSE_CONTENT))

print("Successfully generated animated standalone simulation boxes!")
