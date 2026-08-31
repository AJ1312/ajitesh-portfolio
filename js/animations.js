/**
 * The Sharma Dispatch - High-Craft Interactive Animations
 * Highly inspired by Niccolò Miranda (https://www.niccolomiranda.com/):
 * Custom interactive editorial cursor, 3D card tilt physics, tactile rubber-stamp dynamics,
 * magnetic elements, and GSAP scroll reveals.
 */

document.addEventListener('DOMContentLoaded', () => {
    initCustomCursor();
    init3DPortraitTilt();
    initScrollReveals();
    initMagneticElements();
    initRubberStampInteractions();
    initLivePressClock();
    initEditionToggle();
});

// 1. Niccolò Miranda-Style Custom Editorial Cursor
function initCustomCursor() {
    if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

    // Create cursor elements if not present
    let cursor = document.querySelector('.custom-cursor');
    let dot = document.querySelector('.cursor-dot');
    
    if (!cursor) {
        cursor = document.createElement('div');
        cursor.className = 'custom-cursor';
        cursor.innerHTML = '<span class="cursor-label"></span>';
        document.body.appendChild(cursor);
    }
    
    if (!dot) {
        dot = document.createElement('div');
        dot.className = 'cursor-dot';
        document.body.appendChild(dot);
    }

    const label = cursor.querySelector('.cursor-label');

    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let cursorX = mouseX;
    let cursorY = mouseY;

    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;

        // Position dot immediately
        dot.style.left = `${mouseX}px`;
        dot.style.top = `${mouseY}px`;
    });

    // Smooth Lerp loop for the outer cursor ring
    function renderCursor() {
        cursorX += (mouseX - cursorX) * 0.18;
        cursorY += (mouseY - cursorY) * 0.18;

        cursor.style.left = `${cursorX}px`;
        cursor.style.top = `${cursorY}px`;

        requestAnimationFrame(renderCursor);
    }
    requestAnimationFrame(renderCursor);

    // Hover interactions for links, buttons, and data-cursor targets
    const interactiveElements = document.querySelectorAll('a, button, .editorial-btn, .action-btn-link, .tag-chip, .rubber-stamp, [data-cursor]');
    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', () => {
            const customText = el.getAttribute('data-cursor');
            if (customText) {
                label.textContent = customText;
                cursor.classList.add('has-label');
            } else {
                cursor.classList.add('is-hovering');
            }
        });

        el.addEventListener('mouseleave', () => {
            cursor.classList.remove('is-hovering', 'has-label');
            label.textContent = '';
        });
    });

    // Dispatch card specific cursor
    const dispatchCards = document.querySelectorAll('.dispatch-card, article[class*="col-span"]');
    dispatchCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            if (!card.hasAttribute('data-cursor')) {
                label.textContent = 'OPEN';
                cursor.classList.add('has-label');
            }
        });
        card.addEventListener('mouseleave', () => {
            cursor.classList.remove('has-label');
            label.textContent = '';
        });
    });
}

// 2. 3D Card Tilt on Colorful Hero Portrait
function init3DPortraitTilt() {
    const frame = document.querySelector('.editorial-portrait-frame');
    if (!frame || !window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

    frame.addEventListener('mousemove', (e) => {
        const rect = frame.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;

        const rotateX = (y / (rect.height / 2)) * -10; // max 10 deg tilt
        const rotateY = (x / (rect.width / 2)) * 10;

        frame.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
    });

    frame.addEventListener('mouseleave', () => {
        frame.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
        frame.style.transition = 'transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.5s ease';
    });
}

// 3. Smooth GSAP Scroll Reveals
function initScrollReveals() {
    if (typeof gsap === 'undefined') {
        document.querySelectorAll('.rv').forEach(el => {
            el.style.opacity = '1';
            el.style.transform = 'none';
        });
        return;
    }

    if (typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        const sections = document.querySelectorAll('section, .marquee-strip, .dispatch-card');
        sections.forEach(sec => {
            gsap.fromTo(sec, 
                { opacity: 0, y: 22 },
                {
                    opacity: 1,
                    y: 0,
                    duration: 0.7,
                    ease: "power2.out",
                    scrollTrigger: {
                        trigger: sec,
                        start: "top 88%",
                        toggleActions: "play none none none"
                    }
                }
            );
        });

        const staggerGroups = document.querySelectorAll('.newspaper-grid, .tag-group, .action-btn-group');
        staggerGroups.forEach(group => {
            const items = group.children;
            if (items.length > 1) {
                gsap.fromTo(items,
                    { opacity: 0, y: 14 },
                    {
                        opacity: 1,
                        y: 0,
                        duration: 0.5,
                        stagger: 0.06,
                        ease: "power2.out",
                        scrollTrigger: {
                            trigger: group,
                            start: "top 92%",
                            toggleActions: "play none none none"
                        }
                    }
                );
            }
        });
    }
}

// 4. Magnetic Element Tracking
function initMagneticElements() {
    const magneticTargets = document.querySelectorAll('.editorial-btn, .action-btn-link, .tag-chip, .rubber-stamp');
    if (!window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;

    magneticTargets.forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            
            btn.style.transform = `translate(${x * 0.22}px, ${y * 0.22}px)`;
        });

        btn.addEventListener('mouseleave', () => {
            btn.style.transform = '';
        });
    });
}

