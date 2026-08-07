/**
 * The Sharma Dispatch - Clean, Instant Display Scripts
 * Disabled swoop-in displacement for clean, immediate, stable broadsheet rendering.
 */

document.addEventListener('DOMContentLoaded', () => {
    // Ensure all content is immediately visible with zero swoop-in delay
    const rvElements = document.querySelectorAll('.rv, .dispatch-card, .metric-card-styled, .step-card-item');
    rvElements.forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'none';
    });

    // Clean initial stamp rotation for broadsheet styling
    const stamps = document.querySelectorAll('.dispatch-card__stamp');
    stamps.forEach(stamp => {
        stamp.style.transform = 'rotate(-15deg)';
        stamp.style.transformOrigin = 'center center';
    });
});
