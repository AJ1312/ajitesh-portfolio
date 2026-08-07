import os
from gen_patents import PAGE_TEMPLATE

CIPHERPULSE_CONTENT = """
            <!-- HERO -->
            <section class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <p class="kicker-label rv">DISPATCH A &mdash; OPEN INVESTIGATIONS</p>
                        <h1 class="display-xl rv" style="margin-bottom: 20px;">CipherPulse</h1>
                        <p class="display-sm rv" style="max-width: 800px; font-style: italic;">eBPF-driven network forensics engine for zero-day encrypted C2 beacons.</p>
                        
                        <div class="newspaper-grid" style="margin-top: 30px; border-top: 1px solid var(--rule); padding-top: 20px;">
                            <div class="col-span-4 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">GITHUB REPOSITORY</p>
                                <a href="https://github.com/AJ1312/CipherPulse" target="_blank" class="body-sm" style="color: var(--stamp); font-weight: bold; text-decoration: underline;">AJ1312/CipherPulse &nearr;</a>
                            </div>
                            <div class="col-span-4 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">CORE TECH</p>
                                <p class="body-sm">C++17, eBPF, JA4+ Fingerprinting</p>
                            </div>
                            <div class="col-span-4 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">PERFORMANCE</p>
                                <p class="body-sm">Zero-copy packet inspection</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- DETAILS -->
            <section class="section" style="padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">THE REAL-WORLD SCENARIO</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 32px;">The Encrypted Blindspot</h3>
                        <p class="body-lg rv"><span class="dropcap">T</span>hreat actors increasingly use standard TLS to hide Command and Control (C2) beaconing, rendering traditional Deep Packet Inspection (DPI) obsolete. CipherPulse solves this by intercepting packets at the kernel level using eBPF, executing zero-copy memory operations to perform JA4+ TLS fingerprinting before the traffic even reaches user-space. This allows SOC teams to identify anomalous encrypted traffic flows without performing resource-intensive SSL decryption.</p>
                    </div>
                </div>
            </section>
"""

SENTINEL_CONTENT = """
            <!-- HERO -->
            <section class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <p class="kicker-label rv">DISPATCH B &mdash; OPEN INVESTIGATIONS</p>
                        <h1 class="display-xl rv" style="margin-bottom: 20px;">Sentinel-Stream</h1>
                        <p class="display-sm rv" style="max-width: 800px; font-style: italic;">O(1)-Memory anomaly detection pipeline using LightGBM and Fast-Hoeffding Trees.</p>
                        
                        <div class="newspaper-grid" style="margin-top: 30px; border-top: 1px solid var(--rule); padding-top: 20px;">
                            <div class="col-span-4 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">GITHUB REPOSITORY</p>
                                <a href="https://github.com/AJ1312/sentinel-stream" target="_blank" class="body-sm" style="color: var(--stamp); font-weight: bold; text-decoration: underline;">AJ1312/sentinel-stream &nearr;</a>
                            </div>
                            <div class="col-span-4 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">CORE TECH</p>
                                <p class="body-sm">LightGBM, FastAPI, TreeSHAP</p>
                            </div>
                            <div class="col-span-4 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">CONSTRAINTS</p>
                                <p class="body-sm">Strict O(1) Memory Footprint</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- DETAILS -->
            <section class="section" style="padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">THE REAL-WORLD SCENARIO</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 32px;">Streaming Data Under Constraint</h3>
                        <p class="body-lg rv"><span class="dropcap">I</span>n edge-computing environments (like IoT gateways or industrial controllers), memory is strictly bounded. Traditional machine learning models require batching data, which causes Out-Of-Memory (OOM) crashes in these environments. Sentinel-Stream implements Fast-Hoeffding Trees which update their weights iteratively. This guarantees an O(1) memory footprint regardless of the incoming data stream's velocity, deployed via a low-latency FastAPI inference server with TreeSHAP for explainability.</p>
                    </div>
                </div>
            </section>
"""

with open('pages/cipherpulse.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'CipherPulse').replace('{content}', CIPHERPULSE_CONTENT))

with open('pages/sentinel-stream.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'Sentinel-Stream').replace('{content}', SENTINEL_CONTENT))
