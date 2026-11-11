# Portfolio v3 follow-up — 10 November 2026

The v3 design retains solution storytelling, connected career records, a small command interface and restrained motion. This follow-up applies the reference’s visual language while preserving the existing portfolio structure and factual case-study content. HTML, CSS and JavaScript remain original. No reference implementation, copy, images, illustrations or assets were copied or vendored.

Implementation, automated checks and the requested **headless Playwright/Chromium acceptance pass are complete**. The earlier native Chrome limitation is superseded by the fresh browser evidence below. No user Chrome app, existing Chrome profile, computer-use tool or connected Chrome was used for this completion pass.

## Content and provenance

The featured project is now **Case Assistant**, with the subtitle **Copilot Studio agent for Dynamics 365 Customer Service**. The client is described only as **a regulatory body**. Related anchors, career links, terminal output, metadata, generator text, SVG, documentation, QA text and filenames were updated. The client name is not published. A final UTF-8 repository and filename scan finds zero matches for the private name; binary files are not interpreted as text, and `.git` is pruned before traversal.

All four topics, summary, one-liner, generative orchestration, restricted grounding, reusable user-context Power Automate flow, Assistant Action audit table, configured Dynamics 365 Copilot features, 10 knowledge articles, test-case load, Teams publication, Dataverse solution, source control, ALM runbook, flowcharts, test plan and technology list remain. The four earlier case studies and all five career records retain their factual descriptions, roles, dates and responsibilities. The earlier regulatory project is also described generically as a regulatory body.

AI & Copilot replaces the previous agent section with the four delivered Case Assistant topics, case summaries including custom fields, draft email replies, knowledge-grounded answers with citations, similar-case matching and the supplied AB-100 / AB-620 Learn links. The hero still contains one plain-text PL-600 / linked AB-100 pair. Download CV remains once in the header. The healthcare figure remains 100+ flows in visible, accessible and fallback text.

Six product cards cover Case Assistant / Copilot Studio, Power Automate, Dataverse, Dynamics 365 Customer Service, Power Apps and Power Pages. Their supporting facts come from the current site and `resume.txt`, `linkedin_update.md` and `profile_export_v2.txt` outside the repo. The current site’s 100+ flow figure takes precedence over the older source figure. Product accents and illustrative mono call lines introduce no new delivery claims. The local terminal adds `pac copilot`, documented by `help`; `pac projects` directs users to AI & Copilot as well as Work.

## Token source and typography

Tokens were extracted with curl from the **inline stylesheet at https://ramyachinnadurai.com/**. There is no external stylesheet URL in the retrieved page. The full declared light and dark token lists plus related measurements are saved at `~/portfolio-src/REFERENCE_TOKENS.md`, outside the repository.

| Token family | Light | Dark |
| --- | --- | --- |
| Background | `#7ec8ff` | `#081631` |
| Hero wash | `#a8dff6` | `#0d2247` |
| Surface | `#8fd0ff` | `#0b1d3d` |
| Text | `#0d2b4a` | `#eef5ff` |
| Secondary text | `#1a4670` | `#a8bad6` |
| Accent | `#0b5cc2` | `#8fc3ff` |
| Accent ink | `#08418a` | `#8fc3ff` |
| Highlight | `#1470d2` | `#39d0ff` |
| Glass | white at .62 opacity | `#13264c` at .62 opacity |
| Navigation | sky blue at .72 opacity | `#081631` at .72 opacity |

The exact reference shadow values and glass fills are applied, together with 18px general card radii, 26px product/solution panels, 14px primary actions, 64px navigation height, 20px navigation blur and 180% saturation. Heading sizes, negative tracking, chapter spacing, responsive insets and section heading rhythm follow the measured reference values. Original soft radial light complements the vertical sky wash.

Sora headings, Plus Jakarta Sans body text and JetBrains Mono labels, credentials and terminal are loaded from local variable TTF files obtained from the official Google Fonts repository. OFL notices are included. System fonts are fallbacks only. Native Chrome confirmed that all three font families were loaded. `404.html`, favicons and the regenerated 1200 × 630 social image share the new system. Local CSS/JS cache queries are now `?v=11` after the browser fixes; index, 404 bootstrap and `verify.py` agree.

## Comparison and iteration

All eight reference viewport screenshots were captured in native Chrome at DPR 1, together with the complete light reference page:

