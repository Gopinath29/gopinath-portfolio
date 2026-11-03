#!/usr/bin/env python3
"""Check local references, anchors, structured metadata and public-file privacy."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import struct
import sys

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.ids = []
        self.schemas = []
        self.in_schema = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for key in ('href', 'src', 'poster'):
            if key in attrs:
                self.references.append((tag, key, attrs[key]))
        self.in_schema = tag == 'script' and attrs.get('type') == 'application/ld+json'

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_schema = False

    def handle_data(self, data):
        if self.in_schema:
            self.schemas.append(json.loads(data))


errors = []
checked = 0
for filename in ('index.html', '404.html'):
    page = Page()
    page.feed((ROOT / filename).read_text())
    if len(page.ids) != len(set(page.ids)):
        errors.append(f'{filename}: duplicate IDs')
    for tag, attr, value in page.references:
        url = urlsplit(value)
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
        # A lone # is the explicitly requested Microsoft Learn placeholder.
    for schema in page.schemas:
        if schema.get('@type') != 'Person' or 'telephone' in schema:
            errors.append(f'{filename}: incorrect Person metadata')

# Construct private-number signatures without placing them in public source.
private_signatures = [bytes((57, 53, 54, 54)), bytes((43, 57, 49))]
for file in ROOT.rglob('*'):
    if not file.is_file() or '.git' in file.parts or file.suffix.lower() in ('.pdf', '.bundle'):
        continue
    data = file.read_bytes()
    if any(signature in data for signature in private_signatures):
        errors.append(f'{file.relative_to(ROOT)}: private contact signature found')

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
print(f'PASS: {checked} local file references, anchors, Person JSON-LD, 1200 × 630 PNG and privacy scan.')
