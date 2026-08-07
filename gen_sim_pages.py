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
        .sim-box {{
            border: 2px solid var(--rule-dark);
            background: var(--paper-warm);
            padding: 25px;
            margin: 30px 0;
            font-family: var(--font-mono, monospace);
        }}
        .sim-btn {{
            background: var(--ink);
            color: var(--paper);
            border: 1px solid var(--ink);
            padding: 8px 14px;
            font-size: 12px;
            font-weight: bold;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-right: 8px;
            margin-bottom: 8px;
            transition: all 0.2s ease;
        }}
        .sim-btn:hover {{
            background: var(--stamp);
            border-color: var(--stamp);
            color: #fff;
        }}
        .sim-terminal {{
            background: #111;
            color: #00ff66;
            padding: 15px;
            border-radius: 4px;
            height: 180px;
            overflow-y: auto;
            font-size: 13px;
            line-height: 1.4;
            margin-top: 15px;
            border: 1px solid var(--rule-dark);
        }}
        .shap-bar-container {{
            margin-top: 15px;
            background: var(--paper-bright);
            padding: 15px;
            border: 1px solid var(--rule);
        }}
        .shap-row {{
            display: flex;
            align-items: center;
            margin-bottom: 8px;
            font-size: 12px;
        }}
        .shap-label {{
            width: 180px;
            font-weight: bold;
        }}
        .shap-track {{
            flex: 1;
            background: #eee;
            height: 14px;
            position: relative;
            margin: 0 10px;
        }}
        .shap-fill {{
            height: 100%;
            background: var(--stamp);
            width: 0%;
            transition: width 0.4s ease;
        }}
        .shap-val {{
            width: 50px;
            text-align: right;
            font-weight: bold;
        }}
        .arch-diagram-box {{
            background: var(--paper-bright);
            border: 2px solid var(--rule-dark);
            padding: 20px;
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
    <div class="container">
        <header class="masthead section-rule--double" style="margin-top: 20px;">
            <div class="newspaper-grid" style="border-bottom: 1px solid var(--rule); padding: 5px 0;">
                <div class="col-span-12 meta uppercase" style="display:flex; justify-content: space-between;">
                    <span>BY THE ENGINEERING DESK</span>
                    <span><a href="../index.html">&larr; Back to Front Page</a></span>
                </div>
            </div>
        </header>

        <main class="dispatch-content">
{content}
        </main>
        
        <footer class="section" style="border-top: 4px solid var(--rule-dark); padding: 20px 0; text-align: center;">
            <p class="meta">PRINTED IN VELLORE &middot; AJITESH SHARMA &copy; 2026</p>
        </footer>
    </div>
</body>
</html>
"""

SENTINEL_CONTENT = """
            <section class="portfolio-case-study">
                <div class="project-header rv">
                    <span class="project-badge">AI CYBERSECURITY & UEBA</span>
                    <h2 class="display-lg" style="margin-bottom: 10px;">SENTINEL-STREAM: O(1)-Memory Streaming Anomaly Detection</h2>
                    <p class="tagline">Sub-3ms Real-Time Behavioural UEBA Engine with TreeSHAP Explainability</p>
                </div>

                <!-- Metrics Grid -->
                <div class="metrics-row rv">
                    <div class="metric-box">
                        <span class="metric-val">2.64 ms</span>
                        <span class="metric-lbl">P99 Inference Latency</span>
                    </div>
                    <div class="metric-box">
                        <span class="metric-val">~2 KB</span>
                        <span class="metric-lbl">Fixed Memory / Entity</span>
                    </div>
                    <div class="metric-box">
                        <span class="metric-val">0.9403</span>
                        <span class="metric-lbl">NSL-KDD 5-Fold Macro F1</span>
                    </div>
                    <div class="metric-box">
                        <span class="metric-val">24.6×</span>
                        <span class="metric-lbl">Faster than Random Forest</span>
                    </div>
                </div>

                <!-- Architectural Flow Diagram (Pure CSS/HTML Broadside) -->
                <div class="arch-diagram-box rv">
                    <span class="kicker-label">SYSTEM ARCHITECTURE PIPELINE</span>
                    <h4 class="heading-md" style="margin: 10px 0 15px 0;">O(1) Streaming Profiler &amp; Two-Stage Inference</h4>
                    <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:8px;">
                        <div class="arch-node">Event Stream Ingestion<br><small style="font-weight:normal;">JSON Logs / Kafka</small></div>
                        <span class="arch-arrow">&rarr;</span>
                        <div class="arch-node">O(1) EWMA Profiler<br><small style="font-weight:normal;">4 KB Count-Min Sketch</small></div>
                        <span class="arch-arrow">&rarr;</span>
                        <div class="arch-node">Stage 1: Isolation Forest<br><small style="font-weight:normal;">Cold-Start Risk Score</small></div>
                        <span class="arch-arrow">&rarr;</span>
                        <div class="arch-node">Stage 2: LightGBM<br><small style="font-weight:normal;">Multi-Class Threat Classifier</small></div>
                        <span class="arch-arrow">&rarr;</span>
                        <div class="arch-node">TreeSHAP Explainability<br><small style="font-weight:normal;">Sub-30&mu;s Risk Rationale</small></div>
                    </div>
                </div>

                <!-- Interactive Live Simulation Widget -->
                <div class="sim-box rv">
                    <span class="kicker-label" style="color: var(--stamp);">INTERACTIVE THREAT SIMULATOR</span>
                    <h3 class="heading-lg" style="margin: 5px 0 15px 0;">Live UEBA Stream &amp; TreeSHAP Rationale Generator</h3>
                    <p class="body" style="margin-bottom: 15px; font-family: var(--font-text);">Inject simulated network events into the O(1) profiling pipeline to trigger real-time anomaly decisions and feature attribution values:</p>

                    <div>
                        <button class="sim-btn" onclick="triggerScenario('brute')">⚡ Scenario A: Brute Force Surge</button>
                        <button class="sim-btn" onclick="triggerScenario('travel')">🌍 Scenario B: Impossible Travel</button>
                        <button class="sim-btn" onclick="triggerScenario('exfil')">📤 Scenario C: Data Exfiltration</button>
                        <button class="sim-btn" onclick="triggerScenario('normal')">✅ Scenario D: Normal Baseline</button>
                    </div>

                    <div class="sim-terminal" id="terminalLog">
[SYSTEM INIT] SENTINEL-STREAM Engine active...
[SYSTEM INFO] O(1) Memory Profiler allocated (2.04 KB per entity).
[SYSTEM INFO] Ready for event stream ingestion. Click a scenario button above...
                    </div>

                    <div class="shap-bar-container">
                        <span class="meta bold" style="display:block; margin-bottom:10px;">TREESHAP FEATURE RISK ATTRIBUTION (PER ALERT)</span>
                        
                        <div class="shap-row">
                            <span class="shap-label" id="f1_label">failed_logins_1m</span>
                            <div class="shap-track"><div class="shap-fill" id="f1_bar"></div></div>
                            <span class="shap-val" id="f1_val">+0.00</span>
                        </div>
                        <div class="shap-row">
                            <span class="shap-label" id="f2_label">event_rate_delta</span>
                            <div class="shap-track"><div class="shap-fill" id="f2_bar"></div></div>
                            <span class="shap-val" id="f2_val">+0.00</span>
                        </div>
                        <div class="shap-row">
                            <span class="shap-label" id="f3_label">geo_velocity_kmh</span>
                            <div class="shap-track"><div class="shap-fill" id="f3_bar"></div></div>
                            <span class="shap-val" id="f3_val">+0.00</span>
                        </div>
                        <div class="shap-row">
                            <span class="shap-label" id="f4_label">outbound_bytes_ewma</span>
                            <div class="shap-track"><div class="shap-fill" id="f4_bar"></div></div>
                            <span class="shap-val" id="f4_val">+0.00</span>
                        </div>
                    </div>
                </div>

                <!-- Case Study Details -->
                <div class="case-study-grid rv">
                    <div class="text-block">
                        <h3 class="heading-lg" style="margin-bottom: 20px;">Key Technical Innovations</h3>
                        <ul>
                            <li><b>O(1) Streaming Profiler:</b> Replaces raw event arrays with Exponentially Weighted Moving Averages (EWMA) and Count-Min Sketch tables ($4\text{ KB}$ matrix), bounding memory per entity.</li>
                            <li><b>Zero Cold-Start Vulnerability:</b> Stage 1 Isolation Forest calculates structural anomaly scores ($s_{\text{iso}}$) for newly onboarded entities without historical baseline logs.</li>
                            <li><b>Inline TreeSHAP Explainability:</b> Computes exact directional feature risk attributions in $\approx 30\ \mu\text{s}$ per alert.</li>
                        </ul>
                    </div>
                    <div class="text-block">
                        <h3 class="heading-lg" style="margin-bottom: 20px;">The Real-World Scenario</h3>
                        <p class="body-lg"><span class="dropcap">E</span>nterprise Security Operations Centers (SOCs) ingest tens of millions of audit events daily. Existing UEBA solutions store historical raw event arrays per user, causing memory consumption to scale linearly $O(N)$ and leading to Out-Of-Memory (OOM) failures under burst traffic.</p>
                        <p class="body-lg" style="margin-top: 15px;">SENTINEL-STREAM guarantees strict $O(1)$ memory consumption per entity while rendering sub-3ms anomaly classification with exact TreeSHAP feature attributions.</p>
                    </div>
                </div>

                <!-- Links -->
                <div class="project-links rv">
                    <a href="https://github.com/AJ1312/sentinel-stream" target="_blank" class="btn-github">⭐ View Code on GitHub</a>
                    <a href="https://github.com/AJ1312/sentinel-stream-research" target="_blank" class="btn-research">🔬 View IEEE Research Artifacts</a>
                </div>
            </section>

            <script>
                function triggerScenario(type) {
                    const log = document.getElementById('terminalLog');
                    const ts = new Date().toISOString().substring(11, 19);
                    
                    let logText = '';
                    let f1 = 0, f2 = 0, f3 = 0, f4 = 0;

                    if (type === 'brute') {
                        logText = `[${ts}] [ALERT CRITICAL] Entity: user_adm_82 | Event: AUTH_FAILURE (x45 in 10s)\n` +
                                  `[${ts}] [INFERENCE] P99 Latency: 1.84ms | Memory: 1.98 KB\n` +
                                  `[${ts}] [STAGE 1 IsoForest] Score: 0.88 | [STAGE 2 LightGBM] Class: BRUTE_FORCE (0.965)\n` +
                                  `[${ts}] [TreeSHAP] Top Contributor: failed_logins_1m (+0.54), event_rate_delta (+0.32)`;
                        f1 = 88; f2 = 64; f3 = 10; f4 = 15;
                    } else if (type === 'travel') {
                        logText = `[${ts}] [ALERT HIGH] Entity: user_exec_04 | Event: LOGIN_SUCCESS (Location: Tokyo, Previous: New York)\n` +
                                  `[${ts}] [INFERENCE] P99 Latency: 2.12ms | Memory: 2.01 KB\n` +
                                  `[${ts}] [STAGE 1 IsoForest] Score: 0.81 | [STAGE 2 LightGBM] Class: IMPOSSIBLE_TRAVEL (0.912)\n` +
                                  `[${ts}] [TreeSHAP] Top Contributor: geo_velocity_kmh (+0.68), event_rate_delta (+0.18)`;
                        f1 = 12; f2 = 36; f3 = 92; f4 = 20;
                    } else if (type === 'exfil') {
                        logText = `[${ts}] [ALERT CRITICAL] Entity: dev_service_acct | Event: DB_EXPORT (Outbound: 14.2 GB to unknown ASN)\n` +
                                  `[${ts}] [INFERENCE] P99 Latency: 1.95ms | Memory: 1.99 KB\n` +
                                  `[${ts}] [STAGE 1 IsoForest] Score: 0.94 | [STAGE 2 LightGBM] Class: DATA_EXFILTRATION (0.984)\n` +
                                  `[${ts}] [TreeSHAP] Top Contributor: outbound_bytes_ewma (+0.76), event_rate_delta (+0.25)`;
                        f1 = 15; f2 = 50; f3 = 25; f4 = 95;
                    } else {
                        logText = `[${ts}] [INFO NOMINAL] Entity: user_staff_11 | Event: FILE_READ (Normal Baseline)\n` +
                                  `[${ts}] [INFERENCE] P99 Latency: 1.45ms | Memory: 1.97 KB\n` +
                                  `[${ts}] [STAGE 1 IsoForest] Score: 0.12 | [STAGE 2 LightGBM] Class: BENIGN (0.998)\n` +
                                  `[${ts}] [TreeSHAP] Baseline metrics nominal. Zero threat indicators detected.`;
                        f1 = 2; f2 = 5; f3 = 2; f4 = 4;
                    }

                    log.innerText += '\\n\\n' + logText;
                    log.scrollTop = log.scrollHeight;

                    document.getElementById('f1_bar').style.width = f1 + '%';
                    document.getElementById('f1_val').innerText = '+' + (f1 / 100).toFixed(2);

                    document.getElementById('f2_bar').style.width = f2 + '%';
                    document.getElementById('f2_val').innerText = '+' + (f2 / 100).toFixed(2);

                    document.getElementById('f3_bar').style.width = f3 + '%';
                    document.getElementById('f3_val').innerText = '+' + (f3 / 100).toFixed(2);

                    document.getElementById('f4_bar').style.width = f4 + '%';
                    document.getElementById('f4_val').innerText = '+' + (f4 / 100).toFixed(2);
                }
            </script>
"""

CIPHERPULSE_CONTENT = """
            <section class="portfolio-case-study">
                <div class="project-header rv">
                    <span class="project-badge">HIGH-PERFORMANCE C++17 DPI</span>
                    <h2 class="display-lg" style="margin-bottom: 10px;">CipherPulse: Multi-Threaded Encrypted Traffic Intelligence</h2>
                    <p class="tagline">Line-Rate Packet Inspection, JA4+ Fingerprinting & Non-SNI Traffic Classification</p>
                </div>

                <!-- Metrics Grid -->
                <div class="metrics-row rv">
                    <div class="metric-box">
                        <span class="metric-val">100k+</span>
                        <span class="metric-lbl">Single-Core pps</span>
                    </div>
                    <div class="metric-box">
                        <span class="metric-val">ZERO</span>
                        <span class="metric-lbl">Hot-Path Lock Contention</span>
                    </div>
                    <div class="metric-box">
                        <span class="metric-val">100%</span>
                        <span class="metric-lbl">C2 Beaconing Detection</span>
                    </div>
                    <div class="metric-box">
                        <span class="metric-val">Zero</span>
                        <span class="metric-lbl">External Dependencies</span>
                    </div>
                </div>

                <!-- Architectural Flow Diagram -->
                <div class="arch-diagram-box rv">
                    <span class="kicker-label">C++17 FAST-PATH ARCHITECTURE</span>
                    <h4 class="heading-md" style="margin: 10px 0 15px 0;">Lock-Free 5-Tuple Consistent Hashing &amp; JA4+ Fingerprinting</h4>
                    <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:8px;">
                        <div class="arch-node">RAW Socket Capture<br><small style="font-weight:normal;">AF_PACKET / eBPF</small></div>
                        <span class="arch-arrow">&rarr;</span>
                        <div class="arch-node">5-Tuple Consistent Hash<br><small style="font-weight:normal;">Zero-Mutex Dispatch</small></div>
                        <span class="arch-arrow">&rarr;</span>
                        <div class="arch-node">Fast-Path Worker Threads<br><small style="font-weight:normal;">C++17 Ring Buffers</small></div>
                        <span class="arch-arrow">&rarr;</span>
                        <div class="arch-node">JA4+ &amp; Entropy Engine<br><small style="font-weight:normal;">Welford CoV Profiler</small></div>
                        <span class="arch-arrow">&rarr;</span>
                        <div class="arch-node">C2 Beaconing Alert<br><small style="font-weight:normal;">Non-SNI ETI Stream</small></div>
                    </div>
                </div>

                <!-- Interactive Live Simulation Widget -->
                <div class="sim-box rv">
                    <span class="kicker-label" style="color: var(--stamp);">INTERACTIVE DPI PACKET SIMULATOR</span>
                    <h3 class="heading-lg" style="margin: 5px 0 15px 0;">C++ Multi-Threaded Packet Stream Simulator</h3>
                    <p class="body" style="margin-bottom: 15px; font-family: var(--font-text);">Simulate line-rate packet parsing, 5-tuple consistent hashing, and JA4+ TLS fingerprinting on encrypted streams:</p>

                    <div>
                        <button class="sim-btn" onclick="runPcap('tls')">▶ Stream Normal TLS 1.3 Traffic</button>
                        <button class="sim-btn" onclick="runPcap('c2')">🚨 Inject Non-SNI C2 Beaconing</button>
                        <button class="sim-btn" onclick="runPcap('threads')">⚙️ Fast-Path Worker Thread Distribution</button>
                    </div>

                    <div class="sim-terminal" id="dpiTerminal">
[DPI INIT] C++17 Multi-Threaded Engine Initialized.
[DPI CONFIG] Fast-Path Worker Threads: 4 | Consistent Hash Ring: ACTIVE.
[DPI CONFIG] Zero external dependencies. Strict-aliasing safe memcpy enabled.
Ready. Select a test stream scenario above...
                    </div>
                </div>

                <div class="case-study-grid rv">
                    <div class="text-block">
                        <h3 class="heading-lg" style="margin-bottom: 20px;">Key Technical Innovations</h3>
                        <ul>
                            <li><b>Lock-Free Consistent Hashing:</b> Packets are routed via 5-tuple consistent hashing to isolated Fast Path (FP) threads, eliminating cross-thread mutex bottlenecks.</li>
                            <li><b>Non-SNI Traffic Intelligence (ETI):</b> Classifies encrypted traffic when Encrypted Client Hello (ECH) hides SNI using JA4+ TLS fingerprinting and Welford online flow statistics ($\text{CoV} < 0.12$ beaconing).</li>
                            <li><b>Pure C++17 Memory Safety:</b> Strict-aliasing safe packet parsing using <code>std::memcpy</code> without external dependencies.</li>
                        </ul>
                    </div>
                    <div class="text-block">
                        <h3 class="heading-lg" style="margin-bottom: 20px;">The Real-World Scenario</h3>
                        <p class="body-lg"><span class="dropcap">M</span>odern malware and C2 frameworks (such as Cobalt Strike or Sliver) hide command channels inside standard TLS 1.3 encrypted streams, rendering traditional Deep Packet Inspection (DPI) helpless without full SSL decryption.</p>
                        <p class="body-lg" style="margin-top: 15px;">CipherPulse inspects packets at line-rate without TLS decryption by extracting JA4+ client fingerprints and tracking flow inter-arrival times using Welford's algorithm to flag periodic beaconing.</p>
                    </div>
                </div>
                
                <!-- Links -->
                <div class="project-links rv">
                    <a href="https://github.com/AJ1312/CipherPulse" target="_blank" class="btn-github">⭐ View Code on GitHub</a>
                </div>
            </section>

            <script>
                function runPcap(type) {
                    const term = document.getElementById('dpiTerminal');
                    const ts = new Date().toISOString().substring(11, 19);

                    let msg = '';
                    if (type === 'tls') {
                        msg = `[${ts}] [FP-THREAD-01] PKT #10482: 192.168.1.45:54321 -> 142.250.190.46:443 [TLS 1.3]\n` +
                              `[${ts}] [JA4+ ENGINE] Hash: t13d151600_8daaf6152702_202020202020 | SNI: www.google.com\n` +
                              `[${ts}] [WELFORD STATS] Inter-arrival mean: 452ms | StdDev: 310ms | CoV: 0.686 (NON-PERIODIC)\n` +
                              `[${ts}] [CLASSIFICATION] Status: CLEAN (BENIGN_BROWSING) | Throughput: 114,200 pps`;
                    } else if (type === 'c2') {
                        msg = `[${ts}] [FP-THREAD-03] PKT #10483: 10.0.4.12:49152 -> 185.220.101.5:443 [TLS 1.3 (ECH)]\n` +
                              `[${ts}] [JA4+ ENGINE] Hash: t13d190800_c84a8b291410_000000000000 | SNI: HIDDEN (ECH)\n` +
                              `[${ts}] [WELFORD STATS] Inter-arrival mean: 5000ms | StdDev: 12ms | CoV: 0.0024 (< 0.12 THRESHOLD)\n` +
                              `[${ts}] [ALERT CRITICAL] Non-SNI C2 Beaconing Detected! Target: 185.220.101.5 | Action: ETI STREAM ALERT`;
                    } else {
                        msg = `[${ts}] [HASH RING DIST] Distributing 100,000 packets across 4 Fast-Path Workers:\n` +
                              `  -> FP-Worker-0: 25,014 pkts (0 mutex locks, 0 drops)\n` +
                              `  -> FP-Worker-1: 24,982 pkts (0 mutex locks, 0 drops)\n` +
                              `  -> FP-Worker-2: 25,008 pkts (0 mutex locks, 0 drops)\n` +
                              `  -> FP-Worker-3: 24,996 pkts (0 mutex locks, 0 drops)\n` +
                              `[PERF METRIC] Zero Hot-Path Lock Contention | Total System Throughput: 448,000 pps (Combined)`;
                    }

                    term.innerText += '\\n\\n' + msg;
                    term.scrollTop = term.scrollHeight;
                }
            </script>
"""

with open('pages/sentinel-stream.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'Sentinel-Stream').replace('{content}', SENTINEL_CONTENT))

with open('pages/cipherpulse.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'CipherPulse').replace('{content}', CIPHERPULSE_CONTENT))
print("Successfully generated self-contained interactive project pages!")
