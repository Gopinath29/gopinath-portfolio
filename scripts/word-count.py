#!/usr/bin/env python3
"""Count body-text whitespace tokens by section, excluding code and decorations.

Include all editorial disclosure text and both responsive menus, so collapsing or
hiding content cannot disguise its length. Omit script/style/SVG and aria-hidden
decoration; retain the visible metric digits and suffixes even when aria-hidden.
Use the same rule on saved baseline HTML and the current index.
"""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import json
import sys

VOID_TAGS = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
             'link', 'meta', 'param', 'source', 'track', 'wbr'}


class WordCounter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.counts = Counter()
        self.in_body = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get('class', '').split()
        if tag == 'body':
            self.in_body = True
        section = self.stack[-1][1] if self.stack else 'other'
        if tag == 'section' and attrs.get('id'):
            section = attrs['id']
        if tag in ('header', 'footer'):
            section = tag
        if {'delivery-metrics', 'chapter-divider'} & set(classes):
            section = 'metrics'
        if {'mobile-nav', 'skip-link'} & set(classes):
            section = 'navigation'
        if tag == 'section' and 'education-band' in classes:
            section = 'education-languages'
        excluded = ((self.stack[-1][2] if self.stack else False)
                    or tag in ('script', 'style', 'svg')
                    or 'atmosphere' in classes
                    or (attrs.get('aria-hidden') == 'true' and section != 'metrics'))
        if tag not in VOID_TAGS:
            self.stack.append((tag, section, excluded))

    def handle_endtag(self, tag):
        if tag == 'body':
            self.in_body = False
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if self.in_body and self.stack and not self.stack[-1][2]:
            self.counts[self.stack[-1][1]] += len(data.split())


def count_words(html):
    parser = WordCounter()
    parser.feed(html)
    return {'total': sum(parser.counts.values()), 'sections': {key: value for key, value in parser.counts.items() if value}}


if __name__ == '__main__':
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / 'index.html'
    print(json.dumps(count_words(source.read_text()), indent=2))
