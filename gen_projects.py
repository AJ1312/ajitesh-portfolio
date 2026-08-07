import os

from gen_patents import PAGE_TEMPLATE

SNAPSEAT_CONTENT = """
            <!-- HERO -->
            <section class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <p class="kicker-label rv">DISPATCH C &mdash; FIELD REPORT</p>
                        <h1 class="display-xl rv" style="margin-bottom: 20px;">SeatSnap</h1>
                        <p class="display-sm rv" style="max-width: 800px; font-style: italic;">Containerized Microservices Ticketing Platform with Zero-Downtime CI/CD</p>
                        
                        <div class="newspaper-grid" style="margin-top: 30px; border-top: 1px solid var(--rule); padding-top: 20px;">
                            <div class="col-span-4 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">GITHUB REPOSITORY</p>
                                <a href="https://github.com/AJ1312/SeatSnap-devops" target="_blank" class="body-sm" style="color: var(--stamp); font-weight: bold; text-decoration: underline;">AJ1312/SeatSnap-devops &nearr;</a>
                            </div>
                            <div class="col-span-4 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">ORCHESTRATION</p>
                                <p class="body-sm">Docker + Kubernetes (AWS EKS)</p>
                            </div>
                            <div class="col-span-4 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">SECURITY & PIPELINE</p>
                                <p class="body-sm">Jenkins Declarative Pipelines, Trivy, JWT/OAuth2</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- THE INCIDENT (Problem & Scenario) -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">THE REAL-WORLD SCENARIO</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 32px;">The Double-Booking Crisis</h3>
                        <p class="body-lg rv"><span class="dropcap">I</span>n high-demand event ticketing, legacy monolithic systems crash under sudden traffic spikes ("ticket drops"), leading to race conditions and double-booked seats. SeatSnap solves this by decoupling the reservation engine from the user gateway, utilizing a highly available, containerized microservices architecture built from the ground up with cloud-native DevOps principles.</p>
                    </div>
                </div>
            </section>

            <!-- ENGINEERING / STEP BY STEP -->
            <section class="section" style="padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <span class="kicker-label">THE ARCHITECTURE</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 32px;">Step-by-Step Construction</h3>
                    </div>
                    
                    <div class="col-span-6 rv column-bordered" style="padding-right: 30px;">
                        <h4 class="heading-md" style="margin-bottom: 15px; border-bottom: 2px solid var(--rule-dark); padding-bottom: 5px;">1. Microservices Containerization</h4>
                        <p class="body" style="margin-bottom: 15px;">Each domain (Users, Ticketing, Payment) was built as an independent Docker container. Multi-stage Dockerfiles were utilized to minimize the attack surface and image size, ensuring rapid spin-ups.</p>
                        
                        <h4 class="heading-md" style="margin-bottom: 15px; border-bottom: 2px solid var(--rule-dark); padding-bottom: 5px; margin-top: 30px;">2. Continuous Integration (CI)</h4>
                        <p class="body" style="margin-bottom: 15px;">A robust Jenkins declarative pipeline runs automatically on every Git commit. It executes unit tests, performs static code analysis, and scans container images using Trivy to prevent vulnerable dependencies from reaching production.</p>
                    </div>
                    
                    <div class="col-span-6 rv" style="padding-left: 30px;">
                        <h4 class="heading-md" style="margin-bottom: 15px; border-bottom: 2px solid var(--rule-dark); padding-bottom: 5px;">3. Kubernetes Orchestration</h4>
                        <p class="body" style="margin-bottom: 15px;">The containers are orchestrated using Kubernetes (AWS EKS). The cluster features auto-scaling policies to handle ticket-drop traffic spikes without manual intervention, routing traffic through an NGINX Ingress controller.</p>
                        
                        <h4 class="heading-md" style="margin-bottom: 15px; border-bottom: 2px solid var(--rule-dark); padding-bottom: 5px; margin-top: 30px;">4. Observability & Monitoring</h4>
                        <p class="body" style="margin-bottom: 15px;">Prometheus actively scrapes metrics from the Kubernetes pods, feeding into Grafana dashboards. This provides real-time visibility into booking latencies, API error rates, and node resource utilization.</p>
                    </div>
                </div>
            </section>
"""

NUTRIVISION_CONTENT = """
            <!-- HERO -->
            <section class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <p class="kicker-label rv">DISPATCH D &mdash; OPEN INVESTIGATION</p>
                        <h1 class="display-xl rv" style="margin-bottom: 20px;">NutriVision Pro</h1>
                        <p class="display-sm rv" style="max-width: 800px; font-style: italic;">AI-powered dietary analysis tool leveraging Gemini Vision API.</p>
                        
                        <div class="newspaper-grid" style="margin-top: 30px; border-top: 1px solid var(--rule); padding-top: 20px;">
                            <div class="col-span-4 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">LIVE DEPLOYMENT</p>
                                <a href="https://nutrivison-pro.vercel.app/" target="_blank" class="body-sm" style="color: var(--stamp); font-weight: bold; text-decoration: underline;">nutrivison-pro.vercel.app &nearr;</a>
                            </div>
                            <div class="col-span-4 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">GITHUB REPOSITORY</p>
                                <a href="https://github.com/AJ1312/nutrivison-pro" target="_blank" class="body-sm" style="color: var(--stamp); font-weight: bold; text-decoration: underline;">AJ1312/nutrivison-pro &nearr;</a>
                            </div>
                            <div class="col-span-4 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">CORE TECH</p>
                                <p class="body-sm">Next.js, Google Gemini Pro Vision API</p>
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
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 32px;">Frictionless Nutrition Tracking</h3>
                        <p class="body-lg rv"><span class="dropcap">T</span>raditional calorie counting apps suffer from high user drop-off rates due to the sheer friction of manually logging every ingredient. NutriVision Pro bridges this gap by allowing users to simply take a photo of their meal. Leveraging the multimodal capabilities of the Gemini Vision API, the application identifies food items, estimates portion sizes, and instantly returns a comprehensive macro-nutritional breakdown.</p>
                    </div>
                </div>
            </section>
"""

with open('pages/snapseat.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'SeatSnap').replace('{content}', SNAPSEAT_CONTENT))

with open('pages/nutrivision.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'NutriVision Pro').replace('{content}', NUTRIVISION_CONTENT))
