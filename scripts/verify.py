#!/usr/bin/env python3
"""Check local references, anchors, structured metadata and public-file privacy."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
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
        self.in_schema = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
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
        if tag == 'script':
            self.in_schema = False

    def handle_data(self, data):
        if self.in_schema:
            self.schemas.append(json.loads(data))


errors = []
checked = 0
for html_file in sorted(ROOT.rglob('*.html')):
    if '.git' in html_file.parts:
        continue
    filename = html_file.relative_to(ROOT).as_posix()
    page = Page()
    page.feed(html_file.read_text())
    if len(page.ids) != len(set(page.ids)):
        errors.append(f'{filename}: duplicate IDs')
    for tag, attr, value in page.references:
        url = urlsplit(value)
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
        expected_headshot = {
            'src': 'assets/img/headshot.jpg', 'alt': 'Gopinath Gurusamy',
            'width': '400', 'height': '400', 'loading': 'eager',
            'fetchpriority': 'high', 'decoding': 'async',
        }
        if len(page.headshots) != 1 or any(page.headshots[0].get(key) != value for key, value in expected_headshot.items()):
            errors.append(f'{filename}: missing or incorrect hero headshot')
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

# Construct private-number signatures without placing them in public source.
private_signatures = [bytes((57, 53, 54, 54)), bytes((43, 57, 49))]
# Catch phone-like numbers even when spaces, parentheses or dashes are used.
# Alphanumeric boundaries exclude credential IDs and image/binary data.
phone_pattern = re.compile(r'(?<![\w])\+?\d(?:[\d ()\-\u00a0]{7,}\d)(?![\w])')
for file in ROOT.rglob('*'):
    if not file.is_file() or '.git' in file.parts or file.suffix.lower() in ('.pdf', '.bundle'):
        continue
    data = file.read_bytes()
    if any(signature in data for signature in private_signatures):
        errors.append(f'{file.relative_to(ROOT)}: private contact signature found')
    try:
        content = data.decode('utf-8')
    except UnicodeDecodeError:
        continue
    if any(10 <= sum(char.isdigit() for char in match.group()) <= 15 for match in phone_pattern.finditer(content)):
        errors.append(f'{file.relative_to(ROOT)}: phone-like number found')

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
print(f'PASS: {checked} local file references, anchors (no placeholder hrefs), supplied Learn links, five JSON-LD credentials, JPEG headshot, 1200 × 630 PNG and privacy scan (no phone numbers in repo text files).')
