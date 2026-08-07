import os, re

filepath = "pages/paper-compsac.html"
with open(filepath, "r") as f:
    content = f.read()

# Replace Methodology Pipeline Mermaid block
new_methodology_card = """                    <div class="col-span-12 rv">
                        <div class="arch-diagram-box" style="background: var(--paper-warm); border: 2px solid var(--rule-dark); padding: 25px; text-align: center;">
                            <span class="kicker-label" style="color: var(--stamp);">EXPERIMENTAL PIPELINE ARCHITECTURE</span>
                            <h4 class="heading-md" style="margin: 10px 0 15px 0;">GoEmotions Activation Extraction & Steering Flow</h4>
                            <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:8px; font-family: var(--font-mono, monospace);">
                                <div class="arch-node">GoEmotions Dataset<br><small style="font-weight:normal;">27 Categories + Neutral (1,000 samples)</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Contrastive Prompts<br><small style="font-weight:normal;">16 Pairs across 8 Categories</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Activation Extraction<br><small style="font-weight:normal;">Neutralisation Vector ($v_{neutral}$)</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Activation Steering<br><small style="font-weight:normal;">Gemma-2B (L6,9,12,16) | Llama-3-8B (L10,16,21,30)</small></div>
                                <span class="arch-arrow">&rarr;</span>
                                <div class="arch-node">Degradation Analysis<br><small style="font-weight:normal;">Brittleness vs Affective Erasure</small></div>
                            </div>
                        </div>
                    </div>"""

content = re.sub(
    r"<div class=\"col-span-12 rv\">\s*<div class=\"mermaid\">\s*flowchart TD\s*A\[GoEmotions Dataset.*?\s*</div>\s*</div>",
    new_methodology_card,
    content,
    flags=re.DOTALL
)

# Overhaul Discussion Section (Social Safety Gap)
new_discussion_section = """            <!-- SOCIAL SAFETY GAP & THEORETICAL DISCUSSION -->
            <section class="section" style="padding: 40px 0; background: var(--paper-warm); border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12 rv">
                        <span class="kicker-label">THE DISCUSSION</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 32px;">The Social Safety Gap &amp; Emotional Flattening</h3>
                        <p class="body-lg" style="max-width: 900px; margin-bottom: 25px; font-style: italic;">
                            "Treating 'safety' as synonymous with toxicity prevention made sense when AI systems were passive query responders. It makes far less sense once those systems handle mental health triage or customer grievance escalation, where reading and matching emotional state is essential to effective communication."
                        </p>
                    </div>

                    <div class="col-span-6 rv column-bordered">
                        <h4 class="heading-md" style="margin-bottom: 15px; font-size: 22px;">Theoretical Framework</h4>
                        <p class="body-lg" style="margin-bottom: 15px;">
                            <span class="dropcap">C</span>onventional safety evaluation frameworks quantify AI risk primarily through <i>technical toxicity reduction</i>—measuring the suppression of harmful, abusive, or non-compliant outputs. However, alignment techniques (such as RLHF, DPO, and aggressive activation steering) exert strong directional pressure on the model's latent representation space.
                        </p>
                        <p class="body-lg">
                            Our empirical findings reveal that this alignment pressure induces an unintended trade-off: as the model is steered to minimize technical harm, its internal capacity to represent and respond to nuanced human affective signals is systematically suppressed.
                        </p>
                    </div>

                    <div class="col-span-6 rv">
                        <div class="arch-diagram-box" style="background: var(--paper-bright); border: 2px solid var(--rule-dark); padding: 20px; text-align: center; margin: 0;">
                            <span class="kicker-label" style="color: var(--stamp);">THEORETICAL DYNAMICS</span>
                            <h4 class="heading-md" style="margin: 10px 0 15px 0;">Mechanistic Trade-Off Model</h4>
                            <div style="display:flex; flex-direction:column; gap:12px; align-items:center; font-family: var(--font-mono, monospace); font-size: 13px;">
                                <div class="arch-node" style="background: var(--ink); color: var(--paper); width: 80%;">ALIGNMENT PRESSURE (RLHF / Steering)</div>
                                <div style="display:flex; justify-content:space-around; width:100%;">
                                    <span class="arch-arrow">&swarr;</span>
                                    <span class="arch-arrow">&searr;</span>
                                </div>
                                <div style="display:flex; gap:10px; width:100%;">
                                    <div class="arch-node" style="flex:1;">Harmful Output<br><small style="color:var(--stamp); font-weight:bold;">&darr; REDUCED</small></div>
                                    <div class="arch-node" style="flex:1;">Emotional Signal<br><small style="color:var(--stamp); font-weight:bold;">&darr; FLATTENED</small></div>
                                </div>
                                <div style="display:flex; justify-content:space-around; width:100%;">
                                    <span class="arch-arrow">&darr;</span>
                                    <span class="arch-arrow">&darr;</span>
                                </div>
                                <div style="display:flex; gap:10px; width:100%;">
                                    <div class="arch-node" style="flex:1; background:#e0f2fe; border-color:#0284c7;">TECHNICAL SAFETY<br><small>(Standard Benchmark)</small></div>
                                    <div class="arch-node" style="flex:1; background:#ffe4e6; border-color:#e11d48; color:#9f1239;">SOCIAL SAFETY GAP<br><small>(Empathy Deficit Risk)</small></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-span-12 rv" style="margin-top: 30px; border-top: 1px solid var(--rule); padding-top: 20px;">
                        <h4 class="heading-md" style="margin-bottom: 10px;">Implications for Proactive AI Deployment</h4>
                        <p class="body-lg">
                            This divergence between <b>Technical Safety</b> (passing automated adversarial benchmarks) and <b>Social Safety</b> (maintaining empathetic attunement) creates a critical risk vector for real-world deployments. When an AI agent fails to match or acknowledge a user's distress during crisis response or customer grievance, the resulting "affective erasure" induces user frustration, alienation, and downstream loss of trust—proving that over-aligned safety can become its own failure mode.
                        </p>
                    </div>
                </div>
            </section>"""

content = re.sub(
    r"<!-- SOCIAL SAFETY GAP -->\s*<section class=\"section\".*?</section>",
    new_discussion_section,
    content,
    flags=re.DOTALL
)

with open(filepath, "w") as f:
    f.write(content)
print("Successfully updated paper-compsac.html discussion and methodology!")
