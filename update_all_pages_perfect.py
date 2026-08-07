import os

# 1. Update Sentinel-Stream with Image
with open('pages/sentinel-stream.html', 'r') as f:
    sentinel_html = f.read()

sentinel_img_card = """            <!-- ARCHITECTURE PIPELINE (GENERATED WELL-EXPLAINED IMAGE) -->
            <section class="section" style="padding: 30px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label" style="color: var(--stamp);">SYSTEM ARCHITECTURE PIPELINE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0;">O(1) Streaming Profiler &amp; Machine Learning Pipeline</h3>
                        <div class="featured-image" style="border: 2px solid var(--rule-dark); background: #fdfbf7; padding: 10px;">
                            <img src="../images/architecture/sentinel_stream_pipeline.png" alt="Sentinel-Stream System Architecture Pipeline" style="width:100%; display:block;">
                        </div>
                    </div>
                </div>
            </section>"""

# Replace old arch section
import re
sentinel_html = re.sub(
    r"<!-- ARCHITECTURE PIPELINE -->\s*<section class=\"section\".*?</section>",
    sentinel_img_card,
    sentinel_html,
    flags=re.DOTALL
)

with open('pages/sentinel-stream.html', 'w') as f:
    f.write(sentinel_html)

# 2. Update CipherPulse with Image
with open('pages/cipherpulse.html', 'r') as f:
    cipher_html = f.read()

cipher_img_card = """            <!-- ARCHITECTURE PIPELINE (GENERATED WELL-EXPLAINED IMAGE) -->
            <section class="section" style="padding: 30px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label" style="color: var(--stamp);">SYSTEM ARCHITECTURE PIPELINE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0;">Lock-Free 5-Tuple Fast-Path Inspection Pipeline</h3>
                        <div class="featured-image" style="border: 2px solid var(--rule-dark); background: #fdfbf7; padding: 10px;">
                            <img src="../images/architecture/cipherpulse_pipeline.png" alt="CipherPulse Lock-Free DPI Architecture Pipeline" style="width:100%; display:block;">
                        </div>
                    </div>
                </div>
            </section>"""

cipher_html = re.sub(
    r"<!-- ARCHITECTURE PIPELINE -->\s*<section class=\"section\".*?</section>",
    cipher_img_card,
    cipher_html,
    flags=re.DOTALL
)

with open('pages/cipherpulse.html', 'w') as f:
    f.write(cipher_html)

