/**
 * The Sharma Dispatch - Elite Scroll & Entrance Animations
 * Triggers animations ONCE on initial viewport entry to eliminate scroll jitter.
 */

document.addEventListener('DOMContentLoaded', () => {
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        initScrollAnimations();
    }
});

function initScrollAnimations() {
    gsap.registerPlugin(ScrollTrigger);

    const defaultEase = 'power2.out';
    const defaultDuration = 0.6;

    // 1. Reveal elements with 'once: true' so they never re-animate or flicker on scroll
    ScrollTrigger.batch('.rv', {
        interval: 0.05,
        batchMax: 12,
        onEnter: batch => {
            gsap.fromTo(batch, 
                { opacity: 0, y: 20 },
                { 
                    opacity: 1, 
                    y: 0, 
                    duration: defaultDuration, 
                    ease: defaultEase,
                    stagger: 0.05,
                    overwrite: 'auto'
                }
            );
        },
        start: 'top 92%',
        once: true // CRITICAL: Run only once on load, never jitter on scroll
    });

    // 2. Card entrances with 'once: true'
    ScrollTrigger.batch('.dispatch-card, .metric-card-styled, .step-card-item', {
        onEnter: batch => {
            gsap.fromTo(batch,
                { opacity: 0, y: 25 },
                {
                    opacity: 1,
                    y: 0,
                    duration: defaultDuration,
                    ease: defaultEase,
                    stagger: 0.08,
                    overwrite: 'auto'
                }
            );
        },
        start: 'top 92%',
        once: true
    });

    // 3. Initial stamp rotation
    gsap.set('.dispatch-card__stamp', {
        rotation: -15,
        transformOrigin: 'center center'
    });
}
