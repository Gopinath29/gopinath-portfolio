# Portfolio v3 follow-up verification — 10 November 2026

**PASS: the requested local headless Playwright/Chromium acceptance is complete.** See [E2E_REPORT.md](E2E_REPORT.md) for preserved design/token notes, detailed results, fixes and evidence limits.

| Requirement | Final outcome |
| --- | --- |
| Content and provenance | Case Assistant first; four original topics and delivery facts; six supported product cards; prior case studies and career records retained |
| Privacy | PASS; UTF-8 repository text and filename scan; the client name is not published; no phone or unsupported personal projects |
| Credentials, CV and flows | PASS; one header CV, unlinked PL-600, supplied Learn links; 100+ unchanged |
| Reference design | Exact measured token system retained; six side-by-side sheets inspected at 1440, 768 and 390 in both themes |
| Fonts and headshot | All local fonts loaded; corrected portrait crop visually inspected across required widths |
| Required index screenshots | Eight DPR 1 top captures at 1440/1280/768/390; full 1440 light page inspected |
| 404 screenshots | Four DPR 1 captures at 1440/390, both themes; corrected label contrast and return link |
| Overflow | None at the four required widths in either theme, including expanded details; seven additional breakpoints pass |
| Terminal | Browser keyboard tests pass for help, certs, contact, projects, copilot and clear; accurate/private output, focus and safe text |
| Theme | Both themes rendered; keyboard toggle persists across actual reloads in both directions |
| Reduced motion | Browser emulation passes in both themes; no running animations, automatic scrolling disabled, 100+ visible, commands work |
| Other browser interactions | Skip-to-main, linked career disclosure, actual clipboard copy and valid CV PDF download pass |
| Accessibility | Targeted text contrast has zero failures across 12 index/404 samples; index axe has zero reported A/AA violations in eight expanded samples; gradient contrast marked incomplete by axe |
| Static hosting | Relative v11 assets; 404 bootstrap at nested project-prefix path passes with intercepted Pages routing; deployed routing unverified |
| Static checks | Verifier PASS; six privacy regressions; 55 DOM assertions; HTML validation and JS syntax PASS |
| HTTP links | Earlier six-destination HTTP 200 audit retained; no destination changes in this completion pass |
| Repository operations | No commit, push, deployment or `.git` operations; no repo node_modules; preview on 8093; ports 8080 and 8765 untouched |

## Evidence and commands

- `qa-artifacts/v3-playwright-results.json` — PASS, 233 browser assertions, 12 samples, zero page/request errors.
- `qa-artifacts/v3-playwright-extra.json` — 14 extra width/theme combinations, skip-link keyboard checks and nested-404 bootstrap emulation.
- `qa-artifacts/v3-{1440,1280,768,390}-{light,dark}.png` — final top captures.
- `qa-artifacts/v3-1440-full-light.png` — final full page, 1440 × 12437.
- `qa-artifacts/v3-404-{1440,390}-{light,dark}.png` — final 404 captures.
- `qa-artifacts/v3-compare-{1440,768,390}-{light,dark}.png` — inspected comparison sheets; same-day reference captures reused.
- `qa-artifacts/v3-390-{work,credentials,terminal}-{light,dark}.png` — supplemental scrolled captures.

```sh
python3 scripts/verify.py
python3 scripts/test-verifier.py
node --check assets/js/main.js
npm exec --cache /private/tmp/portfolio-v3-pw/npm-cache --yes --package html-validate@10.17.0 -- html-validate index.html 404.html
NODE_PATH=/private/tmp/portfolio-v3-test/node_modules node scripts/test-interactions.cjs
NODE_PATH=/private/tmp/portfolio-v3-pw/node_modules PLAYWRIGHT_BROWSERS_PATH=/private/tmp/portfolio-v3-pw/browsers node qa-artifacts/v3-playwright-runner.cjs
NODE_PATH=/private/tmp/portfolio-v3-pw/node_modules PLAYWRIGHT_BROWSERS_PATH=/private/tmp/portfolio-v3-pw/browsers node qa-artifacts/v3-playwright-extra-runner.cjs
```

Playwright 1.65.0 runs cached Chromium 158.0.8127.18 headlessly with `--single-process --no-zygote`, using a fresh temporary profile per context. Dependencies and Chromium live outside the repo in `/private/tmp/portfolio-v3-pw`. The user's Google Chrome app/profile and computer-use tools were not used.

Remaining visual differences: framed JPEG, denser résumé content, different hero proportions and omitted reference artwork/particles. No deployment, production routing, other engine, screen-reader, touch/physical-device or live client-system testing is claimed. This is a targeted browser/accessibility check, not formal accessibility certification. Historical `v3-followup-*` observations and initial captures are superseded by the final evidence above.
