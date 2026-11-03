# Portfolio redesign E2E report

## Brief 8 follow-up — 3 November 2026

PASS: the national healthcare programme figure is **100+ Power Automate flows** in the visible stat, its accessible name, `data-count`, `data-target` and healthcare case study. The about copy, SEO/OG/Twitter descriptions, Person JSON-LD and editable/raster social images contain no flows figure. Other metrics and the Brief 7 design remain intact.

The flows stat now has a small intersection-triggered animation; it retains the final value as source text and a stable accessible name. In native Chrome DevTools, a mutation observer recorded intermediate values from 3 through 100, finishing at `100+`. The normal 1440 × 900 and 390 × 844 light layouts have no horizontal overflow. With all stylesheets disabled, Chrome reports zero active stylesheets and the five stat values `13+`, `9`, `4`, `~3,000`, `100+`, each once. Visual review confirms the corrected figure remains readable. The CSS marker gates animation; reduced motion and missing JavaScript retain the final value.

Refreshed top-of-page screenshots: [1440 light](qa-artifacts/v2-1440-light.png) and [390 light](qa-artifacts/v2-390-light.png). These are exact viewport crops from native Chrome screenshots with no resizing. Additional evidence: [desktop flows](qa-artifacts/brief8-1440-flows.png), [mobile flows](qa-artifacts/brief8-390-flows.png), [CSS disabled](qa-artifacts/brief8-no-css.png), and `qa-artifacts/brief8-results.json`. Chrome's browser connector host was unavailable; all browser checks used its native UI/DevTools. Earlier v2 evidence except the two refreshed screenshots remains the Brief 7 baseline.

PASS: `python3 scripts/verify.py`, `node --check assets/js/main.js`, and `html-validate` 10.17.0 on both pages. Eight isolated verifier mutations also pass: seven incorrect stat/content/metadata cases are rejected and an unrelated 20+ figure is accepted. No commit, push or deployment was performed. The wider Brief 7 checks below are retained as historical results; this follow-up retests the corrected metric and affected layouts.

Completed 3 November 2026 with connected Chrome on local port 8092. The test server also simulates the GitHub Pages project prefix and serves the real 404 document for missing nested paths. Headless Chromium was not used. No git command, commit, push or deployment was performed; the reserved port was not used or stopped.

## Template and scope