- `qa-artifacts/ref-1440-{light,dark}.png` — 1440 × 900.
- `qa-artifacts/ref-1280-{light,dark}.png` — 1280 × 900.
- `qa-artifacts/ref-768-{light,dark}.png` — 768 × 1024.
- `qa-artifacts/ref-390-{light,dark}.png` — 390 × 844.
- `qa-artifacts/ref-1440-full-light.png` — 1440 × 14462.

Four intermediate portfolio captures are labelled `v3-followup-initial-<width>-<theme>.png`, at 390 and 768 in both themes. These were inspected alongside the aligned reference captures. The palette, type families, raised controls and glass treatment are close. The comparison exposed a narrow-layout difference: the reference places its portrait before its story. Our CSS now follows that order below 960px, with compact portrait captions and a featured-work link. Original soft sky light and a subtle primary-button highlight were also added after the comparison.

Those refinements have now been recaptured and visually reviewed with headless Chromium. Final `v3-<width>-<theme>.png` files and `v3-1440-full-light.png` replace the missing acceptance evidence. Older v3 captures remain archived at `~/portfolio-src/qa-before-v3-followup`; the labelled initial captures are historical only.

Six side-by-side sheets, `qa-artifacts/v3-compare-{1440,768,390}-{light,dark}.png`, were written and visually inspected. The same-day reference captures remain valid for this comparison and their dimensions were checked; no recapture was needed. The palette, local type families, navigation, mono labels, glass fills and raised controls are consistent with the reference. Remaining visual gaps are the framed original JPEG versus its cut-out portrait, illustrated companion and particle treatment, plus denser résumé content and different hero text proportions. These are intentional content/art differences; no reference art or implementation was copied. The final 1440 light full page was reviewed in seven readable tiles, including cards, career records, product grid, AI, credentials, terminal and footer. No further overlap, clipped text or broken wrapping was found in the reviewed captures.

## Contrast and accessibility

The native contrast helper opens all disclosures temporarily and measures rendered text against composed translucent ancestor fills, testing both sky endpoints. Large text uses 3:1; normal text uses 4.5:1. This is a targeted AA check, not a formal accessibility certification.

The first light sample found certification register codes at 3.49:1 on the sky. The exact brand accent was preserved; adding the reference’s translucent glass fill behind the codes corrected the non-brand background. Subsequent 390 light and 768 light/dark samples reported **zero text-contrast failures**, no horizontal overflow, loaded fonts and a loaded headshot fully inside its frame. A high-contrast rim was later added to the theme-toggle thumb; it is now included in the accepted headless captures in both themes.

Earlier native observations remain in `qa-artifacts/v3-followup-browser-observations.json`. Fresh headless samples in `v3-playwright-results.json` cover all eight index viewports and four 404 viewports. The targeted composed-fill contrast helper reports zero failures after the fixes. The index also has zero reported axe WCAG A/AA violations in all eight samples with disclosures expanded. Axe marks gradient/translucency contrast as incomplete; the targeted helper and visual inspection supplement it, and this is not a formal accessibility certification. Semantic landmarks, alt text, labelled input, focus styles, live terminal log, native disclosures and reduced-motion rules remain. Physical keyboard events and real reduced-motion emulation passed in headless Chromium.

## Automated and HTTP verification

| Check | Result |
| --- | --- |
| `python3 scripts/verify.py` | PASS |
| `python3 scripts/test-verifier.py` | PASS, 6 assertions |
| `node --check assets/js/main.js` | PASS |
| html-validate 10.17.0, index and 404 | PASS |
| `scripts/test-interactions.cjs`, jsdom | PASS, 55 assertions |
| Repository-wide client text / filename scan | PASS, zero matches |
| Unsupported personal-project text scan | PASS, includes assets, documentation and QA text |
| Phone privacy, credentials, flows, CV and metadata | PASS |
| Six external link destinations | HTTP 200 for all |
| Local index, assets, fonts, CV and explicit 404 page | HTTP 200 |
| Project-prefix index and CSS | HTTP 200 |
| Nested missing project path | HTTP 404 with custom page |
| Social image | Original 1200 × 630 PNG generated and visually inspected |

The negative probes introduce encoded test values into a QA UTF-8 file and published text asset in turn, confirm a failing verifier, remove each temporary fixture and confirm a clean pass. No prohibited literal test fixture remains. The verifier keeps earlier checks and additionally requires Case Assistant first, the four topics and delivery facts, the new AI section and Learn links, six supported product cards, numbered double-slash labels and v10 assets. It continues to reject the previous single-slash Profile label.

