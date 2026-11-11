# Portfolio v5 verification — 11 November 2026

## Light-theme rocket follow-up

Home and 404 now use two original small SVG rockets with five fading smoke puffs and a flickering nozzle flame each. The three clouds, dark scene, new-tab links and CV query remain intact. CSS/JS use `?v=18`. Scenery remains decorative, fixed, pointer-transparent and behind content; reduced motion hides it, inactive scenes do not render, and hidden-document timelines pause and resume.

The complete local suite passed: word count (1,243 total, 350 Work), static/privacy verifier, 44 verifier regressions, JavaScript syntax, HTML validation, 242 DOM assertions, 909 external-runner assertions and 961 repository browser assertions. Both headless Chromium suites covered both themes at 1440/1280/768/390, seven extra widths, reduced motion, simulated hidden-document pause/resume, accessibility, new-tab behaviour, terminal interactions and home/404 navigation. Rocket checks confirm flight direction, elapsed-time smoke drift/fading and flame flicker on both pages. No page/request errors or motion-related layout shifts were reported; text contrast minimum remains 4.55:1. The repository suite also retained dark-star and shooting-trail pixel checks.

The visually inspected desktop screenshot is `/Users/gopinathgurusamy/portfolio-burst/logs/portfolio-rockets-light.png`. Only browser animation time was sought and paused for this still; production delays and opacity were preserved. A screenshot comparison confirms visible smoke pixels behind the rocket. Results remain in `qa-artifacts/v5-playwright-results.json` and `qa-artifacts/v5-stars-chromium-results.json`; run logs and screenshot evidence are outside the repo in `portfolio-burst/logs/rockets-*.log` and `rockets-screenshot-evidence.json`. No user Chrome app/profile was used. Earlier evidence below describes prior revisions; deployment and production routing are not asserted by these local checks.

**PASS: requested local V5 acceptance checks complete.** The page has **1,211 words**, down from **2,038**; Selected Work is **350 words**. The GG follow-up removes two header words. Full section counts, screenshots and evidence are in [E2E_REPORT.md](E2E_REPORT.md).

| Requirement | Current result |
| --- | --- |
| Work | Case Assistant first, problem/outcome/four short topics/tech; four other real case studies retained; 350 words total |
| AI & Copilot | Four configured D365 features, Work link, no repeated topics or credential verify links; 41 words |
| Products | Six distinct capability lines; no 100+ repetition on Power Automate card |
| Header | Photo + bold Sora GG on home/404, desktop/mobile, both themes; exact accessible names include GG, full name and destination; inherited masthead ink |
| Hero | One tagline, name/role/portrait/featured-work pointer, single plain PL-600 + linked AB-100 pair and CTAs |
| Metrics / privacy | 100+ visible and accessible, including reduced motion/no JS; repo text, PDF text and filename privacy scan PASS |
| About / Career | Education/languages moved into About; same five employers, dates, roles and locations; all five native disclosures start collapsed; Codec click, Enter/Space, related links and initial/hashchange targeting PASS |
| Credentials / CV | Supplied AB-100/AB-620 Learn links in Credentials; PL-600 unlinked; exactly one Download CV, in header; public recruiter PDF at `?v=15`, original filename retained |
| V4 design | Sky/navy, teal accents, glass cards, local fonts, portrait arrangement and cloud/plane/star/shooting-star scenery retained |
| Layout | Both themes at 1440/1280/768/390, DPR 1; no overflow or clipped headshot; expanded career records fit; seven extra widths pass |
| Theme / motion | Toggle and persistence PASS; matching scene only; scenery off under reduced motion; final 100+ remains; simulated hidden timelines pause/resume |
| Terminal | help, pac certs, pac contact, pac projects, pac copilot, clear PASS in both themes at desktop/mobile and reduced-motion mobile; privacy PASS |
| Contrast / accessibility | Targeted text minimum 4.55:1 in both themes; zero reported axe A/AA violations across eight expanded samples |
| Local 404 | v16 bootstrap/assets, theme/scenery, layout and return navigation PASS at 1440/390 both themes |
| Tests | 547 V5 runner assertions plus 599 `scripts/test-browser.cjs` assertions, 73 DOM assertions, 30 verifier regressions, static verifier, HTML validation and JavaScript syntax PASS |
| Operations | GG header and default-collapsed Codec follow-up on main; v16 CSS/JS; headless Playwright Chromium only; runner/dependencies/cache outside repo; preview 8093; other named ports untouched |

The CV swap preserves the source PDF bytes: SHA-256 `30c6cac33050f60189a6090bba26c89904fbae630d29b8f90b0d0eb606f18746`. The repository tree contains exactly one PDF, at `assets/resume/Gopinath_Gurusamy_Resume.pdf`, and no copy of the old PDF bytes. Poppler extraction confirms the required name, email, credentials, Case Assistant and Codec Ireland text, with no phone number or private client name. Both rendered pages were inspected. The headless browser download has the same SHA-256 and retains `Gopinath_Gurusamy_Resume.pdf`. Poppler setup is documented in README.md.

## Evidence and reproduction

- `qa-artifacts/gg-header-word-counts.json`: current 1,211-word count, including all disclosure content and both responsive menus; `v5-word-counts.json` retains the earlier trim comparison.
- `qa-artifacts/v5-playwright-results.json`: 547 browser assertions, contrast/layout/motion and interaction evidence.
- `qa-artifacts/v5-{1440,1280,768,390}-{light,dark}.png`: eight DPR 1 top captures; desktop light header and mobile light/dark inspected.
- `qa-artifacts/v5-1440-full-light.png`: full light page; current desktop header and mobile light/dark captures inspected.
- `/Users/gopinathgurusamy/portfolio-burst/logs/portfolio-gg-header.png`: inspected light-theme desktop header crop.
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
NODE_PATH=/private/tmp/portfolio-v3-pw/node_modules PLAYWRIGHT_BROWSERS_PATH=/private/tmp/portfolio-v3-pw/browsers node scripts/test-browser.cjs
```

Chromium launches headlessly with `--single-process --no-zygote`; no user Google Chrome app/profile or computer-use tool was used. The owned preview remains on 8093; ports 8080 and 8765 were not used or stopped. Served index bytes match the checkout.

Deployment, current external-link availability, production nested-404 routing, other engines, assistive technology and physical devices remain unverified. Hidden-document tests are simulated. Axe marks gradient contrast incomplete; conservative compositing and visual review supplement it, without formal accessibility certification. The public recruiter CV replaces the earlier binary CV; PDF text now passes through Poppler and the privacy verifier. Missing Poppler or failed extraction fails verification. Earlier V3/V4 report sections and artifacts are historical.
