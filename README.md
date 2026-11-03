# Gopinath Gurusamy — portfolio

A single-page, static portfolio for Dynamics 365 CE & Power Platform solution architecture, technical leadership and remote B2B engagements. Plain HTML, CSS and JavaScript; no build, runtime dependencies, external fonts or CDN requests.

## Preview

From this directory:

```sh
python3 -m http.server 8080
```

Open `http://localhost:8080/`. If that port is occupied, use `8081`. Stop the server with Ctrl-C.

## Edit content

- `index.html`: all visible copy, experience, case studies, links, credentials and Person JSON-LD. The section order follows the supplied brief.
- `assets/css/styles.css`: colour tokens, typography, responsive layout, light/dark themes and reduced-motion rules.
- `assets/js/main.js`: theme preference (`gg-theme` in localStorage), clipboard feedback, scroll reveals, stat counters and active navigation. Content, downloads and navigation remain usable without JavaScript.
- `assets/resume/Gopinath_Gurusamy_Resume.pdf`: downloadable CV, copied unchanged from the supplied PDF.
- `assets/img/og-image.svg`: editable source for the 1200 × 630 PNG social preview. Update the PNG after editing the SVG.
- `favicon.svg`: initials favicon.
- `404.html`, `robots.txt`, `sitemap.xml`, `.nojekyll`: static hosting support.
- `scripts/verify.py`: repeatable asset, anchor, metadata, image-dimension and privacy checks.
- `VERIFICATION.md`: recorded checks and any environment limitations.

Keep claims grounded in the five supplied source files: `resume.txt`, `profile_export_v2.txt`, `linkedin_update.md`, `profile_current.md` and `linkedin_export.txt`. They are deliberately not copied into the public repository. The brief resolves differences: use 13+ years from the September 2013 start, April 2021 for the Central Bank end date, and “2017” for the OpenSky start. Employer names are permitted; the regulator and healthcare clients remain anonymous. Outcomes are qualitative and source-backed. Certifications are listed without issue/expiry dates; current credential status has not been independently checked.

**Privacy:** the public page, metadata and documentation contain no phone number. The downloadable CV itself contains a phone number, as permitted by the brief. Replace it with a phone-free PDF at the same path if desired. Do not copy private contact information from the source files into the website.

## Swap the headshot

Search `index.html` for `HEADSHOT SWAP`. This is the single replacement point. Place the photo at `assets/img/headshot.jpg` and replace the initials avatar with the image element shown in that comment. Keep its alt text and explicit dimensions. The `.headshot` CSS rule handles cropping. The initials are intentional until a photo is supplied.

## Content TODO

Replace the `href="#"` on “Verify on Microsoft Learn” with the verified public credential-profile URL. A matching TODO comment marks the location, and the page labels it “Profile link coming soon”. No verification URL was supplied. The headshot replacement is optional.

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

## Local commit handoff in this environment

The session's filesystem policy makes this folder's `.git` read-only, so `git init -b main` here is denied. A local repository is prepared at `/private/tmp/gopinath-portfolio-local-history`, with this folder as its work tree. The verified commit is also preserved in `.local-history/initial-portfolio.bundle` so it survives temporary-directory cleanup. The bundle and QA artifacts are ignored and are not website files. No Git remote is configured and nothing is pushed.

Inspect the local commit while that temporary metadata is available:

```sh
git --git-dir=/private/tmp/gopinath-portfolio-local-history/.git --work-tree=. log -1
git --git-dir=/private/tmp/gopinath-portfolio-local-history/.git --work-tree=. status --short
```

To restore normal Git metadata in this folder later, run the following outside the restricted session. The fetch reads a **local file** and does not configure a remote:

```sh
git init -b main
git fetch .local-history/initial-portfolio.bundle main
git reset --mixed FETCH_HEAD
```
