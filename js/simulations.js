/**
 * simulations.js
 * The Sharma Dispatch - Interactive Simulations
 * 
 * Provides interactive visualizations for project detail pages.
 * Each init function returns an object with a destroy() method to clean up resources.
 */

window.Simulations = {};

/**
 * 1. DPI Particle Network
 */
window.initDPISimulation = function(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return null;

    container.innerHTML = '';
    container.style.position = 'relative';
    container.style.backgroundColor = '#121212';
    container.style.overflow = 'hidden';
    container.style.fontFamily = '"JetBrains Mono", monospace';

    const canvas = document.createElement('canvas');
    canvas.style.display = 'block';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    container.appendChild(canvas);

    // Overlay for stats and controls
    const overlay = document.createElement('div');
    overlay.style.position = 'absolute';
    overlay.style.top = '10px';
    overlay.style.left = '10px';
    overlay.style.right = '10px';
    overlay.style.display = 'flex';
    overlay.style.justifyContent = 'space-between';
    overlay.style.color = '#E8E6E0';
    overlay.style.fontSize = '12px';
    overlay.style.pointerEvents = 'none';

    const stats = document.createElement('div');
    stats.innerHTML = `
        <div id="${containerId}-packets">Packets/sec: 0</div>
        <div id="${containerId}-threats" style="color: #FF4D6A">Threats Detected: 0</div>
        <div id="${containerId}-latency">Avg Latency: 1.1ms</div>
    `;
    
    const controls = document.createElement('div');
    controls.style.pointerEvents = 'auto';
    controls.innerHTML = `
        <button id="${containerId}-pause" style="background:#1A1A1A; color:#E8E6E0; border:1px solid #555; padding:4px 8px; cursor:pointer; font-family:inherit;">Pause</button>
    `;

    overlay.appendChild(stats);
    overlay.appendChild(controls);
    container.appendChild(overlay);

    let ctx = canvas.getContext('2d');
    let width, height;
    let animationId;
    let isPaused = false;

    const stages = ['CAPTURE', 'DECODE', 'CLASSIFY', 'FINGERPRINT', 'SCORE'];
    let particles = [];
    let packetCount = 0;
    let threatCount = 0;
    
    function resize() {
        const rect = container.getBoundingClientRect();
        width = rect.width;
        height = rect.height;
        canvas.width = width;
        canvas.height = height;
    }
    
    window.addEventListener('resize', resize);
    resize();

    class Particle {
        constructor() {
            this.reset();
            this.x = Math.random() * width; // Initial random spread
        }
        
        reset() {
            this.x = -10;
            this.y = height * 0.1 + Math.random() * (height * 0.8);
            this.vx = 2 + Math.random() * 2;
            this.vy = (Math.random() - 0.5) * 0.5;
            this.stage = -1;
            this.color = '#555555';
            this.isThreat = Math.random() < 0.15;
            packetCount++;
        }
        
        update(speedMult) {
            this.x += this.vx * speedMult;
            this.y += this.vy * speedMult;
            
            // Constrain Y
            if (this.y < height * 0.1 || this.y > height * 0.9) this.vy *= -1;

            const stageWidth = width / stages.length;
            const newStage = Math.floor(this.x / stageWidth);
            
            if (newStage !== this.stage && newStage >= 0 && newStage < stages.length) {
                this.stage = newStage;
                if (this.stage === 1) this.color = '#3A86FF'; // Decoded (Blue)
                if (this.stage === 3) {
                    if (this.isThreat) {
                        this.color = '#FF4D6A'; // Threat (Red)
                        threatCount++;
                    } else {
                        this.color = '#38B000'; // Benign (Green)
                    }
                }
            }
            
            if (this.x > width + 10) {
                this.reset();
            }
        }
        
        draw() {
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, 2, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    for (let i = 0; i < 100; i++) particles.push(new Particle());

    let lastTime = 0;
    let speedMult = 1;

    function drawStages() {
        const stageWidth = width / stages.length;
        ctx.textAlign = 'center';
        ctx.font = '10px "JetBrains Mono"';
        
        for (let i = 0; i < stages.length; i++) {
            ctx.fillStyle = i % 2 === 0 ? 'rgba(255,255,255,0.02)' : 'rgba(255,255,255,0.05)';
            ctx.fillRect(i * stageWidth, 0, stageWidth, height);
            
            ctx.fillStyle = '#888';
            ctx.fillText(stages[i], i * stageWidth + stageWidth/2, height - 20);
            
            if (i > 0) {
                ctx.strokeStyle = 'rgba(255,255,255,0.1)';
                ctx.beginPath();
                ctx.moveTo(i * stageWidth, 0);
                ctx.lineTo(i * stageWidth, height);
                ctx.stroke();
            }
        }
    }

    function drawConnections() {
        ctx.strokeStyle = 'rgba(100, 100, 100, 0.2)';
        ctx.lineWidth = 0.5;
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                if (dx * dx + dy * dy < 4000) {
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.stroke();
                }
            }
        }
    }

    function loop(time) {
        if (!isPaused) {
            ctx.clearRect(0, 0, width, height);
            
            drawStages();
            drawConnections();
            
            particles.forEach(p => {
                p.update(speedMult);
                p.draw();
            });

            // Update stats
            if (time - lastTime > 1000) {
                document.getElementById(`${containerId}-packets`).textContent = `Packets/sec: ${Math.floor(packetCount / (speedMult * 2))}`;
                document.getElementById(`${containerId}-threats`).textContent = `Threats Detected: ${threatCount}`;
                packetCount = 0;
                lastTime = time;
            }
        }
        animationId = requestAnimationFrame(loop);
    }
    
    document.getElementById(`${containerId}-pause`).addEventListener('click', (e) => {
        isPaused = !isPaused;
        e.target.textContent = isPaused ? 'Resume' : 'Pause';
    });

    animationId = requestAnimationFrame(loop);

    return {
        destroy: () => {
            window.removeEventListener('resize', resize);
            cancelAnimationFrame(animationId);
            container.innerHTML = '';
        }
    };
};

