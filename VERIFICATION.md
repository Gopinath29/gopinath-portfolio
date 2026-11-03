# Brief 7 and Brief 8 verification — 3 November 2026

## Brief 8 content correction

The national healthcare programme now consistently states **100+ Power Automate flows** in the stat's visible source text, accessible label, `data-count` / `data-target` and case study. The about text, SEO/OG/Twitter descriptions, Person JSON-LD and SVG/PNG social image were audited: none contains a flows count. All other metrics and the Brief 7 redesign are retained.

`python3 scripts/verify.py`, `node --check assets/js/main.js` and `html-validate` 10.17.0 on both pages PASS. The verifier now rejects stale flows wording anywhere in `index.html` and requires 100+ in the named stat. Eight isolated mutation checks PASS: seven incorrect visible/accessible/target/content/metadata/missing-stat variants fail, while an unrelated 20+ metric passes.

Chrome was operated through its native UI and DevTools because the browser connector host was unavailable. Mutation observation confirmed the flows animation progresses through intermediate values (starting at 3) and finishes at 100, with a stable accessible name of `100+ Power Automate flows`. At 1440 × 900 and 390 × 844, the light layout and flows stat render without horizontal overflow. With every stylesheet disabled, Chrome reports zero active stylesheets and exactly `13+`, `9`, `4`, `~3,000`, `100+` as the five stat values. The flows value appears once and remains readable. The enhancement skips animation without CSS or when reduced motion is requested; the final value is present without JavaScript.

Refreshed `qa-artifacts/v2-1440-light.png` and `v2-390-light.png` show the top of the page. They are exact 1440 × 900 and 390 × 844 crops of native Chrome captures, without resizing. Additional `brief8-1440-flows.png`, `brief8-390-flows.png`, `brief8-no-css.png` and `brief8-results.json` record this follow-up. The remaining v2 artifacts and the wider results below belong to Brief 7. No commit, push or deployment was performed.

## Delivered

Astrofy (MIT) was selected after evaluating eight GitHub candidates. The full license is retained. The production site remains plain static files at the repository root; no build or GitHub Actions workflow is required.

The new design includes a portrait rail, editorial typography, warm light and forest dark palettes, responsive cards, a complete experience timeline and matching 404/social-image designs. Every original content text node is retained except the intentionally removed numbering prefixes and replaced monogram. The content-preservation comparison found zero missing factual text nodes.

## Automated checks

| Check | Result |
| --- | --- |
| `python3 scripts/verify.py` | PASS: local refs including queries, anchor IDs, no placeholders, supplied Learn URLs, five Person credentials, hero credential display, PL-600 unlinked, header-only CV, prohibited content, privacy scan, headshot and 1200 × 630 PNG |
| `node --check assets/js/main.js` | PASS |
| `html-validate` 10.17.0, both pages | PASS |
| Original-content comparison | PASS: no missing text nodes, after permitted presentation changes |
| External links, curl with redirects and Chrome user agent | PASS: all seven unique destinations returned HTTP 200 |
| Local HTTP references | PASS: HTTP 200, valid PDF header and `application/pdf` response |
| Text contrast | PASS: 223 rendered text runs per theme; minimum 5.27:1 light, 6.46:1 dark |

The verifier now checks v8 cache-busting, encoded prohibited text, numbered labels, the hero credential display, a required Person block and unlinked PL-600, in addition to the previous checks.

## Connected Chrome

Local preview used port 8092. No headless browser was used. The portfolio and nested project-path 404 were tested at 1440 × 900, 1280 × 900, 768 × 1024 and 390 × 844 in both themes. Every tested layout has zero horizontal overflow. The portrait loads with alt text, stays within its rounded frame and has intrinsic 400 × 400 dimensions. Desktop rail navigation fits within the 900-pixel test window after the compact-layout fix.

Main navigation, hero exploration, footer return, brand return and skip navigation resolve. The 404 skip targets its own main landmark, and both home links return to the project root. Saved themes survive reload and carry across pages. Copy email announces success. LinkedIn and the blog were also opened and confirmed in Chrome.

A temporary fixture omitted every site stylesheet and inline site style. Reviewed 140 unstyled text blocks plus the raw body text: names, headings, credentials, languages and statistics remain separated and readable. Chrome injects its own opacity style; that is the sole stylesheet in the fixture. The fixture was removed after testing.

Reduced-motion and system-theme fallback were reviewed in CSS/JavaScript. OS media settings were not changed or force-emulated. This is a targeted accessibility verification, not a full WCAG conformance audit.

## Evidence and limits

Current evidence uses the `qa-artifacts/v2-` prefix. The six required viewport PNGs and full-page light PNG are present; extra dark, tablet and 404 evidence is included. PNGs were converted from connected Chrome's JPEG captures without resizing. Browser captures may omit scrollbar space and apply its capture scaling; the actual tested window dimensions are recorded independently in `v2-layout-results.json`.

The full results, inventory and artifact links are in [E2E_REPORT.md](E2E_REPORT.md).

- Automatic approval review rejected the CV browser download because localhost download permission was declined. No alternate download was attempted. The local file, link target and HTTP response pass; completed browser downloads are unverified.
- The copy handler resolves and announces success. Browser clipboard readback was empty, and the paste automation did not complete, so exact clipboard contents remain unverified.
- Nested Pages behavior was simulated locally. The public deployment was not changed or retested.

No unresolved website defect was found in the completed checks. No git command, commit, push or deployment was performed, and the reserved port was not used or stopped.
