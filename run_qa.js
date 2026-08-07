const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const pagesToTest = [
    { name: 'index', url: 'http://localhost:8080/index.html' },
    { name: 'sentinel-stream', url: 'http://localhost:8080/pages/sentinel-stream.html' },
    { name: 'cipherpulse', url: 'http://localhost:8080/pages/cipherpulse.html' },
    { name: 'snapseat', url: 'http://localhost:8080/pages/snapseat.html' },
    { name: 'nutrivision', url: 'http://localhost:8080/pages/nutrivision.html' },
    { name: 'internship', url: 'http://localhost:8080/pages/internship.html' },
    { name: 'patents', url: 'http://localhost:8080/pages/patents.html' },
    { name: 'paper-compsac', url: 'http://localhost:8080/pages/paper-compsac.html' },
    { name: 'certifications', url: 'http://localhost:8080/pages/certifications.html' }
];

(async () => {
    const browser = await chromium.launch();
    const results = {
        consoleErrors: [],
        failedRequests: [],
        brokenImages: [],
        pageStatuses: []
    };

    if (!fs.existsSync('qa_screenshots')) {
        fs.mkdirSync('qa_screenshots');
    }

    for (const p of pagesToTest) {
        console.log(`Auditing: ${p.name}`);
        const page = await browser.newPage();
        
        page.on('console', msg => {
            if (msg.type() === 'error') {
                results.consoleErrors.push({ page: p.name, text: msg.text() });
            }
        });

        page.on('requestfailed', request => {
            results.failedRequests.push({ page: p.name, url: request.url(), error: request.failure().errorText });
        });

        // Desktop Audit
        await page.setViewportSize({ width: 1280, height: 900 });
        const response = await page.goto(p.url, { waitUntil: 'networkidle' });
        
        results.pageStatuses.push({ page: p.name, status: response ? response.status() : 'NO_RESPONSE' });

        // Check broken images
        const images = await page.$$eval('img', imgs => imgs.map(img => ({ src: img.src, naturalWidth: img.naturalWidth })));
        for (const img of images) {
            if (img.naturalWidth === 0) {
                results.brokenImages.push({ page: p.name, src: img.src });
            }
        }

        await page.screenshot({ path: `qa_screenshots/${p.name}_desktop.png`, fullPage: true });

        // Mobile Audit
        await page.setViewportSize({ width: 375, height: 812 });
        await page.screenshot({ path: `qa_screenshots/${p.name}_mobile.png`, fullPage: true });

        await page.close();
    }

    await browser.close();
    fs.writeFileSync('qa_report.json', JSON.stringify(results, null, 2));
    console.log('QA Audit Complete! Results saved to qa_report.json.');
})();
