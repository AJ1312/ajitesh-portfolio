import re

html_projects = """
        <!-- SECTION 3: FIELD DISPATCHES (Projects) -->
        <section id="projects" class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 40px 0;">
            <div class="newspaper-grid" style="border-bottom: 1px solid var(--rule); padding-bottom: 15px; margin-bottom: 30px;">
                <div class="col-span-6">
                    <span class="kicker-label">THE EVIDENCE</span>
                    <h3 class="display-md">Selected Works</h3>
                </div>
                <div class="col-span-6 text-right" style="display:flex; flex-direction: column; justify-content: flex-end;">
                    <span class="meta uppercase">Dispatches A &ndash; E &middot; Filed 2025 &ndash; 2026</span>
                </div>
            </div>
            
            <div class="newspaper-grid">
                <!-- Featured Project: DISPATCH A -->
                <article class="col-span-12 rv" style="border: 1px solid var(--rule-dark); padding: 30px; background: var(--paper-warm); margin-bottom: 30px;">
                    <span class="kicker-label" style="color: var(--stamp); font-size: 14px;">DISPATCH A</span>
                    <h4 class="display-md" style="margin: 10px 0;">CipherPulse</h4>
                    <div class="newspaper-grid">
                        <div class="col-span-8">
                            <p class="body-lg">A high-performance C++17 Deep Packet Inspection (DPI) engine utilizing JA4+ fingerprints and Shannon Entropy for real-time encrypted malware traffic detection. Engineered for multi-threaded packet capture and low-latency feature extraction.</p>
                        </div>
                        <div class="col-span-4" style="display:flex; flex-direction: column; justify-content: space-between; align-items: flex-end;">
                            <div style="display: flex; gap: 8px; flex-wrap: wrap; justify-content: flex-end;">
                                <span class="meta" style="border: 1px solid var(--rule); padding: 4px 8px;">C++17</span>
                                <span class="meta" style="border: 1px solid var(--rule); padding: 4px 8px;">DPI</span>
                                <span class="meta" style="border: 1px solid var(--rule); padding: 4px 8px;">JA4+</span>
                            </div>
                            <a href="pages/cipherpulse.html" class="meta bold" style="background: var(--ink); color: var(--paper); padding: 10px 20px; margin-top: 20px;">OPEN DISPATCH &rarr;</a>
                        </div>
                    </div>
                </article>

                <!-- Grid for remaining projects -->
                <div class="col-span-12 newspaper-grid">
                    <!-- DISPATCH B -->
                    <article class="col-span-6 rv column-bordered">
                        <span class="kicker-label">DISPATCH B</span>
                        <h4 class="heading-lg" style="margin: 10px 0;">Sentinel-Stream</h4>
                        <p class="body" style="margin-bottom: 20px;">O(1)-Memory anomaly detection pipeline using LightGBM and Fast-Hoeffding Trees, deployed via FastAPI for real-time inference with TreeSHAP explanations.</p>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: auto;">
                            <span class="meta">LightGBM &middot; FastAPI</span>
                            <a href="pages/sentinel-stream.html" class="meta bold" style="color: var(--stamp);">OPEN DISPATCH &rarr;</a>
                        </div>
                    </article>

                    <!-- DISPATCH C -->
                    <article class="col-span-6 rv" style="padding-left: 30px;">
                        <span class="kicker-label">DISPATCH C</span>
                        <h4 class="heading-lg" style="margin: 10px 0;">SeatSnap</h4>
                        <p class="body" style="margin-bottom: 20px;">Containerized seat reservation microservices with high-availability scheduling. Built with robust CI/CD and system observability.</p>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: auto;">
                            <span class="meta">Docker &middot; K8s</span>
                            <a href="pages/snapseat.html" class="meta bold" style="color: var(--stamp);">OPEN DISPATCH &rarr;</a>
                        </div>
                    </article>
                    
                    <div class="col-span-12" style="height: 1px; background: var(--rule); margin: 30px 0;"></div>

                    <!-- DISPATCH D -->
                    <article class="col-span-6 rv column-bordered">
                        <span class="kicker-label">DISPATCH D</span>
                        <h4 class="heading-lg" style="margin: 10px 0;">NutriVision Pro</h4>
                        <p class="body" style="margin-bottom: 20px;">AI-powered dietary analysis tool leveraging Gemini Vision API for food recognition and nutritional breakdown.</p>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: auto;">
                            <span class="meta">Next.js &middot; Gemini Vision</span>
                            <a href="https://nutrivison-pro.vercel.app" target="_blank" class="meta bold" style="color: var(--stamp);">OPEN DISPATCH &rarr;</a>
                        </div>
                    </article>

                    <!-- DISPATCH E -->
                    <article class="col-span-6 rv" style="padding-left: 30px;">
                        <span class="kicker-label">DISPATCH E &mdash; HINDALCO</span>
                        <h4 class="heading-lg" style="margin: 10px 0;">Workforce Queue System</h4>
                        <p class="body" style="margin-bottom: 20px;">Enterprise system for digitizing workforce scheduling, reducing manual allocation overhead for 1,200+ site personnel daily.</p>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: auto;">
                            <span class="meta">Spring Boot &middot; Oracle</span>
                            <a href="pages/internship.html" class="meta bold" style="color: var(--stamp);">OPEN DISPATCH &rarr;</a>
                        </div>
                    </article>
                </div>
            </div>
        </section>

        <!-- SECTION 4: THE LAB REPORT (Tech Stack) -->
        <section id="stack" class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 40px 0;">
            <div class="newspaper-grid" style="border-bottom: 1px solid var(--rule); padding-bottom: 15px; margin-bottom: 30px;">
                <div class="col-span-12">
                    <span class="kicker-label">THE LAB REPORT</span>
                    <h3 class="display-md">Technical Competencies</h3>
                </div>
            </div>
            
            <div class="newspaper-grid">
                <div class="col-span-4 rv column-bordered">
                    <h4 class="heading-md" style="margin-bottom: 15px; border-bottom: 1px solid var(--rule); padding-bottom: 10px;">Core CS &amp; Languages</h4>
                    <p class="body">C++17, Java, Python, C, SQL, PL/SQL, JavaScript.</p>
                    <p class="body" style="margin-top: 10px;">Data Structures &amp; Algorithms, OOP, OS, Computer Networks.</p>
                </div>
                <div class="col-span-4 rv column-bordered" style="padding-left: 30px;">
                    <h4 class="heading-md" style="margin-bottom: 15px; border-bottom: 1px solid var(--rule); padding-bottom: 10px;">Systems &amp; Security</h4>
                    <p class="body">DPI, JA4+, YARA, Wireshark, eBPF, Linux, Autopsy, Metasploit.</p>
                </div>
                <div class="col-span-4 rv" style="padding-left: 30px;">
                    <h4 class="heading-md" style="margin-bottom: 15px; border-bottom: 1px solid var(--rule); padding-bottom: 10px;">Backend, Cloud &amp; AI</h4>
                    <p class="body">Spring Boot, FastAPI, Docker, Kubernetes, Jenkins, AWS, PostgreSQL, REST, WebSockets.</p>
                    <p class="body" style="margin-top: 10px;">PyTorch, LightGBM, Scikit-Learn, TreeSHAP.</p>
                </div>
            </div>
        </section>

        <!-- SECTION 5: THE SERVICE RECORD (Experience) & PUBLICATIONS -->
        <section id="experience" class="section" style="padding: 40px 0;">
            <div class="newspaper-grid">
                
                <!-- Left Column (Service Record) -->
                <div class="col-span-6 column-bordered">
                    <div style="border-bottom: 1px solid var(--rule); padding-bottom: 15px; margin-bottom: 30px;">
                        <span class="kicker-label">THE SERVICE RECORD</span>
                        <h3 class="heading-lg">Professional Experience</h3>
                    </div>
                    
                    <div class="rv" style="margin-bottom: 40px;">
                        <h4 class="heading-md" style="margin-bottom: 5px;">Hindalco Industries Ltd.</h4>
                        <p class="meta" style="margin-bottom: 15px;">SOFTWARE ENGINEERING INTERN &middot; MAY 2026 - JUL 2026</p>
                        <p class="body">Architected and developed a digitized workforce scheduling system, migrating from manual legacy processes. Implemented robust Role-Based Access Control (RBAC) ensuring strict data segregation across administrative tiers. Streamlined the daily shift allocation and attendance monitoring for over 1,200 site personnel.</p>
                    </div>

                    <div class="rv">
                        <h4 class="heading-md" style="margin-bottom: 5px;">VIT Vellore</h4>
                        <p class="meta" style="margin-bottom: 15px;">B.TECH CSE (INFORMATION SECURITY) &middot; EXPECTED JUL 2027</p>
                        <p class="body">Pursuing rigorous coursework in Operating Systems, Network Security, Cryptography, and Advanced Data Structures. Core member of ACM-VIT.</p>
                    </div>
                </div>

                <!-- Right Column (Publications) -->
                <div class="col-span-6" style="padding-left: 30px;" id="publications">
                    <div style="border-bottom: 1px solid var(--rule); padding-bottom: 15px; margin-bottom: 30px;">
                        <span class="kicker-label">PUBLISHED FINDINGS</span>
                        <h3 class="heading-lg">Research &amp; Patents</h3>
                    </div>
                    
                    <div class="rv" style="border: 1px solid var(--rule-dark); padding: 20px; background: var(--paper-warm); margin-bottom: 30px;">
                        <span class="meta" style="color: var(--stamp); border: 1px solid var(--stamp); padding: 2px 6px;">ACCEPTED</span>
                        <h4 class="heading-md" style="margin: 10px 0;">The Alignment Paradox: Emotional Flattening and Social Safety Risks in Proactive AI Agents</h4>
                        <p class="meta" style="margin-bottom: 15px;">IEEE COMPSAC 2026 STUDENT SYMPOSIUM</p>
                        <p class="body-sm">This paper investigates the unforeseen consequences of over-aligning proactive AI agents to maximize safety at the expense of social utility.</p>
                        <a href="pages/paper-compsac.html" class="meta bold" style="display: inline-block; margin-top: 15px; color: var(--stamp);">READ FULL ANALYSIS &rarr;</a>
                    </div>
                    
                    <div class="rv">
                        <h4 class="heading-md" style="margin-bottom: 15px; border-bottom: 1px solid var(--rule); padding-bottom: 10px;">Filed Indian Patents</h4>
                        <ul style="list-style: none; padding: 0;">
                            <li style="margin-bottom: 15px;">
                                <p class="meta" style="color: var(--stamp);">PENDING</p>
                                <p class="body bold">System and Method for O(1) Memory Streaming Anomaly Detection</p>
                            </li>
                            <li style="margin-bottom: 15px;">
                                <p class="meta" style="color: var(--stamp);">PENDING</p>
                                <p class="body bold">Audio Deepfake Detection via Shannon Entropy</p>
                            </li>
                            <li>
                                <p class="meta" style="color: var(--stamp);">PENDING</p>
                                <p class="body bold">Real-time Lip-Sync Detection using Visual CNNs</p>
                            </li>
                        </ul>
                        <a href="pages/patents.html" class="meta bold" style="display: inline-block; margin-top: 15px;">VIEW PATENT ARCHITECTURES &rarr;</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- FOOTER / CONTACT -->
        <footer id="contact" class="section" style="border-top: 4px solid var(--rule-dark); padding: 40px 0;">
            <div class="newspaper-grid">
                <div class="col-span-12 text-center rv">
                    <h2 class="display-lg" style="margin-bottom: 20px;">Available for Action.</h2>
                    <p class="body-lg" style="max-width: 600px; margin: 0 auto 30px auto;">Correspondence accepted via electronic mail, or physical courier to Vellore, India.</p>
                    
                    <div style="display: flex; gap: 20px; justify-content: center; margin-bottom: 60px;">
                        <a href="mailto:13ajitesh@gmail.com" class="meta bold" style="background: var(--stamp); color: var(--paper-bright); padding: 15px 30px; font-size: 14px;">13AJITESH@GMAIL.COM</a>
                        <a href="https://linkedin.com/in/ajitesh-sharma" target="_blank" class="meta bold" style="background: var(--ink); color: var(--paper); padding: 15px 30px; font-size: 14px;">LINKEDIN</a>
                        <a href="https://github.com/AJ1312" target="_blank" class="meta bold" style="background: transparent; border: 1px solid var(--ink); color: var(--ink); padding: 15px 30px; font-size: 14px;">GITHUB</a>
                    </div>
                    
                    <p class="meta uppercase">&copy; 2026 Ajitesh Sharma &middot; The Sharma Dispatch &mdash; Vol. I</p>
                </div>
            </div>
        </footer>

    </div> <!-- End container -->

    <svg class="sr-only" aria-hidden="true" style="display: none;">
        <defs>
            <filter id="fm-rough">
                <feTurbulence type="turbulence" baseFrequency="0.02" numOctaves="3" result="noise"/>
                <feDisplacementMap in="SourceGraphic" in2="noise" scale="2" xChannelSelector="R" yChannelSelector="G"/>
            </filter>
        </defs>
    </svg>

    <script src="js/main.js" defer></script>
    <script src="js/animations.js" defer></script>
</body>
</html>
"""

with open('index.html', 'r') as f:
    orig = f.read()

new_html = re.sub(r'<!-- SECTION 3: FIELD DISPATCHES \(Projects\) -->.*</html>', html_projects, orig, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(new_html)
