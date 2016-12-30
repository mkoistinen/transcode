import pytest
from transcode import regex

LINES_TEXT = '''Hear are
some lines. These
lines span 3 lines

This is paragraph 2,
it spends 2 lines.
  
Paragraph 3 is a line line'''

URLS = [
    'http://foobarbaz.com/?search=findme',
    'https://user:password@example.com:8000/some-path_here?foo=bar&spam=eggs#hash'
]

URL_TEXT = '''Within this text block there should be 2 urls.

Here is the first one, very simple: {}

And here is the second, more complex one, {}, within the sentence.'''.format(*URLS)

class TestRegex:

    def test_multiline_splitter(self):
        result = regex.multiline_splitter(LINES_TEXT)
        assert len(result) == 3

    def test_urls(self):
        results = list(regex.url_re.finditer(URL_TEXT))
        assert len(results) == 2
        assert results[0].group() == URLS[0]
        assert results[1].group() == URLS[1]


