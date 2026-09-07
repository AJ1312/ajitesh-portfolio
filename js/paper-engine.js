/**
 * ============================================================================
 * THE PAPER ENGINE — Interactive Controller & Tactile Paper Physics
 * The Sharma Dispatch · Traditional Broadsheet Portfolio
 * ============================================================================
 */

(function () {
  'use strict';

  // --- Persistent Site-Wide Sound State ---
  const SOUND_STORAGE_KEY = 'paper_sound_enabled';
  const getStoredSoundPreference = () => {
    try {
      const stored = localStorage.getItem(SOUND_STORAGE_KEY);
      return stored === null ? true : stored === 'true';
    } catch (e) {
      return true;
    }
  };

  let soundEnabled = getStoredSoundPreference();
  let audioCtx = null;
  let updateAllSoundButtons = () => {};

  const setSoundEnabled = (enabled) => {
    soundEnabled = Boolean(enabled);
    try {
      localStorage.setItem(SOUND_STORAGE_KEY, soundEnabled ? 'true' : 'false');
    } catch (e) {}

    // If muting while audio is playing, pause immediately
    if (!soundEnabled && paperTearAudio) {
      try {
        paperTearAudio.pause();
        paperTearAudio.currentTime = 0;
      } catch (e) {}
    }

    updateAllSoundButtons();
  };

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

  // --- Authentic Acoustic Paper Tearing Audio Engine ---
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

  // Attempt initial load immediately
  loadTearBuffer();

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

    let played = false;
    // 1. Primary: High-fidelity zero-latency decoded AudioBuffer
    if (ctx && tearAudioBuffer) {
      try {
        const source = ctx.createBufferSource();
        source.buffer = tearAudioBuffer;
        const gain = ctx.createGain();
        gain.gain.setValueAtTime(0.95, ctx.currentTime);
        source.connect(gain);
        gain.connect(ctx.destination);
        source.start(0);
        played = true;
      } catch (e) {}
    }

    // 2. Direct HTML5 Audio fallback
    if (!played) {
      try {
        paperTearAudio.currentTime = 0;
        paperTearAudio.volume = 0.95;
        const playPromise = paperTearAudio.play();
        if (playPromise !== undefined) {
          playPromise.catch(() => {});
        }
        played = true;
      } catch (e) {}
    }

    // 3. Ultra-clean procedural fallback (ONLY if both file playbacks fail)
    if (!played && ctx) {
      try {
        const now = ctx.currentTime;
        const totalDuration = 0.75;
        const bufferLength = Math.floor(ctx.sampleRate * totalDuration);
        const buffer = ctx.createBuffer(1, bufferLength, ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferLength; i++) {
          const t = i / ctx.sampleRate;
          const env = t < 0.05 ? t / 0.05 : Math.pow(1 - (t - 0.05) / 0.70, 1.2);
          const snap = Math.random() > 0.88 ? (Math.random() * 2 - 1) * 1.8 : 0;
          data[i] = ((Math.random() * 2 - 1) * 0.5 + snap) * env;
        }
        const node = ctx.createBufferSource();
        node.buffer = buffer;
        const filter = ctx.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(1800, now);
        filter.Q.value = 1.6;
        const gain = ctx.createGain();
        gain.gain.setValueAtTime(0.35, now);
        node.connect(filter);
        filter.connect(gain);
        gain.connect(ctx.destination);
        node.start(now);
        node.stop(now + totalDuration);
      } catch (e) {}
    }
  };

  // --- Direct Access: Broadsheet Overlay Removal ---
  const initPaperTear = () => {
    const tearOverlay = document.getElementById('paperTransitionOverlay');
    if (tearOverlay) {
      tearOverlay.remove();
    }
    document.documentElement.classList.remove('paper-tear-pending');
    try {
      sessionStorage.removeItem('broadsheet_nav_arriving');
      sessionStorage.removeItem('broadsheet_tear_seen');
    } catch (e) {}
  };

  // ==========================================================================
  // REALISTIC SPRING-PHYSICS ENGINE (Hooke's Law: F = -k*x - c*v)
  // Inspired by React Spring & Vikram Thyagarajan's paper mechanics
  // ==========================================================================
  class PaperSpring {
    constructor({ mass = 1.0, tension = 180, friction = 22, onUpdate, onRest } = {}) {
      this.mass = mass;
      this.tension = tension;
      this.friction = friction;
      this.x = 0;
      this.target = 0;
      this.v = 0;
      this.onUpdate = onUpdate;
      this.onRest = onRest;
      this.animating = false;
      this.rafId = null;
      this.lastTime = null;
    }

    setTarget(target, initialVelocity = 0) {
      this.target = target;
      if (initialVelocity !== 0) this.v = initialVelocity;
      if (!this.animating) {
        this.animating = true;
        this.lastTime = performance.now();
        this.rafId = requestAnimationFrame((t) => this.step(t));
      }
    }

    step(now) {
      if (!this.animating) return;
      const dt = Math.min((now - (this.lastTime || now)) / 1000, 0.032);
      this.lastTime = now;

      // Hooke's Law with Viscous Damping: F = -k*(x - target) - c*v
      const fSpring = -this.tension * (this.x - this.target);
      const fDamper = -this.friction * this.v;
      const a = (fSpring + fDamper) / this.mass;

      this.v += a * dt;
      this.x += this.v * dt;

      if (this.onUpdate) this.onUpdate(this.x, this.v);

      // Spring convergence test
      if (Math.abs(this.x - this.target) < 0.001 && Math.abs(this.v) < 0.005) {
        this.x = this.target;
        this.v = 0;
        this.animating = false;
        if (this.onUpdate) this.onUpdate(this.x, 0);
        if (this.onRest) this.onRest();
        return;
      }

      this.rafId = requestAnimationFrame((t) => this.step(t));
    }

    destroy() {
      this.animating = false;
      if (this.rafId) cancelAnimationFrame(this.rafId);
    }
  }

  // --- Ultra-Realistic Page Transition via Double-Sided Paper Curl Reveal ---
  let isTearTransitioning = false;
  const triggerRealisticPaperTear = (href) => {
    if (isTearTransitioning || !href) return;
    isTearTransitioning = true;

    // 1. Play authentic tactile paper tearing acoustic sound
    unlockAudio();
    if (soundEnabled) {
      playPaperTearSound();
    }

    // 2. Build lightweight physics tearing stage
    const stage = document.createElement('div');
    stage.className = 'realistic-paper-tear-stage';
    stage.setAttribute('aria-hidden', 'true');

    stage.innerHTML = `
      <div class="tear-stage-underlay" id="tearUnderlay">
        <div class="tear-underlay-masthead">
          <h1 class="tear-underlay-title">THE SHARMA DISPATCH</h1>
          <div class="tear-underlay-rule"></div>
          <div style="font-family: var(--font-mono); font-size: 0.85rem; letter-spacing: 0.25em; text-transform: uppercase;">
            INCOMING DISPATCH &bull; UNVEILING
          </div>
        </div>
      </div>
      <div class="tear-stage-curl" id="tearCurlSheet">
        <div class="tear-curl-deckle"></div>
      </div>
    `;
    document.body.appendChild(stage);

    const underlay = stage.querySelector('#tearUnderlay');
    const curlSheet = stage.querySelector('#tearCurlSheet');
    const screenW = window.innerWidth;
    const screenH = window.innerHeight;

    // Slanted fold line angle (14 degrees clockwise from downward vertical)
    const thetaDeg = 14;
    const thetaRad = (thetaDeg * Math.PI) / 180;
    const tanTheta = Math.tan(thetaRad);

    // Total distance across viewport accounting for slant
    const startOffset = screenW + screenH * tanTheta + 80;
    const endOffset = -(screenH * tanTheta + 240);
    const totalSpan = startOffset - endOffset;

    // Configure curl leaf dimensions
    curlSheet.style.height = `${screenH * 1.8}px`;

    // 3. Drive the smooth curl reveal with React-Spring physics (Hooke's Law: F = -k*x - c*v)
    // Calibrated for a luxurious, fluid ~620ms paper peel
    const spring = new PaperSpring({
      mass: 1.0,
      tension: 30,
      friction: 9.2,
      onUpdate: (progress) => {
        const p = Math.max(0, Math.min(progress, 1.04));
        const offset = startOffset - p * totalSpan;
        const xTop = offset;
        const xBot = offset - screenH * tanTheta;

        // Clip underlay so incoming edition is unveiled to the right of the rolling crease
        underlay.style.clipPath = `polygon(${xTop}px 0, 100% 0, 100% 100%, ${xBot}px 100%)`;

        // Proportional cylindrical curl leaf rolling to the left of the fold line
        const curlW = Math.min(Math.max((screenW - xTop) * 0.14 + 100, 120), Math.min(screenW * 0.45, 280));
        curlSheet.style.width = `${curlW}px`;
        curlSheet.style.transform = `translate3d(${xTop}px, 0px, 0) rotate(${thetaDeg}deg) translateX(-100%)`;
      },
      onRest: () => {
        spring.destroy();
        window.location.href = href;
      }
    });

    // Release spring smoothly to target 1.0 with zero jerk
    spring.setTarget(1.0, 0);

    // Failsafe timeout in case of unexpected tab throttling
    setTimeout(() => {
      window.location.href = href;
    }, 720);
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

    internalLinks.forEach((link) => {
      const href = link.getAttribute('href');
      if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto:') || href.startsWith('tel:') || link.target === '_blank') {
        return;
      }

      // Prefetch on pointerenter / touchstart for instant response
      link.addEventListener('pointerenter', () => prefetchUrl(href), { passive: true, once: true });
      link.addEventListener('touchstart', () => prefetchUrl(href), { passive: true, once: true });

      // Realistic double-sided paper tear transition on click
      link.addEventListener('click', (e) => {
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
        e.preventDefault();
        triggerRealisticPaperTear(href);
      });
    });
  };

  // --- Tactile Paper Peel on Cards (Inspired by Post-It Physics) ---
  const initPaperPeelCards = () => {
    const cards = document.querySelectorAll('.work-card, .postal-stamp-card, .academic-letter-card');
    cards.forEach((card) => {
      card.classList.add('paper-peelable');
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

    updateAllSoundButtons = () => {
      soundBtns.forEach((btn) => {
        btn.innerHTML = soundEnabled
          ? `${ICONS.soundOn}<span class="btn-text">AUDIO</span>`
          : `${ICONS.soundOff}<span class="btn-text">MUTED</span>`;
        btn.setAttribute('aria-pressed', soundEnabled ? 'true' : 'false');
        btn.setAttribute('aria-label', soundEnabled ? 'Mute Audio Effects' : 'Enable Audio Effects');
        btn.classList.toggle('is-muted', !soundEnabled);
      });
    };

    updateAllSoundButtons();

    soundBtns.forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        setSoundEnabled(!soundEnabled);
        if (soundEnabled) {
          unlockAudio();
          playTactileClick();
        }
      });
    });

    // Synchronize audio state across browser tabs & windows
    window.addEventListener('storage', (e) => {
      if (e.key === SOUND_STORAGE_KEY) {
        soundEnabled = e.newValue === 'true';
        updateAllSoundButtons();
      }
    });

    document.querySelectorAll('a, button, .work-card, .postal-stamp-card, .stamp-3d-vellore').forEach((el) => {
      el.addEventListener('click', () => {
        if (soundEnabled) playTactileClick();
      });
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
    initPaperPeelCards();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})();
