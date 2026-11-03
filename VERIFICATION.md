# Verification — Brief 6, 3 November 2026

- Preserved the existing uncommitted Briefs 4/5 and E2E fixes. No commit, push or deployment was performed.
- Kept the two left-column credential cards: PL-600 is plain text; AB-100 retains its supplied Learn verification link and arrow. Removed the profile card’s credential footer and numbering, including related CSS at every breakpoint. Kept the left-aligned Architecture + engineering heading.
- Profile card bottom and side padding match: 28px on desktop, 22px at the intermediate breakpoint and 16px on tablet. The chip grid has no bottom margin. Connected Chrome measured equal 29px portrait-left/chip-bottom insets at 1280/1440 and equal 17px insets at 768 (including the 1px border). Mobile retains the existing portrait beside the headline.
- The only CV link is in the header. Get in touch is now the primary hero button; LinkedIn remains. The PDF is unchanged.
- Removed the superseded availability claims from page copy and documentation. Audited the About section, metadata, JSON-LD, social SVG and E2E report. Metadata and social-image copy already used only remote B2B wording, so neither social image required editing or regeneration. The hero location remains Based in India · Remote B2B contractor.
- Moved the issuer separator into an `sr-only` span: no visible trailing dot when styled. A temporary page without the external stylesheet confirmed complete, separated credential sentences, with PL-600 unlinked and AB-100 linked. Removed the fixture afterward.
- CSS and local script URLs use `?v=7` in both HTML pages; README matches.
- `python3 scripts/verify.py`: PASS (10 local file references plus anchors, supplied Learn links, five JSON-LD credentials, images, privacy, Brief 6 forbidden-content checks, header-only CV and versioned assets).
- Isolated verifier fixtures: clean copy PASS; all five forbidden-content cases, a duplicate CV link with nested spans, an alternatively labelled CV link outside the header, and obsolete asset versions correctly FAIL.
- `node --check assets/js/main.js`, `html-validate index.html 404.html`, and `git diff --check`: PASS.
- Connected Chrome at `http://127.0.0.1:8090/`: no horizontal overflow at all four requested widths in both light and dark themes. No browser warnings or errors were recorded. Port 8080 was not used or stopped. Reset the viewport override afterward.

| CSS viewport | Page client width | Page scroll width | Light | Dark |
| --- | ---: | ---: | --- | --- |
| 390 × 844 | 375px | 375px | PASS | PASS |
| 768 × 1024 | 753px | 753px | PASS | PASS |
| 1280 × 900 | 1265px | 1265px | PASS | PASS |
| 1440 × 900 | 1425px | 1425px | PASS | PASS |

Saved and visually inspected viewport-only, top-of-page captures in gitignored `qa-artifacts/brief6-1440-light.png`, `brief6-1440-dark.png` and `brief6-390-light.png`. Chrome supplies JPEG captures; these were converted to PNG without resizing or other changes. The browser capture raster is scaled by the connected backend; viewport dimensions above are the measured CSS dimensions.

Prior verification records follow; Brief 6 supersedes their removed hero footer, extra CV action and availability claims.

# Verification — E2E, 3 November 2026

See [E2E_REPORT.md](E2E_REPORT.md) for the completed all-section QA, fixes, 16 final screenshots and verification limits. Current asset version is `?v=7`. Brief 6 supersedes earlier hero-layout and availability records below. Prior brief records follow.

# Verification — Brief 5, 3 November 2026

## Brief 5 checks

- Hero PL-600 is plain text with no link, arrow or link colour. AB-100 uses the supplied Learn URL, `target="_blank"`, `rel="noopener"` and a trailing, `aria-hidden` arrow. Both items use identical card layout, spacing, neutral text and borders; only AB-100 has the arrow and link hover/focus affordance.
- Browser DOM inspection confirms the literal text is `Microsoft Certified · PL-600 · Power Platform Solution Architect Expert` and `Microsoft Certified · AB-100 · Agentic AI Business Solutions Architect Expert ↗`.
- Added real HTML whitespace to navigation, panel labels/footer, architecture chips, engagement chips, certification cards, blog labels, social links and email controls. Intentional joined punctuation such as `13+` and the initials logo remains intact.
- CSS and local script URLs use `?v=5` in both HTML pages; README reflects the current version and credential behaviour.
- `python3 scripts/verify.py`, `node --check assets/js/main.js`, `html-validate` 10.17.0 on both pages, and `git diff --check`: PASS.
- Connected Chrome: inspected the styled hero at 390 × 844 and 1280 × 900. Both cards share layout and padding; desktop card heights are both 79px, with widths equal within 0.02px. No horizontal overflow at either size. Dark and light desktop themes remain readable.
- Loaded a temporary copy without the external stylesheet. Both hero credential sentences read correctly, PL-600 is unlinked, and navigation, panel text, chips and certification labels remain separated. The temporary HTML was removed after inspection.
- Saved browser evidence in gitignored `qa-artifacts/brief5-desktop.jpg`, `brief5-mobile.jpg` and `brief5-no-css.jpg`. Browser viewport override was reset afterward.
- No commit, push or deployment was performed. Existing Brief 4 changes were preserved.

