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
        .pill-tag {{
            display: inline-block;
            background: var(--ink);
            color: var(--paper-bright);
            padding: 4px 12px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-right: 6px;
            margin-bottom: 8px;
        }}
        .summary-box {{
            background: var(--paper-warm);
            border: 2px solid var(--rule-dark);
            padding: 30px;
            margin: 30px 0;
        }}
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }}
        .metric-card-box {{
            background: var(--paper-bright);
            border: 2px solid var(--rule-dark);
            padding: 24px;
            text-align: center;
        }}
        .metric-val-huge {{
            font-family: var(--font-display);
            font-size: 42px;
            font-weight: 900;
            color: var(--stamp);
            margin-bottom: 5px;
            line-height: 1.1;
        }}
        .metric-lbl-bold {{
            font-weight: 700;
            text-transform: uppercase;
            font-size: 12px;
            letter-spacing: 0.5px;
            margin-bottom: 6px;
        }}
        .metric-desc-sm {{
            font-size: 13px;
            color: #555;
            line-height: 1.4;
        }}
        .workbench-container {{
            border: 2px solid var(--rule-dark);
            background: var(--paper-warm);
            padding: 30px;
            margin: 40px 0;
        }}
        .wb-btn-action {{
            background: var(--ink);
            color: var(--paper);
            border: 2px solid var(--ink);
            padding: 10px 18px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-right: 10px;
            margin-bottom: 10px;
            transition: all 0.2s ease;
            font-family: var(--font-body);
        }}
        .wb-btn-action:hover {{
            background: var(--stamp);
            border-color: var(--stamp);
            color: #fff;
        }}
        .wb-table-clean {{
            width: 100%;
            border-collapse: collapse;
            font-family: var(--font-body);
            font-size: 14px;
            margin-top: 20px;
            background: var(--paper-bright);
            border: 2px solid var(--rule-dark);
        }}
        .wb-table-clean th {{
            background: var(--ink);
            color: var(--paper-bright);
            padding: 12px;
            text-align: left;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .wb-table-clean td {{
            padding: 14px 12px;
            border-bottom: 1px solid var(--rule);
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
        .badge-red {{
            display: inline-block;
            padding: 4px 10px;
            background: #fee2e2;
            color: #dc2626;
            border: 1px solid #dc2626;
            font-weight: 700;
            font-size: 12px;
        }}
        .badge-amber {{
            display: inline-block;
            padding: 4px 10px;
            background: #fef3c7;
            color: #d97706;
            border: 1px solid #d97706;
            font-weight: 700;
            font-size: 12px;
        }}
        .badge-green {{
            display: inline-block;
            padding: 4px 10px;
            background: #dcfce7;
            color: #15803d;
            border: 1px solid #15803d;
            font-weight: 700;
            font-size: 12px;
        }}
        .arch-image-card {{
            border: 2px solid var(--rule-dark);
            background: var(--paper-bright);
            padding: 12px;
            margin: 25px 0;
        }}
        .arch-image-card img {{
            width: 100%;
            height: auto;
            display: block;
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
                        <h1 class="display-xl" style="margin-bottom: 15px; font-size: 50px;">SENTINEL-STREAM</h1>
                        <p class="display-sm" style="max-width: 900px; font-style: italic; line-height: 1.4; margin-bottom: 22px;">The AI Security Guard That Detects Rogue Accounts &amp; Data Theft in Real Time Without Crashing Servers</p>
                        
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

            <!-- 2. MOTIVATION PARAGRAPH -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label" style="color: var(--stamp);">PROJECT MOTIVATION</span>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Why I Built SENTINEL-STREAM</h3>
                        <p class="body-lg" style="line-height: 1.75;"><span class="dropcap">I</span> built SENTINEL-STREAM after noticing a pattern in how security tools actually fail in practice: it's rarely that they can't detect something unusual, it's that they detect too much, too vaguely, and analysts stop trusting the alerts. I wanted to build a behavioral anomaly engine that solved the boring, unglamorous parts of that problem properly — bounded memory that doesn't grow forever as more entities get monitored, meaningful scoring for entities with zero history, and an explanation attached to every single alert instead of a bare confidence score. This became my submission to Honeywell's own Q4 hackathon problem statement on behavioral anomaly detection.</p>
                    </div>
                </div>
            </section>

            <!-- 3. REAL-WORLD USE CASE SCENARIO -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label" style="color: var(--stamp);">REAL-WORLD USE CASE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Catching Stolen Credentials Before Damage Happens</h3>
                        <p class="body-lg" style="line-height: 1.75;"><span class="dropcap">P</span>icture a mid-sized company's security team monitoring thousands of employee accounts and IoT devices. A contractor's credentials get compromised, and the attacker logs in from an unfamiliar location at an unusual hour, then starts quietly accessing a finance database this account has never touched before. A rule-based tool would either miss this (nothing here breaks a hard rule) or bury it under hundreds of other low-quality alerts. SENTINEL-STREAM scores this event in real time using the contractor's own behavioral baseline, flags it within milliseconds even though the account has limited history, and hands the analyst a plain-language reason — unusual login velocity, first-time resource access — instead of a bare "anomaly detected."</p>
                    </div>
                </div>
            </section>

            <!-- 4. GENERATED ARCHITECTURE DIAGRAM IMAGE -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label" style="color: var(--stamp);">SYSTEM ARCHITECTURE DIAGRAM</span>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0;">O(1) Streaming Profiler &amp; Threat Pipeline</h3>
                        
                        <div class="arch-image-card">
                            <img src="../images/architecture/sentinel_stream_arch.png" alt="SENTINEL-STREAM End-to-End System Architecture Diagram">
                        </div>
                    </div>
                </div>
            </section>

            <!-- 5. INTERACTIVE LIVE DEMO WORKBENCH -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">INTERACTIVE CONSOLE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0;">Live Threat Radar &amp; AI Explanation Workbench</h3>
                        <p class="body-lg" style="margin-bottom: 25px;">Click any security test button below to trigger a live threat evaluation and watch how SENTINEL-STREAM explains the risk in plain English:</p>

                        <div class="workbench-container">
                            <div>
                                <button class="wb-btn-action" onclick="runSentinelSim('brute')">⚡ Test 1: Password Attack Surge</button>
                                <button class="wb-btn-action" onclick="runSentinelSim('travel')">🌍 Test 2: Impossible Location Login</button>
                                <button class="wb-btn-action" onclick="runSentinelSim('exfil')">📤 Test 3: Secret Database Exfiltration</button>
                                <button class="wb-btn-action" onclick="runSentinelSim('normal')">✅ Test 4: Normal Employee Work Baseline</button>
                            </div>

                            <table class="wb-table-clean">
                                <thead>
                                    <tr>
                                        <th style="width: 110px;">Timestamp</th>
                                        <th style="width: 160px;">User Account</th>
                                        <th>Observed Event</th>
                                        <th style="width: 150px;">Threat Level</th>
                                        <th style="width: 100px;">Latency</th>
                                        <th>Plain-English AI Explanation</th>
                                    </tr>
                                </thead>
                                <tbody id="wbSentinelBody">
                                    <tr class="anim-fade-row">
                                        <td>18:51:01</td>
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
            </section>

            <!-- 6. STEP-BY-STEP PIPELINE WALKTHROUGH -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">DETAILED WALKTHROUGH</span>
                        <h3 class="heading-lg" style="margin: 10px 0 25px 0;">6-Stage Execution Pipeline</h3>

                        <div style="border-bottom: 1px solid var(--rule); padding: 18px 0;">
                            <h4 class="heading-md"><span style="color:var(--stamp); font-weight:900;">01</span> Event Ingestion</h4>
                            <p class="body-lg">Raw audit logs (logins, database access, file downloads) stream in via REST API or Kafka queues without dropping client connections.</p>
                            <p class="meta" style="margin-top:6px;"><b>Tools:</b> FastAPI, Pydantic &middot; <b>Why:</b> Async non-blocking endpoints handle thousands of concurrent events.</p>
                        </div>

                        <div style="border-bottom: 1px solid var(--rule); padding: 18px 0;">
                            <h4 class="heading-md"><span style="color:var(--stamp); font-weight:900;">02</span> Streaming Feature Engineering</h4>
                            <p class="body-lg">Builds a 21-feature vector on the fly using EWMA rolling averages and Count-Min Sketch tables, updating statistics in fixed memory without saving raw logs.</p>
                            <p class="meta" style="margin-top:6px;"><b>Tools:</b> NumPy, Pandas &middot; <b>Why:</b> Vectorized array operations compute statistics in sub-millisecond speed.</p>
                        </div>

                        <div style="border-bottom: 1px solid var(--rule); padding: 18px 0;">
                            <h4 class="heading-md"><span style="color:var(--stamp); font-weight:900;">03</span> Stage 1: Isolation Forest Cold-Start Prior</h4>
                            <p class="body-lg">Evaluates structural anomaly distance for brand-new users or devices with zero historical logs, eliminating cold-start vulnerability.</p>
                            <p class="meta" style="margin-top:6px;"><b>Tools:</b> scikit-learn (<code>IsolationForest</code>) &middot; <b>Why:</b> Tree isolation scoring requires zero historical user baselines.</p>
                        </div>

                        <div style="border-bottom: 1px solid var(--rule); padding: 18px 0;">
                            <h4 class="heading-md"><span style="color:var(--stamp); font-weight:900;">04</span> Stage 2: LightGBM Threat Classifier</h4>
                            <p class="body-lg">Classifies the exact attack category (Brute Force, Impossible Travel, Data Theft) by evaluating features in a fast decision tree.</p>
                            <p class="meta" style="margin-top:6px;"><b>Tools:</b> LightGBM &middot; <b>Why:</b> Leaf-wise tree growth runs 24.6× faster than Random Forest.</p>
                        </div>

                        <div style="border-bottom: 1px solid var(--rule); padding: 18px 0;">
                            <h4 class="heading-md"><span style="color:var(--stamp); font-weight:900;">05</span> TreeSHAP Explainability Engine</h4>
                            <p class="body-lg">Walks decision tree paths directly to calculate exact feature attributions, explaining why the alert fired in microseconds.</p>
                            <p class="meta" style="margin-top:6px;"><b>Tools:</b> SHAP (TreeSHAP) &middot; <b>Why:</b> Exact Shapley values are calculated analytically without noisy perturbation sampling.</p>
                        </div>

                        <div style="padding: 18px 0;">
                            <h4 class="heading-md"><span style="color:var(--stamp); font-weight:900;">06</span> Live Dashboard Stream</h4>
                            <p class="body-lg">Pushes explained alert payloads directly to security analyst dashboards over persistent Server-Sent Events (SSE).</p>
                            <p class="meta" style="margin-top:6px;"><b>Tools:</b> FastAPI (SSE), Chart.js &middot; <b>Why:</b> Real-time streaming with zero WebSocket overhead.</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 7. RESULTS METRICS GRID -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label" style="color: var(--stamp);">EMPIRICAL BENCHMARKS</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0;">Verified Results</h3>

                        <div class="metrics-grid">
                            <div class="metric-card-box">
                                <div class="metric-val-huge">~4.2 KB</div>
                                <div class="metric-lbl-bold">Per-Entity Memory</div>
                                <div class="metric-desc-sm">Audited per-user RAM footprint (EWMA + Count-Min Sketch). Can reach 2KB with 128-width sketch.</div>
                            </div>

                            <div class="metric-card-box">
                                <div class="metric-val-huge">2.64 ms</div>
                                <div class="metric-lbl-bold">P99 Inference Latency</div>
                                <div class="metric-desc-sm">Single-event end-to-end model classification speed (P50 latency: 1.84 ms).</div>
                            </div>

                            <div class="metric-card-box">
                                <div class="metric-val-huge">0.9403</div>
                                <div class="metric-lbl-bold">NSL-KDD Macro F1</div>
                                <div class="metric-desc-sm">5-fold cross-validation score (&plusmn;0.0091) across standard cybersecurity benchmark.</div>
                            </div>

                            <div class="metric-card-box">
                                <div class="metric-val-huge">24.67×</div>
                                <div class="metric-lbl-bold">Speedup vs Random Forest</div>
                                <div class="metric-desc-sm">LightGBM inference (2.64 ms) vs baseline Random Forest (65.15 ms) on identical hardware.</div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 8. KEY TECHNICAL DECISION CALLOUT -->
            <section class="section" style="padding: 30px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <div style="border-left: 6px solid var(--stamp); background: var(--paper-warm); border-top: 2px solid var(--rule-dark); border-right: 2px solid var(--rule-dark); border-bottom: 2px solid var(--rule-dark); padding: 25px 30px;">
                            <span class="kicker-label" style="color: var(--stamp);">KEY DESIGN DECISION</span>
                            <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Constant $O(1)$ Per-Entity Memory Scaling</h3>
                            <p class="body-lg" style="line-height: 1.7; margin: 0;"><span class="dropcap">T</span>o prevent memory exhaustion under continuous streaming, SENTINEL-STREAM enforces a strict constant memory footprint per monitored entity ($\approx 4.2\text{ KB}$). Instead of storing historical event lists $O(N)$, features are computed via Exponentially Weighted Moving Averages (EWMA) and Count-Min Sketch tables. <i>Note on scaling:</i> While memory per entity remains strictly $O(1)$ regardless of stream duration, total system memory scales linearly with the total number of active monitored entities ($O(M)$ for $M$ entities).</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 9. GITHUB CTA & IMPROVEMENTS -->
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
                function runSentinelSim(type) {
                    const tbody = document.getElementById('wbSentinelBody');
                    const ts = new Date().toISOString().substring(11, 19);

                    let user = '', event = '', badge = '', lat = '', why = '';

                    if (type === 'brute') {
                        user = 'admin_john';
                        event = '45 failed login attempts in 10 seconds';
                        badge = '<span class="badge-red">CRITICAL THREAT</span>';
                        lat = '1.84 ms';
                        why = 'Extreme login failure spike (+0.54 risk) + rapid event velocity.';
                    } else if (type === 'travel') {
                        user = 'exec_rachel';
                        event = 'Logged in from Tokyo 5 minutes after NY session';
                        badge = '<span class="badge-amber">HIGH RISK</span>';
                        lat = '2.12 ms';
                        why = 'Impossible physical movement speed (+0.68 geo-velocity risk).';
                    } else if (type === 'exfil') {
                        user = 'dev_service';
                        event = 'Downloaded 14 GB customer database off-hours';
                        badge = '<span class="badge-red">CRITICAL THREAT</span>';
                        lat = '1.95 ms';
                        why = 'Abnormal outbound data volume (+0.76 EWMA volume spike).';
                    } else {
                        user = 'sarah_marketing';
                        event = 'Opened standard project documents';
                        badge = '<span class="badge-green">SAFE (NOMINAL)</span>';
                        lat = '1.42 ms';
                        why = 'Activity matches normal daily baseline behavior.';
                    }

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
                }
            </script>
"""

CIPHERPULSE_CONTENT = """
            <!-- 1. HERO SECTION -->
            <section class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 45px 0 35px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <p class="kicker-label">FIELD DISPATCH &mdash; HIGH-SPEED NETWORKING &amp; SECURITY</p>
                        <h1 class="display-xl" style="margin-bottom: 15px; font-size: 50px;">CipherPulse</h1>
                        <p class="display-sm" style="max-width: 900px; font-style: italic; line-height: 1.4; margin-bottom: 22px;">The X-Ray Security Scanner for Encrypted Traffic That Catches Hidden Malware Without Invading Privacy</p>
                        
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

            <!-- 2. MOTIVATION PARAGRAPH -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label" style="color: var(--stamp);">PROJECT MOTIVATION</span>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Why I Built CipherPulse</h3>
                        <p class="body-lg" style="line-height: 1.75;"><span class="dropcap">M</span>ost of the internet's traffic is encrypted now, and newer TLS features like Encrypted Client Hello are starting to hide even the destination hostname that used to be visible during the handshake. I wanted to explore how much you can still infer about a connection — what kind of application it is, whether it's malicious — using only signals that remain visible even under full encryption: how a client negotiates its handshake, DNS lookups that precede a connection, and the shape and timing of the encrypted traffic itself. CipherPulse is a multi-threaded C++ engine built around that constraint.</p>
                    </div>
                </div>
            </section>

            <!-- 3. REAL-WORLD USE CASE SCENARIO -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label" style="color: var(--stamp);">REAL-WORLD USE CASE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Catching Encrypted Hacker Signals at Line-Rate Speed</h3>
                        <p class="body-lg" style="line-height: 1.75;"><span class="dropcap">P</span>icture a network security appliance sitting at a company's edge, watching gigabit traffic in real time. Malware on an internal machine tries to phone home to its command-and-control server over a fully encrypted connection with no recognizable hostname. CipherPulse can't decrypt the traffic — it doesn't need to. It fingerprints the way the malware's TLS client negotiates its handshake and matches it against known C2 signatures, notices that the packets checked in at suspiciously regular intervals, and flags the flow as likely C2 beaconing — all while processing packets from thousands of other simultaneous connections without a single thread ever waiting on another.</p>
                    </div>
                </div>
            </section>

            <!-- 4. GENERATED ARCHITECTURE DIAGRAM IMAGE -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label" style="color: var(--stamp);">SYSTEM ARCHITECTURE DIAGRAM</span>
                        <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Lock-Free Fast-Path Traffic Inspection Pipeline</h3>
                        
                        <div class="arch-image-card">
                            <img src="../images/architecture/cipherpulse_arch.png" alt="CipherPulse System Architecture Diagram">
                        </div>
                    </div>
                </div>
            </section>

            <!-- 5. INTERACTIVE LIVE DEMO WORKBENCH -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">INTERACTIVE CONSOLE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0;">Live Encrypted Traffic X-Ray Inspection Workbench</h3>
                        <p class="body-lg" style="margin-bottom: 25px;">Select a network stream to observe real-time JA4+ fingerprint extraction and threat classification:</p>

                        <div class="workbench-container">
                            <div>
                                <button class="wb-btn-action" onclick="runCipherSim('normal')">▶ Stream 1: Standard HTTPS Browsing</button>
                                <button class="wb-btn-action" onclick="runCipherSim('c2')">🚨 Stream 2: Encrypted C2 Hacker Beacon</button>
                                <button class="wb-btn-action" onclick="runCipherSim('bench')">⚡ Stream 3: High-Speed Multi-Thread Test</button>
                            </div>

                            <table class="wb-table-clean">
                                <thead>
                                    <tr>
                                        <th style="width: 110px;">Timestamp</th>
                                        <th>Network Connection</th>
                                        <th style="width: 220px;">JA4+ Fingerprint Hash</th>
                                        <th>Traffic Rhythm</th>
                                        <th style="width: 160px;">Security Verdict</th>
                                        <th style="width: 140px;">Action Taken</th>
                                    </tr>
                                </thead>
                                <tbody id="wbCipherBody">
                                    <tr class="anim-fade-row">
                                        <td>18:51:01</td>
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
            </section>

            <!-- 6. STEP-BY-STEP PIPELINE WALKTHROUGH -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">DETAILED WALKTHROUGH</span>
                        <h3 class="heading-lg" style="margin: 10px 0 25px 0;">7-Stage Packet Inspection Pipeline</h3>

                        <div style="border-bottom: 1px solid var(--rule); padding: 18px 0;">
                            <h4 class="heading-md"><span style="color:var(--stamp); font-weight:900;">01</span> RAW Packet Ingestion</h4>
                            <p class="body-lg">Captures raw ethernet frames directly from network sockets using eBPF or high-speed AF_PACKET for zero-copy memory speed.</p>
                            <p class="meta" style="margin-top:6px;"><b>Tools:</b> eBPF / AF_PACKET, POSIX threads &middot; <b>Why:</b> Captures line-rate headers directly at kernel ingress without socket buffer copy overhead.</p>
                        </div>

                        <div style="border-bottom: 1px solid var(--rule); padding: 18px 0;">
                            <h4 class="heading-md"><span style="color:var(--stamp); font-weight:900;">02</span> Consistent 5-Tuple Hashing</h4>
                            <p class="body-lg">Hashes the 5-tuple (source/dest IP, ports, protocol) so all packets of a single flow land on the exact same worker thread queue.</p>
                            <p class="meta" style="margin-top:6px;"><b>Tools:</b> <code>std::hash</code>, custom <code>ThreadSafeQueue</code> &middot; <b>Why:</b> Eliminates cross-thread locks because one thread owns a flow's lifecycle.</p>
                        </div>

                        <div style="border-bottom: 1px solid var(--rule); padding: 18px 0;">
                            <h4 class="heading-md"><span style="color:var(--stamp); font-weight:900;">03</span> Lock-Free Fast Path Processing</h4>
                            <p class="body-lg">Worker threads execute inside dedicated loops with isolated flow tables, enabling 100% lock-free lookups on the hot path.</p>
                            <p class="meta" style="margin-top:6px;"><b>Tools:</b> C++17 STL, <code>std::thread</code> &middot; <b>Why:</b> Eliminates mutex contention on core packet loops during high traffic bursts.</p>
                        </div>

                        <div style="border-bottom: 1px solid var(--rule); padding: 18px 0;">
                            <h4 class="heading-md"><span style="color:var(--stamp); font-weight:900;">04</span> JA4+ Fingerprint Extraction</h4>
                            <p class="body-lg">Parses TLS ClientHello handshakes, sorts ciphers, filters GREASE noise extensions, and hashes into a stable JA4 signature using FNV-1a.</p>
                            <p class="meta" style="margin-top:6px;"><b>Tools:</b> Pure C++17, FNV-1a Hash &middot; <b>Why:</b> Identifies client applications (Cobalt Strike, Sliver) even when hostname is encrypted.</p>
                        </div>

                        <div style="border-bottom: 1px solid var(--rule); padding: 18px 0;">
                            <h4 class="heading-md"><span style="color:var(--stamp); font-weight:900;">05</span> Active DNS Correlation Cache</h4>
                            <p class="body-lg">Maintains an in-memory cache of IP-to-domain mappings from plaintext DNS responses, automatically expiring entries via TTL timestamps.</p>
                            <p class="meta" style="margin-top:6px;"><b>Tools:</b> Custom DNS Correlator &middot; <b>Why:</b> Labels encrypted IP connections with human-readable domain names.</p>
                        </div>

                        <div style="border-bottom: 1px solid var(--rule); padding: 18px 0;">
                            <h4 class="heading-md"><span style="color:var(--stamp); font-weight:900;">06</span> Welford Flow Periodicity Check</h4>
                            <p class="body-lg">Calculates running packet inter-arrival statistics using Welford's algorithm to compute Coefficient of Variation ($\text{CoV} < 0.12$) for beaconing.</p>
                            <p class="meta" style="margin-top:6px;"><b>Tools:</b> Welford Online Variance Engine &middot; <b>Why:</b> Computes exact numerical variance in constant $O(1)$ time per packet.</p>
                        </div>

                        <div style="padding: 18px 0;">
                            <h4 class="heading-md"><span style="color:var(--stamp); font-weight:900;">07</span> Structured Audit Log Output</h4>
                            <p class="body-lg">Outputs filtered PCAPs and streams structured JSON threat alerts detailing matched JA4 signatures and recommended eBPF drop rules.</p>
                            <p class="meta" style="margin-top:6px;"><b>Tools:</b> C++ File I/O, nlohmann::json &middot; <b>Why:</b> Structured audit logs easily consumed by enterprise SIEM modules.</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 7. RESULTS METRICS GRID -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label" style="color: var(--stamp);">EMPIRICAL BENCHMARKS</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0;">System Performance</h3>

                        <div class="metrics-grid">
                            <div class="metric-card-box">
                                <div class="metric-val-huge">ZERO</div>
                                <div class="metric-lbl-bold">Hot-Path Lock Contention</div>
                                <div class="metric-desc-sm">100% thread-isolated flow tables via deterministic 5-tuple consistent hashing.</div>
                            </div>

                            <div class="metric-card-box">
                                <div class="metric-val-huge">JA4+</div>
                                <div class="metric-lbl-bold">TLS Fingerprinting</div>
                                <div class="metric-desc-sm">Extracts ClientHello ciphers &amp; extensions while filtering GREASE noise.</div>
                            </div>

                            <div class="metric-card-box">
                                <div class="metric-val-huge">&lt; 0.12</div>
                                <div class="metric-lbl-bold">C2 Beaconing Threshold</div>
                                <div class="metric-desc-sm">Welford Coefficient of Variation ($\text{CoV}$) threshold flagging automated malware pulses.</div>
                            </div>

                            <div class="metric-card-box">
                                <div class="metric-val-huge">ZERO</div>
                                <div class="metric-lbl-bold">External Dependencies</div>
                                <div class="metric-desc-sm">Built in pure C++17 STL for maximum portability and zero third-party library bloat.</div>
                            </div>
                        </div>

                        <p class="meta text-center" style="margin-top: 15px; color: #666; font-style: italic;">
                            *Note on throughput: CipherPulse targets fast-path lock-free design limits. Throughput figures reflect PCAP offline benchmarks and multi-thread ring queue tests, pending full hardware-in-the-loop 10GbE NIC validation.
                        </p>
                    </div>
                </div>
            </section>

            <!-- 8. KEY TECHNICAL DECISION CALLOUT -->
            <section class="section" style="padding: 30px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <div style="border-left: 6px solid var(--stamp); background: var(--paper-warm); border-top: 2px solid var(--rule-dark); border-right: 2px solid var(--rule-dark); border-bottom: 2px solid var(--rule-dark); padding: 25px 30px;">
                            <span class="kicker-label" style="color: var(--stamp);">KEY DESIGN DECISION</span>
                            <h3 class="heading-lg" style="margin: 10px 0 15px 0;">Lock-Free Threading via 5-Tuple Consistent Hashing</h3>
                            <p class="body-lg" style="line-height: 1.7; margin: 0;"><span class="dropcap">R</span>ather than using a shared global connection table protected by mutex locks, CipherPulse routes every incoming packet through a 5-tuple consistent hashing function. Because all packets belonging to a specific TCP/UDP flow hash to the exact same worker thread, that worker thread owns 100% of the flow's lifecycle inside an isolated <code>std::unordered_map</code>. This eliminates cross-thread mutex contention on the packet processing hot path, allowing worker threads to scale linearly across CPU cores without locking overhead.</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 9. GITHUB CTA & IMPROVEMENTS -->
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
                function runCipherSim(type) {
                    const tbody = document.getElementById('wbCipherBody');
                    const ts = new Date().toISOString().substring(11, 19);

                    let conn = '', ja4 = '', rhythm = '', badge = '', action = '';

                    if (type === 'c2') {
                        conn = '10.0.4.12 &rarr; 185.220.101.5 (Hidden IP)';
                        ja4 = 't13d190800_c84a8b291410';
                        rhythm = 'Strict 5.0s metronome pulse (CoV < 0.12)';
                        badge = '<span class="badge-red">ALERT: C2 BEACON</span>';
                        action = 'Blocked via eBPF';
                    } else if (type === 'bench') {
                        conn = '100,000 Pkts/sec Stream';
                        ja4 = 'Multi-Flow Hash Ring';
                        rhythm = '4 CPU Cores Active (0 Mutex Locks)';
                        badge = '<span class="badge-amber">LOCK-FREE OK</span>';
                        action = '0 Mutex Drops';
                    } else {
                        conn = '192.168.1.45 &rarr; Google:443';
                        ja4 = 't13d151600_8daaf6152702';
                        rhythm = 'Random human interaction timing';
                        badge = '<span class="badge-green">SAFE (BENIGN)</span>';
                        action = 'Allowed';
                    }

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
                }
            </script>
"""

with open('pages/sentinel-stream.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'SENTINEL-STREAM').replace('{content}', SENTINEL_CONTENT))

with open('pages/cipherpulse.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'CipherPulse').replace('{content}', CIPHERPULSE_CONTENT))

print("Successfully generated cool, clean, non-overlapping pages without IEEE mentions!")
