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
            padding: 9px 16px;
            font-size: 12px;
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
            font-family: var(--font-mono, monospace);
            font-size: 13px;
            margin-top: 20px;
            background: var(--paper-bright);
            border: 1px solid var(--rule-dark);
        }}
        .ed-table th {{
            background: var(--ink);
            color: var(--paper);
            padding: 10px;
            text-align: left;
            font-family: var(--font-body);
            font-size: 12px;
            text-transform: uppercase;
        }}
        .ed-table td {{
            padding: 10px;
            border-bottom: 1px solid var(--rule);
        }}
        .ed-gauge-box {{
            background: var(--paper-bright);
            border: 1px solid var(--rule-dark);
            padding: 20px;
            margin-top: 20px;
        }}
        .ed-progress-track {{
            background: var(--rule);
            height: 16px;
            border-radius: 2px;
            overflow: hidden;
            margin-top: 5px;
        }}
        .ed-progress-fill {{
            background: var(--stamp);
            height: 100%;
            width: 0%;
            transition: width 0.4s ease;
        }}
        .arch-diagram-box {{
            background: var(--paper-bright);
            border: 2px solid var(--rule-dark);
            padding: 25px;
            margin: 25px 0;
            text-align: center;
        }}
        .arch-node {{
            display: inline-block;
            border: 1px solid var(--rule-dark);
            background: var(--paper-warm);
            padding: 10px 15px;
            margin: 5px;
            font-size: 13px;
            font-weight: bold;
        }}
        .arch-arrow {{
            display: inline-block;
            margin: 0 5px;
            font-weight: bold;
            color: var(--stamp);
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
                        <span class="project-badge" style="background:var(--ink); color:var(--paper); padding:4px 10px; font-weight:bold; font-size:12px;">AI CYBERSECURITY &amp; UEBA</span>
                        <h1 class="display-lg" style="margin: 15px 0 10px 0; font-size: 42px;">SENTINEL-STREAM: O(1)-Memory UEBA Engine</h1>
                        <p class="tagline" style="font-size: 20px; font-style: italic; color: #444;">Sub-3ms Real-Time Behavioural Anomaly Detection with TreeSHAP Explainability</p>
                    </div>
                </div>
            </section>

            <!-- KEY METRICS BAR -->
            <section class="section" style="padding: 20px 0; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); margin-bottom: 40px;">
                <div class="metrics-row" style="margin:0; border:none; padding:0;">
                    <div class="metric-box">
                        <span class="metric-val" style="font-size:36px; color:var(--stamp);">2.64 ms</span>
                        <span class="metric-lbl">P99 Inference Latency</span>
                    </div>
                    <div class="metric-box">
                        <span class="metric-val" style="font-size:36px; color:var(--stamp);">~2 KB</span>
                        <span class="metric-lbl">Fixed Memory / Entity</span>
                    </div>
                    <div class="metric-box">
                        <span class="metric-val" style="font-size:36px; color:var(--stamp);">0.9403</span>
                        <span class="metric-lbl">NSL-KDD Macro F1</span>
                    </div>
                    <div class="metric-box">
                        <span class="metric-val" style="font-size:36px; color:var(--stamp);">24.6×</span>
                        <span class="metric-lbl">Faster than Random Forest</span>
                    </div>
                </div>
            </section>

            <!-- INTERACTIVE BROADSHEET UEBA STREAM BENCH -->
            <section class="section" style="padding: 10px 0 30px 0;">
                <span class="kicker-label" style="color: var(--stamp); font-size: 14px;">INTERACTIVE INSPECTION BENCH</span>
                <h3 class="heading-lg" style="margin: 5px 0 20px 0;">Real-Time UEBA Threat Detection &amp; TreeSHAP Attribution</h3>

                <div class="ed-sim-card">
                    <span class="meta bold uppercase" style="display:block; margin-bottom:12px;">SELECT AN ENTERPRISE SCENARIO TO TEST PIPELINE:</span>
                    <div>
                        <button class="ed-btn" onclick="testScenario('brute')">⚡ Scenario 1: Brute Force Surge</button>
                        <button class="ed-btn" onclick="testScenario('travel')">🌍 Scenario 2: Impossible Travel</button>
                        <button class="ed-btn" onclick="testScenario('exfil')">📤 Scenario 3: Data Exfiltration</button>
                        <button class="ed-btn" onclick="testScenario('normal')">✅ Scenario 4: Normal Baseline</button>
                    </div>

                    <!-- Live Stream Table -->
                    <table class="ed-table">
                        <thead>
                            <tr>
                                <th>Timestamp</th>
                                <th>Entity ID</th>
                                <th>Observed Event</th>
                                <th>IsoForest Score</th>
                                <th>LightGBM Class</th>
                                <th>Latency</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody id="streamTableBody">
                            <tr>
                                <td>18:28:01</td>
                                <td>user_staff_04</td>
                                <td>FILE_READ (Internal Drive)</td>
                                <td>0.12</td>
                                <td>BENIGN</td>
                                <td>1.42 ms</td>
                                <td style="color:#16a34a; font-weight:bold;">NOMINAL</td>
                            </tr>
                        </tbody>
                    </table>

                    <!-- TreeSHAP Risk Progress Card -->
                    <div class="ed-gauge-box">
                        <span class="meta bold uppercase" style="display:block; margin-bottom:15px;">TREESHAP FEATURE RISK ATTRIBUTION (PER ALERT)</span>
                        
                        <div style="margin-bottom:12px;">
                            <div style="display:flex; justify-content:space-between; font-size:12px; font-weight:bold;">
                                <span>Failed Logins Rate (failed_logins_1m)</span>
                                <span id="val_f1">+0.00</span>
                            </div>
                            <div class="ed-progress-track"><div class="ed-progress-fill" id="bar_f1"></div></div>
                        </div>

                        <div style="margin-bottom:12px;">
                            <div style="display:flex; justify-content:space-between; font-size:12px; font-weight:bold;">
                                <span>Event Velocity Spike (event_rate_delta)</span>
                                <span id="val_f2">+0.00</span>
                            </div>
                            <div class="ed-progress-track"><div class="ed-progress-fill" id="bar_f2"></div></div>
                        </div>

                        <div>
                            <div style="display:flex; justify-content:space-between; font-size:12px; font-weight:bold;">
                                <span>Outbound Data Volume (outbound_bytes_ewma)</span>
                                <span id="val_f3">+0.00</span>
                            </div>
                            <div class="ed-progress-track"><div class="ed-progress-fill" id="bar_f3"></div></div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SYSTEM ARCHITECTURE -->
            <section class="section" style="padding: 30px 0; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); margin-bottom: 40px;">
                <div class="arch-diagram-box" style="background: var(--paper-warm); border: 2px solid var(--rule-dark); padding: 30px; text-align: center;">
                    <span class="kicker-label" style="color: var(--stamp);">SYSTEM ARCHITECTURE PIPELINE</span>
                    <h4 class="heading-md" style="margin: 10px 0 20px 0;">O(1) Streaming Profiler &amp; Two-Stage ML Pipeline</h4>
                    <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:12px; font-family: var(--font-mono, monospace);">
                        <div class="arch-node">Event Ingestion<br><small style="font-weight:normal;">Kafka / Audit Logs</small></div>
                        <span class="arch-arrow" style="font-size:18px;">&rarr;</span>
                        <div class="arch-node">O(1) EWMA Profiler<br><small style="font-weight:normal;">4 KB Matrix / Entity</small></div>
                        <span class="arch-arrow" style="font-size:18px;">&rarr;</span>
                        <div class="arch-node">Stage 1: IsoForest<br><small style="font-weight:normal;">Cold-Start Risk Score</small></div>
                        <span class="arch-arrow" style="font-size:18px;">&rarr;</span>
                        <div class="arch-node">Stage 2: LightGBM<br><small style="font-weight:normal;">Multi-Class Classifier</small></div>
                        <span class="arch-arrow" style="font-size:18px;">&rarr;</span>
                        <div class="arch-node">TreeSHAP Rationale<br><small style="font-weight:normal;">Sub-30&mu;s Per-Alert Explanation</small></div>
                    </div>
                </div>
            </section>

            <!-- TECHNICAL SPECS & IMPACT -->
            <section class="section" style="padding: 20px 0 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-6 column-bordered">
                        <h3 class="heading-lg" style="margin-bottom: 20px;">Technical Innovations</h3>
                        <ul style="list-style:square; padding-left:20px; line-height:1.7; font-size:16px;">
                            <li style="margin-bottom:15px;"><b>O(1) Streaming Profiler:</b> Replaces raw event arrays with EWMA rolling statistics and Count-Min Sketch tables, guaranteeing a fixed memory footprint.</li>
                            <li style="margin-bottom:15px;"><b>Zero Cold-Start Vulnerability:</b> Stage 1 Isolation Forest calculates structural anomaly scores ($s_{\text{iso}}$) for newly onboarded entities without historical baseline logs.</li>
                            <li><b>Inline TreeSHAP Explainability:</b> Computes exact directional feature risk attributions in $\approx 30\ \mu\text{s}$ per alert.</li>
                        </ul>
                    </div>

                    <div class="col-span-6">
                        <h3 class="heading-lg" style="margin-bottom: 20px;">The Real-World Scenario</h3>
                        <p class="body-lg" style="line-height:1.7;"><span class="dropcap">E</span>nterprise Security Operations Centers ingest tens of millions of audit events daily. Existing UEBA solutions store historical raw event arrays per user, causing memory consumption to scale linearly $O(N)$ and leading to Out-Of-Memory (OOM) failures under burst traffic.</p>
                        <p class="body-lg" style="line-height:1.7; margin-top:15px;">SENTINEL-STREAM guarantees strict $O(1)$ memory consumption per entity while rendering sub-3ms anomaly classification with exact TreeSHAP feature attributions.</p>
                    </div>
                </div>

                <div style="margin-top: 40px; display:flex; gap:20px;">
                    <a href="https://github.com/AJ1312/sentinel-stream" target="_blank" class="btn-github">⭐ View Code on GitHub</a>
                    <a href="https://github.com/AJ1312/sentinel-stream-research" target="_blank" class="btn-research">🔬 View IEEE Research Artifacts</a>
                </div>
            </section>

            <script>
                function testScenario(type) {
                    const tbody = document.getElementById('streamTableBody');
                    const ts = new Date().toISOString().substring(11, 19);

                    let entity = '', event = '', iso = '', cls = '', lat = '', statusHtml = '', f1 = 0, f2 = 0, f3 = 0;

                    if (type === 'brute') {
                        entity = 'user_adm_82';
                        event = 'AUTH_FAILURE (x45 in 10s)';
                        iso = '0.88';
                        cls = 'BRUTE_FORCE';
                        lat = '1.84 ms';
                        statusHtml = '<span style="color:#dc2626; font-weight:bold;">ALERT: CRITICAL</span>';
                        f1 = 82; f2 = 54; f3 = 12;
                    } else if (type === 'travel') {
                        entity = 'user_exec_04';
                        event = 'LOGIN_SUCCESS (Tokyo vs NY)';
                        iso = '0.81';
                        cls = 'IMPOSSIBLE_TRAVEL';
                        lat = '2.12 ms';
                        statusHtml = '<span style="color:#d97706; font-weight:bold;">ALERT: HIGH</span>';
                        f1 = 15; f2 = 88; f3 = 24;
                    } else if (type === 'exfil') {
                        entity = 'dev_service_acct';
                        event = 'DB_EXPORT (14.2 GB Outbound)';
                        iso = '0.94';
                        cls = 'DATA_EXFILTRATION';
                        lat = '1.95 ms';
                        statusHtml = '<span style="color:#dc2626; font-weight:bold;">ALERT: CRITICAL</span>';
                        f1 = 10; f2 = 35; f3 = 94;
                    } else {
                        entity = 'user_staff_11';
                        event = 'FILE_READ (Normal Baseline)';
                        iso = '0.11';
                        cls = 'BENIGN';
                        lat = '1.45 ms';
                        statusHtml = '<span style="color:#16a34a; font-weight:bold;">NOMINAL</span>';
                        f1 = 2; f2 = 4; f3 = 3;
                    }

                    const row = `<tr>
                        <td>${ts}</td>
                        <td><b>${entity}</b></td>
                        <td>${event}</td>
                        <td>${iso}</td>
                        <td><b>${cls}</b></td>
                        <td>${lat}</td>
                        <td>${statusHtml}</td>
                    </tr>`;

                    tbody.innerHTML = row + tbody.innerHTML;

                    document.getElementById('bar_f1').style.width = f1 + '%';
                    document.getElementById('val_f1').innerText = '+' + (f1 / 100).toFixed(2);

                    document.getElementById('bar_f2').style.width = f2 + '%';
                    document.getElementById('val_f2').innerText = '+' + (f2 / 100).toFixed(2);

                    document.getElementById('bar_f3').style.width = f3 + '%';
                    document.getElementById('val_f3').innerText = '+' + (f3 / 100).toFixed(2);
                }
            </script>
"""

CIPHERPULSE_CONTENT = """
            <!-- HEADER -->
            <section class="section" style="padding: 40px 0 20px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="project-badge" style="background:var(--ink); color:var(--paper); padding:4px 10px; font-weight:bold; font-size:12px;">HIGH-PERFORMANCE C++17 DPI</span>
                        <h1 class="display-lg" style="margin: 15px 0 10px 0; font-size: 42px;">CipherPulse: Multi-Threaded Encrypted DPI Engine</h1>
                        <p class="tagline" style="font-size: 20px; font-style: italic; color: #444;">Line-Rate Packet Inspection, JA4+ Fingerprinting & Non-SNI Traffic Classification</p>
                    </div>
                </div>
            </section>

            <!-- KEY METRICS BAR -->
            <section class="section" style="padding: 20px 0; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); margin-bottom: 40px;">
                <div class="metrics-row" style="margin:0; border:none; padding:0;">
                    <div class="metric-box">
                        <span class="metric-val" style="font-size:36px; color:var(--stamp);">100k+</span>
                        <span class="metric-lbl">Single-Core pps</span>
                    </div>
                    <div class="metric-box">
                        <span class="metric-val" style="font-size:36px; color:var(--stamp);">ZERO</span>
                        <span class="metric-lbl">Hot-Path Lock Contention</span>
                    </div>
                    <div class="metric-box">
                        <span class="metric-val" style="font-size:36px; color:var(--stamp);">100%</span>
                        <span class="metric-lbl">C2 Beaconing Detection</span>
                    </div>
                    <div class="metric-box">
                        <span class="metric-val" style="font-size:36px; color:var(--stamp);">Zero</span>
                        <span class="metric-lbl">External Dependencies</span>
                    </div>
                </div>
            </section>

            <!-- INTERACTIVE BROADSHEET DPI FORENSIC BENCH -->
            <section class="section" style="padding: 10px 0 30px 0;">
                <span class="kicker-label" style="color: var(--stamp); font-size: 14px;">INTERACTIVE FORENSIC INSPECTOR</span>
                <h3 class="heading-lg" style="margin: 5px 0 20px 0;">Line-Rate Packet Capture &amp; JA4+ Fingerprint Analysis</h3>

                <div class="ed-sim-card">
                    <span class="meta bold uppercase" style="display:block; margin-bottom:12px;">SELECT A TRAFFIC STREAM TO INSPECT:</span>
                    <div>
                        <button class="ed-btn" onclick="testDpi('normal')">▶ Stream Standard TLS 1.3 Traffic</button>
                        <button class="ed-btn" onclick="testDpi('c2')">🚨 Inject Non-SNI C2 Beaconing</button>
                        <button class="ed-btn" onclick="testDpi('bench')">⚡ Benchmark 4-Worker Lock-Free Hash</button>
                    </div>

                    <!-- Packet Stream Table -->
                    <table class="ed-table">
                        <thead>
                            <tr>
                                <th>Packet 5-Tuple (Src &rarr; Dst)</th>
                                <th>TLS Version</th>
                                <th>JA4+ Fingerprint Hash</th>
                                <th>Welford CoV</th>
                                <th>Shannon Entropy</th>
                                <th>Verdict</th>
                            </tr>
                        </thead>
                        <tbody id="dpiTableBody">
                            <tr>
                                <td>192.168.1.45:54321 &rarr; 142.250.190.46:443</td>
                                <td>TLS 1.3</td>
                                <td>t13d151600_8daaf6152702</td>
                                <td>0.686</td>
                                <td>5.42 / 8.0</td>
                                <td style="color:#16a34a; font-weight:bold;">CLEAN (BENIGN)</td>
                            </tr>
                        </tbody>
                    </table>

                    <!-- Entropy & Flow Periodicity Gauge -->
                    <div class="ed-gauge-box">
                        <span class="meta bold uppercase" style="display:block; margin-bottom:15px;">FLOW PERIODICITY &amp; SHANNON ENTROPY METRICS</span>
                        
                        <div style="margin-bottom:12px;">
                            <div style="display:flex; justify-content:space-between; font-size:12px; font-weight:bold;">
                                <span>Shannon Entropy Level (7.9+ indicates encrypted payload)</span>
                                <span id="val_ent">5.42 / 8.0</span>
                            </div>
                            <div class="ed-progress-track"><div class="ed-progress-fill" id="bar_ent" style="width:67%;"></div></div>
                        </div>

                        <div>
                            <div style="display:flex; justify-content:space-between; font-size:12px; font-weight:bold;">
                                <span>Welford Flow Inter-Arrival CoV (&lt; 0.12 indicates periodic C2 beaconing)</span>
                                <span id="val_cov">0.686</span>
                            </div>
                            <div class="ed-progress-track"><div class="ed-progress-fill" id="bar_cov" style="width:85%;"></div></div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SYSTEM ARCHITECTURE -->
            <section class="section" style="padding: 30px 0; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); margin-bottom: 40px;">
                <div class="arch-diagram-box" style="background: var(--paper-warm); border: 2px solid var(--rule-dark); padding: 30px; text-align: center;">
                    <span class="kicker-label" style="color: var(--stamp);">C++17 FAST-PATH ARCHITECTURE</span>
                    <h4 class="heading-md" style="margin: 10px 0 20px 0;">Lock-Free 5-Tuple Consistent Hashing &amp; JA4+ Fingerprinting</h4>
                    <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:12px; font-family: var(--font-mono, monospace);">
                        <div class="arch-node">RAW Socket Capture<br><small style="font-weight:normal;">AF_PACKET / eBPF</small></div>
                        <span class="arch-arrow" style="font-size:18px;">&rarr;</span>
                        <div class="arch-node">5-Tuple Hash Dispatch<br><small style="font-weight:normal;">Zero-Mutex Hashing</small></div>
                        <span class="arch-arrow" style="font-size:18px;">&rarr;</span>
                        <div class="arch-node">Fast-Path Worker Threads<br><small style="font-weight:normal;">C++17 Ring Buffers</small></div>
                        <span class="arch-arrow" style="font-size:18px;">&rarr;</span>
                        <div class="arch-node">JA4+ &amp; Entropy Engine<br><small style="font-weight:normal;">Welford CoV Profiler</small></div>
                        <span class="arch-arrow" style="font-size:18px;">&rarr;</span>
                        <div class="arch-node">C2 Beaconing Alert<br><small style="font-weight:normal;">Non-SNI ETI Stream</small></div>
                    </div>
                </div>
            </section>

            <!-- TECHNICAL SPECS & IMPACT -->
            <section class="section" style="padding: 20px 0 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-6 column-bordered">
                        <h3 class="heading-lg" style="margin-bottom: 20px;">Technical Innovations</h3>
                        <ul style="list-style:square; padding-left:20px; line-height:1.7; font-size:16px;">
                            <li style="margin-bottom:15px;"><b>Lock-Free Consistent Hashing:</b> Packets are routed via 5-tuple consistent hashing to isolated Fast Path (FP) threads, eliminating cross-thread mutex bottlenecks.</li>
                            <li style="margin-bottom:15px;"><b>Non-SNI Traffic Intelligence (ETI):</b> Classifies encrypted traffic when Encrypted Client Hello (ECH) hides SNI using JA4+ TLS fingerprinting and Welford online flow statistics ($\text{CoV} < 0.12$ beaconing).</li>
                            <li><b>Pure C++17 Memory Safety:</b> Strict-aliasing safe packet parsing using <code>std::memcpy</code> without external dependencies.</li>
                        </ul>
                    </div>

                    <div class="col-span-6">
                        <h3 class="heading-lg" style="margin-bottom: 20px;">The Real-World Scenario</h3>
                        <p class="body-lg" style="line-height:1.7;"><span class="dropcap">M</span>odern malware and Command &amp; Control (C2) frameworks (such as Cobalt Strike or Sliver) hide command channels inside standard TLS 1.3 encrypted streams, rendering traditional Deep Packet Inspection (DPI) helpless without full SSL decryption.</p>
                        <p class="body-lg" style="line-height:1.7; margin-top:15px;">CipherPulse inspects packets at line-rate without TLS decryption by extracting JA4+ client fingerprints and tracking flow inter-arrival times using Welford's algorithm to flag periodic beaconing.</p>
                    </div>
                </div>

                <div style="margin-top: 40px;">
                    <a href="https://github.com/AJ1312/CipherPulse" target="_blank" class="btn-github">⭐ View Code on GitHub</a>
                </div>
            </section>

            <script>
                function testDpi(type) {
                    const tbody = document.getElementById('dpiTableBody');

                    let tuple = '', tls = '', ja4 = '', cov = '', ent = '', verdictHtml = '', barEnt = 0, barCov = 0;

                    if (type === 'c2') {
                        tuple = '10.0.4.12:49152 &rarr; 185.220.101.5:443';
                        tls = 'TLS 1.3 (ECH)';
                        ja4 = 't13d190800_c84a8b291410';
                        cov = '0.002 (Periodic)';
                        ent = '7.94 / 8.0';
                        verdictHtml = '<span style="color:#dc2626; font-weight:bold;">ALERT: C2 BEACON DETECTED</span>';
                        barEnt = 99; barCov = 8;
                    } else if (type === 'bench') {
                        tuple = '100,000 Pkts / 4 Worker Cores';
                        tls = 'Multi-Flow';
                        ja4 = 'Hash Ring Distributed';
                        cov = '0 Mutex Locks';
                        ent = '448,000 pps';
                        verdictHtml = '<span style="color:#2563eb; font-weight:bold;">LOCK-FREE (0 MUTEX DROPS)</span>';
                        barEnt = 50; barCov = 100;
                    } else {
                        tuple = '192.168.1.45:54321 &rarr; 142.250.190.46:443';
                        tls = 'TLS 1.3';
                        ja4 = 't13d151600_8daaf6152702';
                        cov = '0.686';
                        ent = '5.42 / 8.0';
                        verdictHtml = '<span style="color:#16a34a; font-weight:bold;">CLEAN (BENIGN)</span>';
                        barEnt = 67; barCov = 85;
                    }

                    const row = `<tr>
                        <td><b>${tuple}</b></td>
                        <td>${tls}</td>
                        <td><code>${ja4}</code></td>
                        <td>${cov}</td>
                        <td>${ent}</td>
                        <td>${verdictHtml}</td>
                    </tr>`;

                    tbody.innerHTML = row + tbody.innerHTML;

                    document.getElementById('bar_ent').style.width = barEnt + '%';
                    document.getElementById('val_ent').innerText = ent;

                    document.getElementById('bar_cov').style.width = barCov + '%';
                    document.getElementById('val_cov').innerText = cov;
                }
            </script>
"""

with open('pages/sentinel-stream.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'Sentinel-Stream').replace('{content}', SENTINEL_CONTENT))

with open('pages/cipherpulse.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'CipherPulse').replace('{content}', CIPHERPULSE_CONTENT))

print("Successfully generated broadsheet editorial simulation benchmarks for CipherPulse and Sentinel-Stream!")
