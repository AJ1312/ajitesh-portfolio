import os

from gen_patents import PAGE_TEMPLATE

PAPER_CONTENT = """
            <!-- HERO -->
            <section class="section" style="border-bottom: 4px solid var(--rule-dark); padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12">
                        <p class="kicker-label rv">IEEE COMPSAC 2026</p>
                        <h1 class="display-xl rv" style="margin-bottom: 20px;">The Alignment Paradox</h1>
                        <p class="display-sm rv" style="max-width: 800px; font-style: italic;">Emotional Flattening & Social Safety Risks in Proactive AI Agents</p>
                        
                        <div class="newspaper-grid" style="margin-top: 30px; border-top: 1px solid var(--rule); padding-top: 20px;">
                            <div class="col-span-12 rv column-bordered">
                                <p class="meta" style="margin-bottom: 5px; font-weight: bold;">PUBLICATION</p>
                                <p class="body-sm">Accepted / Published &mdash; IEEE COMPSAC 2026 Student Symposium</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- RESEARCH QUESTION & KEY CONCEPTS -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-6 rv column-bordered">
                        <h3 class="heading-lg" style="margin: 0 0 20px 0; font-size: 28px;">Research Question</h3>
                        <p class="body-lg" style="font-style: italic; border-left: 2px solid var(--ink); padding-left: 15px;">Can alignment pressure that reduces harmful outputs also suppress a model's ability to recognize and respond to emotional information?</p>
                    </div>
                    
                    <div class="col-span-6 rv" style="padding-left: 30px;">
                        <h3 class="heading-lg" style="margin: 0 0 20px 0; font-size: 28px;">Key Concepts</h3>
                        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                            <span class="meta" style="border: 1px solid var(--ink); padding: 6px 12px; border-radius: 50px;">Emotional Flattening</span>
                            <span class="meta" style="border: 1px solid var(--ink); padding: 6px 12px; border-radius: 50px;">Social Safety Gap</span>
                            <span class="meta" style="border: 1px solid var(--ink); padding: 6px 12px; border-radius: 50px;">Alignment Paradox</span>
                        </div>
                    </div>
                </div>
            </section>

            <!-- METHODOLOGY -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12 rv">
                        <span class="kicker-label">THE METHODOLOGY</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 32px;">Experimental Pipeline</h3>
                    </div>
                    
                    <div class="col-span-12 rv">
                        <div class="mermaid">
flowchart TD
    A[GoEmotions Dataset\\n27 categories + Neutral, 1,000 validation samples] --> B
    B[Emotion / Neutral Pairs] --> C
    C[Contrastive Prompt Construction\\n16 prompt pairs across 8 emotion categories] --> D
    D[Activation Extraction] --> E
    E[Neutralisation Vector]
    
    E --> F1
    E --> F2
    
    F1[Gemma-2B-IT\\nLoRA + NF4] --> G1
    F2[Llama-3-8B-Instruct\\nLoRA + NF4] --> G2
    
    G1[Activation Steering\\nLayers: 6, 9, 12, 16] --> H
    G2[Activation Steering\\nLayers: 10, 16, 21, 30] --> H
    
    H[Emotion Classification] --> I[Measure Emotional Degradation]
    
    I --> J1[Catastrophic Brittleness\\n(Gemma-2B)]
    I --> J2[Affective Erasure\\n(Llama-3-8B)]
                        </div>
                    </div>
                </div>
            </section>

            <!-- RESULTS & FAILURES -->
            <section class="section" style="padding: 40px 0; border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12 rv" style="margin-bottom: 30px;">
                        <span class="kicker-label">THE RESULTS</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 32px;">Baseline & Steering Degradation</h3>
                    </div>
                    
                    <div class="col-span-12 rv" style="overflow-x: auto; margin-bottom: 40px;">
                        <table style="width: 100%; border-collapse: collapse; text-align: left; font-family: var(--font-body);">
                            <tr style="border-bottom: 2px solid var(--rule-dark);">
                                <th style="padding: 10px;">Model</th>
                                <th style="padding: 10px;">Condition</th>
                                <th style="padding: 10px; text-align: right;">Micro-F1</th>
                                <th style="padding: 10px; text-align: right;">Macro-F1</th>
                                <th style="padding: 10px; text-align: right;">EAS</th>
                            </tr>
                            <tr style="border-bottom: 1px solid var(--rule);">
                                <td style="padding: 10px;">Gemma-2B</td>
                                <td style="padding: 10px;">Zero-shot</td>
                                <td style="padding: 10px; text-align: right;">0.034</td>
                                <td style="padding: 10px; text-align: right;">0.022</td>
                                <td style="padding: 10px; text-align: right;">0.003</td>
                            </tr>
                            <tr style="border-bottom: 1px solid var(--rule); background: var(--paper-warm);">
                                <td style="padding: 10px; font-weight: bold;">Gemma-2B</td>
                                <td style="padding: 10px; font-weight: bold;">Fine-tuned</td>
                                <td style="padding: 10px; text-align: right; font-weight: bold;">0.416</td>
                                <td style="padding: 10px; text-align: right; font-weight: bold;">0.419</td>
                                <td style="padding: 10px; text-align: right; font-weight: bold;">0.338</td>
                            </tr>
                            <tr style="border-bottom: 1px solid var(--rule);">
                                <td style="padding: 10px;">Llama-3-8B</td>
                                <td style="padding: 10px;">Zero-shot</td>
                                <td style="padding: 10px; text-align: right;">0.215</td>
                                <td style="padding: 10px; text-align: right;">0.211</td>
                                <td style="padding: 10px; text-align: right;">0.148</td>
                            </tr>
                            <tr style="border-bottom: 1px solid var(--rule); background: var(--paper-warm);">
                                <td style="padding: 10px; font-weight: bold;">Llama-3-8B</td>
                                <td style="padding: 10px; font-weight: bold;">Fine-tuned</td>
                                <td style="padding: 10px; text-align: right; font-weight: bold;">0.332</td>
                                <td style="padding: 10px; text-align: right; font-weight: bold;">0.372</td>
                                <td style="padding: 10px; text-align: right; font-weight: bold;">0.233</td>
                            </tr>
                        </table>
                    </div>

                    <div class="col-span-6 rv column-bordered">
                        <h4 class="heading-md" style="margin-bottom: 15px; color: var(--stamp);">Catastrophic Brittleness (Gemma-2B)</h4>
                        <p class="body" style="margin-bottom: 10px;">&bull; Coherent behavior persisted through approximately <strong>λ = 1.0</strong></p>
                        <p class="body" style="margin-bottom: 10px;">&bull; At <strong>λ ≥ 1.5</strong>, the model exhibited degenerate repetitive neutral-token output</p>
                        <p class="body" style="margin-bottom: 10px;">&bull; Strong steering causes collapse resulting in syntactic degradation</p>
                    </div>

                    <div class="col-span-6 rv" style="padding-left: 30px;">
                        <h4 class="heading-md" style="margin-bottom: 15px; color: var(--stamp);">Affective Erasure (Llama-3-8B)</h4>
                        <p class="body" style="margin-bottom: 10px;">&bull; Model retained structural and syntactic coherence</p>
                        <p class="body" style="margin-bottom: 10px;">&bull; Emotional information progressively weakened</p>
                        <p class="body" style="margin-bottom: 10px;">&bull; Neutral output share increased from 0.33 (λ = 0) to 0.50 (λ ≥ 0.5)</p>
                    </div>
                </div>
            </section>

            <!-- SOCIAL SAFETY GAP -->
            <section class="section" style="padding: 40px 0; background: var(--paper-warm); border-bottom: 1px solid var(--rule);">
                <div class="newspaper-grid">
                    <div class="col-span-12 rv">
                        <span class="kicker-label">THE DISCUSSION</span>
                        <h3 class="heading-lg" style="margin: 10px 0 20px 0; font-size: 32px;">The Social Safety Gap</h3>
                        <p class="body-lg" style="max-width: 800px; margin-bottom: 30px; font-style: italic;">A system may become safer according to conventional harmful-output metrics while simultaneously becoming less emotionally responsive.</p>
                    </div>
                    
                    <div class="col-span-12 rv">
                        <div class="mermaid">
flowchart TD
    A[ALIGNMENT PRESSURE] --> B
    A --> C
    B[Harmful Output] -.-> D[Reduced]
    C[Emotional Signal] -.-> E[Reduced]
    
    D --> F[TECHNICAL SAFETY]
    E --> G[SOCIAL SAFETY GAP]
                        </div>
                    </div>
                </div>
            </section>

            <!-- LIMITATIONS -->
            <section class="section" style="padding: 40px 0;">
                <div class="newspaper-grid">
                    <div class="col-span-12 rv">
                        <h3 class="heading-lg" style="margin-bottom: 20px; font-size: 28px;">Limitations</h3>
                        <p class="body" style="margin-bottom: 10px;">&bull; Only two model architectures evaluated.</p>
                        <p class="body" style="margin-bottom: 10px;">&bull; Activation steering is a controlled proxy for alignment pressure, not a reproduction of RLHF.</p>
                        <p class="body" style="margin-bottom: 10px;">&bull; No direct user study; downstream trust implications are inferred.</p>
                        <p class="body" style="margin-bottom: 10px;">&bull; Prompt construction covered eight emotion categories, not the complete GoEmotions space.</p>
                    </div>
                </div>
            </section>
"""

with open('pages/paper-compsac.html', 'w') as f:
    f.write(PAGE_TEMPLATE.replace('{title}', 'The Alignment Paradox').replace('{content}', PAPER_CONTENT))
