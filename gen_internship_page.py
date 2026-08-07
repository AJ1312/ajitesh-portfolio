import os

internship_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hindalco Workforce Queue System — The Sharma Dispatch</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400;1,700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/styles.css">
    <style>
        .work-sim-container {
            border: 2px solid var(--rule-dark);
            background: #0f172a;
            color: #f8fafc;
            border-radius: 8px;
            padding: 30px;
            margin: 40px 0;
            font-family: var(--font-mono, monospace);
            box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        }
        .work-sim-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #334155;
            padding-bottom: 15px;
            margin-bottom: 20px;
        }
        .status-dot {
            display: inline-block;
            width: 10px;
            height: 10px;
            background: #22c55e;
            border-radius: 50%;
            margin-right: 8px;
        }
        .work-btn {
            background: #1e293b;
            color: #e2e8f0;
            border: 1px solid #475569;
            padding: 10px 16px;
            font-size: 12px;
            font-weight: bold;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-radius: 4px;
            margin-right: 10px;
            margin-bottom: 10px;
            transition: all 0.2s ease;
        }
        .work-btn:hover {
            background: #3b82f6;
            border-color: #3b82f6;
            color: #fff;
        }
        .console-output {
            background: #020617;
            color: #38bdf8;
            padding: 20px;
            border-radius: 6px;
            height: 220px;
            overflow-y: auto;
            font-size: 13px;
            line-height: 1.6;
            border: 1px solid #1e293b;
            margin-top: 20px;
        }
        .metric-badge {
            background: #1e293b;
            padding: 8px 14px;
            border-radius: 4px;
            border: 1px solid #334155;
            font-size: 12px;
        }
        .arch-diagram-box {
            background: var(--paper-bright);
            border: 2px solid var(--rule-dark);
            padding: 30px;
            margin: 25px 0;
            text-align: center;
        }
        .arch-node {
            display: inline-block;
            border: 1px solid var(--rule-dark);
            background: var(--paper-warm);
            padding: 10px 15px;
            margin: 5px;
            font-size: 13px;
            font-weight: bold;
        }
        .arch-arrow {
            display: inline-block;
            margin: 0 5px;
            font-weight: bold;
            color: var(--stamp);
        }
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
            
            <!-- HEADER -->
            <section class="section" style="padding: 40px 0 20px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="project-badge" style="background:var(--ink); color:var(--paper); padding:4px 10px; font-weight:bold; font-size:12px;">HINDALCO INDUSTRIES (ADITYA BIRLA GROUP)</span>
                        <h1 class="display-lg" style="margin: 15px 0 10px 0; font-size: 42px;">Workforce Queue &amp; Scheduling System</h1>
                        <p class="tagline" style="font-size: 20px; font-style: italic; color: #444;">Enterprise Digitization of Shift Allocation &amp; Workforce Logistics for 1,200+ Site Personnel</p>
                    </div>
                </div>
            </section>

            <!-- KEY METRICS BAR -->
            <section class="section" style="padding: 20px 0; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); margin-bottom: 40px;">
                <div class="metrics-row" style="margin:0; border:none; padding:0;">
                    <div class="metric-box">
                        <span class="metric-val" style="font-size:36px; color:var(--stamp);">1,200+</span>
                        <span class="metric-lbl">Personnel Managed Daily</span>
                    </div>
                    <div class="metric-box">
                        <span class="metric-val" style="font-size:36px; color:var(--stamp);">85%</span>
                        <span class="metric-lbl">Overhead Reduction</span>
                    </div>
                    <div class="metric-box">
                        <span class="metric-val" style="font-size:36px; color:var(--stamp);">ZERO</span>
                        <span class="metric-lbl">Scheduling Conflicts</span>
                    </div>
                    <div class="metric-box">
                        <span class="metric-val" style="font-size:36px; color:var(--stamp);">100%</span>
                        <span class="metric-lbl">Audit Trail Compliance</span>
                    </div>
                </div>
            </section>

            <!-- REAL WORK-LIFE ENTERPRISE WORKSTATION SIMULATOR -->
            <section class="section" style="padding: 10px 0 30px 0;">
                <span class="kicker-label" style="color: var(--stamp); font-size: 14px;">REAL WORK-LIFE SIMULATION</span>
                <h3 class="heading-lg" style="margin: 5px 0 20px 0;">Industrial Shift Control &amp; Queue Management Workstation</h3>

                <div class="work-sim-container">
                    <div class="work-sim-header">
                        <div>
                            <span class="status-dot"></span>
                            <span style="font-weight:bold; color:#e2e8f0;">HINDALCO // PLANT OPERATIONS CONTROL CONSOLE</span>
                        </div>
                        <div style="display:flex; gap:10px;">
                            <span class="metric-badge">Backend: Spring Boot + Java 17</span>
                            <span class="metric-badge">Database: Oracle PL/SQL</span>
                        </div>
                    </div>

                    <p style="color:#94a3b8; font-size:13px; margin-bottom:15px;">Simulate plant supervisor shift scheduling and gate verification procedures:</p>

                    <div>
                        <button class="work-btn" onclick="simHindalco('queue')">📋 Run Daily Shift Queue Audit (1,200 Personnel)</button>
                        <button class="work-btn" onclick="simHindalco('swap')">🔄 Automate Shift Allocation Swap</button>
                        <button class="work-btn" onclick="simHindalco('rbac')">🛡️ Verify Multi-Tier RBAC Security</button>
                        <button class="work-btn" onclick="simHindalco('clear')">🔄 Clear Workstation</button>
                    </div>

                    <div class="console-output" id="hindalcoTerminal">
