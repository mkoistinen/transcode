from . import regex
from . import conf

def render_simple(text, **kws):
    text = regex.url_re.sub(r'<a href="\g<0>">\g<0></a>', text)
    lines = multiline_splitter.split(text)
    if len(lines) == 1:
        return lines[0]


def render(text, format, cfg=None):
    if format == conf.SIMPLE_TEXT_FORMAT:
        return render_simple(text)