DOM assertions cover command output, normalization, safe text rendering, bounded history, focus restoration, clear, final metrics, theme switching, saved/system preferences, storage errors, related career records and clipboard success/failure feedback. They do not establish native layout or physical keyboard behavior. HTTP evidence is in `v3-followup-link-audit.json` and `v3-followup-local-requests.json`; final command output is in `v3-followup-check-results.json`.

## Playwright / headless completion

Playwright 1.65.0, Chromium 158.0.8127.18, axe Playwright 4.13.0 and sharp 0.35.5 were installed in `/private/tmp/portfolio-v3-pw`, including a separate browser cache. There is no `node_modules` directory in the repository. The initial default launch failed at macOS Mach-port registration. Chromium's `--single-process --no-zygote` settings run within the available restrictions; each context gets a fresh browser because closing a single-process context ends that browser. Every browser launch was headless and used a temporary Playwright profile.

The repo is served by `python3 -m http.server 8093 --bind 127.0.0.1`; the served index was compared byte-for-byte with this repo before QA. Port 8080 was never used or killed; port 8765 was left alone. No commit, push, deployment or `.git` access/modification was performed.

### Final browser results

**PASS: 233 assertions**, 12 layout/contrast samples, zero page/request errors and zero reported index axe violations. Evidence: `qa-artifacts/v3-playwright-results.json`, with supplemental checks in `v3-playwright-extra.json`.

| Page | Viewports, DPR 1 | Themes | Result |
| --- | --- | --- | --- |
| Index | 1440 × 900, 1280 × 900, 768 × 1024, 390 × 844 | Light and dark | PASS; `scrollWidth` equals viewport width; fonts and headshot loaded |
| Index, all disclosures expanded | Same four viewports | Light and dark | PASS; no horizontal overflow; targeted contrast and axe checks |
| Explicit 404 | 1440 × 900, 390 × 844 | Light and dark | PASS; no overflow, targeted contrast and return link |
| Extra index breakpoints | 320, 360, 650, 960, 1000, 1100, 1200 wide | Light and dark | PASS; no horizontal overflow |
| Reduced motion | 390 × 844 | Light and dark | PASS; no running animations, automatic scrolling disabled, final 100+ visible, terminal usable |

Commands were typed with Playwright keyboard events and submitted with Enter at 1440 and 390 in both themes, and at 390 under reduced motion in both themes: `help`, `pac certs`, `pac contact`, `pac projects`, `pac copilot` and `clear`. Output was checked against the current credentials, project titles, generic client description, email and LinkedIn destination, plus privacy guards. The client name is not published. Clear emptied the log; unknown markup remained text; focus returned to the input. Tab reached Run and Enter activated it. Keyboard theme toggling persisted through actual reloads in both directions. The skip link focused main in both themes. Related career navigation opened its record, clipboard copy returned the actual email, and the browser downloaded a valid PDF with the expected filename.

The nested project-prefix 404 was also loaded with an actual 404 response through Playwright request interception to emulate Pages routing. Real browser asset resolution, local fonts, theme, layout and return navigation passed in both themes. This verifies the page bootstrap under that path; it does **not** verify a deployed host's routing. The required plain Python server intentionally retains its default missing-route response.

### Screenshots written and inspected

All required captures are in `qa-artifacts/`:

- `v3-1440-light.png`, `v3-1440-dark.png` — 1440 × 900.
- `v3-1280-light.png`, `v3-1280-dark.png` — 1280 × 900.
- `v3-768-light.png`, `v3-768-dark.png` — 768 × 1024.
- `v3-390-light.png`, `v3-390-dark.png` — 390 × 844.
- `v3-1440-full-light.png` — 1440 × 12437, full page.
- `v3-404-{1440,390}-{light,dark}.png` — four 404 captures.
- `v3-compare-{1440,768,390}-{light,dark}.png` — six labelled side-by-side sheets using the existing reference captures.
- `v3-390-{work,credentials,terminal}-{light,dark}.png` — six supplemental scrolled viewport captures.

The top captures use scroll position zero and DPR 1; the full-page and supplemental scrolled captures are labelled separately. Screenshot composition only arranges existing captures and adds labels; it does not recreate or change page content.