Selected [Astrofy](https://github.com/manuelernestog/astrofy), MIT, copyright 2022 Manuel Ernesto Garcia. The complete license is retained in `LICENSE-TEMPLATE.md`. Eight candidates, their exact license sources, tradeoffs and selection rationale are recorded in `~/portfolio-src/TEMPLATE_RESEARCH.md`.

The site hand-ports Astrofy's portrait rail, navigation, card hierarchy and resume timeline into plain static HTML/CSS/JavaScript. It adds editorial typography, warm light and forest dark palettes, a matching 404, new favicon assets and a regenerated 1200 × 630 OG PNG. All original factual text is preserved; the source comparison found zero missing content nodes after removing section-number prefixes and replacing the monogram. No new employer, client, date or metric was introduced.

## Issues found and resolved

- The desktop portrait rail's final navigation link was slightly below the 900-pixel window. A compact rule reduces portrait size and navigation spacing for shorter desktop windows. Final retest: navigation bottom is 812.25px at both 1440 and 1280 widths; every rail link fits.
- The previous counter implementation depended on CSS-generated visual values. Brief 7 replaced it with source text; Brief 8 adds a flows-only animation while retaining the final source value and stable accessible name.
- The browser requested a default favicon in addition to the SVG. A matching local ICO fallback now resolves.
- Browser resizing could return stale media-query layout measurements until reload. Final viewport results were collected after a fresh page load at each size, then screenshots regenerated. This was a test-harness observation, not a site change.

No unresolved website defect remains in the completed checks.

## Section and content review

Inspected header, portrait/navigation, hero, About and all four services, five statistics, four expertise groups and engineering note, all four engagements, all five experience entries, all seven certification cards plus additional certifications, Writing, education/languages, Contact, footer and the 404.

All 25 portfolio links and two buttons were inventoried. The 404 adds three links and one theme button. Internal anchors exist; main navigation, exploration, brand return, footer return and skip links were exercised. The main skip moves focus to `main` and renders a solid focus outline; the 404 skip targets its own `main`. Both 404 home links return to `/gopinath-portfolio/`. Links have real hrefs and semantic controls; no placeholder links were found. Mailto addresses were validated without sending email. The license file was checked by HTTP rather than downloaded.

PL-600 appears once in the hero as plain text and once in its certification card, with no link or link styling. AB-100 appears once in the hero and has its supplied verification URL there and in Certifications. AB-620 uses its supplied verification URL. No featured credentials appear on the portrait. Download CV appears exactly once, in the header. Prohibited availability text, numbered section labels and phone details are absent from production page content. The existing CV is the sole phone-data exception.

The original title, description, canonical URL, OG/Twitter metadata and five Person credentials are preserved. Social image dimensions are exactly 1200 × 630. All production asset paths are relative; both pages load local CSS/JS with `?v=8`.

## Layout and images

| Viewport | Light | Dark | Horizontal overflow | Portrait / rail |
| --- | --- | --- | --- | --- |
| 1440 × 900 | [Screenshot](qa-artifacts/v2-1440-light.png) | [Screenshot](qa-artifacts/v2-1440-dark.png) | None in either theme | PASS |
| 1280 × 900 | [Screenshot](qa-artifacts/v2-1280-light.png) | [Screenshot](qa-artifacts/v2-1280-dark.png) | None in either theme | PASS |
| 768 × 1024 | [Screenshot](qa-artifacts/v2-768-light.png) | [Screenshot](qa-artifacts/v2-768-dark.png) | None in either theme | PASS |
| 390 × 844 | [Screenshot](qa-artifacts/v2-390-light.png) | [Screenshot](qa-artifacts/v2-390-dark.png) | None in either theme | PASS |

The headshot loads at intrinsic 400 × 400, with nonempty alt text, eager loading, fetch priority and a rounded frame. It stays fully inside its container at every tested size. Main content contains no clipped or overlapping sections in the full-page review.

The nested 404 also has no horizontal overflow at all four dimensions in both themes. Its CSS/JS resolve beneath the project prefix. Missing paths return HTTP 404 and the real error-page content; the return links reach the portfolio. Direct `404.html` also works.

Required screenshots are present: `v2-1440-light.png`, `v2-1440-dark.png`, `v2-1280-light.png`, `v2-768-light.png`, `v2-390-light.png`, `v2-390-dark.png`, plus [full-page light](qa-artifacts/v2-1440-full-light.png). Extra dark/full-page, tablet and 404 screenshots are included. PNGs were converted from the connected Chrome JPEGs without resizing. The browser capture backend can omit scrollbar space and apply capture scaling; actual test-window dimensions are recorded in the layout JSON rather than inferred from image dimensions.

## Controls, themes and accessibility

Theme toggles change rendered colors and accessible labels/pressed state. Both preferences persist after reload, and the same preference carries to the 404 and back. System dark preference is currently true in Chrome; code and CSS use the system preference when no explicit selection is stored. Storage failures have a fallback. Reduced-motion CSS disables transitions and smooth scrolling. OS media preferences were not altered or force-emulated.

Targeted contrast measurement covered 223 visible text runs per theme against their rendered surface backgrounds. Minimum ratios: 5.27:1 light and 6.46:1 dark, with zero failures below 4.5:1. Semantic header/aside/navigation/main/footer landmarks, descriptive image alt, heading hierarchy, skip links and visible focus states are present. This is not a full WCAG conformance certification.

Copy email resolves and displays `Copied!` plus the live success announcement. Exact clipboard readback is unverified: the browser clipboard read returned empty and the paste automation did not complete. No copy-handler exception or site defect was established.

A temporary Brief 7 fixture omitted every site stylesheet and inline site style. Reviewed 140 text blocks plus the raw body text, including `Gopinath Gurusamy`, headings, credential labels and `English Professional Tamil Native`. All five statistics appeared once. Chrome's own injected opacity style remained; no site styles were loaded. No unintended word joins or new typos were identified. Both temporary QA fixtures were removed. Brief 8 repeats the flows check with every stylesheet disabled and confirms the corrected `100+` value, as recorded above.

## External destinations

All checks followed redirects with curl and a Chrome user agent. Neither LinkedIn nor WordPress was bot-blocked in this run; both were also opened in Chrome and confirmed as the intended profile/blog.

| Destination | HTTP | Result |
| --- | --- | --- |
| https://github.com/Gopinath29 | 200 | PASS |
| https://github.com/manuelernestog/astrofy | 200 | PASS |
| https://gopinathgurusamy.wordpress.com/ | 200 | PASS |
| https://learn.microsoft.com/en-us/users/gopinathgurusamy-9343/credentials/33c24ca4ad0be38e | 200 | PASS |
| https://learn.microsoft.com/en-us/users/gopinathgurusamy-9343/credentials/71c8c88020980655 | 200 | PASS |
| https://www.linkedin.com/in/gopinath-gurusamy | 200 | PASS |
| https://x.com/GopinathGuru1 | 200 | PASS |

Duplicate external anchor occurrences share these verified destinations. Both supplied Learn URLs remain exact and use the expected new-tab/noopener behavior. All local resource HEAD checks pass, including versioned styles/scripts, portrait, favicon, license and CV. Project-prefixed OG PNG, robots, sitemap, home and direct 404 also return 200.

## Link inventory

| Portfolio label | Destination | Verification |
| --- | --- | --- |
| Skip to content | `#main` | Anchor exists / exercised |
| Gopinath Gurusamy, back to top | `#top` | Anchor exists / exercised |
| Download CV ↓ | `assets/resume/Gopinath_Gurusamy_Resume.pdf` | Target/HTTP PASS; browser download blocked |
| About | `#about` | Anchor exists / exercised |
| Expertise | `#expertise` | Anchor exists / exercised |
| Work | `#work` | Anchor exists / exercised |
| Experience | `#experience` | Anchor exists / exercised |
| Certifications | `#certifications` | Anchor exists / exercised |
| Writing | `#writing` | Anchor exists / exercised |
| Contact | `#contact` | Anchor exists / exercised |
| Microsoft Certified · AB-100 · Agentic AI Business Solutions Architect Expert — verify (opens in a new tab) | `https://learn.microsoft.com/en-us/users/gopinathgurusamy-9343/credentials/71c8c88020980655` | HTTP PASS |
| Get in touch ↗ | `mailto:itiangopi@gmail.com` | Address validated |
| LinkedIn ↗ | `https://www.linkedin.com/in/gopinath-gurusamy` | HTTP PASS |
| ↓ Explore my work | `#about` | Anchor exists / exercised |
| Verify AB-100 on Microsoft Learn (opens in a new tab) | `https://learn.microsoft.com/en-us/users/gopinathgurusamy-9343/credentials/71c8c88020980655` | HTTP PASS |
| Verify AB-620 on Microsoft Learn (opens in a new tab) | `https://learn.microsoft.com/en-us/users/gopinathgurusamy-9343/credentials/33c24ca4ad0be38e` | HTTP PASS |
| The blog Notes on Dynamics 365 & Power Platform Read the blog ↗ { } | `https://gopinathgurusamy.wordpress.com/` | HTTP PASS |
| itiangopi@gmail.com ↗ | `mailto:itiangopi@gmail.com` | Address validated |
| LinkedIn ↗ | `https://www.linkedin.com/in/gopinath-gurusamy` | HTTP PASS |
| X ↗ | `https://x.com/GopinathGuru1` | HTTP PASS |
| GitHub ↗ | `https://github.com/Gopinath29` | HTTP PASS |
| Blog ↗ | `https://gopinathgurusamy.wordpress.com/` | HTTP PASS |
| Back to top ↑ | `#top` | Anchor exists / exercised |
| Astrofy | `https://github.com/manuelernestog/astrofy` | HTTP PASS |
| MIT license | `LICENSE-TEMPLATE.md` | HTTP PASS |

404 links: Skip to content → current error URL plus `#main`; brand home and Back to portfolio → project root. All were exercised successfully. Its theme toggle was tested in both states and all requested dimensions.

## Final validation and evidence

- `python3 scripts/verify.py`: PASS, including query-aware local refs, anchors, prohibited content, exact credential URLs, five structured credentials, hero/headshot checks, unlinked PL-600, header-only CV, v8 assets, PNG dimensions and repository text privacy scan.
- `node --check assets/js/main.js`: PASS.
- `html-validate` 10.17.0 on both HTML documents: PASS.
- Connected Chrome diagnostics filtered to the local origin: no warnings or errors captured during final checks. The deliberately missing nested URL correctly returns 404.
- Current viewport override was reset after testing. Template source and generation scripts remain in `~/portfolio-src`, outside the public static root.

Evidence: `v2-content-preservation.json`, `v2-dom-audit.json`, `v2-anchor-clicks.json`, `v2-layout-results.json`, `v2-404-results.json`, `v2-no-css-text.json`, `v2-interaction-results.json`, `v2-contrast.json`, `v2-external-links.json`, `v2-external-browser.json`, `v2-local-http.json`, `v2-final-browser.json`, all beneath `qa-artifacts/`. Artifacts without the v2 prefix belong to previous versions and are not evidence for this redesign.

## Verification limits

Automatic approval review rejected the CV browser download because localhost download permission was declined. No alternative download or permission bypass was attempted. The existing local file has a valid PDF signature and its response is HTTP 200 with `application/pdf`; completed browser downloads are not claimed. Clipboard contents have the separate automation limit described above. Live GitHub Pages deployment was neither changed nor retested.

The redesign, static delivery, requested screenshots, documentation and available verification are complete. Sixteen requested page/theme/viewport combinations pass without horizontal overflow, and all seven unique external destinations return 200. The two interaction verification limits are explicit; neither is represented as a completed browser operation.

E2E SUMMARY
