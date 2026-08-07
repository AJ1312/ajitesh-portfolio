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
        .ed-sim-card {{
            border: 2px solid var(--rule-dark);
            background: var(--paper-warm);
            padding: 30px;
            margin: 35px 0;
            border-radius: 4px;
        }}
        .ed-btn {{
            background: var(--ink);
            color: var(--paper);
            border: 1px solid var(--ink);
            padding: 10px 18px;
            font-size: 13px;
            font-weight: bold;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-right: 10px;
            margin-bottom: 10px;
            transition: all 0.2s ease;
            font-family: var(--font-body);
        }}
        .ed-btn:hover {{
            background: var(--stamp);
            border-color: var(--stamp);
            color: #fff;
        }}
        .ed-table {{
            width: 100%;
            border-collapse: collapse;
            font-family: var(--font-body);
            font-size: 14px;
            margin-top: 20px;
            background: var(--paper-bright);
            border: 1px solid var(--rule-dark);
        }}
        .ed-table th {{
            background: var(--ink);
            color: var(--paper);
            padding: 12px;
            text-align: left;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .ed-table td {{
            padding: 12px;
            border-bottom: 1px solid var(--rule);
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

            <!-- EXECUTIVE SUMMARY (EASY TO UNDERSTAND) -->
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

            <!-- KEY OUTCOMES (VISUAL CARDS) -->
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

            <!-- INTERACTIVE DEMO (SIMPLE & CLEAR) -->
            <section class="section" style="padding: 10px 0 30px 0;">
                <span class="kicker-label" style="color: var(--stamp); font-size: 14px;">TRY IT LIVE</span>
                <h3 class="heading-lg" style="margin: 5px 0 20px 0;">Interactive Threat Detection Simulator</h3>
                <p class="body-lg" style="margin-bottom: 20px;">Click any security scenario below to watch how Sentinel-Stream evaluates user activity and explains the threat in plain English:</p>

                <div class="ed-sim-card">
                    <div>
                        <button class="ed-btn" onclick="runSimpleScenario('brute')">⚡ Test 1: Password Attack</button>
                        <button class="ed-btn" onclick="runSimpleScenario('travel')">🌍 Test 2: Impossible Location</button>
                        <button class="ed-btn" onclick="runSimpleScenario('exfil')">📤 Test 3: Data Theft Spike</button>
                        <button class="ed-btn" onclick="runSimpleScenario('normal')">✅ Test 4: Normal Employee Work</button>
                    </div>

                    <!-- Clean Simple Table -->
                    <table class="ed-table">
                        <thead>
                            <tr>
                                <th>User Account</th>
                                <th>Observed Activity</th>
                                <th>Threat Risk Level</th>
                                <th>Response Time</th>
                                <th>Why Was This Alert Triggered?</th>
                            </tr>
                        </thead>
                        <tbody id="simTableBody">
                            <tr>
                                <td><b>sarah_marketing</b></td>
                                <td>Opened standard project documents</td>
                                <td><span style="color:#16a34a; font-weight:bold;">SAFE (LOW RISK)</span></td>
                                <td>1.45 ms</td>
                                <td>Activity matches normal daily baseline behavior.</td>
                            </tr>
                        </tbody>
                    </table>
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
                function runSimpleScenario(type) {
                    const tbody = document.getElementById('simTableBody');

                    let user = '', activity = '', risk = '', time = '', why = '';

                    if (type === 'brute') {
                        user = 'admin_john';
                        activity = '45 failed login attempts in 10 seconds';
                        risk = '<span style="color:#dc2626; font-weight:bold;">CRITICAL THREAT</span>';
                        time = '1.84 ms';
                        why = 'Extreme login failure spike (82% risk factor) + rapid event velocity.';
                    } else if (type === 'travel') {
                        user = 'exec_rachel';
                        activity = 'Logged in from Tokyo 5 minutes after logging out in NY';
                        risk = '<span style="color:#d97706; font-weight:bold;">HIGH RISK</span>';
                        time = '2.12 ms';
                        why = 'Impossible physical movement speed (88% geographical anomaly risk).';
                    } else if (type === 'exfil') {
                        user = 'dev_service';
                        activity = 'Downloaded 14 GB customer database off-hours';
                        risk = '<span style="color:#dc2626; font-weight:bold;">CRITICAL THREAT</span>';
                        time = '1.95 ms';
                        why = 'Abnormal outbound data volume (94% volume spike) outside work hours.';
                    } else {
                        user = 'sarah_marketing';
                        activity = 'Opened standard project documents';
                        risk = '<span style="color:#16a34a; font-weight:bold;">SAFE (LOW RISK)</span>';
                        time = '1.45 ms';
                        why = 'Activity matches normal daily baseline behavior.';
                    }

                    const row = `<tr>
                        <td><b>${user}</b></td>
                        <td>${activity}</td>
                        <td>${risk}</td>
                        <td>${time}</td>
                        <td>${why}</td>
                    </tr>`;

                    tbody.innerHTML = row + tbody.innerHTML;
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

            <!-- EXECUTIVE SUMMARY (EASY TO UNDERSTAND) -->
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

            <!-- KEY OUTCOMES (VISUAL CARDS) -->
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

            <!-- INTERACTIVE DEMO (SIMPLE & CLEAR) -->
            <section class="section" style="padding: 10px 0 30px 0;">
                <span class="kicker-label" style="color: var(--stamp); font-size: 14px;">TRY IT LIVE</span>
                <h3 class="heading-lg" style="margin: 5px 0 20px 0;">Interactive Encrypted Traffic Inspector</h3>
                <p class="body-lg" style="margin-bottom: 20px;">Click any network stream below to see how CipherPulse classifies connection safety without opening encrypted packets:</p>

                <div class="ed-sim-card">
                    <div>
                        <button class="ed-btn" onclick="runSimpleDpi('normal')">▶ Stream 1: Standard Web Browsing</button>
                        <button class="ed-btn" onclick="runSimpleDpi('c2')">🚨 Stream 2: Encrypted Hacker Connection</button>
                        <button class="ed-btn" onclick="runSimpleDpi('bench')">⚡ Stream 3: High-Speed Multi-Thread Test</button>
                    </div>

                    <!-- Clean Simple Table -->
                    <table class="ed-table">
                        <thead>
                            <tr>
                                <th>Network Connection</th>
                                <th>Connection Fingerprint (JA4+)</th>
                                <th>Traffic Rhythm</th>
                                <th>Security Verdict</th>
                                <th>Action Taken</th>
                            </tr>
                        </thead>
                        <tbody id="dpiTableBody">
                            <tr>
                                <td>192.168.1.45 &rarr; 142.250.190.46 (Google)</td>
                                <td><code>t13d151600_8daaf6152702</code></td>
                                <td>Random human timing (Normal)</td>
                                <td><span style="color:#16a34a; font-weight:bold;">SAFE (BENIGN)</span></td>
                                <td>Allowed</td>
                            </tr>
                        </tbody>
                    </table>
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
                function runSimpleDpi(type) {
                    const tbody = document.getElementById('dpiTableBody');

                    let conn = '', ja4 = '', rhythm = '', verdict = '', action = '';

                    if (type === 'c2') {
                        conn = '10.0.4.12 &rarr; 185.220.101.5 (Hidden IP)';
                        ja4 = 't13d190800_c84a8b291410';
                        rhythm = 'Strict 5.0s pulse (Hacker Beacon)';
                        verdict = '<span style="color:#dc2626; font-weight:bold;">MALICIOUS HACKER C2</span>';
                        action = 'Blocked at Kernel Level';
                    } else if (type === 'bench') {
                        conn = '100,000 Packets / Sec Stream';
                        ja4 = 'Multi-Flow Hash Ring';
                        rhythm = '4 CPU Cores Active';
                        verdict = '<span style="color:#2563eb; font-weight:bold;">LOCK-FREE SPEED OK</span>';
                        action = '0 Mutex Drops';
                    } else {
                        conn = '192.168.1.45 &rarr; 142.250.190.46 (Google)';
                        ja4 = 't13d151600_8daaf6152702';
                        rhythm = 'Random human timing (Normal)';
                        verdict = '<span style="color:#16a34a; font-weight:bold;">SAFE (BENIGN)</span>';
                        action = 'Allowed';
                    }

                    const row = `<tr>
                        <td><b>${conn}</b></td>
                        <td><code>${ja4}</code></td>
                        <td>${rhythm}</td>
                        <td>${verdict}</td>
                        <td><b>${action}</b></td>
                    </tr>`;

                    tbody.innerHTML = row + tbody.innerHTML;
                }
            </script>
"""

with open('pages/sentinel-stream.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'Sentinel-Stream').replace('{content}', SENTINEL_CONTENT))

with open('pages/cipherpulse.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'CipherPulse').replace('{content}', CIPHERPULSE_CONTENT))

print("Successfully generated accessible, crystal-clear, intuitive project pages!")
