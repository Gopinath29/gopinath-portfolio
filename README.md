# Gopinath Gurusamy — portfolio

A single-page, static portfolio for Dynamics 365 CE & Power Platform solution architecture, technical leadership and remote B2B engagements, with PL-600 and AB-100 featured and Copilot Studio & AI agents included. Plain HTML, CSS and JavaScript; no build, runtime dependencies, external fonts or CDN requests.

## Preview

From this directory:

```sh
python3 -m http.server 8090 --bind 127.0.0.1
```

Open `http://127.0.0.1:8090/`. Use port 8090 for local QA. Stop the server with Ctrl-C.

## Edit content

- `index.html`: all visible copy, experience, case studies, links, credentials and Person JSON-LD. The section order follows the supplied brief.
- `assets/css/styles.css`: colour tokens, typography, responsive layout, light/dark themes and reduced-motion rules.
- `assets/js/main.js`: theme preference (`gg-theme` in localStorage), clipboard feedback, scroll reveals, stat counters and active navigation. Content, downloads and navigation remain usable without JavaScript.
- `assets/resume/Gopinath_Gurusamy_Resume.pdf`: downloadable CV, copied unchanged from the supplied PDF.
- `assets/img/og-image.svg`: editable source for the 1200 × 630 PNG social preview. Update the PNG after editing the SVG.
- `assets/img/headshot.jpg`: supplied 400 × 400 portrait, compressed with macOS `sips` at JPEG quality 82.
- `favicon.svg`: initials favicon.
- `404.html`, `robots.txt`, `sitemap.xml`, `.nojekyll`: static hosting support.
- `scripts/verify.py`: repeatable asset, anchor, metadata, image-dimension and privacy checks.
- `VERIFICATION.md`: recorded checks and any environment limitations.

Keep claims grounded in the five supplied source files: `resume.txt`, `profile_export_v2.txt`, `linkedin_update.md`, `profile_current.md` and `linkedin_export.txt`. They are deliberately not copied into the public repository. The brief resolves differences: use 13+ years from the September 2013 start, April 2021 for the Central Bank end date, and “2017” for the OpenSky start. Employer names are permitted; the regulator and healthcare clients remain anonymous. Outcomes are qualitative and source-backed. Certifications are listed without issue/expiry dates. Brief 3 supplies the exact Microsoft Learn credential URLs for AB-100 and AB-620; only those credentials have verification links, including in Person JSON-LD. PL-600 and AB-100 are featured in the two left-column hero cards and social image. The About services row comes from the supplied LinkedIn copy. The hero location reads “Based in India · Remote B2B contractor”.

**Privacy:** the public page, metadata and documentation contain no phone number. The downloadable CV itself contains a phone number, as permitted by the brief. Replace it with a phone-free PDF at the same path if desired. Do not copy private contact information from the source files into the website.

## Swap the headshot

The supplied portrait is installed at `assets/img/headshot.jpg` (400 × 400, about 42 KB). To replace it, prepare a square 400 × 400 source and run:

```sh
sips -s format jpeg -s formatOptions 82 /path/to/replacement.png --out assets/img/headshot.jpg
```

The hero uses `<picture>` with a JPEG fallback, explicit dimensions, eager loading and high fetch priority. The `.headshot` rule sets the rounded accent border and `object-position: center 20%`; adjust the position if the replacement needs a different crop. The portrait fills the desktop and tablet card’s content width, aligned with its text and chip grid. A small embedded style in `index.html` constrains its width even if the external stylesheet fails to load. On narrow screens the 160px portrait sits beside the headline. The profile card contains the heading, portrait, delivery statement and architecture chips, with bottom padding matching its side padding. Credentials remain in the two left-column cards. The CV download appears only in the top header; Get in touch is the primary hero action. CSS and local script URLs use `?v=7` on both HTML pages to refresh cached assets. `cwebp` was unavailable for this update, so only JPEG is included. If you later generate `assets/img/headshot.webp`, add a `<source type="image/webp" srcset="assets/img/headshot.webp">` before the JPEG `<img>` inside the existing `<picture>`.

## Credential links

Only these supplied Microsoft Learn credential URLs are used in the HTML and Person JSON-LD, and accepted by `scripts/verify.py`:

- AB-100: https://learn.microsoft.com/en-us/users/gopinathgurusamy-9343/credentials/71c8c88020980655
- AB-620: https://learn.microsoft.com/en-us/users/gopinathgurusamy-9343/credentials/33c24ca4ad0be38e

The hero presents PL-600 as plain text and AB-100 as a link with a trailing arrow. Both use literal spaces and middle-dot separators so they remain readable without CSS. The separator after “Microsoft Certified” sits in an `sr-only` span, preventing a visible trailing dot when styled. Other grouped labels, chips and certification cards also include real HTML whitespace. Do not add verification links for the other credentials without a supplied source.

## Verify

```sh
python3 scripts/verify.py
node --check assets/js/main.js
npx --yes html-validate index.html 404.html
```

Use a writable npm cache if your default cache is unavailable, for example `npm_config_cache=/tmp/portfolio-npm-cache`. Browser QA should cover 360px, tablet and desktop widths; both themes; keyboard focus; reduced motion; clipboard success/failure; downloads; and a server rooted at the GitHub Pages project path. A single automated accessibility score does not establish full WCAG conformance.

## Deploy later to GitHub Pages

This handoff is local only. It does not create a remote or push anything.

When ready, create a repository and upload or push the site yourself. In repository **Settings → Pages**, select **Deploy from a branch**, branch **main**, folder **/ (root)**. The intended URL is:

`https://gopinath29.github.io/gopinath-portfolio/`

All HTML asset references are relative so the project prefix is preserved. Canonical, social-image and sitemap URLs are absolute by design for search engines and social crawlers. If the repository name or domain changes, update those URLs in `index.html`, `robots.txt` and `sitemap.xml`. GitHub Pages uses a domain-root robots file; the project-level `robots.txt` is supplied, but site-wide crawler policy must be managed at the account domain root if needed.

## Local changes

Brief 3 builds on the existing Brief 2 edits. No commit or push was run for either update. Review the changes with:

```sh
git status --short
git diff
```
