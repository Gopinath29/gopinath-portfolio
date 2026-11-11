#!/usr/bin/env python3
"""Check local references, anchors, structured metadata and public-file privacy."""
from html.parser import HTMLParser
from html import unescape
from pathlib import Path
from urllib.parse import unquote, urlsplit
import os
import json
import re
import struct
import sys
import runpy
import shutil
import subprocess

count_words = runpy.run_path(str(Path(__file__).with_name("word-count.py")))["count_words"]

ROOT = Path(__file__).resolve().parents[1]
VERIFICATION_URLS = {
    'AB-100': 'https://learn.microsoft.com/en-us/users/gopinathgurusamy-9343/credentials/71c8c88020980655',
    'AB-620': 'https://learn.microsoft.com/en-us/users/gopinathgurusamy-9343/credentials/33c24ca4ad0be38e',
}


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.ids = []
        self.schemas = []
        self.credential_links = []
        self.headshots = []
        self.links = []
        self.career_records = []
        self.current_link = None
        self.in_header = False
        self.in_schema = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'details' and 'career-record' in attrs.get('class', '').split():
            self.career_records.append(attrs)
        if tag == 'header':
            self.in_header = True
        if tag == 'a':
            self.current_link = {'attrs': attrs, 'text': '', 'in_header': self.in_header}
            self.links.append(self.current_link)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for key in ('href', 'src', 'poster'):
            if key in attrs:
                self.references.append((tag, key, attrs[key]))
        if tag == 'a' and urlsplit(attrs.get('href', '')).hostname == 'learn.microsoft.com':
            self.credential_links.append(attrs)
        if tag == 'img' and 'headshot' in attrs.get('class', '').split():
            self.headshots.append(attrs)
        self.in_schema = tag == 'script' and attrs.get('type') == 'application/ld+json'

    def handle_endtag(self, tag):
        if tag == 'a':
            self.current_link = None
        if tag == 'header':
            self.in_header = False
        if tag == 'script':
            self.in_schema = False

    def handle_data(self, data):
        if self.current_link is not None:
            self.current_link['text'] += data
        if self.in_schema:
            self.schemas.append(json.loads(data))


def repository_files():
    for directory, directories, filenames in os.walk(ROOT):
        directories[:] = [name for name in directories if name != '.git']
        for name in filenames:
            yield Path(directory) / name


