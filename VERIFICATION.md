# Verification — Brief 3, 3 November 2026

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
- Availability follows the supplied LinkedIn copy: full AU/NZ business hours, UK/EU mornings, and no notice period for contracts.
- At the Brief 2 baseline, AB-100 and AB-620 used the verification URLs supplied in Brief 2; Brief 3 replaces these with the supplied credential-page URLs. They were not independently fetched in this update. No verification link is invented for another credential; only those two credentials have JSON-LD URLs. The placeholder and its TODO/CSS were removed.
- Browser checks are targeted layout and interaction QA, not a claim of complete WCAG certification. No new Lighthouse score is claimed.
- Changes remain local. No commit, push or deployment was performed.