## Prior Brief 4 verification

Brief 4 supersedes Brief 3's fixed portrait widths and labels beneath the photo.

## Brief 4 checks

- Served locally at `http://127.0.0.1:8090/`. Port 8080 was not used or stopped.
- Desktop/tablet portrait fills the panel content width with a square crop, 16px corners, a subtle accent border and no outer shadow ring. Mobile retains its 160px portrait beside the headline. The left-column credential badges and panel footer text are unchanged.
- Removed the obsolete portrait labels and their CSS at every breakpoint. `scripts/verify.py` now rejects `portrait-credentials` anywhere in `index.html`.
- CSS and local script references use `?v=4` in both `index.html` and `404.html`. The verifier already uses `urlsplit(...).path`, so query strings do not affect local file lookup.
- `python3 scripts/verify.py`: PASS (11 local file references plus existing metadata, anchor, credential, image and privacy checks). Isolated fixtures also passed with versioned asset URLs and correctly failed for restored portrait labels and a missing CSS asset with a query string.
- `html-validate` on `index.html` and `404.html`, `node --check assets/js/main.js`, and `git diff --check`: PASS.
- Browser JavaScript measured `getBoundingClientRect()` for the panel, headshot and chip grid. Both desktop assertions pass within 1px:

| Viewport | Panel width | Left inset | Right inset | Headshot width | Chip grid width |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1280 × 900 | 410px | 29px | 29px | 352px | 352px |
| 1440 × 900 | 410px | 29px | 29px | 352px | 352px |

- Tablet widths 561, 768 and 800px: equal 17px portrait insets, matching portrait/chip widths and no horizontal page overflow. At 390 × 844, the portrait is 160 × 160px with no horizontal overflow. All checked pages have zero obsolete portrait-label elements and a loaded image.
- Disabled the external stylesheet in a temporary local fixture: the embedded fallback kept the image at its container width (359px), with proportional height. Removed the fixture afterward.
- Saved and visually inspected the requested screenshots: `qa-artifacts/brief4-1280.png` (1280 × 900), `qa-artifacts/brief4-1440.png` (1440 × 900), and `qa-artifacts/brief4-mobile.png` (390 × 844). Connected Chrome produces JPEG captures; these were converted to PNG without resizing. Full rectangle measurements are saved in `qa-artifacts/brief4-measurements.json`. All artifacts are gitignored.
- **Verification limitation:** headless Chromium could not launch because the sandbox denied macOS `bootstrap_check_in` permission. The measurements, assertions and screenshots above used connected Chrome with explicit viewport sizes instead; the requested headless run is not claimed as completed.
- No commit, push or deployment was performed.

## Prior Brief 3 verification

Brief 3 is applied on top of the existing, uncommitted Brief 2 edits.

## Brief 3 checks

