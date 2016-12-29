from . import regex
from . import conf
from markdown2 import Markdown
from docutils.core import  publish_parts


def render_simple(text, cfg=None):
    text = regex.url_re.sub(r'<a href="\g<0>">\g<0></a>', text)
    lines = multiline_splitter.split(text)
    return '\n'.join(['<p>{}</p>'.format(p) for p in lines])


def render_markdown(source, cfg=None):
    return Markdown().convert(source)


def render_restructuredtext(source, cfg=None):
    result = publish_parts(source, writer_name='html4css1')
    return result['html_body']


def render(source, format, cfg=None):
    if format == conf.SIMPLE_TEXT_FORMAT:
        result = render_simple(source, cfg)
    elif format == conf.HTML_FORMAT:
        result = source
    elif format == conf.MARKDOWN_FORMAT:
        result = render_markdown(source, cfg)
    elif format == conf.RST_FROMAT:
        result = render_restructuredtext(source, cfg)
    else:
        raise ValueError('Unknown format "{}"'.format(format))

    return result