errors = []
checked = 0
for html_file in sorted(file for file in repository_files() if file.suffix == '.html'):
    filename = html_file.relative_to(ROOT).as_posix()
    page = Page()
    html = html_file.read_text()
    page.feed(html)
    if len(page.ids) != len(set(page.ids)):
        errors.append(f'{filename}: duplicate IDs')
    for link in page.links:
        attrs = link['attrs']
        href = attrs.get('href', '')
        url = urlsplit(href)
        if url.scheme in ('http', 'https', 'mailto') or url.netloc:
            if attrs.get('target') != '_blank' or not {'noopener', 'noreferrer'} <= set(attrs.get('rel', '').split()):
                errors.append(f'{filename}: external link needs target=_blank and rel=noopener noreferrer: {href}')
            name = attrs.get('aria-label') or link['text']
            if 'opens in new tab' not in name.casefold():
                errors.append(f'{filename}: external link needs accessible opens in new tab hint: {href}')
        elif href.startswith(('#', './')) or href == 'assets/resume/Gopinath_Gurusamy_Resume.pdf?v=15':
            if attrs.get('target') == '_blank':
                errors.append(f'{filename}: navigation and CV links must stay same-tab: {href}')
        else:
            errors.append(f'{filename}: unrecognised same-tab link exception: {href}')
    for tag, attr, value in page.references:
        url = urlsplit(value)  # Check only the path; allow cache-busting queries.
        if attr == 'href' and (not value.strip() or value.strip() == '#'):
            errors.append(f'{filename}: empty or placeholder href')
        if url.scheme or url.netloc:
            if attr == 'src' or (tag == 'link' and attr == 'href' and not url.path.endswith('/gopinath-portfolio/')):
                errors.append(f'{filename}: non-relative asset {value}')
            continue
        if value.startswith('/'):
            errors.append(f'{filename}: root-relative reference {value}')
        if url.path:
            if not (ROOT / unquote(url.path)).exists():
                errors.append(f'{filename}: missing asset {value}')
            checked += 1
        elif url.fragment and unquote(url.fragment) not in page.ids:
            errors.append(f'{filename}: missing anchor {value}')
    for link in page.credential_links:
        if link['href'] not in VERIFICATION_URLS.values():
            errors.append(f'{filename}: unknown Microsoft Learn verification URL')
        if link.get('target') != '_blank' or not {'noopener', 'noreferrer'} <= set(link.get('rel', '').split()):
            errors.append(f'{filename}: credential link needs target=_blank and rel=noopener noreferrer')
    if filename == 'index.html' and {link['href'] for link in page.credential_links} != set(VERIFICATION_URLS.values()):
        errors.append(f'{filename}: missing supplied Microsoft Learn verification links')
    if filename == 'index.html':
        # Check the named metric in context; unrelated 20+ figures are allowed.
        plain_html = unescape(html)
        text = re.sub(r'<[^>]+>', ' ', plain_html)
        old_flows = r'(?<![\w])20\s*\+\s*(?:Power\s+Automate\s+)?flows\b|Power\s+Automate\s+flows[^.!?;<>]{0,80}?(?<![\w])20\s*\+'
        if any(re.search(old_flows, value, re.I) for value in (plain_html, text)):
            errors.append(f'{filename}: Power Automate flows must not use the old 20+ figure')
        flows_stat = re.search(r'<dt>\s*Power Automate flows coordinated in that programme\s*</dt>\s*<dd>(.*?)</dd>', plain_html, re.S)
        if not flows_stat or re.sub(r'<[^>]+>', '', flows_stat.group(1)).strip() != '100+':
            errors.append(f'{filename}: flows stat must visibly contain 100+ (including without CSS/JS)')
        if flows_stat:
            stat = flows_stat.group(1)
            if not all(re.search(rf'\b{attr}=[\"\']100[\"\']', stat) for attr in ('data-count', 'data-target')):
                errors.append(f'{filename}: flows counter must target 100')
            if not re.search(r'aria-label=[\"\']100\+ Power Automate flows[\"\']', stat):
                errors.append(f'{filename}: flows accessible text must say 100+ Power Automate flows')
        for forbidden in ('AU/NZ', 'notice period', 'UK & EU mornings', '01 / Profile', 'panel-footer', 'portrait-credentials'):
            if forbidden.casefold() in unescape(html).casefold():
                errors.append(f'{filename}: forbidden hero content {forbidden!r}')
        if len(page.schemas) != 1:
            errors.append(f'{filename}: expected one Person JSON-LD block')
        hero = re.search(r'<section class="hero(?: [^"]*)?".*?</section>', html, re.S)
        if not hero or any(hero.group().count(code) != 1 for code in ('PL-600', '<strong>AB-100</strong>')):
            errors.append(f'{filename}: expected one hero credential display per featured credential')
        cv_links = [link for link in page.links if re.search(r'\bdownload\s+cv\b', link['text'], re.I)]
        if len(cv_links) != 1 or not cv_links[0]['in_header']:
            errors.append(f'{filename}: expected exactly one Download CV link, in the header')
        for link in page.links:
            if urlsplit(link['attrs'].get('href', '')).path.endswith('/Gopinath_Gurusamy_Resume.pdf') and not link['in_header']:
                errors.append(f'{filename}: CV link outside the header')
        for link in page.links:
            if 'PL-600' in link['text'] or 'PL-600' in link['attrs'].get('aria-label', ''):
                errors.append(f'{filename}: PL-600 must be plain text, never linked')
        if not re.search(r'>0[1-9] // ', html):
            errors.append(f'{filename}: missing numbered double-slash labels')
        work = re.search(r'<section[^>]*id="work".*?</section>', html, re.S)
        project_titles = re.findall(r'<h3>(.*?)</h3>', work.group() if work else '', re.S)
        if not project_titles or project_titles[0] != 'Case Assistant':
            errors.append(f'{filename}: Case Assistant must be the first Work project')
        for topic in ('Find and summarise a case', 'Find case documents', 'Suggest next steps', 'Create a case'):
            if not work or topic not in work.group():
                errors.append(f'{filename}: missing Case Assistant topic {topic}')
        for fact in ('Power Fx', 'PAC CLI', 'PowerShell', 'Azure DevOps/Git'):
            if not work or fact not in work.group():
                errors.append(f'{filename}: missing Case Assistant technology {fact}')
        if work and 'contribution-list' in work.group():
            errors.append(f'{filename}: remove the long contribution list')
        copilot = re.search(r'<section[^>]*id="copilot".*?</section>', html, re.S)
        ai_text = unescape(copilot.group() if copilot else '')
        for fact in ('AI & Copilot', 'Dynamics 365 Customer Service', 'Case summaries that include custom fields', 'Draft email replies', 'Knowledge-grounded answers with citations', 'Similar-case matching'):
            if fact not in ai_text:
                errors.append(f'{filename}: missing AI & Copilot fact {fact}')
        if 'href="#case-assistant"' not in ai_text:
            errors.append(f'{filename}: AI & Copilot must link to Case Assistant work')
        if any(url in ai_text for url in VERIFICATION_URLS.values()):
            errors.append(f'{filename}: AI & Copilot must not repeat credential verify links')
        for topic in ('Find and summarise a case', 'Find case documents', 'Suggest next steps', 'Create a case'):
            if topic in ai_text:
                errors.append(f'{filename}: AI & Copilot must not repeat Work topics')
        credentials_section = re.search(r'<section[^>]*id="certifications".*?</section>', html, re.S)
        for url in VERIFICATION_URLS.values():
            if not credentials_section or url not in credentials_section.group():
                errors.append(f'{filename}: Credentials must retain supplied Learn links')
        if sum(link['href'] == VERIFICATION_URLS['AB-100'] for link in page.credential_links) != 2 or sum(link['href'] == VERIFICATION_URLS['AB-620'] for link in page.credential_links) != 1:
            errors.append(f'{filename}: credential verify links belong only in hero and Credentials')
        hero_text = unescape(re.sub(r'<[^>]+>', ' ', hero.group() if hero else ''))
        hero_text = re.sub(r'\s+', ' ', hero_text)
        if hero_text.count('Architecture that holds up. Engineering that follows through.') != 1:
            errors.append(f'{filename}: hero must retain its single strongest tagline')
        for dropped in ('Design authority.', 'Hands-on delivery.', 'Solution architecture. Personal ownership.'):
            if dropped in hero_text:
                errors.append(f'{filename}: redundant hero tagline remains')
        about = re.search(r'<section[^>]*id="about".*?</section>', html, re.S)
        about_text = unescape(about.group() if about else '')
        for fact in ('Education', 'Languages', 'B.Tech, Information Technology', 'Kongu Engineering College', '2009–2013', 'English', 'Professional', 'Tamil', 'Native'):
            if fact not in about_text:
                errors.append(f'{filename}: About must contain education/languages fact {fact}')
        counts = count_words(html)
        if not 1100 <= counts['total'] <= 1300:
            errors.append(f'{filename}: total word count must be 1100–1300')
        if not 320 <= counts['sections'].get('work', 0) <= 380:
            errors.append(f'{filename}: Work must be about 350 words (320–380)')
        if not work or 'a regulatory body' not in unescape(work.group()):
            errors.append(f'{filename}: featured client must be described as a regulatory body')
        cards = re.findall(r'<article class="platform-card.*?</article>', html, re.S)
        if len(cards) != 6:
            errors.append(f'{filename}: expected exactly six product cards')
        for product in ('Case Assistant', 'Power Automate', 'Dataverse', 'Dynamics 365 Customer Service', 'Power Apps', 'Power Pages'):
            matching = [card for card in cards if '<h3>' + product + '</h3>' in card]
            if len(matching) != 1 or 'class="product-call"' not in matching[0]:
                errors.append(f'{filename}: missing supported product card with illustrative call: {product}')
            if product == 'Power Automate' and matching and '100+' in matching[0]:
                errors.append(f'{filename}: Power Automate card must not repeat 100+')
        capability_lines = [re.findall(r'<p>(.*?)</p>', card, re.S) for card in cards]
        if any(len(lines) != 1 for lines in capability_lines) or len({lines[0] for lines in capability_lines if lines}) != 6:
            errors.append(f'{filename}: product cards need six distinct capability lines')
        if 'data-terminal' not in html or 'id="terminal-command"' not in html or 'role="log"' not in html:
            errors.append(f'{filename}: missing accessible terminal widget')
        javascript = (ROOT / 'assets/js/main.js').read_text()
        for command in ('help', 'pac certs', 'pac contact', 'pac projects', 'pac copilot'):
            if "'" + command + "'" not in javascript:
                errors.append(f'{filename}: missing terminal command {command}')
        if 'verify links in AI & Copilot' in javascript:
            errors.append(f'{filename}: terminal must point credential verification to Credentials')
        if len(re.findall(r'class="solution-card(?: [^\"]*)?"', work.group() if work else '')) != 5:
            errors.append(f'{filename}: expected featured solution and four retained case studies')
        expected_headshot = {
            'src': 'assets/img/headshot.jpg', 'alt': 'Gopinath Gurusamy',
            'width': '400', 'height': '400', 'loading': 'eager',
            'fetchpriority': 'high', 'decoding': 'async',
        }
        if len(page.headshots) != 1 or any(page.headshots[0].get(key) != value for key, value in expected_headshot.items()):
            errors.append(f'{filename}: missing or incorrect hero headshot')
    if filename in ('index.html', '404.html'):
        wordmarks = [link for link in page.links if 'wordmark' in link['attrs'].get('class', '').split()]
        action = 'back to top' if filename == 'index.html' else 'home'
        target = '#top' if filename == 'index.html' else './'
        if len(wordmarks) != 1 or wordmarks[0]['text'].strip() != 'GG' or wordmarks[0]['attrs'].get('aria-label') != f'GG, Gopinath Gurusamy, {action}' or wordmarks[0]['attrs'].get('href') != target:
            errors.append(f'{filename}: expected accessible GG wordmark and original target')
        if filename == 'index.html' and (len(page.career_records) != 5 or any('open' in record or 'aria-expanded' in record for record in page.career_records)):
            errors.append(f'{filename}: expected five native career records closed by default')

        if not re.search(r'<div class="atmosphere"[^>]*aria-hidden="true"', html):
            errors.append(f'{filename}: missing decorative background layer')
    if filename == '404.html':
        # The 404 bootstrap requests assets only after resolving its project base.
        for value in re.findall(r"(?:stylesheet\.href|script\.src|icon\.href)\s*=\s*['\"]([^'\"]+)['\"]", html):
            page.references.append(('script' if value.endswith('.js?v=17') else 'link', 'src' if value.endswith('.js?v=17') else 'href', value))
            checked += 1
            if not (ROOT / urlsplit(value).path).is_file():
                errors.append(f'{filename}: missing bootstrap asset {value}')
        if "script.src = 'assets/js/main.js?v=17'" not in html:
            errors.append(f'{filename}: expected v=17 bootstrap JavaScript')
    for tag, attr, value in page.references:
        if (tag, attr) in (('link', 'href'), ('script', 'src')) and urlsplit(value).path in ('assets/css/styles.css', 'assets/js/main.js'):
            if urlsplit(value).query != 'v=17':
                errors.append(f'{filename}: expected v=17 cache-busting for {value}')
    for schema in page.schemas:
        if schema.get('@type') != 'Person' or 'telephone' in schema:
            errors.append(f'{filename}: incorrect Person metadata')
        credentials = schema.get('hasCredential', [])
        if {credential.get('identifier') for credential in credentials} != {'PL-600', 'AB-100', 'AB-620', 'PL-400', 'PL-100'} or len(credentials) != 5:
            errors.append(f'{filename}: expected five Microsoft credentials')
        for credential in credentials:
            if credential.get('@type') != 'EducationalOccupationalCredential':
                errors.append(f'{filename}: incorrect credential metadata type')
            expected = VERIFICATION_URLS.get(credential.get('identifier'))
            if (expected and credential.get('url') != expected) or (not expected and 'url' in credential):
                errors.append(f'{filename}: incorrect credential verification metadata')

