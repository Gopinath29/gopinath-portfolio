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

## E2E SUMMARY

- **Result:** requested local headless acceptance complete; 233 browser assertions pass, plus 55 DOM and six verifier assertions, HTML/JS validation and final content/privacy verification.
- **Visual evidence:** eight final index viewports, one full page, four 404 captures, six reference comparisons and six supplemental captures, visually reviewed. No horizontal overflow at required widths or seven extra breakpoints in either theme.
- **Fixes:** portrait crop, 404 label contrast, opaque themed canvas and consistent v11 cache queries.
- **Facts/privacy:** Case Assistant and the generic regulatory-body description retained; 100+ flows unchanged; no phone, private client name or unsupported personal-project text in scanned repository files.
- **Remaining visual gaps:** framed photo, denser résumé content and different hero text proportions; reference illustrations/cut-out/particles intentionally omitted.
- **Unverified:** deployment/production routing, other engines, assistive technology and physical devices; gradient contrast is supplemented by targeted/manual review rather than a formal audit.
- **Repository/runtime:** no commits or `.git` operations, dependencies/browser cache outside the repo, headless-only browser work, preview on 8093; ports 8080 and 8765 untouched.