/**
 * 2. Anomaly Dashboard
 */
window.initAnomalyDashboard = function(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return null;

    container.innerHTML = '';
    container.style.backgroundColor = '#0D1117';
    container.style.color = '#C9D1D9';
    container.style.fontFamily = '"JetBrains Mono", monospace';
    container.style.display = 'grid';
    container.style.gridTemplateColumns = '1fr 1fr';
    container.style.gridTemplateRows = '1fr 1fr';
    container.style.gap = '10px';
    container.style.padding = '10px';
    container.style.height = '100%';
    container.style.boxSizing = 'border-box';

    const panelStyle = `
        background: #161B22;
        border: 1px solid #30363D;
        border-radius: 0;
        padding: 15px;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        position: relative;
    `;

    const titleStyle = `
        font-size: 10px;
        color: #8B949E;
        margin-bottom: 10px;
        letter-spacing: 1px;
    `;

    // Panel 1: Gauge
    const p1 = document.createElement('div');
    p1.style.cssText = panelStyle;
    p1.innerHTML = `
        <div style="${titleStyle}">CURRENT RISK SCORE</div>
        <div style="flex:1; display:flex; align-items:center; justify-content:center; position:relative;">
            <svg width="150" height="100" viewBox="0 0 200 120">
                <path d="M 20 100 A 80 80 0 0 1 180 100" fill="none" stroke="#238636" stroke-width="15"/>
                <path d="M 80 40 A 80 80 0 0 1 180 100" fill="none" stroke="#D29922" stroke-width="15"/>
                <path d="M 140 28 A 80 80 0 0 1 180 100" fill="none" stroke="#F85149" stroke-width="15"/>
                <polygon id="${containerId}-needle" points="100,20 95,100 105,100" fill="#E6EDF3" style="transform-origin: 100px 100px; transition: transform 0.5s ease;"/>
                <circle cx="100" cy="100" r="8" fill="#E6EDF3"/>
            </svg>
            <div id="${containerId}-score" style="position:absolute; bottom:0; font-size:24px; font-weight:bold;">45</div>
        </div>
    `;

    // Panel 2: Chart
    const p2 = document.createElement('div');
    p2.style.cssText = panelStyle;
    p2.innerHTML = `
        <div style="${titleStyle}; display:flex; justify-content:space-between;">
            <span>LIVE TELEMETRY</span>
            <span><span style="color:#58A6FF;">■ Normal</span> <span style="color:#F85149;">■ Anomaly</span></span>
        </div>
        <canvas id="${containerId}-chart" style="flex:1; width:100%;"></canvas>
    `;

    // Panel 3: Alerts
    const p3 = document.createElement('div');
    p3.style.cssText = panelStyle;
    p3.innerHTML = `
        <div style="${titleStyle}">ALERT FEED</div>
        <div id="${containerId}-feed" style="flex:1; overflow-y:auto; font-size:11px; line-height:1.4;">
        </div>
    `;

    // Panel 4: SHAP
    const p4 = document.createElement('div');
    p4.style.cssText = panelStyle;
    p4.innerHTML = `
        <div style="${titleStyle}">SHAP ATTRIBUTION</div>
        <div id="${containerId}-shap" style="flex:1; display:flex; flex-direction:column; justify-content:space-around;">
        </div>
    `;

    container.appendChild(p1);
    container.appendChild(p2);
    container.appendChild(p3);
    container.appendChild(p4);

    let intervals = [];
    let animationId;

    // Logic for Gauge
    const needle = document.getElementById(`${containerId}-needle`);
    const scoreText = document.getElementById(`${containerId}-score`);
    intervals.push(setInterval(() => {
        const score = 20 + Math.random() * 60;
        const angle = -90 + (score / 100) * 180;
        needle.style.transform = \`rotate(\${angle}deg)\`;
        scoreText.textContent = Math.round(score);
        scoreText.style.color = score < 40 ? '#238636' : (score < 70 ? '#D29922' : '#F85149');
    }, 2000));

    // Logic for Alerts
    const feed = document.getElementById(`${containerId}-feed`);
    const alerts = [
        { l: 'CRITICAL', c: '#F85149', m: 'Port scan detected from 192.168.1.x' },
        { l: 'HIGH', c: '#D29922', m: 'Anomalous beacon pattern on port 443' },
        { l: 'MEDIUM', c: '#8B949E', m: 'Unusual payload entropy: 7.9 bits/byte' },
        { l: 'LOW', c: '#238636', m: 'New TLS fingerprint observed' }
    ];
    
    function addAlert() {
        const a = alerts[Math.floor(Math.random() * alerts.length)];
        const time = new Date().toLocaleTimeString('en-US', {hour12: false, fractionalSecondDigits: 1});
        const div = document.createElement('div');
        div.style.marginBottom = '6px';
        div.style.opacity = '0';
        div.style.transition = 'opacity 0.5s';
        div.innerHTML = \`<span style="color:#8B949E">[\${time}]</span> <span style="color:\${a.c}">[\${a.l}]</span> \${a.m}\`;
        feed.insertBefore(div, feed.firstChild);
        setTimeout(() => div.style.opacity = '1', 50);
        if (feed.children.length > 20) feed.removeChild(feed.lastChild);
    }
    intervals.push(setInterval(addAlert, 2500));
    addAlert();

    // Logic for Chart
    const chartCanvas = document.getElementById(`${containerId}-chart`);
    const ctx = chartCanvas.getContext('2d');
    let cWidth, cHeight;
    let chartData = Array(50).fill(0).map(() => ({n: 20 + Math.random()*10, a: 5 + Math.random()*5}));
    
    function resizeChart() {
        const rect = chartCanvas.parentElement.getBoundingClientRect();
        chartCanvas.width = rect.width - 30;
        chartCanvas.height = rect.height - 40;
        cWidth = chartCanvas.width;
        cHeight = chartCanvas.height;
    }
    window.addEventListener('resize', resizeChart);
    resizeChart();

    function drawChart() {
        ctx.clearRect(0, 0, cWidth, cHeight);
        
        // Grid
        ctx.strokeStyle = '#30363D';
        ctx.lineWidth = 1;
        for(let i=0; i<4; i++) {
            const y = (cHeight/4)*i;
            ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(cWidth, y); ctx.stroke();
        }

        const step = cWidth / 49;
        
        // Normal
        ctx.beginPath();
        ctx.strokeStyle = '#58A6FF';
        ctx.lineWidth = 2;
        chartData.forEach((d, i) => {
            const x = i * step;
            const y = cHeight - (d.n / 100) * cHeight;
            if (i===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
        });
        ctx.stroke();

        // Anomaly
        ctx.beginPath();
        ctx.strokeStyle = '#F85149';
        ctx.lineWidth = 2;
        chartData.forEach((d, i) => {
            const x = i * step;
            const y = cHeight - (d.a / 100) * cHeight;
            if (i===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
        });
        ctx.stroke();

        animationId = requestAnimationFrame(drawChart);
    }
    drawChart();

    intervals.push(setInterval(() => {
        chartData.shift();
        const isSpike = Math.random() < 0.1;
        chartData.push({
            n: 20 + Math.random()*15,
            a: isSpike ? 60 + Math.random()*30 : 5 + Math.random()*10
        });
    }, 100));

    // Logic for SHAP
    const shapContainer = document.getElementById(`${containerId}-shap`);
    const features = ['payload_entropy', 'iat_variance', 'packet_size_mean', 'flow_duration', 'ja4_hash_match'];
    
    function updateShap() {
        shapContainer.innerHTML = '';
        features.forEach(f => {
            const val = (Math.random() * 2 - 1).toFixed(2);
            const w = Math.abs(val) * 100;
            const c = val > 0 ? '#F85149' : '#58A6FF';
            const left = val < 0 ? \`calc(50% - \${w}px)\` : '50%';
            
            shapContainer.innerHTML += \`
                <div style="display:flex; justify-content:space-between; font-size:10px; margin-bottom:2px;">
                    <span style="color:#8B949E; width:100px; overflow:hidden; text-overflow:ellipsis;">\${f}</span>
                    <div style="flex:1; position:relative; height:8px; margin:2px 10px; background:rgba(255,255,255,0.05);">
                        <div style="position:absolute; left:50%; top:0; bottom:0; width:1px; background:#30363D;"></div>
                        <div style="position:absolute; top:0; height:100%; left:\${left}; width:\${w}px; background:\${c}; transition:all 0.5s;"></div>
                    </div>
                    <span style="width:30px; text-align:right;">\${val}</span>
                </div>
            \`;
        });
    }
    updateShap();
    intervals.push(setInterval(updateShap, 3000));

    return {
        destroy: () => {
            window.removeEventListener('resize', resizeChart);
            cancelAnimationFrame(animationId);
            intervals.forEach(clearInterval);
            container.innerHTML = '';
        }
    };
};

/**
 * 3. CI/CD Pipeline Visualization
 */
window.initPipelineViz = function(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return null;

    container.innerHTML = '';
    container.style.backgroundColor = '#1A1A1A';
    container.style.color = '#E0E0E0';
    container.style.fontFamily = '"JetBrains Mono", monospace';
    container.style.padding = '20px';
    container.style.display = 'flex';
    container.style.flexDirection = 'column';
    container.style.height = '100%';
    container.style.boxSizing = 'border-box';

    const stages = [
        { id: 'CODE', icon: '📝' },
        { id: 'LINT', icon: '🔍' },
        { id: 'TEST', icon: '🧪' },
        { id: 'SCAN', icon: '🛡️' },
        { id: 'BUILD', icon: '📦' },
        { id: 'PUSH', icon: '☁️' },
        { id: 'DEPLOY', icon: '🚀' },
        { id: 'VERIFY', icon: '✅' }
    ];

    const pipelineHtml = stages.map((s, i) => \`
        <div id="\${containerId}-stage-\${i}" style="
            display:flex; flex-direction:column; align-items:center; opacity:0.5; transition:all 0.3s;
        ">
            <div style="
                width:40px; height:40px; border:2px solid #555; display:flex; align-items:center; justify-content:center; 
                font-size:20px; background:#222; position:relative; z-index:2;
            ">
                <span class="icon">\${s.icon}</span>
                <span class="status" style="position:absolute; bottom:-5px; right:-5px; font-size:12px;"></span>
            </div>
            <div style="font-size:10px; margin-top:8px; letter-spacing:1px;">\${s.id}</div>
        </div>
        \${i < stages.length - 1 ? \`<div style="flex:1; height:2px; background:#555; margin-top:20px; position:relative; z-index:1;"></div>\` : ''}
    \`).join('');

    container.innerHTML = \`
        <div style="display:flex; justify-content:space-between; margin-bottom:30px; padding:0 10px;">
            \${pipelineHtml}
        </div>
        <div id="\${containerId}-banner" style="
            background: #238636; color: white; text-align: center; padding: 10px; font-weight: bold; 
            letter-spacing: 2px; font-family: 'Inter', sans-serif; opacity: 0; transition: opacity 0.5s;
            margin-bottom: 20px;
        ">DEPLOYMENT SUCCESSFUL</div>
        <div style="
            flex: 1; background: #000; border: 1px solid #333; padding: 10px; overflow-y: auto;
            font-size: 11px; line-height: 1.5; color: #aaa;
        " id="\${containerId}-logs">
            > Initializing pipeline...<br>
        </div>
    \`;

    const logs = document.getElementById(`\${containerId}-logs`);
    const banner = document.getElementById(`\${containerId}-banner`);
    let currentStage = 0;
    let timeoutId;
    let isRunning = true;

    function log(msg, color = '#aaa') {
        const time = new Date().toISOString().substring(11,19);
        logs.innerHTML += \`<span style="color:#555">[\${time}]</span> <span style="color:\${color}">\${msg}</span><br>\`;
        logs.scrollTop = logs.scrollHeight;
    }

    function runPipeline() {
        if (!isRunning) return;

        // Reset
        if (currentStage === 0) {
            banner.style.opacity = '0';
            logs.innerHTML = '> Starting new deployment...<br>';
            stages.forEach((_, i) => {
                const el = document.getElementById(`\${containerId}-stage-\${i}`);
                if (el) {
                    el.style.opacity = '0.5';
                    el.querySelector('div').style.borderColor = '#555';
                    el.querySelector('div').style.boxShadow = 'none';
                    el.querySelector('.status').innerHTML = '';
                }
            });
        }

        if (currentStage < stages.length) {
            const stage = stages[currentStage];
            const el = document.getElementById(`\${containerId}-stage-\${currentStage}`);
            
            // Set to running
            el.style.opacity = '1';
            el.querySelector('div').style.borderColor = '#D29922';
            el.querySelector('div').style.boxShadow = '0 0 10px rgba(210,153,34,0.5)';
            el.querySelector('.status').innerHTML = '⏳';
            log(`Running stage: \${stage.id}...`, '#D29922');

            timeoutId = setTimeout(() => {
                if (!isRunning) return;
                // Set to success
                el.querySelector('div').style.borderColor = '#238636';
                el.querySelector('div').style.boxShadow = '0 0 10px rgba(35,134,54,0.5)';
                el.querySelector('.status').innerHTML = '✅';
                log(`Stage \${stage.id} completed successfully.`, '#238636');
                
                currentStage++;
                timeoutId = setTimeout(runPipeline, 500);
            }, 1500);
        } else {
            banner.style.opacity = '1';
            log('Pipeline execution finished.', '#58A6FF');
            currentStage = 0;
            timeoutId = setTimeout(runPipeline, 4000);
        }
    }

    // Start
    timeoutId = setTimeout(runPipeline, 1000);

    return {
        destroy: () => {
            isRunning = false;
            clearTimeout(timeoutId);
            container.innerHTML = '';
        }
    };
};

/**
 * 4. Queue Management Simulation
 */
window.initQueueSimulation = function(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return null;

    container.innerHTML = '';
    container.style.backgroundColor = '#F9F8F4';
    container.style.color = '#1A1A1A';
    container.style.fontFamily = '"Inter", sans-serif';
    container.style.display = 'flex';
    container.style.flexDirection = 'column';
    container.style.height = '100%';
    container.style.boxSizing = 'border-box';
    container.style.border = '1px solid #1A1A1A';

    const header = document.createElement('div');
    header.style.borderBottom = '3px double #1A1A1A';
    header.style.padding = '10px';
    header.style.display = 'flex';
    header.style.justifyContent = 'space-between';
    header.style.alignItems = 'center';
    header.innerHTML = \`
        <div style="font-family:'Playfair Display', serif; font-size:18px; font-weight:bold;">SERVICE RECORD</div>
        <div style="font-family:'JetBrains Mono', monospace; font-size:11px;">
            <span id="\${containerId}-s-pending">Pending: 0</span> | 
            <span id="\${containerId}-s-active">Active: 0</span> | 
            <span id="\${containerId}-s-done">Completed: 0</span>
        </div>
    \`;

    const board = document.createElement('div');
    board.style.flex = '1';
    board.style.display = 'flex';
    board.style.overflow = 'hidden';

    const colStyle = "flex:1; border-right:1px solid #E0E0E0; display:flex; flex-direction:column; padding:10px; overflow-y:auto; position:relative;";
    
    board.innerHTML = \`
        <div style="\${colStyle}" id="\${containerId}-col-queue">
            <div style="font-family:'JetBrains Mono', monospace; font-size:10px; font-weight:bold; letter-spacing:1px; margin-bottom:10px;">QUEUE</div>
        </div>
        <div style="\${colStyle}" id="\${containerId}-col-progress">
            <div style="font-family:'JetBrains Mono', monospace; font-size:10px; font-weight:bold; letter-spacing:1px; margin-bottom:10px;">IN PROGRESS</div>
        </div>
        <div style="\${colStyle}; border-right:none;" id="\${containerId}-col-completed">
            <div style="font-family:'JetBrains Mono', monospace; font-size:10px; font-weight:bold; letter-spacing:1px; margin-bottom:10px;">COMPLETED</div>
        </div>
    \`;

    container.appendChild(header);
    container.appendChild(board);

    const names = ['Aarav Patel', 'Diya Sharma', 'Rohan Gupta', 'Ananya Singh', 'Vihaan Kumar', 'Zara Das', 'Arjun Reddy', 'Kavya Iyer'];
    const roles = ['OPERATOR', 'SUPERVISOR', 'MANAGER'];
    const depts = ['SMELTER', 'POWER', 'ADMIN'];

    let intervals = [];
    let stats = { pending: 0, active: 0, done: 0 };
    
    function updateStats() {
        document.getElementById(`\${containerId}-s-pending`).textContent = \`Pending: \${stats.pending}\`;
        document.getElementById(`\${containerId}-s-active`).textContent = \`Active: \${stats.active}\`;
        document.getElementById(`\${containerId}-s-done`).textContent = \`Completed: \${stats.done}\`;
    }

    function createCard() {
        const name = names[Math.floor(Math.random() * names.length)];
        const role = roles[Math.floor(Math.random() * roles.length)];
        const dept = depts[Math.floor(Math.random() * depts.length)];
        
        const card = document.createElement('div');
        card.style.border = '1px solid #1A1A1A';
        card.style.padding = '8px';
        card.style.marginBottom = '8px';
        card.style.backgroundColor = '#FFFFFF';
        card.style.boxShadow = '2px 2px 0px #E0E0E0';
        card.style.fontSize = '12px';
        card.style.transition = 'all 0.3s ease';
        card.style.opacity = '0';
        card.style.transform = 'translateY(10px)';
        
        card.innerHTML = \`
            <div style="font-weight:bold; margin-bottom:4px; display:flex; justify-content:space-between;">
                \${name} <span style="color:\${role==='MANAGER'?'#C41E3A':'#555'};">●</span>
            </div>
            <div style="font-family:'JetBrains Mono', monospace; font-size:9px; color:#555;">
                \${role} / \${dept}
            </div>
        \`;

        const qCol = document.getElementById(`\${containerId}-col-queue`);
        const pCol = document.getElementById(`\${containerId}-col-progress`);
        const cCol = document.getElementById(`\${containerId}-col-completed`);
        
        if(!qCol) return; // if destroyed

        qCol.appendChild(card);
        stats.pending++;
        updateStats();

        // Animate in
        requestAnimationFrame(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        });

        // Move to Progress
        setTimeout(() => {
            if(!pCol) return;
            card.style.opacity = '0';
            setTimeout(() => {
                pCol.appendChild(card);
                stats.pending--;
                stats.active++;
                updateStats();
                card.style.opacity = '1';
            }, 300);
        }, 4000);

        // Move to Completed
        setTimeout(() => {
            if(!cCol) return;
            card.style.opacity = '0';
            setTimeout(() => {
                card.style.backgroundColor = '#F0F0F0';
                card.style.color = '#888';
                cCol.appendChild(card);
                stats.active--;
                stats.done++;
                updateStats();
                card.style.opacity = '1';
                
                // Cleanup old completed
                if(cCol.children.length > 6) {
                    cCol.removeChild(cCol.children[1]); // keep header
                }
            }, 300);
        }, 10000);
    }

    createCard();
    intervals.push(setInterval(createCard, 3000));

    return {
        destroy: () => {
            intervals.forEach(clearInterval);
            container.innerHTML = '';
        }
    };
};
