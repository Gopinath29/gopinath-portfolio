# Portfolio v5 verification — 11 November 2026

**PASS: requested local V5 acceptance checks complete.** The page has **1,213 words**, down from **2,038**; Selected Work is **350 words**. Full before/after section counts, screenshots and evidence are in [E2E_REPORT.md](E2E_REPORT.md#v5--content-trim-preserved-v4-design--11-november-2026).

| Requirement | Current result |
| --- | --- |
| Work | Case Assistant first, problem/outcome/four short topics/tech; four other real case studies retained; 350 words total |
| AI & Copilot | Four configured D365 features, Work link, no repeated topics or credential verify links; 41 words |
| Products | Six distinct capability lines; no 100+ repetition on Power Automate card |
| Hero | One tagline, name/role/portrait/featured-work pointer, single plain PL-600 + linked AB-100 pair and CTAs |
| Metrics / privacy | 100+ visible and accessible, including reduced motion/no JS; repo text and filename privacy scan PASS |
| About / Career | Education/languages moved into About; same five employers, dates, roles and locations with concise responsibilities |
| Credentials / CV | Supplied AB-100/AB-620 Learn links in Credentials; PL-600 unlinked; exactly one Download CV, in header |
| V4 design | Sky/navy, teal accents, glass cards, local fonts, portrait arrangement and cloud/plane/star/shooting-star scenery retained |
| Layout | Both themes at 1440/1280/768/390, DPR 1; no overflow or clipped headshot; expanded career records fit; seven extra widths pass |
| Theme / motion | Toggle and persistence PASS; matching scene only; scenery off under reduced motion; final 100+ remains; simulated hidden timelines pause/resume |
| Terminal | help, pac certs, pac contact, pac projects, pac copilot, clear PASS in both themes at desktop/mobile and reduced-motion mobile; privacy PASS |
| Contrast / accessibility | Targeted text minimum 4.55:1 in both themes; zero reported axe A/AA violations across eight expanded samples |
| Local 404 | v13 bootstrap/assets, theme/scenery, layout and return navigation PASS at 1440/390 both themes |
| Tests | 407 browser assertions, 55 DOM assertions, 18 verifier regressions, static verifier, HTML validation and JavaScript syntax PASS |
| Operations | No commit or .git access/modification; v13 CSS/JS; headless Playwright Chromium only; runner/dependencies/cache outside repo; preview 8093; other named ports untouched |

## Evidence and reproduction

- `qa-artifacts/v5-word-counts.json`: identical before/after counting method; all disclosure content and both responsive menus included.
- `qa-artifacts/v5-playwright-results.json`: 407 browser assertions, contrast/layout/motion and interaction evidence.
- `qa-artifacts/v5-{1440,1280,768,390}-{light,dark}.png`: eight DPR 1 top captures, visually inspected.
- `qa-artifacts/v5-1440-full-light.png`: 1440 × 10590 full light page, inspected throughout.
- `/private/tmp/portfolio-v3-pw/v5-playwright-runner.cjs`: current headless runner; Chromium cache and dependencies beside it, outside the repo.

With `python3 -m http.server 8093 --bind 127.0.0.1` serving this checkout:

```sh
python3 scripts/word-count.py
python3 scripts/verify.py
python3 scripts/test-verifier.py
node --check assets/js/main.js
NODE_PATH=/private/tmp/portfolio-v3-test/node_modules node scripts/test-interactions.cjs
npm exec --cache /private/tmp/portfolio-v3-pw/npm-cache --yes --package html-validate@10.17.0 -- html-validate index.html 404.html
PLAYWRIGHT_BROWSERS_PATH=/private/tmp/portfolio-v3-pw/browsers node /private/tmp/portfolio-v3-pw/v5-playwright-runner.cjs
```

Chromium launches headlessly with `--single-process --no-zygote`; no user Google Chrome app/profile or computer-use tool was used. The owned preview remains on 8093; ports 8080 and 8765 were not used or stopped. Served index bytes match the checkout.

Deployment, current external-link availability, production nested-404 routing, other engines, assistive technology and physical devices remain unverified. Hidden-document tests are simulated. Axe marks gradient contrast incomplete; conservative compositing and visual review supplement it, without formal accessibility certification. The unchanged binary CV is outside the UTF-8 privacy scan. Earlier V3/V4 report sections and artifacts are historical.