css = (ROOT / 'assets/css/styles.css').read_text()
if not re.search(r'@media\s*\(prefers-reduced-motion:\s*reduce\)\s*\{\.atmosphere\{display:none!important', css):
    errors.append('Background must be fully disabled under reduced motion')

# The browser suite additionally checks pixels and elapsed animation time.
javascript = (ROOT / 'assets/js/main.js').read_text()
star_count = re.search(r'for \(let i = 0; i < (\d+); i\+\+\)', javascript)
if not star_count or not 80 <= int(star_count.group(1)) <= 120:
    errors.append('Dark scenery must create 80–120 stars')
if '--star-size' not in javascript or '--star-size' not in css:
    errors.append('Dark scenery must keep mixed star sizes')
if not re.search(r'\.atmosphere\{[^}]*z-index:0;', css):
    errors.append('Background must paint above the page wash')
if 'animation:shoot 12s' not in css or 'animation-delay:-6.55s' not in css:
    errors.append('Dark shooting trails must retain their six-second stagger')

# Construct private-number signatures without placing them in public source.
private_signatures = [bytes((57, 53, 54, 54)), bytes((43, 57, 49))]
# Catch phone-like numbers even when spaces, parentheses or dashes are used.
# Alphanumeric boundaries exclude credential IDs and image/binary data.
phone_pattern = re.compile(r'(?<![\w])\+?\d(?:[\d ()\-\u00a0]{7,}\d)(?![\w])')
# Prune .git before traversing: no repository metadata is read or modified.
client_signature = bytes((67, 67, 80, 67)).decode().casefold()
blocked_products = tuple(bytes(value).decode().casefold() for value in (
    (83,101,108,108,101,114,74,111,121),
    (83,116,111,99,107,32,68,101,115,107),
    (71,83,84,32,70,105,108,105,110,103),
))
text_count = 0
pdf_count = 0
pdftotext = shutil.which('pdftotext')
for directory, directories, filenames in os.walk(ROOT):
    directories[:] = [name for name in directories if name != '.git']
    for name in filenames:
        file = Path(directory) / name
        relative = file.relative_to(ROOT)
        if client_signature in relative.as_posix().casefold():
            errors.append('Repository filename contains the private client name')
        data = file.read_bytes()
        is_pdf = file.suffix.casefold() == '.pdf'
        if is_pdf:
            pdf_count += 1
            if not pdftotext:
                errors.append(f'{relative}: PDF privacy check requires pdftotext (install Poppler; see README.md)')
                continue
            try:
                extracted = subprocess.run(
                    [pdftotext, '-layout', str(file), '-'],
                    capture_output=True, text=True, encoding='utf-8', timeout=30, check=True,
                )
                content = extracted.stdout
                data = content.encode('utf-8')
            except (OSError, subprocess.SubprocessError, UnicodeError):
                errors.append(f'{relative}: PDF text extraction failed; privacy could not be checked')
                continue
        else:
            try:
                content = data.decode('utf-8')
            except UnicodeDecodeError:
                continue  # Other binary assets; PDFs are extracted above.
            text_count += 1
        if client_signature in content.casefold():
            errors.append(f'{relative}: private client name found')
        # Include documentation and QA text as well as all published text assets.
        if any(value in content.casefold() for value in blocked_products):
            errors.append(f'{relative}: unsupported personal project found')
        if any(signature in data for signature in private_signatures):
            errors.append(f'{relative}: private contact signature found')
        # Skip gitignored QA JSON (animation timings look like phone numbers). Still scan those files for client/product names.
        if (is_pdf or 'qa-artifacts' not in relative.parts) and any(10 <= sum(char.isdigit() for char in match.group()) <= 15 for match in phone_pattern.finditer(content)):
            errors.append(f'{relative}: phone-like number found')

headshot = ROOT / 'assets/img/headshot.jpg'
if not headshot.is_file() or not headshot.read_bytes().startswith(b'\xff\xd8\xff'):
    errors.append('Missing or invalid JPEG headshot')

png = ROOT / 'assets/img/og-image.png'
if png.exists():
    data = png.read_bytes()
    if data[:8] != b'\x89PNG\r\n\x1a\n' or struct.unpack('>II', data[16:24]) != (1200, 630):
        errors.append('Social image must be a 1200 × 630 PNG')
else:
    errors.append('Missing social PNG')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'PASS: {checked} local references; anchors; Learn links; five JSON-LD credentials; headshot; social PNG; accessible GG headers; five closed native career records; header-only CV; 100+ flows; Case Assistant first; AI & Copilot features and work link; credential placement; single tagline; education/languages in About; word limits; six supported product cards; accessible terminal; 104 mixed stars; six-second trails; decorative background and reduced motion; v=17 assets; {text_count} UTF-8 files and {pdf_count} PDFs scanned; private client name and filename scan clear; published personal-project scan clear; text and PDF phone privacy clear.')
