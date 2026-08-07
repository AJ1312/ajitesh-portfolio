/**
 * The Sharma Dispatch - Scroll Animations
 * Utilizes GSAP and ScrollTrigger for editorial-style entrance animations.
 */

document.addEventListener('DOMContentLoaded', () => {
    // Ensure GSAP is loaded
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        initScrollAnimations();
    } else {
        console.warn('GSAP or ScrollTrigger not loaded.');
    }
});

function initScrollAnimations() {
    // Register the plugin
    gsap.registerPlugin(ScrollTrigger);

    const defaultEase = 'power2.out';
    const defaultDuration = 0.8;

    // 8. Stamp Interaction - Initial setup via GSAP
    // The hover state is handled in CSS, but we set initial rotated state here
    gsap.set('.dispatch-card__stamp', {
        rotation: -15, // A slight initial rotation for the stamp aesthetic
        transformOrigin: 'center center'
    });

    // 10. Batch Animations for Text Reveals (.rv)
    // 2. Text Reveal
    ScrollTrigger.batch('.rv', {
        interval: 0.1, // time window for batching
        batchMax: 10,  // max elements per batch
        onEnter: batch => {
            gsap.fromTo(batch, 
                { opacity: 0, y: 30 },
                { 
                    opacity: 1, 
                    y: 0, 
                    duration: defaultDuration, 
                    ease: defaultEase,
                    stagger: {
                        each: 0.1,
                    }
                }
            );
        },
        start: 'top 85%'
    });

    // 3. Rule Expansion (.rv-rule)
    ScrollTrigger.batch('.rv-rule', {
        onEnter: batch => {
            gsap.fromTo(batch,
                { scaleX: 0 },
                {
                    scaleX: 1,
                    duration: defaultDuration,
                    ease: 'power3.out',
                    transformOrigin: 'left center',
                    stagger: 0.1
                }
            );
        },
        start: 'top 90%'
    });

    // 4. Word-by-Word Reveal (.rv-word)
    // Assuming words are wrapped in a container, or directly using batch.
    // For words staggered by custom CSS vars, we handle them nicely with batch or a simpler loop.
    const rvWordContainers = document.querySelectorAll('.rv-word-container');
    rvWordContainers.forEach(container => {
        const words = container.querySelectorAll('.rv-word');
        if (words.length) {
            gsap.fromTo(words,
                { opacity: 0, y: 10 },
                {
                    opacity: 1,
                    y: 0,
                    duration: 0.6,
                    ease: defaultEase,
                    stagger: 0.05,
                    scrollTrigger: {
                        trigger: container,
                        start: 'top 85%',
                    }
                }
            );
        }
    });

    // 5. Parallax (.parallax)
    const parallaxElements = document.querySelectorAll('.parallax');
    parallaxElements.forEach(el => {
        gsap.to(el, {
            yPercent: 30, // Moves down slightly as we scroll down
            ease: 'none',
            scrollTrigger: {
                trigger: el.parentElement || el,
                start: 'top bottom', // Start when element enters bottom of screen
                end: 'bottom top',   // End when element leaves top of screen
                scrub: true          // Smoothly scrub animation based on scroll position
            }
        });
    });

    // 6. Card Stagger (.dispatch-card)
    // Batch dispatch cards for a nice staggered entrance
    ScrollTrigger.batch('.dispatch-card', {
        onEnter: batch => {
            gsap.fromTo(batch,
                { opacity: 0, y: 40 },
                {
                    opacity: 1,
                    y: 0,
                    duration: defaultDuration,
                    ease: 'power3.out',
                    stagger: 0.1
                }
            );
        },
        start: 'top 85%'
    });

    // 7. Section Transitions
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        gsap.fromTo(section,
            { opacity: 0 },
            {
                opacity: 1,
                duration: 1,
                ease: 'power2.inOut',
                scrollTrigger: {
                    trigger: section,
                    start: 'top 85%', // Trigger when top of section hits 85% of viewport
                    once: true        // Only animate once
                }
            }
        );
    });

    // 9. Horizontal Scroll Section (.hscroll-track)
    const hscrollSections = document.querySelectorAll('.hscroll-track');
    hscrollSections.forEach(track => {
        const container = track.parentElement;
        
        // Calculate the total horizontal scroll distance
        const getScrollAmount = () => {
            let trackWidth = track.scrollWidth;
            return -(trackWidth - window.innerWidth);
        };

        const tween = gsap.to(track, {
            x: getScrollAmount,
            ease: 'none'
        });

        ScrollTrigger.create({
            trigger: container,
            start: 'top top',
            end: () => `+=${getScrollAmount() * -1}`,
            pin: true,
            animation: tween,
            scrub: 1,
            invalidateOnRefresh: true // Recalculate values on resize
        });
    });

    // 11. Refresh on load
    // Ensures ScrollTrigger recalculates positions after images and fonts load
    window.addEventListener('load', () => {
        ScrollTrigger.refresh();
    });
}