# 3. Rewrite Hospital Queue Management System Internship Page (pages/internship.html)
hospital_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hindalco Community Hospital Queue System — The Sharma Dispatch</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,800;0,900;1,400;1,700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/styles.css">
    <style>
        .workbench-box {
            border: 2px solid var(--rule-dark);
            background: var(--paper-warm);
            padding: 35px;
            margin: 40px 0;
            border-radius: 2px;
        }
        .wb-btn {
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
        }
        .wb-btn:hover {
            background: var(--stamp);
            border-color: var(--stamp);
            color: #fff;
        }
        .wb-table {
            width: 100%;
            border-collapse: collapse;
            font-family: var(--font-body);
            font-size: 14px;
            margin-top: 25px;
            background: var(--paper-bright);
            border: 2px solid var(--rule-dark);
        }
        .wb-table th {
            background: var(--ink);
            color: var(--paper-bright);
            padding: 12px 15px;
            text-align: left;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .wb-table td {
            padding: 14px 15px;
            border-bottom: 1px solid var(--rule);
            line-height: 1.5;
        }
        .anim-row {
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
        .badge-emergency {
            display: inline-block;
            padding: 4px 10px;
            background: #fee2e2;
            color: #dc2626;
            border: 1px solid #dc2626;
            font-weight: 700;
            font-size: 12px;
        }
        .badge-opd {
            display: inline-block;
            padding: 4px 10px;
            background: #e0f2fe;
            color: #0369a1;
            border: 1px solid #0369a1;
            font-weight: 700;
            font-size: 12px;
        }
        .badge-pharmacy {
            display: inline-block;
            padding: 4px 10px;
            background: #dcfce7;
            color: #15803d;
            border: 1px solid #15803d;
            font-weight: 700;
            font-size: 12px;
        }
        .arch-diagram-box {
            background: var(--paper-bright);
            border: 2px solid var(--rule-dark);
            padding: 30px;
            margin: 30px 0;
            text-align: center;
        }
        .arch-node {
            display: inline-block;
            border: 1px solid var(--rule-dark);
            background: var(--paper-warm);
            padding: 12px 18px;
            margin: 6px;
            font-size: 14px;
            font-weight: bold;
        }
        .arch-arrow {
            display: inline-block;
            margin: 0 8px;
            font-weight: bold;
            color: var(--stamp);
            font-size: 18px;
        }
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
            
            <!-- HERO -->
            <section class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <p class="kicker-label">FIELD DISPATCH &mdash; HINDALCO INDUSTRIES (ADITYA BIRLA GROUP)</p>
                        <h1 class="display-xl" style="margin-bottom: 20px; font-size: 52px;">Hospital &amp; Local Resident Queue System</h1>
                        <p class="display-sm" style="max-width: 850px; font-style: italic; line-height: 1.4;">Digitized Community Healthcare &amp; Outpatient (OPD) Queue Logistics for Local Residents &amp; Plant Personnel</p>
                        
                        <div class="newspaper-grid" style="margin-top: 35px; border-top: 1px solid var(--rule); padding-top: 25px;">
                            <div class="col-span-4 column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">ORGANIZATION</p>
                                <p class="body-sm">Hindalco Community Healthcare</p>
                            </div>
                            <div class="col-span-4 column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">BENEFICIARIES</p>
                                <p class="body-sm">Local Residents &amp; Plant Workforce</p>
                            </div>
                            <div class="col-span-4">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">CORE TECH STACK</p>
                                <p class="body-sm">Spring Boot, Java 17, Oracle DB, PL/SQL, REST APIs</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- THE PROBLEM & THE SOLUTION -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-6 column-bordered">
                        <span class="kicker-label" style="color: var(--stamp);">THE HEALTHCARE CHALLENGE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 28px;">Overcrowded OPD &amp; Gate Bottlenecks</h3>
                        <p class="body-lg" style="line-height: 1.7;"><span class="dropcap">L</span>ocal township residents and plant workers seeking medical care at Hindalco's community hospital previously endured long physical queues for OPD registration, doctor consultations, and pharmacy token dispensing. Manual paper registration created long wait times, triage delays for emergency cases, and zero real-time queue visibility.</p>
                    </div>
                    
                    <div class="col-span-6">
                        <span class="kicker-label" style="color: var(--stamp);">THE DIGITIZED SOLUTION</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 28px;">Digitized OPD Triage &amp; Token Pipeline</h3>
                        <p class="body-lg" style="line-height: 1.7;"><span class="dropcap">T</span>he Healthcare Queue Management System digitizes patient intake from registration kiosk to pharmacy collection. Utilizing Spring Boot middleware and Oracle PL/SQL stored procedures, it manages real-time token assignments, auto-prioritizes emergency triage cases, and cuts patient waiting overhead by <b>85%</b>.</p>
                    </div>
                </div>
            </section>

            <!-- KEY RESULTS METRICS -->
            <section class="section" style="padding: 30px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-3 text-center column-bordered">
                        <p class="display-lg" style="margin:0; color: var(--stamp); font-size: 44px;">1,200+</p>
                        <p class="meta bold uppercase" style="margin-top: 5px;">Patients Served Daily</p>
                    </div>
                    <div class="col-span-3 text-center column-bordered">
                        <p class="display-lg" style="margin:0; color: var(--stamp); font-size: 44px;">85%</p>
                        <p class="meta bold uppercase" style="margin-top: 5px;">Wait Time Reduction</p>
                    </div>
                    <div class="col-span-3 text-center column-bordered">
                        <p class="display-lg" style="margin:0; color: var(--stamp); font-size: 44px;">100%</p>
                        <p class="meta bold uppercase" style="margin-top: 5px;">Emergency Priority Triage</p>
                    </div>
                    <div class="col-span-3 text-center">
                        <p class="display-lg" style="margin:0; color: var(--stamp); font-size: 44px;">ZERO</p>
                        <p class="meta bold uppercase" style="margin-top: 5px;">Manual Token Loss</p>
                    </div>
                </div>
            </section>

            <!-- ARCHITECTURE PIPELINE -->
            <section class="section" style="padding: 30px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <div class="arch-diagram-box">
                            <span class="kicker-label" style="color: var(--stamp);">SYSTEM ARCHITECTURE</span>
                            <h4 class="heading-md" style="margin: 10px 0 15px 0;">Outpatient Intake &amp; Oracle Database Queue Pipeline</h4>
                            <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:center;">
                                <div class="arch-node">Hospital Gate Kiosk<br><small style="font-weight:normal;">Resident / Employee Scan</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Spring Boot API Gateway<br><small style="font-weight:normal;">Patient Intake Middleware</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Triage &amp; Priority Engine<br><small style="font-weight:normal;">OPD vs Emergency Routing</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Oracle PL/SQL Procedures<br><small style="font-weight:normal;">Atomic Token Assignment</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Doctor &amp; Pharmacy Display<br><small style="font-weight:normal;">Real-Time Queue Monitor</small></div>
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
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 32px;">Live Hospital OPD Queue Control Workbench</h3>
                        <p class="body-lg" style="margin-bottom: 25px;">Select a healthcare intake action below to observe real-time patient token generation, triage prioritization, and pharmacy queue processing:</p>

                        <div class="workbench-box">
                            <div>
                                <button class="wb-btn" onclick="runHospitalSim('opd')">🏥 Register Local Resident (OPD Consultation)</button>
                                <button class="wb-btn" onclick="runHospitalSim('emerg')">🚨 Prioritize Emergency Triage Case</button>
                                <button class="wb-btn" onclick="runHospitalSim('pharm')">💊 Dispense Pharmacy Collection Token</button>
                            </div>

                            <table class="wb-table">
                                <thead>
                                    <tr>
                                        <th style="width: 120px;">Timestamp</th>
                                        <th style="width: 180px;">Patient Category</th>
                                        <th>Registered Department</th>
                                        <th style="width: 160px;">Queue Priority</th>
                                        <th style="width: 120px;">Token #</th>
                                        <th>Queue Processing Status</th>
                                    </tr>
                                </thead>
                                <tbody id="wbHospBody">
                                    <tr class="anim-row">
                                        <td>18:38:01</td>
                                        <td><b>Local Resident (Township)</b></td>
                                        <td>General OPD &mdash; Room 104</td>
                                        <td><span class="badge-opd">OPD STANDARD</span></td>
                                        <td>OPD-1042</td>
                                        <td>Assigned to Doctor Queue. Estimated Wait: 6 mins.</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </section>

            <script>
                function runHospitalSim(type) {
                    const tbody = document.getElementById('wbHospBody');
                    const ts = new Date().toISOString().substring(11, 19);

                    let cat = '', dept = '', badge = '', token = '', status = '';

                    if (type === 'emerg') {
                        cat = 'Emergency Resident';
                        dept = 'Acute Trauma & Triage';
                        badge = '<span class="badge-emergency">EMERGENCY PRIORITY</span>';
                        token = 'EMG-008';
                        status = 'Prioritized to Top of Queue! Dispatched directly to ER Bed 2.';
                    } else if (type === 'pharm') {
                        cat = 'Plant Employee Dependent';
                        dept = 'Pharmacy Counter 3';
                        badge = '<span class="badge-pharmacy">PHARMACY DISPENSE</span>';
                        token = 'RX-412';
                        status = 'Prescription Verified. Medication Batch Ready for Pickup.';
                    } else {
                        cat = 'Local Resident (Township)';
                        dept = 'General OPD — Room 104';
                        badge = '<span class="badge-opd">OPD STANDARD</span>';
                        token = 'OPD-1043';
                        status = 'Assigned to Doctor Queue. Estimated Wait: 4 mins.';
                    }

                    const newRow = document.createElement('tr');
                    newRow.className = 'anim-row';
                    newRow.innerHTML = `
                        <td>${ts}</td>
                        <td><b>${cat}</b></td>
                        <td>${dept}</td>
                        <td>${badge}</td>
                        <td><code>${token}</code></td>
                        <td>${status}</td>
                    `;

                    tbody.insertBefore(newRow, tbody.firstChild);
                }
            </script>
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

with open('pages/internship.html', 'w') as f:
    f.write(hospital_content)

print("Successfully updated Sentinel-Stream & CipherPulse with generated architecture images, and rewritten Hospital Queue System page!")
