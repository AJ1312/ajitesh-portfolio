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

                <!-- Live Demo / Screenshot Banner -->
                <div class="featured-image rv" style="filter: grayscale(100%) contrast(1.1); border: 2px solid var(--rule-dark);">
                    <img src="../output/paper_architecture_diagram.png" alt="SENTINEL-STREAM System Architecture" style="width:100%;">
                    <span class="image-caption">Figure 1: End-to-End System Pipeline (Ingestion ➔ O(1) Profiler ➔ Two-Stage ML ➔ TreeSHAP)</span>
                </div>

                <!-- Live Interactive Simulation Container -->
                <div class="project-demo-container rv" style="margin: 40px 0; padding: 20px; border: 1px solid var(--rule); background: var(--paper-warm);">
                    <h3 class="heading-lg" style="margin-bottom:10px;">⚡ Interactive Live Simulator</h3>
                    <p class="body" style="margin-bottom:20px;">Click "Inject Threat Scenario" below to see sub-3ms anomaly detection and TreeSHAP waterfall explanations in real time:</p>
                    <iframe src="https://sentinel-stream.vercel.app" width="100%" height="650px" style="border:1px solid var(--rule-dark);"></iframe>
                </div>

                <!-- Project Metrics Grid -->
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

                <!-- Key Highlights -->
                <div class="case-study-grid rv">
                    <div class="text-block">
                        <h3 class="heading-lg" style="margin-bottom: 20px;">Key Innovations</h3>
                        <ul>
                            <li><b>O(1) Streaming Profiler:</b> Replaces raw event arrays with EWMA rolling stats and Count-Min Sketch tables (4 KB matrix), bounding memory per entity.</li>
                            <li><b>Zero Cold-Start Vulnerability:</b> Stage 1 Isolation Forest calculates structural anomaly scores for newly onboarded entities without historical baseline logs.</li>
                            <li><b>Inline TreeSHAP Explainability:</b> Computes exact directional feature risk attributions in &approx;30 &mu;s per alert.</li>
                        </ul>
                    </div>
                    <div class="visual-card">
                        <h4 class="heading-md" style="margin-bottom: 15px;">Real-Time Threat Explainability</h4>
                        <div style="filter: grayscale(100%) contrast(1.1);">
                            <img src="../output/shap_waterfall.png" alt="TreeSHAP Waterfall Rationale" style="width:100%; border: 1px solid var(--rule);">
                            <span class="image-caption">Figure 2: TreeSHAP Waterfall Chart detailing per-alert feature risk factors</span>
                        </div>
                    </div>
                </div>

                <!-- Links -->
                <div class="project-links rv">
                    <a href="https://github.com/AJ1312/sentinel-stream" target="_blank" class="btn-github">⭐ View Code on GitHub</a>
                    <a href="https://github.com/AJ1312/sentinel-stream-research" target="_blank" class="btn-research">🔬 View IEEE Research Artifacts</a>
                </div>
            </section>
"""

CIPHERPULSE_CONTENT = """
            <section class="portfolio-case-study">
                <div class="project-header rv">
                    <span class="project-badge">HIGH-PERFORMANCE C++17 DPI</span>
                    <h2 class="display-lg" style="margin-bottom: 10px;">CipherPulse: Multi-Threaded Encrypted Traffic Intelligence</h2>
                    <p class="tagline">Line-Rate Packet Inspection, JA4+ Fingerprinting & Non-SNI Traffic Classification</p>
                </div>

                <div class="metrics-row rv">
                    <div class="metric-box">
                        <span class="metric-val">100k+</span>
                        <span class="metric-lbl">Single-Core Throughput (pps)</span>
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

                <!-- Live Interactive Simulation Container -->
                <div class="project-demo-container rv" style="margin: 40px 0; padding: 20px; border: 1px solid var(--rule); background: var(--paper-warm);">
                    <h3 class="heading-lg" style="margin-bottom:10px;">⚡ Interactive Live Simulator</h3>
                    <p class="body" style="margin-bottom:20px;">Stream a live <code>.pcap</code> file into the dashboard to visualize JA4+ TLS fingerprinting and Shannon Entropy checks in real-time:</p>
                    <iframe src="../CipherPulse/deployable_app/static/index.html" width="100%" height="550px" style="border:1px solid var(--rule-dark);"></iframe>
                </div>

                <div class="case-study-grid rv">
                    <div class="text-block">
                        <h3 class="heading-lg" style="margin-bottom: 20px;">Key Innovations</h3>
                        <ul>
                            <li><b>Lock-Free Consistent Hashing:</b> Packets are routed via 5-tuple consistent hashing to isolated Fast Path (FP) threads, eliminating cross-thread mutex bottlenecks.</li>
                            <li><b>Non-SNI Traffic Intelligence (ETI):</b> Classifies encrypted traffic when Encrypted Client Hello (ECH) hides SNI using JA4+ TLS fingerprinting and Welford online flow statistics (CoV &lt; 0.12 beaconing).</li>
                            <li><b>Pure C++17 Memory Safety:</b> Strict-aliasing safe packet parsing using <code>std::memcpy</code> without external dependencies.</li>
                        </ul>
                    </div>
                </div>
                
                <!-- Links -->
                <div class="project-links rv">
                    <a href="https://github.com/AJ1312/CipherPulse" target="_blank" class="btn-github">⭐ View Code on GitHub</a>
                </div>
            </section>
"""

with open('pages/sentinel-stream.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'Sentinel-Stream').replace('{content}', SENTINEL_CONTENT))

with open('pages/cipherpulse.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'CipherPulse').replace('{content}', CIPHERPULSE_CONTENT))
