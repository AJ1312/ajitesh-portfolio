# The Sharma Dispatch — Portfolio Website

> *The Engineering Record of a Systems Builder*

A newspaper-inspired editorial portfolio website for **Ajitesh Sharma**, styled after The Indian Express broadsheet aesthetic with interactive fluid-scroll animations.

## 🗞️ Live Preview

Open `index.html` in your browser, or serve locally:

```bash
npx serve .
```

## 🏗️ Architecture

```
ajitesh-portfolio/
├── index.html              # Main broadsheet homepage
├── css/styles.css          # Complete design system (1200+ lines)
├── js/
│   ├── main.js             # Core interactions, nav, theme switcher
│   ├── animations.js       # GSAP ScrollTrigger scroll animations
│   └── simulations.js      # 4 interactive simulations
├── pages/
│   ├── cipherpulse.html    # DPI Engine deep-dive + particle sim
│   ├── sentinel-stream.html # Anomaly detection + SOC dashboard
│   ├── snapseat.html       # DevOps platform + CI/CD pipeline viz
│   ├── nutrivision.html    # AI dietary intel + live demo
│   ├── internship.html     # Hindalco internship + queue sim
│   ├── paper-compsac.html  # IEEE COMPSAC paper presentation
│   ├── patents.html        # 3 Indian patent architectures
│   └── certifications.html # Certification gallery
└── images/
    ├── portrait.jpg
    └── patents/
        ├── cognitive-security.jpg
        ├── audio-deepfake.jpg
        └── lipsync-detection.jpg
```

## ✨ Features

- **Newspaper-style editorial design** inspired by The Indian Express & Robert Tran
- **GSAP ScrollTrigger** fluid scroll animations
- **4 Interactive Simulations**: DPI particle network, anomaly dashboard, CI/CD pipeline, queue manager
- **Dark mode** ("Night Edition" toggle)
- **Responsive** mobile-first design
- **Hand-drawn patent architecture diagrams**
- **MathJax equations** for IEEE paper presentation

## 🛠️ Tech Stack

- HTML5, CSS3, Vanilla JavaScript
- GSAP + ScrollTrigger (CDN)
- Google Fonts: Playfair Display, Inter, JetBrains Mono
- MathJax (for paper equations)

## 👤 Contact

- **Email**: 13ajitesh@gmail.com
- **LinkedIn**: [linkedin.com/in/ajitesh-sharma](https://linkedin.com/in/ajitesh-sharma)
- **GitHub**: [github.com/AJ1312](https://github.com/AJ1312)

---

*Hand-set in Playfair and Inter. © 2026 Ajitesh Sharma. All rights reserved.*