### Browser fixes

- Preserved the top of the portrait by changing its `object-position` to `center top`. Its face and hair were visibly clipped in the initial desktop capture; the final desktop/tablet/mobile captures show the corrected crop.
- Changed the small 404 label to the existing accent-ink token after the light theme measured 3.49:1 against the sky. Both final 404 themes pass the targeted check.
- Added an opaque themed background colour to html/body so areas beyond the fixed-gradient viewport retain the correct canvas in full-page captures and short pages.
- Bumped local CSS/JS cache queries from v10 to v11 in both HTML pages and the verifier. JavaScript behaviour and portfolio facts were not changed.

### Reproduction and limits

The complete browser runners and comparison script are saved in the ignored QA directory as `v3-playwright-runner.cjs`, `v3-playwright-extra-runner.cjs` and `v3-comparison-runner.cjs`. From this repo, run:

```sh
NODE_PATH=/private/tmp/portfolio-v3-pw/node_modules PLAYWRIGHT_BROWSERS_PATH=/private/tmp/portfolio-v3-pw/browsers node qa-artifacts/v3-playwright-runner.cjs
NODE_PATH=/private/tmp/portfolio-v3-pw/node_modules PLAYWRIGHT_BROWSERS_PATH=/private/tmp/portfolio-v3-pw/browsers node qa-artifacts/v3-playwright-extra-runner.cjs
```

Fresh final static checks pass: `python3 scripts/verify.py`, six verifier regression assertions, JavaScript syntax, HTML validation and 55 DOM assertions. The earlier six-destination external-link HTTP audit remains retained evidence; the CSS-only fixes do not change those destinations. No deployment, other browser engine, screen reader, physical device, touch input or live client-system testing is claimed. Full formal accessibility conformance and the production host's nested-404 routing remain unverified; all required local headless checks are complete.

## E2E SUMMARY — preserved v3 results

- **Result:** requested local headless acceptance complete; 233 browser assertions pass, plus 55 DOM and six verifier assertions, HTML/JS validation and final content/privacy verification.
- **Visual evidence:** eight final index viewports, one full page, four 404 captures, six reference comparisons and six supplemental captures, visually reviewed. No horizontal overflow at required widths or seven extra breakpoints in either theme.
- **Fixes:** portrait crop, 404 label contrast, opaque themed canvas and consistent v11 cache queries.
- **Facts/privacy:** Case Assistant and the generic regulatory-body description retained; 100+ flows unchanged; no phone, private client name or unsupported personal-project text in scanned repository files.
- **Remaining visual gaps:** framed photo, denser résumé content and different hero text proportions; reference illustrations/cut-out/particles intentionally omitted.
- **Unverified:** deployment/production routing, other engines, assistive technology and physical devices; gradient contrast is supplemented by targeted/manual review rather than a formal audit.
- **Repository/runtime:** no commits or `.git` operations, dependencies/browser cache outside the repo, headless-only browser work, preview on 8093; ports 8080 and 8765 untouched.


## V4 — original scenery, teal-blue accents and hero composition — 11 November 2026

Completed locally in the requested checkout. Only HTML, CSS and JavaScript are used in production. The preview ran at `http://127.0.0.1:8093/` with `python3 -m http.server 8093 --bind 127.0.0.1`; served index bytes were compared to the checkout. No commit or `.git` operation was performed. Ports 8080 and 8765 were left untouched. The owned 8093 QA server was stopped after verification.

### Implementation and provenance

- The hero now has a compact portrait/profile rail beside a wide headline and role statement. A separate band spans the hero below them, grouping the single plain PL-600 / linked AB-100 pair with the CTAs. Tablets retain the compact portrait rail; phones use a horizontal identity card above the headline. The image remains inside its frame at `object-position: center top`; the full square source preserves the hairline. Download CV stays only in the header.
- Original inline SVG clouds and two plane silhouettes decorate light mode. Twenty-eight deterministic CSS stars and two occasional shooting trails decorate dark mode. The fixed, inert, pointer-transparent layer sits below content in an isolated stacking context. No geometry changes page layout. No external images, artwork or animation libraries were added.
- Only transform and opacity animate. There is no JavaScript per-frame loop or timer. `visibilitychange` reads `document.hidden` and pauses every CSS timeline, then resumes it. Reduced motion hides the entire layer and removes all its animations, including when the preference changes while the page is open. The same behavior is applied to the 404 page.
- Saved theme selection wins over system settings; an unsaved system preference change updates both palette and scenery. The inactive scene is `display:none`, so its CSS animations do not run.
- Local CSS and JavaScript use `?v=12` in the index, 404 bootstrap/noscript fallback and verifier. Fonts, all career records, Case Assistant, AI & Copilot, six product cards, terminal and factual text remain.

