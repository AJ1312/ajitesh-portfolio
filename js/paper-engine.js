/**
 * ============================================================================
 * THE PAPER ENGINE — Interactive Controller & Tactile Paper Physics
 * The Sharma Dispatch · Traditional Broadsheet Portfolio
 * ============================================================================
 */

(function () {
  'use strict';

  // --- Web Audio Synthesizer (Tactile Click & Rubber Stamp Thump) ---
  let soundEnabled = true; // Enabled by default for tactile portfolio feel
  let audioCtx = null;

  const getAudioContext = () => {
    if (!audioCtx) {
      const AudioContextClass = window.AudioContext || window.webkitAudioContext;
      if (AudioContextClass) audioCtx = new AudioContextClass();
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
    return audioCtx;
  };

  const playTactileClick = () => {
    if (!soundEnabled) return;
    try {
      const ctx = getAudioContext();
      if (!ctx) return;
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(650, ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(180, ctx.currentTime + 0.035);
      gain.gain.setValueAtTime(0.04, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.035);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 0.035);
    } catch (e) {}
  };

  const playStampThump = () => {
    if (!soundEnabled) return;
    try {
      const ctx = getAudioContext();
      if (!ctx) return;

      // Primary rubber resonance
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(140, ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(38, ctx.currentTime + 0.12);
      gain.gain.setValueAtTime(0.2, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.12);

      // Noise burst for paper friction
      const bufferSize = ctx.sampleRate * 0.05;
      const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
      const data = buffer.getChannelData(0);
      for (let i = 0; i < bufferSize; i++) {
        data[i] = Math.random() * 2 - 1;
      }
      const noise = ctx.createBufferSource();
      noise.buffer = buffer;
      const filter = ctx.createBiquadFilter();
      filter.type = 'lowpass';
      filter.frequency.value = 800;
      const noiseGain = ctx.createGain();
      noiseGain.gain.setValueAtTime(0.06, ctx.currentTime);
      noiseGain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.05);

      noise.connect(filter);
      filter.connect(noiseGain);
      noiseGain.connect(ctx.destination);

      osc.connect(gain);
      gain.connect(ctx.destination);

      osc.start();
      noise.start();
      osc.stop(ctx.currentTime + 0.13);
      noise.stop(ctx.currentTime + 0.05);
    } catch (e) {}
  };

  // --- Authentic Recorded & Synthesized Paper Tearing Audio Engine ---
  const isSubpage = window.location.pathname.includes('/pages/');
  const audioTearPath = isSubpage ? '../audio/paper_tear.wav' : 'audio/paper_tear.wav';
  const paperTearAudio = new Audio(audioTearPath);
  paperTearAudio.preload = 'auto';

  let tearAudioBuffer = null;
  const loadTearBuffer = () => {
    try {
      const ctx = getAudioContext();
      if (!ctx || tearAudioBuffer) return;
      fetch(audioTearPath)
        .then((res) => res.arrayBuffer())
        .then((arrayBuffer) => ctx.decodeAudioData(arrayBuffer))
        .then((decoded) => {
          tearAudioBuffer = decoded;
        })
        .catch(() => {});
    } catch (e) {}
  };

  // Unlock AudioContext and Audio elements on first user interaction
  const unlockAudio = () => {
    const ctx = getAudioContext();
    if (ctx && ctx.state === 'suspended') {
      ctx.resume();
    }
    loadTearBuffer();
    try {
      paperTearAudio.load();
    } catch (e) {}
  };
  window.addEventListener('pointerdown', unlockAudio, { once: true });
  window.addEventListener('keydown', unlockAudio, { once: true });
  window.addEventListener('touchstart', unlockAudio, { once: true, passive: true });

  const playPaperTearSound = () => {
    if (!soundEnabled) return;
    const ctx = getAudioContext();
    if (ctx && ctx.state === 'suspended') {
      ctx.resume();
    }

    // 1. Primary: High-fidelity zero-latency decoded AudioBuffer
    let playedBuffer = false;
    if (ctx && tearAudioBuffer) {
      try {
        const source = ctx.createBufferSource();
        source.buffer = tearAudioBuffer;
        const gain = ctx.createGain();
        gain.gain.setValueAtTime(1.0, ctx.currentTime);
        source.connect(gain);
        gain.connect(ctx.destination);
        source.start(0);
        playedBuffer = true;
      } catch (e) {}
    }

    // Direct HTML5 Audio fallback
    if (!playedBuffer) {
      try {
        paperTearAudio.currentTime = 0;
        paperTearAudio.volume = 0.95;
        const playPromise = paperTearAudio.play();
        if (playPromise !== undefined) {
          playPromise.catch(() => {});
        }
      } catch (e) {}
    }

    // 2. Secondary: Granular procedural paper fiber snap & tearing rasp synthesis
    if (ctx) {
      try {
        const now = ctx.currentTime;
        const totalDuration = 0.44;

        // LAYER 1: Sharp Granular Cellulose Fiber Snaps
        const crackleLength = Math.floor(ctx.sampleRate * totalDuration);
        const crackleBuffer = ctx.createBuffer(1, crackleLength, ctx.sampleRate);
        const crackleData = crackleBuffer.getChannelData(0);

        for (let i = 0; i < crackleLength; i++) {
          const t = i / ctx.sampleRate;
          const env = t < 0.04 ? t / 0.04 : Math.exp(-(t - 0.04) / 0.22);
          const fiberSnap = Math.random() > 0.82 ? (Math.random() * 2 - 1) * 2.8 : 0;
          const friction = (Math.random() * 2 - 1) * 0.7;
          crackleData[i] = (fiberSnap + friction) * env;
        }

        const crackleNode = ctx.createBufferSource();
        crackleNode.buffer = crackleBuffer;

        const crackleFilter = ctx.createBiquadFilter();
        crackleFilter.type = 'highpass';
        crackleFilter.frequency.setValueAtTime(1600, now);
        crackleFilter.frequency.exponentialRampToValueAtTime(3800, now + 0.12);
        crackleFilter.frequency.exponentialRampToValueAtTime(1800, now + totalDuration);

        const crackleGain = ctx.createGain();
        crackleGain.gain.setValueAtTime(0.35, now);
        crackleGain.gain.exponentialRampToValueAtTime(0.001, now + totalDuration);

        crackleNode.connect(crackleFilter);
        crackleFilter.connect(crackleGain);
        crackleGain.connect(ctx.destination);
        crackleNode.start(now);
        crackleNode.stop(now + totalDuration);

        // LAYER 2: Resonant Ripping Rasp
        const raspLength = Math.floor(ctx.sampleRate * 0.38);
        const raspBuffer = ctx.createBuffer(1, raspLength, ctx.sampleRate);
        const raspData = raspBuffer.getChannelData(0);
        for (let i = 0; i < raspLength; i++) {
          const t = i / ctx.sampleRate;
          const flutter = Math.sin(2 * Math.PI * 55 * t);
          raspData[i] = (Math.random() * 2 - 1) * (0.85 + 0.35 * flutter);
        }

        const raspNode = ctx.createBufferSource();
        raspNode.buffer = raspBuffer;

        const raspFilter = ctx.createBiquadFilter();
        raspFilter.type = 'bandpass';
        raspFilter.frequency.setValueAtTime(3400, now);
        raspFilter.frequency.exponentialRampToValueAtTime(1100, now + 0.35);
        raspFilter.Q.value = 2.4;

        const raspGain = ctx.createGain();
        raspGain.gain.setValueAtTime(0.28, now);
        raspGain.gain.exponentialRampToValueAtTime(0.001, now + 0.38);

        raspNode.connect(raspFilter);
        raspFilter.connect(raspGain);
        raspGain.connect(ctx.destination);
        raspNode.start(now);
        raspNode.stop(now + 0.38);

        // LAYER 3: Low-mid Paper Body Flutter
        const bodyOsc = ctx.createOscillator();
        const bodyGain = ctx.createGain();
        bodyOsc.type = 'triangle';
        bodyOsc.frequency.setValueAtTime(135, now);
        bodyOsc.frequency.exponentialRampToValueAtTime(36, now + 0.28);

        bodyGain.gain.setValueAtTime(0.18, now);
        bodyGain.gain.exponentialRampToValueAtTime(0.001, now + 0.28);

        bodyOsc.connect(bodyGain);
        bodyGain.connect(ctx.destination);
        bodyOsc.start(now);
        bodyOsc.stop(now + 0.28);
      } catch (e) {}
    }
  };

  // --- Two Paper Tearing Away Transition & Entrance Controller ---
  const initPaperTear = () => {
    let tearOverlay = document.getElementById('paperTransitionOverlay');
    const crestPath = isSubpage ? '../images/dispatch_crest.svg' : 'images/dispatch_crest.svg';

    if (!tearOverlay) {
      tearOverlay = document.createElement('div');
      tearOverlay.id = 'paperTransitionOverlay';
      tearOverlay.className = 'paper-tear-overlay';
      tearOverlay.setAttribute('aria-hidden', 'true');
      tearOverlay.innerHTML = `
        <div class="paper-tear-half paper-tear-left" id="paperTearLeft">
          <div class="paper-fiber-texture"></div>
          <div class="paper-laid-lines"></div>
          <div class="tear-sheet-content tear-content-left">
            <div class="tear-top-folio font-mono">
              <span>VOL. 2026 &bull; ISSUE NO. 43</span>
              <span class="tear-sec-tag">BROADSHEET FOLIO &bull; SEC. A</span>
            </div>
            <div class="tear-masthead-wrap">
              <h1 class="tear-masthead-title font-serif">THE SHARMA</h1>
              <div class="tear-masthead-sub font-mono">CHRONICLE OF SYSTEMS &bull; DEFENSIVE ARCHITECTURE</div>
            </div>
            <div class="tear-ornamental-rule"></div>
            <div class="tear-columns-grid">
              <div class="tear-col">
                <span class="tear-kicker font-mono">SPECIAL REPORT</span>
                <h2 class="tear-headline font-serif">A Systems Engineer Who Builds Things &mdash; <span style="color: var(--accent-red);">Kernel to Cloud</span></h2>
                <p class="tear-p font-serif"><span class="tear-dropcap">A</span>s a systems engineer and security researcher at VIT Vellore, I investigate and build software engineered to hold under intense adversarial load.</p>
                <div class="tear-col-divider"></div>
                <div class="tear-wire-notice font-mono">VELLORE WIRE &bull; DISPATCH RECEIVED</div>
              </div>
              <div class="tear-col tear-col-secondary">
                <span class="tear-kicker font-mono">CURRICULUM</span>
                <h3 class="tear-subhead font-serif">Vellore Institute of Technology</h3>
                <p class="tear-p-sm font-sans">B.Tech Computer Science &amp; Engineering (Spec. Information Security), 2023&ndash;2027.</p>
                <div class="tear-badge-pill font-mono">VERIFIED ARCHIVAL COPY</div>
              </div>
            </div>
            <div class="tear-bottom-folio font-mono">
              <span>LEFT SHEET &bull; CONTINUED ON SEC. B</span>
              <span>EST. 2023 &bull; HAND-SET MONO</span>
            </div>
          </div>
          <svg class="deckle-edge deckle-right" viewBox="0 0 60 1000" preserveAspectRatio="none" aria-hidden="true">
            <path class="deckle-white-fringe" d="M0,0 L32,0 L24,18 L36,35 L22,58 L38,82 L20,115 L35,138 L24,165 L42,198 L26,225 L38,255 L20,285 L44,325 L24,360 L38,395 L18,430 L45,475 L22,510 L40,545 L20,585 L46,630 L24,665 L41,705 L18,745 L47,790 L23,830 L41,875 L19,915 L48,965 L25,995 L30,1000 L0,1000 Z" fill="#fffdf9"></path>
            <path class="deckle-face" d="M0,0 L26,0 L18,16 L30,33 L16,55 L32,79 L14,112 L29,135 L18,162 L36,195 L20,222 L32,252 L14,282 L38,322 L18,357 L32,392 L12,427 L39,472 L16,507 L34,542 L14,582 L40,627 L18,662 L35,702 L12,742 L41,787 L17,827 L35,872 L13,912 L42,962 L19,992 L24,1000 L0,1000 Z" fill="#f6f0e2"></path>
          </svg>
        </div>
        <div class="paper-tear-seam" id="tearSeamSeal">
          <div class="seam-badge" id="tearBadgeBtn" role="button" tabindex="0" aria-label="Tear Broadsheet to Open">
            <div class="seam-badge-inner">
              <img src="${crestPath}" alt="Seal" class="seam-crest" />
              <span class="seam-title font-serif">THE SHARMA DISPATCH</span>
              <span class="seam-instruction font-mono">✂ TAP / CLICK TO TEAR OPEN ✂</span>
            </div>
          </div>
        </div>
        <div class="paper-tear-half paper-tear-right" id="paperTearRight">
          <div class="paper-fiber-texture"></div>
          <div class="paper-laid-lines"></div>
          <div class="tear-sheet-content tear-content-right">
            <div class="tear-top-folio font-mono">
              <span class="tear-sec-tag">BROADSHEET FOLIO &bull; SEC. B</span>
              <span>PRICE: ONE SSH SESSION</span>
            </div>
            <div class="tear-masthead-wrap">
              <h1 class="tear-masthead-title font-serif">DISPATCH</h1>
              <div class="tear-masthead-sub font-mono">ENGINEERED UNDER ADVERSARIAL RESILIENCE &bull; 2026</div>
            </div>
            <div class="tear-ornamental-rule"></div>
            <div class="tear-columns-grid">
              <div class="tear-col">
                <span class="tear-kicker font-mono">RESEARCH DISPATCH</span>
                <h2 class="tear-headline font-serif">Lock-Free Backends &amp; Applied AI.</h2>
                <p class="tear-p font-serif"><span class="tear-dropcap">T</span>he boundary between infrastructure and threat landscape has collapsed. Building zero-trust authentication pipelines.</p>
                <div class="tear-col-divider"></div>
                <div class="tear-wire-notice font-mono">PATENTS PENDING &bull; 3 FILED INVENTIONS</div>
              </div>
              <div class="tear-col tear-col-secondary">
                <span class="tear-kicker font-mono">CORRESPONDENCE</span>
                <h3 class="tear-subhead font-serif">Open for Collaboration</h3>
                <p class="tear-p-sm font-sans">Available for systems engineering and defensive security engagements.</p>
                <div class="tear-badge-pill font-mono">SEC. B FOLIO VERIFIED</div>
              </div>
            </div>
            <div class="tear-bottom-folio font-mono">
              <span>RIGHT SHEET &bull; COMPLETE DISPATCH</span>
              <span>PRESS RUN: 1ST PRINT</span>
            </div>
          </div>
          <svg class="deckle-edge deckle-left" viewBox="0 0 60 1000" preserveAspectRatio="none" aria-hidden="true">
            <path class="deckle-white-fringe" d="M60,0 L28,0 L36,18 L24,35 L38,58 L22,82 L40,115 L25,138 L36,165 L18,198 L34,225 L22,255 L40,285 L16,325 L36,360 L22,395 L42,430 L15,475 L38,510 L20,545 L40,585 L14,630 L36,665 L19,705 L42,745 L13,790 L37,830 L19,875 L41,915 L12,965 L35,995 L30,1000 L60,1000 Z" fill="#fffdf9"></path>
            <path class="deckle-face" d="M60,0 L34,0 L42,16 L30,33 L44,55 L28,79 L46,112 L31,135 L42,162 L24,195 L40,222 L28,252 L46,282 L22,322 L42,357 L28,392 L48,427 L21,472 L44,507 L26,542 L46,582 L20,627 L42,662 L25,702 L48,742 L19,787 L43,827 L25,872 L47,912 L18,962 L41,992 L36,1000 L60,1000 Z" fill="#f6f0e2"></path>
          </svg>
        </div>
      `;
      document.body.prepend(tearOverlay);
    }

    const hasSeenTear = sessionStorage.getItem('broadsheet_tear_seen');
    const isNavArriving = sessionStorage.getItem('broadsheet_nav_arriving') === 'true';
    const urlParams = new URLSearchParams(window.location.search);
    const forceReplay = urlParams.has('replay');

    // Function to perform the snappy, fluid tearing animation
    let isTearingActive = false;
    const triggerTear = (autoCloseDelay = 450) => {
      if (isTearingActive) return;
      isTearingActive = true;

      tearOverlay.style.display = 'flex';
      void tearOverlay.offsetWidth;
      tearOverlay.classList.remove('is-tearing');

      requestAnimationFrame(() => {
        playPaperTearSound();
        tearOverlay.classList.add('is-tearing');
        sessionStorage.setItem('broadsheet_tear_seen', 'true');
        document.documentElement.classList.remove('paper-tear-pending');

        setTimeout(() => {
          tearOverlay.style.display = 'none';
          tearOverlay.classList.remove('is-tearing');
          isTearingActive = false;
        }, autoCloseDelay);
      });
    };

    // User can tap/click anywhere to rip immediately
    tearOverlay.addEventListener('click', () => {
      unlockAudio();
      triggerTear(450);
    });

    // 1. ARRIVAL TRANSITION ACROSS ANY PAGE NAVIGATION (Index <-> Subpage, Subpage <-> Subpage)
    if (isNavArriving) {
      sessionStorage.removeItem('broadsheet_nav_arriving');
      tearOverlay.style.display = 'flex';
      tearOverlay.classList.remove('is-tearing');

      // Immediate 25ms trigger for ultra-snappy tear-open into the newly loaded page
      setTimeout(() => {
        unlockAudio();
        triggerTear(380);
      }, 25);
      return;
    }

    // 2. INITIAL SITE VISIT (Never seen broadsheet tear, or forced replay)
    if ((!hasSeenTear && !isSubpage) || forceReplay) {
      tearOverlay.style.display = 'flex';
      tearOverlay.classList.remove('is-tearing');

      // Snappy 60ms frame delay so initial paint completes smoothly
      const autoTimer = setTimeout(() => {
        triggerTear(520);
      }, 60);

      // Dismiss immediately on any user action
      const quickDismiss = () => {
        clearTimeout(autoTimer);
        tearOverlay.style.display = 'none';
        sessionStorage.setItem('broadsheet_tear_seen', 'true');
      };
      window.addEventListener('keydown', quickDismiss, { once: true, passive: true });
      window.addEventListener('wheel', quickDismiss, { once: true, passive: true });
      window.addEventListener('touchstart', quickDismiss, { once: true, passive: true });
    } else {
      tearOverlay.style.display = 'none';
      document.documentElement.classList.remove('paper-tear-pending');
    }

    // Connect Menu "✂ REPLAY TEAR ↺" Button
    const menuTearBtn = document.getElementById('menuTearDispatchBtn');
    if (menuTearBtn) {
      menuTearBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        unlockAudio();
        const menuOverlay = document.getElementById('menuOverlay');
        if (menuOverlay) menuOverlay.classList.remove('is-active');
        setTimeout(() => {
          triggerTear(520);
        }, 120);
      });
    }
  };

  // --- Ultra-Fluid Page Transitions & Instant Link Prefetching ---
  const initPageTransitions = () => {
    const internalLinks = document.querySelectorAll('a[href$=".html"], a[href^="pages/"], a[href^="../"], a[href*=".html"]');
    const prefetched = new Set();

    const prefetchUrl = (url) => {
      if (!url || prefetched.has(url)) return;
      prefetched.add(url);
      const link = document.createElement('link');
      link.rel = 'prefetch';
      link.href = url;
      link.as = 'document';
      document.head.appendChild(link);
    };

    const navigateWithPaperTear = (href) => {
      if (!href) return;

      // 1. Arm destination page to execute opening tear on arrival
      sessionStorage.setItem('broadsheet_nav_arriving', 'true');

      // 2. Play tactile audio rip immediately
      playPaperTearSound();

      // 3. Smooth tactile departure on current page
      document.body.classList.add('page-is-leaving');

      // 4. Close paper halves over current document
      const tearOverlay = document.getElementById('paperTransitionOverlay');
      if (tearOverlay) {
        tearOverlay.style.display = 'flex';
        tearOverlay.classList.remove('is-tearing');
      }

      // 5. Navigate at 160ms (allows tactile rip sound to articulate cleanly before page swap)
      setTimeout(() => {
        window.location.href = href;
      }, 160);
    };

    internalLinks.forEach((link) => {
      const href = link.getAttribute('href');
      if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto:') || href.startsWith('tel:') || link.target === '_blank') {
        return;
      }

      // Prefetch on pointerenter / touchstart for instant <15ms response
      link.addEventListener('pointerenter', () => prefetchUrl(href), { passive: true, once: true });
      link.addEventListener('touchstart', () => prefetchUrl(href), { passive: true, once: true });

      // Fluid transition on click
      link.addEventListener('click', (e) => {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
        e.preventDefault();
        navigateWithPaperTear(href);
      });
    });
  };

  // --- Encore Live Ticket Countdown Timer ---
  const initEncoreCountdown = () => {
    const countdownEl = document.getElementById('encoreCountdown');
    if (!countdownEl) return;
    let secondsLeft = 14 * 60 + 59;
    const updateCountdown = () => {
      const m = Math.floor(secondsLeft / 60).toString().padStart(2, '0');
      const s = (secondsLeft % 60).toString().padStart(2, '0');
      countdownEl.textContent = `${m}:${s}`;
      if (secondsLeft > 0) {
        secondsLeft--;
      } else {
        secondsLeft = 15 * 60;
      }
    };
    updateCountdown();
    setInterval(updateCountdown, 1000);
  };

  // --- Click-to-Stamp Quirk on Education Card ---
  const initEducationCardQuirk = () => {
    const academicCards = document.querySelectorAll('.academic-letter-card');
    if (!academicCards.length) return;

    academicCards.forEach((card) => {
      card.addEventListener('click', (e) => {
        // Do not double-stamp if clicking on an interactive link inside the card
        if (e.target.closest('a, button')) return;

        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        playStampThump();

        // Unique dynamic stamp with random rotation
        const stamp = document.createElement('div');
        stamp.className = 'dynamic-stamp';
        const randomRot = (Math.random() * 32 - 16).toFixed(1);
        stamp.style.left = `${x}px`;
        stamp.style.top = `${y}px`;
        stamp.style.setProperty('--rot', `${randomRot}deg`);

        const uniqueId = `arc_${Date.now()}_${Math.floor(Math.random() * 1000)}`;
        stamp.innerHTML = `
          <svg viewBox="0 0 140 140" style="width: 100%; height: 100%; overflow: visible;" aria-hidden="true">
            <circle cx="70" cy="70" r="64" fill="none" stroke="#b3261e" stroke-width="3" />
            <circle cx="70" cy="70" r="58" fill="none" stroke="#b3261e" stroke-width="1.5" stroke-dasharray="3,3" />
            <circle cx="70" cy="70" r="46" fill="none" stroke="#b3261e" stroke-width="1.5" />
            <defs>
              <path id="${uniqueId}" d="M 18,70 A 52,52 0 1,1 122,70" />
            </defs>
            <text fill="#b3261e" font-family="JetBrains Mono, monospace" font-size="8.5" font-weight="900" letter-spacing="0.12em">
              <textPath href="#${uniqueId}" startOffset="50%" text-anchor="middle">
                VELLORE INST OF TECH
              </textPath>
            </text>
            <text x="70" y="63" fill="#b3261e" font-family="JetBrains Mono, monospace" font-size="10.5" font-weight="900" letter-spacing="0.1em" text-anchor="middle">OFFICIAL</text>
            <text x="70" y="76" fill="#b3261e" font-family="Playfair Display, Georgia, serif" font-style="italic" font-size="10" font-weight="800" text-anchor="middle">2023–2027</text>
            <text x="70" y="88" fill="#b3261e" font-family="JetBrains Mono, monospace" font-size="8.5" font-weight="800" letter-spacing="0.12em" text-anchor="middle">INFOSEC</text>
          </svg>
        `;

        card.appendChild(stamp);

        // Limit stamps per card to 10
        const existingStamps = card.querySelectorAll('.dynamic-stamp');
        if (existingStamps.length > 10) {
          existingStamps[0].remove();
        }
      });
    });
  };

  // --- Buttery-Smooth Scroll Reveals ---
  const initScrollReveals = () => {
    const revealElements = document.querySelectorAll('[data-reveal], .reveal-rule');
    if (!revealElements.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-revealed');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.05, rootMargin: '0px 0px -15px 0px' }
    );

    revealElements.forEach((el) => observer.observe(el));
  };

  // --- 3D Portrait Frame Perspective & Specular Sheen ---
  const init3DPortraitTilt = () => {
    const container = document.querySelector('.portrait-container');
    const frame = document.querySelector('.portrait-frame');
    const sheen = document.querySelector('.portrait-sheen');
    if (!container || !frame) return;

    if (window.matchMedia('(hover: none) or (pointer: coarse)').matches) {
      return;
    }

    let targetRotX = 0;
    let targetRotY = 0;
    let currentRotX = 0;
    let currentRotY = 0;
    let isHovered = false;
    let isRendering = false;

    const render = () => {
      currentRotX += (targetRotX - currentRotX) * 0.14;
      currentRotY += (targetRotY - currentRotY) * 0.14;

      if (isHovered || Math.abs(currentRotX) > 0.05 || Math.abs(currentRotY) > 0.05) {
        frame.style.transform = `rotateX(${currentRotX.toFixed(2)}deg) rotateY(${currentRotY.toFixed(2)}deg) translateZ(8px)`;
        requestAnimationFrame(render);
      } else {
        frame.style.transform = '';
        isRendering = false;
      }
    };

    const startRender = () => {
      if (!isRendering) {
        isRendering = true;
        requestAnimationFrame(render);
      }
    };

    container.addEventListener('mousemove', (e) => {
      const rect = container.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;

      targetRotX = -y * 14;
      targetRotY = x * 14;

      if (sheen) {
        const angle = Math.atan2(y, x) * (180 / Math.PI) + 180;
        sheen.style.background = `linear-gradient(${angle}deg, rgba(255,255,255,0.3) 0%, rgba(255,255,255,0.06) 40%, rgba(255,255,255,0) 70%)`;
      }
      isHovered = true;
      startRender();
    });

    container.addEventListener('mouseleave', () => {
      targetRotX = 0;
      targetRotY = 0;
      isHovered = false;
      startRender();
    });
  };

  // --- Interactive Stamps (3D Vellore Seal & Postal Stamp) ---
  const initStampInteraction = () => {
    // All 3D Vellore Stamps across the page
    const velloreStamps = document.querySelectorAll('[data-stamp-vellore]');
    velloreStamps.forEach((stamp) => {
      const card = stamp.closest('.academic-letter-card') || stamp.parentElement;

      // 3D Perspective tilt over card
      if (card && !window.matchMedia('(hover: none) or (pointer: coarse)').matches) {
        card.addEventListener('mousemove', (e) => {
          const rect = card.getBoundingClientRect();
          const x = (e.clientX - rect.left) / rect.width - 0.5;
          const y = (e.clientY - rect.top) / rect.height - 0.5;
          const tiltX = -y * 16;
          const tiltY = x * 16;
          stamp.style.transform = `rotate(-10deg) rotateX(${tiltX.toFixed(1)}deg) rotateY(${tiltY.toFixed(1)}deg) translateZ(30px) scale(1.08)`;
        });

        card.addEventListener('mouseleave', () => {
          stamp.style.transform = '';
        });
      }

      // Stamp thump click
      stamp.addEventListener('click', (e) => {
        e.stopPropagation();
        stamp.classList.add('is-stamped');
        playStampThump();
        setTimeout(() => {
          stamp.classList.remove('is-stamped');
        }, 420);
      });
    });

    // Postal stamp cards
    const postalStamps = document.querySelectorAll('.postal-stamp-card');
    postalStamps.forEach((stamp) => {
      stamp.addEventListener('click', () => {
        playStampThump();
      });
    });
  };

  // --- Selected Works Reel Momentum Drag & Dynamic Skew Physics ---
  const initWorksReel = () => {
    const reel = document.querySelector('[data-works-reel]');
    const track = document.querySelector('.works-reel-track');
    const counterText = document.querySelector('#reelCounterText');
    const progressBar = document.querySelector('#reelProgressFill');
    if (!reel) return;

    let isDown = false;
    let startX = 0;
    let scrollLeft = 0;
    let lastX = 0;
    let velocity = 0;
    let currentSkew = 0;
    let targetSkew = 0;
    let animationId = null;

    // Update progress bar and counter
    const updateProgress = () => {
      const maxScroll = reel.scrollWidth - reel.clientWidth;
      if (maxScroll <= 0) return;
      const progress = Math.min(Math.max(reel.scrollLeft / maxScroll, 0), 1);
      const cardIndex = Math.min(5, Math.max(1, Math.round(progress * 4) + 1));

      if (counterText) {
        counterText.textContent = `DISPATCH 0${cardIndex} / 05`;
      }
      if (progressBar) {
        progressBar.style.width = `${Math.max(18, Math.round((cardIndex / 5) * 100))}%`;
      }
    };

    reel.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();

    // Physics loop for dynamic skewing
    const updateSkewPhysics = () => {
      currentSkew += (targetSkew - currentSkew) * 0.2;
      if (track) {
        track.style.transform = Math.abs(currentSkew) > 0.02 ? `skewX(${currentSkew.toFixed(2)}deg)` : '';
      }
      if (Math.abs(targetSkew) > 0.05 || Math.abs(currentSkew) > 0.05) {
        targetSkew *= 0.88;
        animationId = requestAnimationFrame(updateSkewPhysics);
      } else {
        if (track) track.style.transform = '';
        animationId = null;
      }
    };

    reel.addEventListener('mousedown', (e) => {
      isDown = true;
      reel.classList.add('is-dragging');
      startX = e.pageX - reel.offsetLeft;
      scrollLeft = reel.scrollLeft;
      lastX = e.pageX;
      velocity = 0;
      targetSkew = 0;
    });

    const stopDragging = () => {
      if (!isDown) return;
      isDown = false;
      reel.classList.remove('is-dragging');

      // Momentum fling
      if (Math.abs(velocity) > 2) {
        reel.scrollBy({
          left: -velocity * 12,
          behavior: 'smooth'
        });
      }
      targetSkew = 0;
    };

    reel.addEventListener('mouseleave', stopDragging);
    reel.addEventListener('mouseup', stopDragging);

    reel.addEventListener('mousemove', (e) => {
      if (!isDown) return;
      e.preventDefault();
      const x = e.pageX - reel.offsetLeft;
      const walk = (x - startX) * 1.4;
      reel.scrollLeft = scrollLeft - walk;

      velocity = e.pageX - lastX;
      lastX = e.pageX;

      // Clamp skew angle between -3.5 and 3.5 degrees
      targetSkew = Math.max(-3.5, Math.min(3.5, velocity * -0.22));

      if (!animationId) {
        animationId = requestAnimationFrame(updateSkewPhysics);
      }
    });
  };

  // --- Scroll-Velocity Reactive Marquee ---
  const initScrollVelocityMarquee = () => {
    const marqueeTrack = document.querySelector('.marquee-track');
    if (!marqueeTrack) return;

    let lastScrollY = window.scrollY;
    let scrollVelocity = 0;
    let ticking = false;

    window.addEventListener('scroll', () => {
      const currentScrollY = window.scrollY;
      scrollVelocity = Math.abs(currentScrollY - lastScrollY);
      lastScrollY = currentScrollY;

      if (!ticking) {
        requestAnimationFrame(() => {
          if (scrollVelocity > 5) {
            const speedMultiplier = Math.min(scrollVelocity * 0.08, 2.5);
            marqueeTrack.style.animationDuration = `${Math.max(10, 26 / (1 + speedMultiplier))}s`;
          } else {
            marqueeTrack.style.animationDuration = '26s';
          }
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  };

  // --- Clean Plan Vector SVGs for Broadsheet Navbar Controls ---
  const ICONS = {
    sun: '<svg class="nav-svg sun-icon" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"></path></svg>',
    moon: '<svg class="nav-svg moon-icon" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>',
    soundOn: '<svg class="nav-svg sound-icon-on" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path><path d="M19.07 4.93a10 10 0 0 1 0 14.14"></path></svg>',
    soundOff: '<svg class="nav-svg sound-icon-off" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line></svg>',
    tear: '<svg class="nav-svg tear-icon" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="6" cy="6" r="3"></circle><circle cx="6" cy="18" r="3"></circle><line x1="20" y1="4" x2="8.12" y2="15.88"></line><line x1="14.47" y1="14.48" x2="20" y2="20"></line><line x1="8.12" y1="8.12" x2="12" y2="12"></line></svg>',
    menu: '<svg class="nav-svg menu-icon" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>'
  };

  // --- Theme Controller (Morning Broadsheet vs. Night Edition) ---
  const initTheme = () => {
    const themeBtns = document.querySelectorAll('[data-edition-toggle]');
    const root = document.documentElement;
    const storedTheme = localStorage.getItem('paper_edition');

    const setTheme = (theme) => {
      if (theme === 'night') {
        root.setAttribute('data-theme', 'night');
        themeBtns.forEach((btn) => {
          btn.innerHTML = `${ICONS.sun}<span class="btn-text theme-text">DAY</span>`;
          btn.setAttribute('aria-label', 'Switch to Day Edition');
        });
      } else {
        root.removeAttribute('data-theme');
        themeBtns.forEach((btn) => {
          btn.innerHTML = `${ICONS.moon}<span class="btn-text theme-text">NIGHT</span>`;
          btn.setAttribute('aria-label', 'Switch to Night Edition');
        });
      }
      localStorage.setItem('paper_edition', theme);
    };

    if (storedTheme) {
      setTheme(storedTheme);
    } else {
      setTheme('day');
    }

    themeBtns.forEach((btn) => {
      btn.addEventListener('click', () => {
        const current = root.getAttribute('data-theme') === 'night' ? 'night' : 'day';
        setTheme(current === 'night' ? 'day' : 'night');
      });
    });
  };

  // --- Live Clock & Dateline ---
  const initClock = () => {
    const clockEl = document.querySelector('[data-live-clock]');
    if (!clockEl) return;

    const updateTime = () => {
      const now = new Date();
      const options = {
        timeZone: 'Asia/Kolkata',
        hour12: false,
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      };
      const timeStr = new Intl.DateTimeFormat('en-GB', options).format(now);
      clockEl.textContent = `IST ${timeStr}`;
    };

    updateTime();
    setInterval(updateTime, 1000);
  };

  // --- Fullscreen Dramatic Overlay Menu ---
  const initMenu = () => {
    const trigger = document.querySelector('[data-menu-open]');
    const closeBtn = document.querySelector('[data-menu-close]');
    const overlay = document.querySelector('#menuOverlay');
    const menuLinks = document.querySelectorAll('.menu-nav-item');

    if (!overlay) return;

    const openMenu = () => {
      overlay.classList.add('is-active');
      overlay.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    };

    const closeMenu = () => {
      overlay.classList.remove('is-active');
      overlay.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    };

    if (trigger) trigger.addEventListener('click', openMenu);
    if (closeBtn) closeBtn.addEventListener('click', closeMenu);

    menuLinks.forEach((link) => {
      link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');
        if (href && href.startsWith('#')) {
          e.preventDefault();
          closeMenu();
          const target = document.querySelector(href);
          if (target) {
            setTimeout(() => {
              target.scrollIntoView({ behavior: 'smooth' });
            }, 60);
          }
        } else {
          closeMenu();
        }
      });
    });

    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && overlay.classList.contains('is-active')) {
        closeMenu();
      }
    });
  };

  // --- Custom Ink-Dot Cursor (Desktop Only) ---
  const initCursor = () => {
    if (window.matchMedia('(hover: none) or (pointer: coarse)').matches) {
      return;
    }

    const cursor = document.createElement('div');
    cursor.className = 'paper-cursor';
    cursor.setAttribute('aria-hidden', 'true');
    document.body.appendChild(cursor);

    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let cursorX = mouseX;
    let cursorY = mouseY;
    let isVisible = false;
    let isRunning = false;

    const render = () => {
      cursorX += (mouseX - cursorX) * 0.28;
      cursorY += (mouseY - cursorY) * 0.28;
      cursor.style.transform = `translate3d(${cursorX.toFixed(1)}px, ${cursorY.toFixed(1)}px, 0) translate(-50%, -50%)`;

      if (Math.abs(mouseX - cursorX) > 0.15 || Math.abs(mouseY - cursorY) > 0.15) {
        requestAnimationFrame(render);
      } else {
        isRunning = false;
      }
    };

    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      if (!isVisible) {
        cursor.style.opacity = '1';
        isVisible = true;
      }
      if (!isRunning) {
        isRunning = true;
        requestAnimationFrame(render);
      }
    }, { passive: true });

    window.addEventListener('mouseleave', () => {
      cursor.style.opacity = '0';
      isVisible = false;
    });

    const hoverTargets = document.querySelectorAll('[data-cursor]');
    hoverTargets.forEach((target) => {
      target.addEventListener('mouseenter', () => {
        const label = target.getAttribute('data-cursor') || 'VIEW';
        cursor.classList.add('is-hovering');
        cursor.textContent = label;
      });
      target.addEventListener('mouseleave', () => {
        cursor.classList.remove('is-hovering');
        cursor.textContent = '';
      });
    });
  };

  // --- Stat Counters with IntersectionObserver ---
  const initCounters = () => {
    const counterElements = document.querySelectorAll('[data-count]');
    if (!counterElements.length) return;

    const observer = new IntersectionObserver(
      (entries, obs) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const el = entry.target;
            const targetVal = parseInt(el.getAttribute('data-count'), 10);
            const prefix = el.getAttribute('data-prefix') || '';
            const suffix = el.getAttribute('data-suffix') || '';
            const duration = 1200;
            const startTime = performance.now();

            const animateCount = (currentTime) => {
              const elapsed = currentTime - startTime;
              const progress = Math.min(elapsed / duration, 1);
              const easeOut = 1 - (1 - progress) * (1 - progress);
              const currentCount = Math.floor(easeOut * targetVal);

              el.textContent = `${prefix}${currentCount.toLocaleString()}${suffix}`;

              if (progress < 1) {
                requestAnimationFrame(animateCount);
              } else {
                el.textContent = `${prefix}${targetVal.toLocaleString()}${suffix}`;
              }
            };

            requestAnimationFrame(animateCount);
            obs.unobserve(el);
          }
        });
      },
      { threshold: 0.25 }
    );

    counterElements.forEach((el) => observer.observe(el));
  };

  // --- Audio / Sound Effects Toggle ---
  const initSoundToggle = () => {
    const soundBtns = document.querySelectorAll('[data-sound-toggle]');
    if (!soundBtns.length) return;

    const updateSoundBtns = () => {
      soundBtns.forEach((btn) => {
        btn.innerHTML = soundEnabled
          ? `${ICONS.soundOn}<span class="btn-text">AUDIO</span>`
          : `${ICONS.soundOff}<span class="btn-text">MUTED</span>`;
        btn.setAttribute('aria-pressed', soundEnabled ? 'true' : 'false');
        btn.setAttribute('aria-label', soundEnabled ? 'Mute Audio Effects' : 'Enable Audio Effects');
      });
    };

    updateSoundBtns();

    soundBtns.forEach((btn) => {
      btn.addEventListener('click', () => {
        soundEnabled = !soundEnabled;
        updateSoundBtns();
        if (soundEnabled) playTactileClick();
      });
    });

    document.querySelectorAll('a, button, .work-card, .postal-stamp-card, .stamp-3d-vellore').forEach((el) => {
      el.addEventListener('click', playTactileClick);
    });
  };

  // --- Sticky Topbar Shadow on Scroll ---
  const initStickyTopbar = () => {
    const topbar = document.querySelector('.paper-topbar');
    if (!topbar) return;

    let ticking = false;
    const checkScroll = () => {
      if (window.scrollY > 20) {
        topbar.classList.add('is-scrolled');
      } else {
        topbar.classList.remove('is-scrolled');
      }
      ticking = false;
    };

    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(checkScroll);
        ticking = true;
      }
    }, { passive: true });

    checkScroll();
  };

  // --- Broadsheet Nav Active Section Tracking ---
  const initNavObserver = () => {
    const navLinks = document.querySelectorAll('.broadsheet-nav .nav-item-link');
    if (!navLinks.length) return;

    const sections = Array.from(navLinks)
      .map((link) => {
        const id = link.getAttribute('href');
        return id && id.startsWith('#') ? document.querySelector(id) : null;
      })
      .filter(Boolean);

    if (!sections.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const id = `#${entry.target.id}`;
            navLinks.forEach((link) => {
              if (link.getAttribute('href') === id) {
                link.classList.add('is-active');
              } else {
                link.classList.remove('is-active');
              }
            });
          }
        });
      },
      { rootMargin: '-20% 0px -65% 0px', threshold: 0 }
    );

    sections.forEach((sec) => observer.observe(sec));
  };

  // --- Document Ready / Initialization ---
  const initAll = () => {
    initPaperTear();
    initPageTransitions();
    initTheme();
    initClock();
    initMenu();
    initStickyTopbar();
    initNavObserver();
    initCursor();
    init3DPortraitTilt();
    initStampInteraction();
    initEducationCardQuirk();
    initScrollReveals();
    initWorksReel();
    initScrollVelocityMarquee();
    initCounters();
    initSoundToggle();
    initEncoreCountdown();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})();
