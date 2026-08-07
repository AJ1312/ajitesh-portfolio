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
        .workbench-box {{
            border: 2px solid var(--rule-dark);
            background: var(--paper-warm);
            padding: 35px;
            margin: 40px 0;
            border-radius: 2px;
        }}
        .wb-btn {{
            background: var(--ink);
            color: var(--paper);
            border: 2px solid var(--ink);
            padding: 10px 20px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-right: 12px;
            margin-bottom: 12px;
            transition: all 0.2s ease;
            font-family: var(--font-body);
        }}
        .wb-btn:hover {{
            background: var(--stamp);
            border-color: var(--stamp);
            color: #fff;
        }}
        .wb-table {{
            width: 100%;
            border-collapse: collapse;
            font-family: var(--font-body);
            font-size: 14px;
            margin-top: 25px;
            background: var(--paper-bright);
            border: 2px solid var(--rule-dark);
        }}
        .wb-table th {{
            background: var(--ink);
            color: var(--paper-bright);
            padding: 12px 15px;
            text-align: left;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .wb-table td {{
            padding: 14px 15px;
            border-bottom: 1px solid var(--rule);
            line-height: 1.5;
        }}
        .anim-row {{
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
        .badge-critical {{
            display: inline-block;
            padding: 4px 10px;
            background: #fee2e2;
            color: #dc2626;
            border: 1px solid #dc2626;
            font-weight: 700;
            font-size: 12px;
        }}
        .badge-high {{
            display: inline-block;
            padding: 4px 10px;
            background: #fef3c7;
            color: #d97706;
            border: 1px solid #d97706;
            font-weight: 700;
            font-size: 12px;
        }}
        .badge-safe {{
            display: inline-block;
            padding: 4px 10px;
            background: #dcfce7;
            color: #15803d;
            border: 1px solid #15803d;
            font-weight: 700;
            font-size: 12px;
        }}
        .arch-diagram-box {{
            background: var(--paper-bright);
            border: 2px solid var(--rule-dark);
            padding: 30px;
            margin: 30px 0;
            text-align: center;
        }}
        .arch-node {{
            display: inline-block;
            border: 1px solid var(--rule-dark);
            background: var(--paper-warm);
            padding: 12px 18px;
            margin: 6px;
            font-size: 14px;
            font-weight: bold;
        }}
        .arch-arrow {{
            display: inline-block;
            margin: 0 8px;
            font-weight: bold;
            color: var(--stamp);
            font-size: 18px;
        }}
    </style>
</head>
<body class="newspaper-theme">
    <div class="container">
        
        <!-- SUBPAGE HEADER -->
        <header class="masthead" style="margin-top: 20px;">
            <nav class="nav" id="main-nav" style="border-bottom: 4px solid var(--rule-dark); padding: 15px 0;">
                <div class="newspaper-grid" style="align-items: center;">
                    <div class="col-span-6 heading-md" style="margin:0;"><a href="../index.html" style="text-decoration: none; color: inherit;">&larr; THE SHARMA DISPATCH</a></div>
                    <div class="col-span-6" style="display: flex; justify-content: flex-end; gap: 25px; align-items: center;">
                        <a href="../index.html#projects" class="meta bold">WORK</a>
                        <a href="../index.html#contact" class="meta bold">CONTACT</a>
                        <a href="mailto:13ajitesh@gmail.com" style="background: var(--ink); color: var(--paper); padding: 6px 16px;" class="meta bold">HIRE HIM</a>
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
            <!-- HERO -->
            <section class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <p class="kicker-label">DISPATCH A &mdash; RESEARCH &amp; SYSTEM BUILD</p>
                        <h1 class="display-xl" style="margin-bottom: 20px; font-size: 52px;">Sentinel-Stream</h1>
                        <p class="display-sm" style="max-width: 850px; font-style: italic; line-height: 1.4;">O(1)-Memory Streaming Anomaly Detection Engine for Real-Time Enterprise UEBA</p>
                        
                        <div class="newspaper-grid" style="margin-top: 35px; border-top: 1px solid var(--rule); padding-top: 25px;">
                            <div class="col-span-4 column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">GITHUB REPOSITORY</p>
                                <a href="https://github.com/AJ1312/sentinel-stream" target="_blank" class="body-sm" style="color: var(--stamp); font-weight: bold; text-decoration: underline;">AJ1312/sentinel-stream &nearr;</a>
                            </div>
                            <div class="col-span-4 column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">IEEE ARTIFACTS</p>
                                <a href="https://github.com/AJ1312/sentinel-stream-research" target="_blank" class="body-sm" style="color: var(--stamp); font-weight: bold; text-decoration: underline;">IEEE Research Paper &nearr;</a>
                            </div>
                            <div class="col-span-4 column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">CORE TECH STACK</p>
                                <p class="body-sm">Python, Count-Min Sketch, LightGBM, TreeSHAP</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- THE PROBLEM & THE SOLUTION -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-6 column-bordered">
                        <span class="kicker-label" style="color: var(--stamp);">THE SYSTEM CHALLENGE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 28px;">Memory Bottlenecks Under High Volume</h3>
                        <p class="body-lg" style="line-height: 1.7;"><span class="dropcap">E</span>nterprise Security Operations Centers (SOCs) process tens of millions of audit events daily. Conventional User and Entity Behavior Analytics (UEBA) tools store raw historical log arrays per user, causing memory consumption to grow linearly $O(N)$ and triggering server out-of-memory (OOM) crashes during traffic spikes.</p>
                    </div>
                    
                    <div class="col-span-6">
                        <span class="kicker-label" style="color: var(--stamp);">THE ARCHITECTURAL SOLUTION</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 28px;">Fixed $O(1)$ Memory Profiling</h3>
                        <p class="body-lg" style="line-height: 1.7;"><span class="dropcap">S</span>entinel-Stream replaces raw event arrays with Exponentially Weighted Moving Averages (EWMA) and Count-Min Sketch tables ($4\text{ KB}$ fixed matrix), bounding memory per user to just <b>2 KB of RAM</b>. It detects anomalous behavior in under <b>2.64 milliseconds</b> while providing immediate TreeSHAP feature explanations.</p>
                    </div>
                </div>
            </section>

            <!-- KEY RESULTS METRICS -->
            <section class="section" style="padding: 30px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-3 text-center column-bordered">
                        <p class="display-lg" style="margin:0; color: var(--stamp); font-size: 44px;">2.64 ms</p>
                        <p class="meta bold uppercase" style="margin-top: 5px;">P99 Inference Speed</p>
                    </div>
                    <div class="col-span-3 text-center column-bordered">
                        <p class="display-lg" style="margin:0; color: var(--stamp); font-size: 44px;">~2 KB</p>
                        <p class="meta bold uppercase" style="margin-top: 5px;">Fixed RAM / Entity</p>
                    </div>
                    <div class="col-span-3 text-center column-bordered">
                        <p class="display-lg" style="margin:0; color: var(--stamp); font-size: 44px;">0.9403</p>
                        <p class="meta bold uppercase" style="margin-top: 5px;">NSL-KDD Macro F1</p>
                    </div>
                    <div class="col-span-3 text-center">
                        <p class="display-lg" style="margin:0; color: var(--stamp); font-size: 44px;">24.6×</p>
                        <p class="meta bold uppercase" style="margin-top: 5px;">Faster Than Random Forest</p>
                    </div>
                </div>
            </section>

            <!-- ARCHITECTURE PIPELINE -->
            <section class="section" style="padding: 30px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <div class="arch-diagram-box">
                            <span class="kicker-label" style="color: var(--stamp);">SYSTEM ARCHITECTURE</span>
                            <h4 class="heading-md" style="margin: 10px 0 15px 0;">O(1) Profiler &amp; Two-Stage Machine Learning Pipeline</h4>
                            <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:center;">
                                <div class="arch-node">Event Ingestion<br><small style="font-weight:normal;">Kafka / Audit Stream</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">O(1) EWMA Profiler<br><small style="font-weight:normal;">4 KB Matrix / Entity</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Stage 1: IsoForest<br><small style="font-weight:normal;">Cold-Start Risk Score</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Stage 2: LightGBM<br><small style="font-weight:normal;">Multi-Class Classifier</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">TreeSHAP Rationale<br><small style="font-weight:normal;">Sub-30&mu;s Explanation</small></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- INTERACTIVE DEMO WORKBENCH -->
            <section class="section" style="padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">INTERACTIVE DEMONSTRATION</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 32px;">Live UEBA Threat Inspection Workbench</h3>
                        <p class="body-lg" style="margin-bottom: 25px;">Select an enterprise threat scenario to observe real-time anomaly classification, latency metrics, and feature attributions:</p>

                        <div class="workbench-box">
                            <div>
                                <button class="wb-btn" onclick="runScenario('brute')">⚡ Test 1: Password Brute-Force</button>
                                <button class="wb-btn" onclick="runScenario('travel')">🌍 Test 2: Impossible Geo-Travel</button>
                                <button class="wb-btn" onclick="runScenario('exfil')">📤 Test 3: Data Exfiltration</button>
                                <button class="wb-btn" onclick="runScenario('normal')">✅ Test 4: Normal Employee Baseline</button>
                            </div>

                            <table class="wb-table">
                                <thead>
                                    <tr>
                                        <th style="width: 120px;">Timestamp</th>
                                        <th style="width: 160px;">User Account</th>
                                        <th>Observed Event</th>
                                        <th style="width: 140px;">Threat Level</th>
                                        <th style="width: 100px;">Latency</th>
                                        <th>Detection Rationale</th>
                                    </tr>
                                </thead>
                                <tbody id="wbTableBody">
                                    <tr class="anim-row">
                                        <td>18:36:01</td>
                                        <td><b>sarah_marketing</b></td>
                                        <td>Opened standard project documents</td>
                                        <td><span class="badge-safe">SAFE (NOMINAL)</span></td>
                                        <td>1.42 ms</td>
                                        <td>Activity matches normal daily baseline behavior.</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </section>

            <script>
                function runScenario(type) {
                    const tbody = document.getElementById('wbTableBody');
                    const ts = new Date().toISOString().substring(11, 19);

                    let user = '', event = '', badge = '', lat = '', why = '';

                    if (type === 'brute') {
                        user = 'admin_john';
                        event = '45 failed login attempts in 10 seconds';
                        badge = '<span class="badge-critical">CRITICAL THREAT</span>';
                        lat = '1.84 ms';
                        why = 'High login failure frequency (+0.54 risk attribution) + sudden rate spike.';
                    } else if (type === 'travel') {
                        user = 'exec_rachel';
                        event = 'Login from Tokyo 5m after New York session';
                        badge = '<span class="badge-high">HIGH RISK</span>';
                        lat = '2.12 ms';
                        why = 'Physical speed threshold exceeded (+0.68 geo-velocity risk attribution).';
                    } else if (type === 'exfil') {
                        user = 'dev_service';
                        event = '14.2 GB database download outside work hours';
                        badge = '<span class="badge-critical">CRITICAL THREAT</span>';
                        lat = '1.95 ms';
                        why = 'Abnormal outbound data volume (+0.76 EWMA volume risk attribution).';
                    } else {
                        user = 'sarah_marketing';
                        event = 'Opened standard project documents';
                        badge = '<span class="badge-safe">SAFE (NOMINAL)</span>';
                        lat = '1.42 ms';
                        why = 'Activity matches normal daily baseline behavior.';
                    }

                    const newRow = document.createElement('tr');
                    newRow.className = 'anim-row';
                    newRow.innerHTML = `
                        <td>${ts}</td>
                        <td><b>${user}</b></td>
                        <td>${event}</td>
                        <td>${badge}</td>
                        <td>${lat}</td>
                        <td>${why}</td>
                    `;

                    tbody.insertBefore(newRow, tbody.firstChild);
                }
            </script>
"""

CIPHERPULSE_CONTENT = """
            <!-- HERO -->
            <section class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <p class="kicker-label">DISPATCH B &mdash; SYSTEMS ENGINEERING REPORT</p>
                        <h1 class="display-xl" style="margin-bottom: 20px; font-size: 52px;">CipherPulse</h1>
                        <p class="display-sm" style="max-width: 850px; font-style: italic; line-height: 1.4;">Multi-Threaded C++ Engine for Encrypted Traffic Intelligence &amp; Line-Rate Inspection</p>
                        
                        <div class="newspaper-grid" style="margin-top: 35px; border-top: 1px solid var(--rule); padding-top: 25px;">
                            <div class="col-span-6 column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">GITHUB REPOSITORY</p>
                                <a href="https://github.com/AJ1312/CipherPulse" target="_blank" class="body-sm" style="color: var(--stamp); font-weight: bold; text-decoration: underline;">AJ1312/CipherPulse &nearr;</a>
                            </div>
                            <div class="col-span-6">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">CORE TECH STACK</p>
                                <p class="body-sm">C++17, eBPF, Lock-Free Ring Buffers, JA4+ Fingerprinting</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- THE PROBLEM & THE SOLUTION -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-6 column-bordered">
                        <span class="kicker-label" style="color: var(--stamp);">THE NETWORK CHALLENGE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 28px;">Encrypted Traffic Blindspots</h3>
                        <p class="body-lg" style="line-height: 1.7;"><span class="dropcap">O</span>ver 95% of modern internet traffic is encrypted (HTTPS / TLS 1.3). Threat actors hide Command and Control (C2) channels inside encrypted tunnels. Traditional Deep Packet Inspection (DPI) requires costly SSL decryption, breaking privacy and degrading throughput.</p>
                    </div>
                    
                    <div class="col-span-6">
                        <span class="kicker-label" style="color: var(--stamp);">THE ARCHITECTURAL SOLUTION</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 28px;">Lock-Free Fingerprint &amp; Rhythm DPI</h3>
                        <p class="body-lg" style="line-height: 1.7;"><span class="dropcap">C</span>ipherPulse inspects packets at line-rate <i>without decrypting payload content</i>. By combining outer JA4+ client fingerprints with Welford online flow statistics (tracking metronome-like C2 beaconing rhythms), it classifies encrypted threats at <b>100k+ packets per second</b>.</p>
                    </div>
                </div>
            </section>

            <!-- KEY RESULTS METRICS -->
            <section class="section" style="padding: 30px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-3 text-center column-bordered">
                        <p class="display-lg" style="margin:0; color: var(--stamp); font-size: 44px;">100k+</p>
                        <p class="meta bold uppercase" style="margin-top: 5px;">Single-Core pps</p>
                    </div>
                    <div class="col-span-3 text-center column-bordered">
                        <p class="display-lg" style="margin:0; color: var(--stamp); font-size: 44px;">ZERO</p>
                        <p class="meta bold uppercase" style="margin-top: 5px;">Hot-Path Lock Contention</p>
                    </div>
                    <div class="col-span-3 text-center column-bordered">
                        <p class="display-lg" style="margin:0; color: var(--stamp); font-size: 44px;">100%</p>
                        <p class="meta bold uppercase" style="margin-top: 5px;">C2 Beaconing Detection</p>
                    </div>
                    <div class="col-span-3 text-center">
                        <p class="display-lg" style="margin:0; color: var(--stamp); font-size: 44px;">ZERO</p>
                        <p class="meta bold uppercase" style="margin-top: 5px;">External Dependencies</p>
                    </div>
                </div>
            </section>

            <!-- ARCHITECTURE PIPELINE -->
            <section class="section" style="padding: 30px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <div class="arch-diagram-box">
                            <span class="kicker-label" style="color: var(--stamp);">C++17 FAST-PATH ARCHITECTURE</span>
                            <h4 class="heading-md" style="margin: 10px 0 15px 0;">Lock-Free 5-Tuple Consistent Hashing Pipeline</h4>
                            <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:center;">
                                <div class="arch-node">RAW Socket Capture<br><small style="font-weight:normal;">eBPF / AF_PACKET</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">5-Tuple Hash Dispatch<br><small style="font-weight:normal;">Zero-Mutex Router</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Fast-Path Worker Threads<br><small style="font-weight:normal;">C++17 Ring Buffers</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">JA4+ &amp; Welford Profiler<br><small style="font-weight:normal;">Flow Periodicity Engine</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">ETI Alert Stream<br><small style="font-weight:normal;">Non-SNI Threat Classification</small></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- INTERACTIVE DEMO WORKBENCH -->
            <section class="section" style="padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">INTERACTIVE DEMONSTRATION</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 32px;">Live Encrypted Traffic Forensic Workbench</h3>
                        <p class="body-lg" style="margin-bottom: 25px;">Select a network connection stream to observe real-time JA4+ fingerprint extraction and threat classification:</p>

                        <div class="workbench-box">
                            <div>
                                <button class="wb-btn" onclick="runDpi('normal')">▶ Stream 1: Standard HTTPS Browsing</button>
                                <button class="wb-btn" onclick="runDpi('c2')">🚨 Stream 2: Encrypted C2 Hacker Beacon</button>
                                <button class="wb-btn" onclick="runDpi('bench')">⚡ Stream 3: High-Speed Multi-Thread Test</button>
                            </div>

                            <table class="wb-table">
                                <thead>
                                    <tr>
                                        <th style="width: 120px;">Timestamp</th>
                                        <th>Network Connection</th>
                                        <th style="width: 220px;">JA4+ Fingerprint Hash</th>
                                        <th>Traffic Rhythm</th>
                                        <th style="width: 160px;">Security Verdict</th>
                                        <th style="width: 140px;">Action Taken</th>
                                    </tr>
                                </thead>
                                <tbody id="wbDpiBody">
                                    <tr class="anim-row">
                                        <td>18:36:01</td>
                                        <td><b>192.168.1.45 &rarr; Google:443</b></td>
                                        <td><code>t13d151600_8daaf6152702</code></td>
                                        <td>Random human interaction timing</td>
                                        <td><span class="badge-safe">SAFE (BENIGN)</span></td>
                                        <td>Allowed</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </section>

            <script>
                function runDpi(type) {
                    const tbody = document.getElementById('wbDpiBody');
                    const ts = new Date().toISOString().substring(11, 19);

                    let conn = '', ja4 = '', rhythm = '', badge = '', action = '';

                    if (type === 'c2') {
                        conn = '10.0.4.12 &rarr; 185.220.101.5 (Hidden IP)';
                        ja4 = 't13d190800_c84a8b291410';
                        rhythm = 'Strict 5.0s metronome pulse (CoV < 0.12)';
                        badge = '<span class="badge-critical">ALERT: C2 BEACON</span>';
                        action = 'Blocked via eBPF';
                    } else if (type === 'bench') {
                        conn = '100,000 Pkts/sec Stream';
                        ja4 = 'Multi-Flow Hash Ring';
                        rhythm = '4 CPU Cores Active (0 Mutex Locks)';
                        badge = '<span class="badge-high">LOCK-FREE SPEED OK</span>';
                        action = '0 Mutex Drops';
                    } else {
                        conn = '192.168.1.45 &rarr; Google:443';
                        ja4 = 't13d151600_8daaf6152702';
                        rhythm = 'Random human interaction timing';
                        badge = '<span class="badge-safe">SAFE (BENIGN)</span>';
                        action = 'Allowed';
                    }

                    const newRow = document.createElement('tr');
                    newRow.className = 'anim-row';
                    newRow.innerHTML = `
                        <td>${ts}</td>
                        <td><b>${conn}</b></td>
                        <td><code>${ja4}</code></td>
                        <td>${rhythm}</td>
                        <td>${badge}</td>
                        <td><b>${action}</b></td>
                    `;

                    tbody.insertBefore(newRow, tbody.firstChild);
                }
            </script>
"""

with open('pages/sentinel-stream.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'Sentinel-Stream').replace('{content}', SENTINEL_CONTENT))

with open('pages/cipherpulse.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'CipherPulse').replace('{content}', CIPHERPULSE_CONTENT))

print("Successfully generated clean, perfectly structured, ultra-readable broadsheet pages!")
