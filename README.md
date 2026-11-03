# Gopinath Gurusamy — architecture résumé

A static portfolio for a Dynamics 365 CE / Power Platform Solution Architect and Technical Lead. The site preserves the factual content of the previous portfolio and presents services, expertise, four engagements, five experience entries, certifications, writing, education, languages and contact details.

## Stack and design

Plain semantic HTML, custom CSS and small vanilla JavaScript enhancements. No framework runtime, remote fonts, analytics, backend, package installation or deployment build is required. All production assets are local, with relative paths for GitHub Pages project hosting. CSS and JavaScript use `?v=8`.

The design is a hand-port and substantial adaptation of [Astrofy by Manuel Ernesto Garcia](https://github.com/manuelernestog/astrofy): portrait rail, résumé timeline, rounded cards and light/dark surface hierarchy. The upstream [MIT license](https://github.com/manuelernestog/astrofy/blob/main/LICENSE), copyright 2022 Manuel Ernesto Garcia, is preserved verbatim in [LICENSE-TEMPLATE.md](LICENSE-TEMPLATE.md). A small voluntary footer credit links to the template. Typography, palette, responsive behavior and all portfolio content are customized; no sample claims or template profile images are used.

Eight candidate evaluations and source snapshots are in the companion workspace: `~/portfolio-src/TEMPLATE_RESEARCH.md` and `~/portfolio-src/templates/`. That workspace also contains the pre-redesign HTML backup and reproducible OG-image generator. It is not needed to serve the site.

## Files

- `index.html`: portfolio and SEO metadata, including five structured Microsoft credentials.
- `404.html`: matching error page; a small base-resolution script handles nested project-path URLs.
- `assets/css/styles.css`: responsive layout, themes, focus states and reduced-motion rules.
- `assets/js/main.js`: saved theme preference, email-copy feedback, current-section navigation and the flows counter.
- `assets/img/headshot.jpg`: original portrait; `og-image.png` is the regenerated 1200 × 630 social image, with an editable SVG companion.
- `assets/resume/Gopinath_Gurusamy_Resume.pdf`: existing CV, linked once from the header.
- `scripts/verify.py`: local-reference, credential, content, image and privacy checks.
- `qa-artifacts/v2-*`: current redesign evidence. Other artifact names belong to earlier versions.

PL-600 is plain text. The two supplied Microsoft Learn verification destinations are retained. Phone contact information is excluded from site text; the existing CV is the sole exception.

## Preview and verify

From the repository root:

```sh
python3 -m http.server 8092 --bind 127.0.0.1
python3 scripts/verify.py
node --check assets/js/main.js
npx html-validate@10.17.0 index.html 404.html
```

The companion `~/portfolio-src/serve-preview7.py` can instead run the local server with a `/gopinath-portfolio/` prefix and Pages-like nested 404 behavior. It uses the same port. Run only one preview server at a time.

Themes follow the system preference until the visitor selects light or dark. The selection persists when browser storage is available. Navigation and content remain usable without JavaScript. CSS disables transitions and smooth scrolling for reduced-motion preferences. No data is submitted by the email links; they open the visitor's email app.

The national healthcare programme figure is **100+ Power Automate flows**. The delivery stat and case study use this owner-corrected count. Its source text and accessible name retain 100+; the stat animates to 100+ when visible, with CSS loaded and reduced motion off. Without CSS, JavaScript or animation support, the final count remains readable. The about text, SEO/OG/Twitter descriptions, Person JSON-LD and social image contain no flows count to correct. `scripts/verify.py` rejects stale flows wording and checks the visible, accessible and animation values. Brief 8 Chrome evidence and refreshed light screenshots are recorded in [E2E_REPORT.md](E2E_REPORT.md).

## Deployment

GitHub Pages serves **main / repository root** at https://gopinath29.github.io/gopinath-portfolio/. Keep `.nojekyll`, `index.html`, `404.html`, assets, favicon files, robots and sitemap at the root. There is no Actions workflow or build step to configure. Deployment occurs through the repository's existing publishing process after its owner commits and pushes the reviewed static files.

This task did not commit, push or deploy. The live site is not evidence of this local redesign. See [E2E_REPORT.md](E2E_REPORT.md) and [VERIFICATION.md](VERIFICATION.md) for results and test limitations.
