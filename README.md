# Gopinath Gurusamy — portfolio v5

An original static résumé for a Dynamics 365 CE / Power Platform Solution Architect and Technical Lead. V5 trims the page; the current page has 1,243 words, including accessible new-tab hints, while retaining the V4 sky/cloud and navy/star backgrounds, teal-blue accents and hero composition. White glass cards and the existing fonts and section rhythm remain.

Case Assistant leads Work with the subtitle “Copilot Studio agent for Dynamics 365 Customer Service”. Its client is described only as a regulatory body. The 350-word Work section holds the four Case Assistant topics and four shorter real case studies. AI & Copilot covers the four configured Dynamics 365 Copilot features and links to Work; supplied AB-100 / AB-620 verification links stay in Credentials, with the single linked AB-100 hero exception. Six product cards cover Case Assistant, Power Automate, Dataverse, Dynamics 365 Customer Service, Power Apps and Power Pages. Monospaced call lines are illustrative.

## Preview

```sh
python3 -m http.server 8093 --bind 127.0.0.1
```

Open <http://127.0.0.1:8093/>. Reuse an existing preview of this repository on that port. V5 QA uses the plain Python server above. The historical optional Pages-style handler is `qa-artifacts/v3-pages-preview.py`; it additionally simulates the `/gopinath-portfolio/` prefix and nested custom 404 responses. Leave the existing preview services on other ports alone.

## Static hosting and fonts

GitHub Pages serves the repository root at <https://gopinath29.github.io/gopinath-portfolio/>. No build step, framework, backend, analytics or production dependencies are required. CSS and JavaScript paths are relative and use `?v=18`. The header CV link uses `?v=15` and explicitly preserves the download filename `Gopinath_Gurusamy_Resume.pdf`. The 404 page shares the same theme and type system and resolves the project base before loading its assets.

