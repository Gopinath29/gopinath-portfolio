# Portfolio v4 verification — 11 November 2026

**PASS: all requested local V4 acceptance checks are complete.** Detailed evidence, contrast tokens, fixes and preserved V3 notes are in [E2E_REPORT.md](E2E_REPORT.md).

| Requirement | Current result |
| --- | --- |
| Original animated background | Light: three drifting clouds and two planes; dark: 28 twinkling stars and two occasional shooting trails; original SVG/CSS only |
| Layering and performance | Fixed below content, pointer-transparent, no layout contribution; transform/opacity only; no JavaScript render loop |
| Hero | Compact portrait rail, wide headline, separate credential/action band; horizontal portrait identity card on phones; top-aligned photo inside frame |
| Accents | Light `#075d73` / ink `#064c60`; dark `#80ded5` / highlight `#73dbdf`; links, controls and focus updated |
| Theme switching | Background and accent switch together, no inactive scene rendering; saved selection survives reload; unsaved system changes work |
| Reduced motion | Entire scenery layer hidden and all animations removed, including initial load and live preference changes; final 100+ retained |
| Hidden document | Simulated hidden/visibilitychange pauses every CSS timeline; measured times stop and advance again on resume |
| Layout | No overflow at 1440/1280/768/390 in either theme, including expanded records; seven extra widths pass; 0 px delta against reduced-motion baseline |
| Content and privacy | Case Assistant first, AI & Copilot, six product cards, five JSON-LD credentials, supplied Learn links, header-only CV, plain PL-600, 100+ flows; repository scan clear |
| Terminal | help, pac certs, pac contact, pac projects, pac copilot, clear; browser keyboard tests in both themes and mobile reduced motion; output privacy checked |
| Contrast | All text minimum 4.55:1 in both themes; links at least 4.70:1 light / 5.90:1 dark; tested UI boundaries at least 4.70:1 / 6.23:1 |
| Accessibility | No reported axe A/AA violations in eight expanded index samples; gradient contrast remains incomplete in axe, supplemented by conservative compositing and visual review |
| 404 | Shared scenery and v12 bootstrap work; local return link, no overflow and targeted contrast pass in both themes at 1440/390 |
| Browser results | 407 main and 12 supplemental assertions PASS; zero page/request errors; headless Playwright Chromium 158.0.8127.18 |
| Static checks | Verifier PASS; 9 verifier regressions; 55 DOM assertions; JavaScript syntax and HTML validation PASS |
| Operations | No commit or `.git` operations; CSS/JS cache queries v12; dependencies outside repo; preview only 8093; ports 8080 and 8765 untouched |

## Evidence

- `qa-artifacts/v4-playwright-results.json` — current browser results, contrast samples and pause/layout evidence.
- `qa-artifacts/v4-motion-details.json` and `v4-motion-detail-runner.cjs` — animation-phase samples and all five final counter values.
- `qa-artifacts/v4-playwright-runner.cjs` — reproducible headless runner using dependencies outside the repo.
- `qa-artifacts/v4-{1440,1280,768,390}-{light,dark}.png` — eight DPR 1 top captures, all inspected.
- `qa-artifacts/v4-1440-full-light.png` — full light page, 1440 × 12298, inspected throughout.

```sh
python3 -m http.server 8093 --bind 127.0.0.1
```

In another terminal, with the cached dependencies available:

```sh
python3 scripts/verify.py
python3 scripts/test-verifier.py
node --check assets/js/main.js
NODE_PATH=/private/tmp/portfolio-v3-test/node_modules node scripts/test-interactions.cjs
npm exec --cache /private/tmp/portfolio-v3-pw/npm-cache --yes --package html-validate@10.17.0 -- html-validate index.html 404.html
NODE_PATH=/private/tmp/portfolio-v3-pw/node_modules PLAYWRIGHT_BROWSERS_PATH=/private/tmp/portfolio-v3-pw/browsers node qa-artifacts/v4-playwright-runner.cjs
NODE_PATH=/private/tmp/portfolio-v3-pw/node_modules PLAYWRIGHT_BROWSERS_PATH=/private/tmp/portfolio-v3-pw/browsers node qa-artifacts/v4-motion-detail-runner.cjs
```

Chromium launches headlessly with `--single-process --no-zygote`. No user Google Chrome app/profile or computer-use tool was used. The owned QA server was stopped after verification. Deployment, current external-link availability, production nested-404 routing, other engines, assistive technology and physical devices remain unverified. Hidden-tab testing is simulated; contrast verification is targeted and is not formal certification. Preserved V3 results in the report remain historical evidence.
