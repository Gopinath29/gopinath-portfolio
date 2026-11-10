# Gopinath Gurusamy — portfolio v3

An original static résumé for a Dynamics 365 CE / Power Platform Solution Architect and Technical Lead. The follow-up retains the v3 case studies, connected career records, terminal and factual content, while adopting the live reference’s sky-blue and navy visual tokens, glass panels and section rhythm.

Case Assistant leads Work with the subtitle “Copilot Studio agent for Dynamics 365 Customer Service”. Its client is described only as a regulatory body. AI & Copilot presents the four delivered topics, configured Dynamics 365 Copilot features and supplied AB-100 / AB-620 verification links. Six product cards cover Case Assistant, Power Automate, Dataverse, Dynamics 365 Customer Service, Power Apps and Power Pages. Monospaced call lines are illustrative.

## Preview

```sh
python3 -m http.server 8093 --bind 127.0.0.1
```

Open <http://127.0.0.1:8093/>. Reuse an existing preview of this repository on that port. The current optional Pages-style handler is `qa-artifacts/v3-pages-preview.py`; it additionally simulates the `/gopinath-portfolio/` prefix and nested custom 404 responses. Leave the existing preview services on other ports alone.

## Static hosting and fonts

GitHub Pages serves the repository root at <https://gopinath29.github.io/gopinath-portfolio/>. No build step, framework, backend, analytics or production dependencies are required. CSS and JavaScript paths are relative and use `?v=11`. The 404 page shares the same theme and type system and resolves the project base before loading its assets.

Sora headings, Plus Jakarta Sans body text and JetBrains Mono labels, credentials and terminal are self-hosted in `assets/fonts/`. The variable fonts come from the official [Google Fonts repository](https://github.com/google/fonts), with their OFL notices beside them. The site needs no font CDN.

## Content and interactions

- Theme selection persists; system colour preference applies until a valid selection is saved. Storage failure still allows switching. Reduced motion disables animation, transitions and smooth scrolling.
- All five career records, four earlier case studies, services, expertise, certifications, education, languages, writing and contact facts remain. Native disclosures retain their detailed content. Related links open career records.
- The terminal accepts `help`, `pac certs`, `pac contact`, `pac projects`, `pac copilot` and `clear`. Use Enter or Run. It is a local portfolio interaction; output is text and does not execute system commands.
- PL-600 remains plain text; the hero contains one PL-600 / linked AB-100 pair. AB-100 and AB-620 retain the supplied Microsoft Learn links. Download CV appears once, in the header.
- The healthcare programme figure remains **100+ Power Automate flows** in visible text, accessible text, counter targets and no-CSS fallback.
- Core content and native disclosures remain available without JavaScript. Semantic landmarks, keyboard focus, labelled input, a live terminal log and real text spacing support accessibility.
- Public repository text contains no phone number; the existing binary CV PDF is the specified exception. The client name is not published.

## Checks

```sh
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

The verifier scans all UTF-8 repository files and filenames for the private client name, pruning `.git` before traversal. It also rejects unsupported personal-project names in published assets, documentation and QA text. Negative regression probes prove that these checks fail when prohibited content is introduced and pass after cleanup.

Generate the original 1200 × 630 light-theme social PNG and SVG companion with `UV_CACHE_DIR=/private/tmp/portfolio-uv-cache uv run --with pillow scripts/generate_og.py`. Pillow is only a development dependency; the generator uses the same local fonts as the site.

See [E2E_REPORT.md](E2E_REPORT.md) and [VERIFICATION.md](VERIFICATION.md) for current test evidence and browser-access limits. Historical screenshots must not be treated as verification of this follow-up.

## Design provenance

Visual token values were extracted with curl from the inline stylesheet at [ramyachinnadurai.com](https://ramyachinnadurai.com/). The complete list and measured typography, spacing, radii and shadows are saved outside this repository at `~/portfolio-src/REFERENCE_TOKENS.md`. Storytelling, related career records, product accents, numbered mono labels, a small terminal, glass surfaces and portrait-first narrow layouts inform the design. All portfolio markup, styles and interaction logic are original; no reference implementation, copy, photo, illustration or other asset was copied or vendored.

`LICENSE-TEMPLATE.md` remains unchanged as historical documentation of the earlier Astrofy adaptation. The original HTML backup remains at `~/portfolio-src/index-before-v3.html`. No commit, push, deployment or repository metadata modification was performed.