Sora headings, Plus Jakarta Sans body text and JetBrains Mono labels, credentials and terminal are self-hosted in `assets/fonts/`. The variable fonts come from the official [Google Fonts repository](https://github.com/google/fonts), with their OFL notices beside them. The site needs no font CDN.

## Content and interactions

- Home and 404 headers show the circular headshot plus bold Sora “GG” at desktop and mobile widths. Accessible link names include GG, the full name and the destination.
- The hero uses one tagline: “Architecture that holds up. Engineering that follows through.” It pairs a compact portrait/profile rail with the headline, followed by a separate credential/action band. On small screens the portrait becomes a compact horizontal identity card. PL-600 and linked AB-100 stay together near the top.
- Original CSS/SVG scenery sits behind the page: three drifting clouds and two small rockets with fading smoke puffs and flickering nozzle flames in light mode; 104 twinkling stars and two occasional shooting trails in dark mode. It is decorative, fixed, pointer-transparent and uses transform/opacity animations. There is no JavaScript render loop, particle dependency or downloaded artwork.
- Theme selection persists; system colour preference applies until a valid selection is saved. Storage failure still allows switching. Reduced motion removes the entire scenery layer and disables animation, transitions and smooth scrolling. Visibility changes pause and resume the CSS animation timelines; the other theme’s scene is removed from rendering.
- All five career records and five Work projects remain in concise form. All five career records start collapsed and retain native disclosures; summary clicks, Enter/Space, related links and direct hashes open them. Education and languages now sit within About. Services, expertise, certifications, writing and contact remain.
- The terminal accepts `help`, `pac certs`, `pac contact`, `pac projects`, `pac copilot` and `clear`. Use Enter or Run. It is a local portfolio interaction; output is text and does not execute system commands.
- PL-600 remains plain text; the hero contains one PL-600 / linked AB-100 pair. AB-100 and AB-620 retain the supplied Microsoft Learn links. Download CV appears once, in the header.
- The healthcare programme figure remains **100+ Power Automate flows** in visible text, accessible text, counter targets and no-CSS fallback.
- Core content and native disclosures remain available without JavaScript. Semantic landmarks, keyboard focus, labelled input, a live terminal log and real text spacing support accessibility.
- Public repository text and the public recruiter CV PDF contain no phone number or private client name. The CV describes the client only as a regulatory body.

## Word count and checks

Run `scripts/word-count.py` for the full per-section count. It counts body-text whitespace tokens, including disclosures and both responsive menus; scripts, styles, SVG and decorative aria-hidden text are excluded, while metric digits remain. The same method gives 2,038 before, 1,211 after the original trim, and 1,243 with the accessible new-tab hints. See the report and `qa-artifacts/v5-word-counts.json` for the historical trim comparison; `qa-artifacts/gg-header-word-counts.json` holds the current count.

PDF privacy verification requires Poppler (`pdftotext`) as a development tool, with no production dependency. On macOS install it with `brew install poppler`. If Homebrew is unavailable or read-only, install [micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html) outside the repository and run:

```sh
mkdir -p /private/tmp/cv-swap-poppler/conda-meta
touch /private/tmp/cv-swap-poppler/conda-meta/history
XDG_CACHE_HOME=/private/tmp/cv-swap-cache MAMBA_ROOT_PREFIX=/private/tmp/cv-swap-mamba CONDA_PKGS_DIRS=/private/tmp/cv-swap-mamba/pkgs micromamba --no-rc install -y -p /private/tmp/cv-swap-poppler -c conda-forge poppler=26.11.0
export PATH="/private/tmp/cv-swap-poppler/bin:$PATH"
```

```sh
python3 scripts/word-count.py
python3 scripts/verify.py
python3 scripts/test-verifier.py
node --check assets/js/main.js
npx --yes html-validate@10.17.0 index.html 404.html
```

The optional DOM suite uses jsdom installed outside the repository:

```sh
npm install --prefix /private/tmp/portfolio-v3-test jsdom@26.1.0 --no-audit --no-fund
NODE_PATH=/private/tmp/portfolio-v3-test/node_modules node scripts/test-interactions.cjs
```

The verifier scans all UTF-8 repository files and filenames for the private client name, pruning `.git` before traversal. It extracts every PDF with `pdftotext -layout` and applies the same privacy rules, including phone checks in QA PDFs. Missing Poppler or failed PDF extraction fails verification. It also rejects unsupported personal-project names in published assets, documentation and QA text. The verifier also enforces the 1,100–1,300 total / about-350 Work word limits, V5 credential/topic placement, single tagline, distinct product capabilities and About education. Forty-four regression assertions verify broken fixtures are rejected and cleaned up, including compressed PDF privacy probes generated temporarily and removed after each check.

Generate the original 1200 × 630 light-theme social PNG and SVG companion with `UV_CACHE_DIR=/private/tmp/portfolio-uv-cache uv run --with pillow scripts/generate_og.py`. Pillow is only a development dependency; the generator uses the same local fonts as the site.

See [E2E_REPORT.md](E2E_REPORT.md) and [VERIFICATION.md](VERIFICATION.md) for current test evidence and browser-access limits. Historical screenshots must not be treated as verification of this follow-up.

## Preserved V4 accents and current V5 browser QA

Light: accent/button `#075d73`, link/heading ink `#064c60`, secondary accent `#087e96`. Dark: accent/link/button `#80ded5`, highlight `#73dbdf`, button ink `#081631`. Focus uses the theme accent; terminal controls use their high-contrast panel highlight.

The light sky base is `#91d6ff` to give the accent enough contrast; dark glow alpha is `.02` and star/trail opacity is bounded to preserve muted text contrast. Measured text minima are 4.55:1 in both themes; tested UI boundaries are at least 4.70:1. See the report for the conservative scenery/gradient model and its limits.

```sh
PLAYWRIGHT_BROWSERS_PATH=/private/tmp/portfolio-v3-pw/browsers node /private/tmp/portfolio-v3-pw/v5-playwright-runner.cjs
NODE_PATH=/private/tmp/portfolio-v3-pw/node_modules PLAYWRIGHT_BROWSERS_PATH=/private/tmp/portfolio-v3-pw/browsers node scripts/test-browser.cjs
```

This uses cached headless Chromium outside the repo with `--single-process --no-zygote`. The current browser assertion totals are recorded in VERIFICATION.md. Eight DPR 1 top captures and one full light page are in `qa-artifacts/v5-*.png`; results are in `qa-artifacts/v5-playwright-results.json`. No user browser app or profile is used.

## Design provenance

The earlier v3 visual study extracted tokens with curl from the inline stylesheet at [ramyachinnadurai.com](https://ramyachinnadurai.com/). V4 deliberately changes the accent palette and hero composition and adds original background geometry. The complete list and measured typography, spacing, radii and shadows are saved outside this repository at `~/portfolio-src/REFERENCE_TOKENS.md`. Storytelling, related career records, product accents, numbered mono labels, a small terminal, glass surfaces and portrait-first narrow layouts inform the design. All portfolio markup, styles and interaction logic are original; no reference implementation, copy, photo, illustration or other asset was copied or vendored.

`LICENSE-TEMPLATE.md` remains unchanged as historical documentation of the earlier Astrofy adaptation. The original HTML backup remains at `~/portfolio-src/index-before-v3.html`.
