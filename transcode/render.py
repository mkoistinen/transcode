from . import regex
from . import conf
from markdown2 import Markdown
from docutils.core import  publish_parts


def render_simple(source, *args, **kwargs):
    source = regex.url_re.sub(r'<a href="\g<0>">\g<0></a>', source)
    lines = regex.multiline_splitter(source)
    return '\n'.join(['<p>{}</p>'.format(p) for p in lines])


def render_markdown(source, *args, **kwargs):
    return Markdown().convert(source)


def render_restructuredtext(source, *args, **kwargs):
    result = publish_parts(source, writer_name='html4css1')
    return result['html_body']


def render_html(source, *args, **kwargs):
    return source


def render(source, format, cfg=None):
    transcoder, args, kwargs = conf.get_transcoder(format, cfg)
    return transcoder(source, *args, **kwargs)