[PLANT GATE INIT] Hindalco Industrial Queue Management System Online...
[SHIFT CONSOLE] Ready for supervisor dispatch commands. Select an action button above...
                    </div>
                </div>
            </section>

            <!-- SYSTEM ARCHITECTURE -->
            <section class="section" style="padding: 30px 0; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); margin-bottom: 40px;">
                <div class="arch-diagram-box" style="background: var(--paper-warm); border: 2px solid var(--rule-dark); padding: 30px; text-align: center;">
                    <span class="kicker-label" style="color: var(--stamp);">ENTERPRISE SYSTEM ARCHITECTURE</span>
                    <h4 class="heading-md" style="margin: 10px 0 20px 0;">Role-Based Queue Pipeline &amp; Oracle Stored Procedures</h4>
                    <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:12px; font-family: var(--font-mono, monospace);">
                        <div class="arch-node">Industrial Gate Kiosk<br><small style="font-weight:normal;">RFID / Badge Scanner</small></div>
                        <span class="arch-arrow" style="font-size:18px;">&rarr;</span>
                        <div class="arch-node">Spring Boot API Gateway<br><small style="font-weight:normal;">RESTful Middleware</small></div>
                        <span class="arch-arrow" style="font-size:18px;">&rarr;</span>
                        <div class="arch-node">RBAC Authorization Engine<br><small style="font-weight:normal;">Supervisor &amp; Security Roles</small></div>
                        <span class="arch-arrow" style="font-size:18px;">&rarr;</span>
                        <div class="arch-node">Oracle PL/SQL Procedures<br><small style="font-weight:normal;">Atomic Queue Lock &amp; Allocation</small></div>
                        <span class="arch-arrow" style="font-size:18px;">&rarr;</span>
                        <div class="arch-node">Live Dashboard &amp; Audit Trail<br><small style="font-weight:normal;">Compliance &amp; Attendance Logs</small></div>
                    </div>
                </div>
            </section>

            <!-- TECHNICAL SPECS & IMPACT -->
            <section class="section" style="padding: 20px 0 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-6 column-bordered">
                        <h3 class="heading-lg" style="margin-bottom: 20px;">Technical Innovations</h3>
                        <ul style="list-style:square; padding-left:20px; line-height:1.7; font-size:16px;">
                            <li style="margin-bottom:15px;"><b>Multi-Tier Role-Based Access Control (RBAC):</b> Implemented strict data segregation across plant floor supervisors, plant managers, and security gate personnel.</li>
                            <li style="margin-bottom:15px;"><b>PL/SQL Queue Stored Procedures:</b> Designed concurrency-safe database queue procedures handling 1,200+ simultaneous worker check-ins during peak shift handovers without deadlock.</li>
                            <li><b>Automated Auditability &amp; Reporting:</b> Eliminated manual paperwork by generating automated daily attendance logs, compliance reports, and labor cost metrics.</li>
                        </ul>
                    </div>

                    <div class="col-span-6">
                        <h3 class="heading-lg" style="margin-bottom: 20px;">The Real-World Problem Solved</h3>
                        <p class="body-lg" style="line-height:1.7;"><span class="dropcap">P</span>rior to digitizing, workforce scheduling for over 1,200 industrial site personnel at Hindalco relied on manual logbooks and physical queue cards during shift handovers. This caused severe plant gate bottlenecks, shift swap security risks, and zero real-time visibility for plant leadership.</p>
                        <p class="body-lg" style="line-height:1.7; margin-top:15px;">The digitized Workforce Queue System streamlined shift allocation, reduced gate processing times by 85%, and provided plant operations with a 100% auditable, real-time workforce management pipeline.</p>
                    </div>
                </div>
            </section>

        </main>
        
        <footer class="section" style="border-top: 4px solid var(--rule-dark); padding: 40px 0; text-align: center; margin-top: 60px;">
            <p class="meta">&copy; 2026 AJITESH SHARMA &middot; THE SHARMA DISPATCH &middot; VOL. I</p>
        </footer>
    </div>

    <script>
        function simHindalco(type) {
            const term = document.getElementById('hindalcoTerminal');
            const ts = new Date().toISOString().substring(11, 19);

            let msg = '';
            if (type === 'queue') {
                msg = `[${ts}] [PLANT GATE DISPATCH] Executing 06:00 AM Shift Queue Audit...\\n` +
                      `  -> Total Checked In: 1,214 Personnel (Shift A)\\n` +
                      `  -> Gate Processing Latency: 420ms per 100 scans (PL/SQL Stored Procedure)\\n` +
                      `  -> Gate Bottlenecks: 0 | Concurrency Lock Contention: 0.00%\\n` +
                      `  -> Allocation Status: 100% DEPLOYED TO SECTORS 1 - 8`;
            } else if (type === 'swap') {
                msg = `[${ts}] [SHIFT SWAP PROCEDURE] Emergency Shift Swap Request #HIN-8812\\n` +
                      `  -> Outgoing Worker: ID #4920 (Furnace Sector B)\\n` +
                      `  -> Replacement Worker: ID #5104 (Certified Standby Pool)\\n` +
                      `  -> Validation: Skill Matrix Verified &amp; RBAC Approved\\n` +
                      `  -> Result: Shift Roster Updated &amp; Gate RFID Badge Permissions Synced`;
            } else if (type === 'rbac') {
                msg = `[${ts}] [SECURITY RBAC AUDIT] Verifying Access Levels:\\n` +
                      `  -> Floor Supervisor: Tier 2 (Sector Allocation Only)\\n` +
                      `  -> Security Gate Kiosk: Tier 1 (Read/Verify RFID Only)\\n` +
                      `  -> Plant Manager: Tier 3 (Full Roster &amp; Labor Cost Analytics)\\n` +
                      `  -> Compliance Status: 100% AUDIT PASS (Zero Unauthorized Privilege Escalations)`;
            } else {
                msg = `[${ts}] [PLANT CONSOLE RESET] System monitoring active. Standby for supervisor commands...`;
            }

            term.innerText += '\\n\\n' + msg;
            term.scrollTop = term.scrollHeight;
        }
    </script>
</body>
</html>
"""

with open("pages/internship.html", "w") as f:
    f.write(internship_content)

print("Successfully generated rich, complete Hindalco Workforce Queue System page!")
