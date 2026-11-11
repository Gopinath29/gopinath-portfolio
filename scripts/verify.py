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
        self.current_link = None
        self.in_header = False
        self.in_schema = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
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
        if link.get('target') != '_blank' or 'noopener' not in link.get('rel', '').split():
            errors.append(f'{filename}: credential link needs target=_blank and rel=noopener')
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
        for fact in ('generative orchestration', 'general knowledge and web search turned off', 'Assistant Action', 'Completed or Failed', '10 knowledge articles', 'test-case load', 'ALM runbook', 'Power Fx', 'PAC CLI', 'PowerShell', 'Azure DevOps/Git'):
            if not work or fact not in work.group():
                errors.append(f'{filename}: missing Case Assistant delivery fact {fact}')
        copilot = re.search(r'<section[^>]*id="copilot".*?</section>', html, re.S)
        ai_text = unescape(copilot.group() if copilot else '')
        for fact in ('AI & Copilot', 'Find and summarise a case', 'Find case documents', 'Suggest next steps', 'Create a case', 'Case summaries that include custom fields', 'Draft email replies', 'Knowledge-grounded answers with citations', 'Similar-case matching', 'AB-100', 'AB-620'):
            if fact not in ai_text:
                errors.append(f'{filename}: missing AI & Copilot fact {fact}')
        for url in VERIFICATION_URLS.values():
            if url not in ai_text:
                errors.append(f'{filename}: missing AI & Copilot credential link')
        if not work or 'a regulatory body' not in unescape(work.group()):
            errors.append(f'{filename}: featured client must be described as a regulatory body')
        for product in ('Case Assistant', 'Power Automate', 'Dataverse', 'Dynamics 365 Customer Service', 'Power Apps', 'Power Pages'):
            if not re.search(r'class="platform-card[^>]*>.*?<h3>' + re.escape(product) + r'</h3>.*?class="product-call"', html, re.S):
                errors.append(f'{filename}: missing supported product card with illustrative call: {product}')
        if 'data-terminal' not in html or 'id="terminal-command"' not in html or 'role="log"' not in html:
            errors.append(f'{filename}: missing accessible terminal widget')
        javascript = (ROOT / 'assets/js/main.js').read_text()
        for command in ('help', 'pac certs', 'pac contact', 'pac projects'):
            if "'" + command + "'" not in javascript:
                errors.append(f'{filename}: missing terminal command {command}')
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
        if not re.search(r'<div class="atmosphere"[^>]*aria-hidden="true"', html):
            errors.append(f'{filename}: missing decorative background layer')
    if filename == '404.html':
        # The 404 bootstrap requests assets only after resolving its project base.
        for value in re.findall(r"(?:stylesheet\.href|script\.src|icon\.href)\s*=\s*['\"]([^'\"]+)['\"]", html):
            page.references.append(('script' if value.endswith('.js?v=12') else 'link', 'src' if value.endswith('.js?v=12') else 'href', value))
            checked += 1
            if not (ROOT / urlsplit(value).path).is_file():
                errors.append(f'{filename}: missing bootstrap asset {value}')
        if "script.src = 'assets/js/main.js?v=12'" not in html:
            errors.append(f'{filename}: expected v=12 bootstrap JavaScript')
    for tag, attr, value in page.references:
        if (tag, attr) in (('link', 'href'), ('script', 'src')) and urlsplit(value).path in ('assets/css/styles.css', 'assets/js/main.js'):
            if urlsplit(value).query != 'v=12':
                errors.append(f'{filename}: expected v=12 cache-busting for {value}')
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
for directory, directories, filenames in os.walk(ROOT):
    directories[:] = [name for name in directories if name != '.git']
    for name in filenames:
        file = Path(directory) / name
        relative = file.relative_to(ROOT)
        if client_signature in relative.as_posix().casefold():
            errors.append('Repository filename contains the private client name')
        data = file.read_bytes()
        try:
            content = data.decode('utf-8')
        except UnicodeDecodeError:
            continue  # Binary assets only; all UTF-8 files are scanned regardless of extension.
        text_count += 1
        if client_signature in content.casefold():
            errors.append(f'{relative}: private client name found')
        # Include documentation and QA text as well as all published text assets.
        if any(value in content.casefold() for value in blocked_products):
            errors.append(f'{relative}: unsupported personal project found')
        if any(signature in data for signature in private_signatures):
            errors.append(f'{relative}: private contact signature found')
        if any(10 <= sum(char.isdigit() for char in match.group()) <= 15 for match in phone_pattern.finditer(content)):
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
print(f'PASS: {checked} local references; anchors; Learn links; five JSON-LD credentials; headshot; social PNG; header-only CV; 100+ flows; Case Assistant first; AI & Copilot facts and credentials; six supported product cards; accessible terminal; decorative background and reduced motion; v=12 assets; {text_count} UTF-8 files scanned; private client name and filename scan clear; published personal-project scan clear; phone privacy clear.')