// 5. Dynamic Rubber Stamp Interactions
function initRubberStampInteractions() {
    const stamps = document.querySelectorAll('.rubber-stamp, .patent-tag-pill, .kicker-label');
    stamps.forEach(stamp => {
        stamp.addEventListener('mouseenter', () => {
            const randomAngle = (Math.random() * 8 - 4) - 6;
            stamp.style.transform = `rotate(${randomAngle}deg) scale(1.1)`;
        });

        stamp.addEventListener('mouseleave', () => {
            stamp.style.transform = '';
        });
    });
}

// 6. Live Printing Press Clock
function initLivePressClock() {
    const clockEl = document.querySelector('[data-live-clock]');
    if (!clockEl) return;

    function updateClock() {
        const now = new Date();
        const hrs = String(now.getHours()).padStart(2, '0');
        const mins = String(now.getMinutes()).padStart(2, '0');
        const secs = String(now.getSeconds()).padStart(2, '0');
        clockEl.textContent = `TIME: ${hrs}:${mins}:${secs} IST`;
    }

    updateClock();
    setInterval(updateClock, 1000);
}

// 7. Morning / Night Edition Broadsheet Switcher
function initEditionToggle() {
    const toggleBtn = document.querySelector('[data-edition-toggle]');
    if (!toggleBtn) return;

    const currentTheme = localStorage.getItem('sharma_dispatch_theme') || 'light';
    if (currentTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        toggleBtn.textContent = 'MORNING EDITION ☀️';
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        toggleBtn.textContent = 'NIGHT EDITION 🌙';
    }

    toggleBtn.addEventListener('click', () => {
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        if (isDark) {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('sharma_dispatch_theme', 'light');
            toggleBtn.textContent = 'NIGHT EDITION 🌙';
        } else {
            document.documentElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('sharma_dispatch_theme', 'dark');
            toggleBtn.textContent = 'MORNING EDITION ☀️';
        }
    });
}

// 8. Stat Strip Count-Up Animation
function initStatStripCountUp() {
    const statNums = document.querySelectorAll('.stat-strip__num');
    if (!statNums.length) return;

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const targetCount = parseInt(el.getAttribute('data-count'), 10);
                if (!isNaN(targetCount)) {
                    animateValue(el, 0, targetCount, 1200);
                }
                obs.unobserve(el);
            }
        });
    }, { threshold: 0.5 });

    statNums.forEach(num => observer.observe(num));

    function animateValue(obj, start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            const current = Math.floor(progress * (end - start) + start);
            
            if (end >= 10000) {
                obj.innerHTML = (current >= 10000 ? '10K+' : current.toLocaleString() + '+');
            } else if (end >= 1000) {
                obj.innerHTML = current.toLocaleString() + '+';
            } else {
                obj.innerHTML = current;
            }

            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }
}

// 9. Stamp Thud Entrance on Scroll
function initStampThudOnScroll() {
    const stamps = document.querySelectorAll('.rubber-stamp, .dispatch-card__stamp');
    if (!stamps.length) return;

    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('stamp-thud');
                obs.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    stamps.forEach(stamp => observer.observe(stamp));
}

// Initialize additional helpers
document.addEventListener('DOMContentLoaded', () => {
    initStatStripCountUp();
    initStampThudOnScroll();
});

