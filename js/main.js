/**
 * The Sharma Dispatch - Main Interaction Scripts
 * Core functionality for navigation, theme switching, and basic UI interactions.
 */

document.addEventListener('DOMContentLoaded', () => {
    initDynamicDate();
    initReadingProgressBar();
    initStickyNav();
    initMobileMenu();
    initThemeSwitcher();
    initSmoothScroll();
    initActiveNavObserver();
    initCounterAnimation();
    initTypewriter();
});

// 1. Dynamic Date in Masthead
function initDynamicDate() {
    const dateElements = document.querySelectorAll('.masthead__date, [data-dynamic-date]');
    if (dateElements.length === 0) return;

    const now = new Date();
    const days = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY'];
    const months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER'];
    
    const dayName = days[now.getDay()];
    const dayNum = now.getDate();
    const monthName = months[now.getMonth()];
    const year = now.getFullYear();

    const formattedDate = `${dayName} ${dayNum} ${monthName} ${year} · VOL. I`;

    dateElements.forEach(el => {
        el.textContent = formattedDate;
    });
}

// 1.5 Reading Progress Bar
function initReadingProgressBar() {
    const progressBar = document.getElementById('reading-progress-bar');
    if (!progressBar) return;

    window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
        progressBar.style.width = `${progress}%`;
    }, { passive: true });
}

// 2. Sticky Navigation
function initStickyNav() {
    const header = document.querySelector('header');
    if (!header) return;

    const scrollThreshold = 150; // pixels before nav becomes sticky

    window.addEventListener('scroll', () => {
        if (window.scrollY > scrollThreshold) {
            document.body.classList.add('scrolled');
        } else {
            document.body.classList.remove('scrolled');
        }
    }, { passive: true });
}

// 3. Mobile Hamburger Menu
function initMobileMenu() {
    const hamburger = document.querySelector('.hamburger');
    const mobileNav = document.querySelector('.mobile-nav');
    
    if (!hamburger || !mobileNav) return;

    hamburger.addEventListener('click', () => {
        const isExpanded = hamburger.getAttribute('aria-expanded') === 'true';
        hamburger.setAttribute('aria-expanded', !isExpanded);
        hamburger.classList.toggle('active');
        mobileNav.classList.toggle('open');
        document.body.classList.toggle('no-scroll');
    });
}

// 4. Theme Switcher
function initThemeSwitcher() {
    const themeToggles = document.querySelectorAll('.theme-toggle');
    if (themeToggles.length === 0) return;

    // Check localStorage or system preference
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    let currentTheme = savedTheme || (systemPrefersDark ? 'dark' : 'light');
    applyTheme(currentTheme);

    themeToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            currentTheme = currentTheme === 'light' ? 'dark' : 'light';
            applyTheme(currentTheme);
            localStorage.setItem('theme', currentTheme);
        });
    });

    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        const buttonText = theme === 'dark' ? 'MORNING EDITION' : 'NIGHT EDITION';
        themeToggles.forEach(toggle => {
            toggle.textContent = buttonText;
        });
    }
}

// 5. Smooth Scroll
function initSmoothScroll() {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    
    anchorLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            const targetId = link.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                
                // Close mobile menu if open
                const mobileNav = document.querySelector('.mobile-nav');
                const hamburger = document.querySelector('.hamburger');
                if (mobileNav && mobileNav.classList.contains('open')) {
                    mobileNav.classList.remove('open');
                    hamburger.classList.remove('active');
                    hamburger.setAttribute('aria-expanded', 'false');
                    document.body.classList.remove('no-scroll');
                }
                
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// 6. Active Nav Link
function initActiveNavObserver() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    
    if (sections.length === 0 || navLinks.length === 0) return;

    const observerOptions = {
        root: null,
        rootMargin: '-50% 0px -50% 0px', // Trigger when section crosses middle of viewport
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const currentId = entry.target.getAttribute('id');
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${currentId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        observer.observe(section);
    });
}

// 7. Counter Animation
function initCounterAnimation() {
    const counters = document.querySelectorAll('.stat-counter');
    if (counters.length === 0) return;

    const observerOptions = {
        threshold: 0.5
    };

    const animateCounter = (el) => {
        const target = parseInt(el.getAttribute('data-target') || el.textContent.replace(/[^0-9]/g, ''), 10);
        const duration = 2000; // ms
        const startTime = performance.now();
        const suffix = el.getAttribute('data-suffix') || '';
        
        const updateCounter = (currentTime) => {
            const elapsedTime = currentTime - startTime;
            const progress = Math.min(elapsedTime / duration, 1);
            
            // Easing function (easeOutExpo)
            const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
            
            const currentCount = Math.floor(easeProgress * target);
            el.textContent = currentCount + suffix;
            
            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            } else {
                el.textContent = target + suffix; // Ensure final value is exact
            }
        };
        
        requestAnimationFrame(updateCounter);
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                observer.unobserve(entry.target); // Animate only once
            }
        });
    }, observerOptions);

    counters.forEach(counter => {
        // Store initial text if data-target is not set
        if (!counter.hasAttribute('data-target')) {
            const text = counter.textContent;
            const number = parseInt(text.replace(/[^0-9]/g, ''), 10);
            const suffix = text.replace(/[0-9]/g, '');
            counter.setAttribute('data-target', number);
            if (suffix) counter.setAttribute('data-suffix', suffix);
        }
        counter.textContent = '0' + (counter.getAttribute('data-suffix') || '');
        observer.observe(counter);
    });
}

// 8. Typewriter Effect
function initTypewriter() {
    const typewriters = document.querySelectorAll('.typewriter');
    if (typewriters.length === 0) return;

    typewriters.forEach(el => {
        const text = el.textContent;
        el.textContent = '';
        el.style.opacity = 1;
        
        let i = 0;
        const speed = parseInt(el.getAttribute('data-speed') || 50, 10); // ms per character
        
        function typeWriter() {
            if (i < text.length) {
                el.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, speed);
            }
        }
        
        // Start typing after a short delay
        setTimeout(typeWriter, 500);
    });
}
