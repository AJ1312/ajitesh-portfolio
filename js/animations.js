/**
 * The Sharma Dispatch - Editorial & Broadside Interactive Animations
 * Inspired by Niccolò Miranda's craft: tactile physical interactions, magnetic elements,
 * rubber-stamp dynamics, and smooth scroll reveals.
 */

document.addEventListener('DOMContentLoaded', () => {
    initScrollReveals();
    initMagneticElements();
    initRubberStampInteractions();
    initLivePressClock();
    initCardHoverPhysics();
});

// 1. Smooth GSAP Scroll Reveals
function initScrollReveals() {
    if (typeof gsap === 'undefined') {
        // Fallback if GSAP is unavailable
        document.querySelectorAll('.rv').forEach(el => {
            el.style.opacity = '1';
            el.style.transform = 'none';
        });
        return;
    }

    if (typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        // Animate editorial sections
        const sections = document.querySelectorAll('section, .marquee-strip, .dispatch-card, .editorial-portrait-frame');
        sections.forEach((sec, idx) => {
            gsap.fromTo(sec, 
                { opacity: 0, y: 24 },
                {
                    opacity: 1,
                    y: 0,
                    duration: 0.8,
                    ease: "power2.out",
                    scrollTrigger: {
                        trigger: sec,
                        start: "top 88%",
                        toggleActions: "play none none none"
                    }
                }
            );
        });

        // Stagger list items in patents and dispatches
        const staggerGroups = document.querySelectorAll('.newspaper-grid, .tag-group, .action-btn-group');
        staggerGroups.forEach(group => {
            const items = group.children;
            if (items.length > 1) {
                gsap.fromTo(items,
                    { opacity: 0, y: 16 },
                    {
                        opacity: 1,
                        y: 0,
                        duration: 0.6,
                        stagger: 0.08,
                        ease: "power2.out",
                        scrollTrigger: {
                            trigger: group,
                            start: "top 90%",
                            toggleActions: "play none none none"
                        }
                    }
                );
            }
        });
    } else {
        document.querySelectorAll('.rv').forEach(el => {
            el.style.opacity = '1';
            el.style.transform = 'none';
        });
    }
}

// 2. Magnetic Pull on Buttons & Interactive Badges
function initMagneticElements() {
    const magneticTargets = document.querySelectorAll('.editorial-btn, .action-btn-link, .tag-chip, .rubber-stamp');
    
    // Only apply on non-touch devices
    if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
        magneticTargets.forEach(btn => {
            btn.addEventListener('mousemove', (e) => {
                const rect = btn.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                
                btn.style.transform = `translate(${x * 0.25}px, ${y * 0.25}px)`;
            });

            btn.addEventListener('mouseleave', () => {
                btn.style.transform = '';
            });
        });
    }
}

// 3. Dynamic Rubber Stamp Interactions
function initRubberStampInteractions() {
    const stamps = document.querySelectorAll('.rubber-stamp, .patent-tag-pill, .kicker-label');
    stamps.forEach(stamp => {
        stamp.addEventListener('mouseenter', () => {
            const randomAngle = (Math.random() * 8 - 4) - 6; // random tilt between -10 and -2
            stamp.style.transform = `rotate(${randomAngle}deg) scale(1.08)`;
        });

        stamp.addEventListener('mouseleave', () => {
            stamp.style.transform = '';
        });
    });
}

// 4. Live Printing Press Clock in Dateline
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

// 5. Card Hover Physics
function initCardHoverPhysics() {
    const cards = document.querySelectorAll('.dispatch-card, article[class*="col-span"], .metric-card-styled');
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transition = 'all 0.3s cubic-bezier(0.16, 1, 0.3, 1)';
        });
    });
}