### Tokens and contrast adjustments

| Token/use | Light | Dark |
| --- | --- | --- |
| Accent / focus | `#075d73` | `#80ded5` |
| Accent ink / text links | `#064c60` | `#80ded5` |
| Secondary accent | `#087e96` | `#73dbdf` |
| Primary button | `#075d73` | `#80ded5` |
| Primary button text | `#ffffff` | `#081631` |
| HUD labels | `#064c60` | `#73dbdf` |
| Terminal highlight / Run | `#7fd8ff` | `#73dbdf` |
| Sky / page base | `#91d6ff` | `#081631` |
| Hero sky | `#a8dff6` | `#0d2247` |

The initial teal accent measured 4.11:1 on the previous light sky. The non-brand sky base was lightened to `#91d6ff` first, producing 4.70:1 for the accent and 6.00:1 for link ink on that base. Planes are white, so light scenery brightens the sky. In dark mode the radial glow alpha was reduced from `.12` to `.02`, twinkles peak at `.08`, and shooting trails peak at `.0504` effective opacity. This preserves contrast even under the conservative bound where both glow maxima, a twinkle and a shooting trail coincide. Theme-toggle and copy-button borders now use accent ink so control edges remain distinguishable. Terminal buttons use the panel highlight and panel ink.

The targeted check composites text and ancestor surfaces over sky endpoints and the conservative scenery/glow bound; it also accounts for the lightening at the top of primary-button gradients. Every rendered text node is checked, including all expanded disclosures. Normal text requires 4.5:1; large text requires 3:1. Primary-button fills and tested control edges require 3:1.

| Category minimum | Light | Dark |
| --- | --- | --- |
| All text | 4.55:1 | 4.55:1 |
| Muted text | 6.16:1 | 4.99:1 |
| Links | 4.70:1 | 5.90:1 |
| Button text | 5.60:1 | 11.83:1 |
| Tested UI boundaries | 4.70:1 | 6.23:1 |

This is a targeted AA check with conservative compositing and visual review. Axe reports no A/AA violations in the eight expanded index samples, but marks gradient color contrast incomplete; formal accessibility certification is not claimed.

### Browser and regression results

**PASS: 407 main browser assertions plus 12 supplemental animation-phase/counter assertions**, eight main samples, zero page/request errors, zero reported axe A/AA violations. Evidence: `qa-artifacts/v4-playwright-results.json` and `qa-artifacts/v4-motion-details.json`. Browser: Playwright headless Chromium 158.0.8127.18, DPR 1, with `--single-process --no-zygote`. Dependencies and browser cache remain outside the repo at `/private/tmp/portfolio-v3-pw`. No Google Chrome app/profile, connected browser or computer-use tool was used.

| Coverage | Result |
| --- | --- |
| 1440 × 900, 1280 × 900, 768 × 1024, 390 × 844; both themes | PASS; no horizontal overflow, all fonts loaded, headshot inside frame and aligned to top |
| Expanded disclosures at all eight combinations | PASS; no overflow, text contrast checks and axe A/AA checks |
| Motion vs reduced-motion layout | PASS; maximum rectangle delta 0 px in every main sample; initial observed CLS 0 |
| Background selection | PASS; five light CSS animations or thirty dark CSS animations, with only the matching scene rendered; phase sampling confirms clouds/planes move and twinkles/shooting trails change opacity |
| Hidden-tab simulation at all eight combinations | PASS; 5 light / 30 dark timelines paused with unchanged current times, then resumed and advanced |
| Reduced-motion change at all eight combinations | PASS; layer hidden, no running scenery or other animations, final 100+ retained; motion resumes when allowed |
| Reduced motion on initial load | PASS in both themes at 390; terminal works; theme toggling keeps scenery disabled; supplemental checks confirm all five counters retain their final target values |
| Keyboard theme toggle, accent and persistence | PASS at all four widths in both directions; actual reload retains scene and theme; saved preference wins |
| Unsaved system theme change | PASS in both directions; matching scene follows the system |
| Terminal keyboard commands | PASS at 1440 and 390 in both themes and reduced-motion mobile: help, certs, contact, projects, copilot and clear; privacy and safe text checks |
| Existing interactions | PASS; related career opens, actual clipboard copy and valid CV PDF download |
| Extra widths | PASS at 320, 360, 650, 960, 1000, 1100 and 1200 in both themes |
| Explicit 404 | PASS at 1440 and 390, both themes; scenery selection, contrast, overflow and return navigation |
| Static/content/privacy | PASS; verifier, HTML validation, JS syntax, 55 retained DOM assertions and 9 verifier regression assertions |