- `python3 scripts/verify.py`: passes 11 local asset references, anchors with no placeholder hrefs, the two supplied Microsoft Learn credential-page URLs, all five JSON-LD credential entries, JPEG headshot presence/markup, social PNG dimensions and privacy scan. No phone numbers found in repo text files; the previously permitted CV PDF remains excluded from that text scan.
- `html-validate` 10.17.0: `index.html` and `404.html` pass with zero errors or warnings and no relaxed rules.
- `node --check assets/js/main.js` and `git diff --check`: pass.
- Isolated verifier fixtures pass for the valid site and reject a missing headshot, a placeholder href and a phone-like number. Fixtures were created outside the repository and removed afterward.
- `sips` produced `assets/img/headshot.jpg` from the supplied PNG at quality 82. Dimensions are 400 × 400; size is 42 KB (below 80 KB). `cwebp` is unavailable, so the `<picture>` contains the JPEG fallback only.
- Connected Chrome: visually inspected dark and light themes at 360 × 800 and 1440 × 900, plus dark at 768 × 1024. No horizontal page overflow at these widths. The portrait loads at its natural 400 × 400 dimensions and displays at 160px beside the mobile headline, 180px on tablet and 240px on desktop. The accent border and PL-600 / AB-100 pills remain legible in both themes.
- At 360px, the portrait starts about 162px from the top; both full hero credential badges end by about 604px, inside the first 800px screen. Desktop badges also remain on the first screen. Saved the mobile preview at `qa-artifacts/brief3-mobile.png` (ignored by git).
- Headless Chrome could not launch under the filesystem sandbox, so layout QA used the connected Chrome browser.
- No legacy credential share URLs or lone-hash hrefs remain in repository text. README now documents the installed photo, replacement steps and both supplied credential-page URLs. The existing Brief 2 social image is retained, as permitted by Brief 3.
- No commit, push or deployment was performed.

The Brief 2 report below records the prior baseline; Brief 3 supersedes its credential URLs and portrait placeholder.

## Brief 2 baseline — 3 November 2026

Positioning: **Dynamics 365 CE & Power Platform Solution Architect · Technical Lead · Copilot Studio & AI Agents.** PL-600 and AB-100 are featured immediately below this sub-line, in the side-panel footer and in the social image.

### Checks completed for Brief 2

- `python3 scripts/verify.py`: passes ten local asset references, in-page anchors, duplicate IDs, supplied Microsoft Learn links, Person JSON-LD with five `EducationalOccupationalCredential` entries, PNG dimensions and the public-file privacy scan.
- `html-validate` 10.17.0: `index.html` and `404.html` pass with zero errors or warnings and no relaxed rules.
- `node --check assets/js/main.js`: passes. The existing enhancement script required no changes.
- `git diff --check`: passes.
- Isolated verifier fixtures confirm that the exact supplied Learn links pass, while a lone hash href, missing anchor, unformatted or formatted phone-like number, unknown Learn URL, and invented PL-600 credential URL fail. Test fixtures stayed outside the website.
- HTTP checks: index, CSS, JS, SVG, PNG, CV and the 404 document return 200 at both the server root and a simulated `/gopinath-portfolio/` prefix.
- The CV remains byte-for-byte identical to `~/portfolio-src/Gopinath_Gurusamy.pdf`. Its original contact details remain confined to that previously permitted PDF; no phone number was added to the page, metadata, image or documentation.
- The 1200 × 630 PNG was regenerated from the editable SVG and visually inspected. It shows PL-600 + AB-100, Microsoft Certified, and Copilot Studio & AI agents.
- Connected Chrome at 360 × 800 and 1440 × 900: both hero badges are fully visible on the first screen, with no horizontal page overflow. Four services form a desktop row and stack on mobile. PL-600 and AB-100 occupy the first certification row, with AB-100 and AB-620 verification links. Light and dark themes inspected.

### Brief 2 content and scope

- All added professional copy comes from `CODEX_BRIEF_2.md`, `profile_export_v2.txt` and `linkedin_update.md` in `~/portfolio-src`. The original brief's rules for experience totals and conflicting dates remain in force.
- About includes design authority, Dataverse data models, business units/teams/roles, GDPR/DSAR, Azure Functions/Logic Apps/Web API, Azure DevOps ALM/CI/CD with managed solutions, and Copilot Studio & AI agents.
- Contract services cover fractional architecture, platform assessments/health checks, migrations and Copilot Studio/AI agents. No specific AI agent project, pricing, follower count or recommendation was added.
- Availability copy was simplified in Brief 6 to remote B2B contracts, based in India.
- At the Brief 2 baseline, AB-100 and AB-620 used the verification URLs supplied in Brief 2; Brief 3 replaces these with the supplied credential-page URLs. They were not independently fetched in this update. No verification link is invented for another credential; only those two credentials have JSON-LD URLs. The placeholder and its TODO/CSS were removed.
- Browser checks are targeted layout and interaction QA, not a claim of complete WCAG certification. No new Lighthouse score is claimed.
- Changes remain local. No commit, push or deployment was performed.
