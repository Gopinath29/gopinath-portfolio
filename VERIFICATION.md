# Verification — 3 November 2026

Headline: **Dynamics 365 CE & Power Platform Solution Architect.** Supporting line: “Architecture and hands-on engineering for regulated, high-stakes CRM programmes.”

## Passed

- `html-validate` 10.17.0: `index.html` and `404.html`, zero errors or warnings after fixes. No relaxed validation configuration.
- `node --check assets/js/main.js`: valid syntax.
- `python3 scripts/verify.py`: ten local file references exist, internal anchors resolve, IDs are unique, Person JSON-LD parses without a telephone field, social PNG is 1200 × 630, and private-number signatures are absent from public files. The explicitly requested Microsoft Learn `#` placeholder is allowed.
- Separate recursive text-file privacy scan: no private-number signature outside the permitted PDF. Source documents are not included in the site repository.
- Downloadable PDF is byte-for-byte identical to the supplied `Gopinath_Gurusamy.pdf`.
- HTTP checks: index, CSS, JavaScript, PDF, social PNG and 404 document each returned 200. Project-prefixed index and every linked asset returned 200. A missing nested project URL returned the custom page with 404 status, correct styles and a working home link.
- Connected Chrome visual/layout checks at widths 360, 390, 560, 561, 768, 800, 801, 1024 and 1440; also inspected at 1920. No horizontal page overflow. Both themes inspected, including the mobile hero, desktop case study and contact layouts.
- Theme switch changes the palette and accessible label; selected light mode persists after reload. Baseline CSS also follows the system theme without JavaScript.
- Sticky header and active Work/Contact links checked after smooth scrolling. Scroll-revealed case study becomes visible at its destination. Source stats are rendered as final values before any animation and retain authoritative accessible values during counting.
- Keyboard: first Tab exposes the skip link with a visible focus outline; Enter moves focus to `main`. No positive tabindex or keyboard trap is introduced.
- Copy-email click reports success. Isolated local fixtures also checked denied clipboard access and blocked localStorage; feedback and the theme switch remain usable.
- No-enhancement-script fixture: content and source stats remain visible, PDF link remains available, and unavailable theme/copy buttons stay hidden.
- Simulated reduced-motion fixture: no reveal hiding or stat counting; all final stats remain visible. CSS `prefers-reduced-motion` removes smooth scrolling and transition durations. The operating system preference itself was not changed.
- Axe-core WCAG A/AA audit: zero violations on the portfolio in light and dark desktop themes, zero on dark mobile, and zero on the light error page. There were 26 passing rule groups on the portfolio and 17 on the error page. Manual-review items concerned decorative symbol glyphs and the mobile blueprint background. Text palette pairs have minimum contrast of 8.18:1 in dark and 5.57:1 in light; the faint blueprint grid was visually inspected. This is targeted QA, not a certification of complete WCAG conformance.
- Social PNG rendered from the editable local SVG and visually inspected. No external fonts, CDN assets or runtime packages.

## Source review

All biography, skills, experience, case studies, education and credential copy was derived from the five allowed source files. The source wording supports the qualitative outcomes. Regulator and healthcare clients remain anonymous. Date conflicts follow the brief: 13+ years from September 2013, Central Bank through April 2021, OpenSky start shown as 2017. No invented client logos, testimonials or performance metrics. Current certification validity was not independently checked; no issue/expiry dates are displayed.

## Environment limitations and handoff

- Port 8080 belongs to an existing Caddy service. It was left running. Python preview attempts on other ports did not become ready; verification used a temporary Node static server on loopback port 8090, including a simulated `/gopinath-portfolio/` mount. Owned preview processes were stopped after verification.
- Lighthouse was installed and attempted with the installed Google Chrome. Both the direct headless launch and Lighthouse failed under the sandbox (Chrome launch/Crashpad restrictions; Lighthouse could not obtain a debugging port). **No Lighthouse scores are claimed.** Connected Chrome was used for the browser checks above.
- The workspace denies writes to `.git`; standard initialization in the requested folder failed with “Operation not permitted.” Local commit metadata is stored in `/private/tmp/gopinath-portfolio-local-history/.git` and the completed local commit is preserved as `.local-history/initial-portfolio.bundle`. See README for inspection and restoration without adding a remote. The website itself remains in the requested folder.
- No publication, remote creation, push or external integration was performed.
- An unexpected second set of CSS/JS/404 edits appeared during implementation. Those versions were saved under `/private/tmp/gopinath-portfolio-qa/unexpected-versions/`; the delivered page, stylesheet and script were reconciled and checked together.

## Content TODO

- Supply the verified public Microsoft Learn profile URL to replace the clearly labelled placeholder.
- Optional: replace the initials avatar at the single `HEADSHOT SWAP` comment with a headshot.
- Optional: replace the supplied CV with a phone-free PDF; only that permitted PDF contains private contact information.