Hidden-tab behavior is tested by overriding `document.hidden` and dispatching `visibilitychange`, as requested; an OS-level tab-hide/minimize action is not claimed. Layout comparison measures the hero, story, credential band, portrait/frame and major downstream section bounds against an emulated reduced-motion baseline. Initial CLS was also observed in Chromium.

### Screenshots written and visually inspected

- `qa-artifacts/v4-1440-light.png`, `qa-artifacts/v4-1440-dark.png`.
- `qa-artifacts/v4-1280-light.png`, `qa-artifacts/v4-1280-dark.png`.
- `qa-artifacts/v4-768-light.png`, `qa-artifacts/v4-768-dark.png`.
- `qa-artifacts/v4-390-light.png`, `qa-artifacts/v4-390-dark.png`.
- `qa-artifacts/v4-1440-full-light.png` — 1440 × 12298, reviewed in seven consecutive crops outside the repo.

All eight viewport screenshots are at the top of the page with DPR 1. Review confirmed the compact portrait, intact hairline, readable content over scenery, and retained downstream section layout. The dark scenery is intentionally faint. V3 screenshots and notes above are historical; the V4 files are the current evidence.

### Reproduction and limits

With the plain Python server on 8093 and the cached test dependencies available:

```sh
python3 scripts/verify.py
python3 scripts/test-verifier.py
node --check assets/js/main.js
NODE_PATH=/private/tmp/portfolio-v3-test/node_modules node scripts/test-interactions.cjs
npm exec --cache /private/tmp/portfolio-v3-pw/npm-cache --yes --package html-validate@10.17.0 -- html-validate index.html 404.html
NODE_PATH=/private/tmp/portfolio-v3-pw/node_modules PLAYWRIGHT_BROWSERS_PATH=/private/tmp/portfolio-v3-pw/browsers node qa-artifacts/v4-playwright-runner.cjs
NODE_PATH=/private/tmp/portfolio-v3-pw/node_modules PLAYWRIGHT_BROWSERS_PATH=/private/tmp/portfolio-v3-pw/browsers node qa-artifacts/v4-motion-detail-runner.cjs
```

No deployment, current external-link HTTP audit, production nested-404 routing, other browser engine, screen reader or physical-device testing was performed in V4. The supplied Learn links and local references are checked statically. The multiset of visible body-text tokens was compared to the saved v3 served HTML and is identical; only hero order changed. No new content, client identity or personal-project claims were introduced.

## E2E SUMMARY

- **Result:** V4 implemented and locally verified; 407 main and 12 supplemental headless browser assertions pass, plus 55 DOM assertions, 9 verifier regressions, HTML validation, JavaScript syntax and final content/privacy verification.
- **Design:** original cloud/plane and twinkle/shooting-star backgrounds; teal-blue accent system; compact portrait rail plus separate credential/action band, with a horizontal identity card on phones.
- **Motion/accessibility:** fully disabled under reduced motion; hidden timelines stop/resume; no motion-related layout delta; all targeted text and control contrast thresholds pass; zero reported axe A/AA violations.
- **Evidence:** eight required DPR 1 top screenshots and one full light page, all visually inspected, plus the reproducible browser runner and JSON results in `qa-artifacts/`.
- **Preservation:** factual content, privacy, Case Assistant first, AI & Copilot, all six product cards, five JSON-LD credentials, supplied Learn links, header-only CV and 100+ flows remain intact.
- **Limits:** simulated hidden-document event; no production deployment/routing, new external-link audit, other engines, assistive technology, physical devices or formal accessibility certification.
- **Repository/runtime:** no commit or `.git` access/modification; headless Chromium and test dependencies outside the repo; preview used only 8093; ports 8080 and 8765 untouched.
