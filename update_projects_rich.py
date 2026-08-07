import os, re

# 1. Update snapseat.html
snapseat_path = "pages/snapseat.html"
with open(snapseat_path, "r") as f:
    seat_content = f.read()

seat_arch_card = """            <!-- THE ARCHITECTURE FLOW -->
            <section class="section" style="padding: 30px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <div class="arch-diagram-box" style="background: var(--paper-warm); border: 2px solid var(--rule-dark); padding: 25px; text-align: center;">
                            <span class="kicker-label" style="color: var(--stamp);">SYSTEM ARCHITECTURE PIPELINE</span>
                            <h4 class="heading-md" style="margin: 10px 0 15px 0;">Containerized Microservices &amp; Distributed Locking</h4>
                            <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:8px; font-family: var(--font-mono, monospace);">
                                <div class="arch-node">Client Gateway<br><small style="font-weight:normal;">Web / Mobile App</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">NGINX Ingress<br><small style="font-weight:normal;">TLS &amp; Rate Limiting</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">AWS EKS Cluster<br><small style="font-weight:normal;">User, Booking &amp; Payment Pods</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Redis Redlock<br><small style="font-weight:normal;">Zero Double-Booking Lock</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">PostgreSQL Cluster<br><small style="font-weight:normal;">ACID Seat Transactions</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Prometheus &amp; Grafana<br><small style="font-weight:normal;">Pod Metrics &amp; Tracing</small></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>"""

seat_content = re.sub(
    r"<!-- ENGINEERING / STEP BY STEP -->",
    seat_arch_card + "\n\n            <!-- ENGINEERING / STEP BY STEP -->",
    seat_content
)

with open(snapseat_path, "w") as f:
    f.write(seat_content)

# 2. Update nutrivision.html
nutri_path = "pages/nutrivision.html"
with open(nutri_path, "r") as f:
    nutri_content = f.read()

nutri_arch_card = """            <!-- ARCHITECTURE FLOW -->
            <section class="section" style="padding: 30px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <div class="arch-diagram-box" style="background: var(--paper-warm); border: 2px solid var(--rule-dark); padding: 25px; text-align: center;">
                            <span class="kicker-label" style="color: var(--stamp);">MULTIMODAL AI PIPELINE</span>
                            <h4 class="heading-md" style="margin: 10px 0 15px 0;">Google Gemini Vision Multimodal Processing Flow</h4>
                            <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:8px; font-family: var(--font-mono, monospace);">
                                <div class="arch-node">Meal Snapshot<br><small style="font-weight:normal;">Camera / File Upload</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Next.js Edge API<br><small style="font-weight:normal;">Image Pre-processing &amp; Base64</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Gemini Pro Vision API<br><small style="font-weight:normal;">Multimodal Object Recognition</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Nutritional Engine<br><small style="font-weight:normal;">Portion &amp; Macro Breakdown</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Dashboard Analytics<br><small style="font-weight:normal;">Calorie &amp; Goal Insights</small></div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- KEY INNOVATIONS & DETAILS -->
            <section class="section" style="padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-6 rv column-bordered">
                        <h4 class="heading-md" style="margin-bottom: 15px; border-bottom: 2px solid var(--rule-dark); padding-bottom: 5px;">1. Multimodal Recognition</h4>
                        <p class="body" style="margin-bottom: 15px;">By supplying image embeddings directly into Google Gemini Pro Vision, NutriVision Pro classifies multi-item plates (e.g., distinguishing grilled salmon from roasted side vegetables) with zero manual tagging.</p>
                        
                        <h4 class="heading-md" style="margin-bottom: 15px; border-bottom: 2px solid var(--rule-dark); padding-bottom: 5px; margin-top: 30px;">2. Portion &amp; Calorie Estimation</h4>
                        <p class="body" style="margin-bottom: 15px;">The inference prompt guides Gemini to output structured JSON containing estimated gram weights, caloric counts, protein, carbohydrate, and fat breakdowns per identified item.</p>
                    </div>
                    
                    <div class="col-span-6 rv">
                        <h4 class="heading-md" style="margin-bottom: 15px; border-bottom: 2px solid var(--rule-dark); padding-bottom: 5px;">3. Serverless Edge Deployment</h4>
                        <p class="body" style="margin-bottom: 15px;">Hosted on Vercel's global edge network, API routes stream responses back to the client interface in sub-800ms, maintaining a ultra-smooth user experience.</p>
                        
                        <h4 class="heading-md" style="margin-bottom: 15px; border-bottom: 2px solid var(--rule-dark); padding-bottom: 5px; margin-top: 30px;">4. Production Access</h4>
                        <p class="body" style="margin-bottom: 15px;">Live application available at <a href="https://nutrivison-pro.vercel.app/" target="_blank" style="color:var(--stamp); font-weight:bold;">nutrivison-pro.vercel.app &nearr;</a> with source code on <a href="https://github.com/AJ1312/nutrivison-pro" target="_blank" style="color:var(--stamp); font-weight:bold;">GitHub &nearr;</a>.</p>
                    </div>
                </div>
            </section>"""

nutri_content = re.sub(
    r"</main>",
    nutri_arch_card + "\n        </main>",
    nutri_content
)

with open(nutri_path, "w") as f:
    f.write(nutri_content)

print("Successfully updated SeatSnap and NutriVision Pro with architectural diagrams and elaborate details!")
