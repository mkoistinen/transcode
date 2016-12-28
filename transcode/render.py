from . import regex

def render_simple(text, **kws):
    text = regex.url_re.sub(r'<a href="\g<0>">\g<0></a>', text)
    lines = multiline_splitter.split(text)
    if len(lines) == 1:
        return lines[0]

    return '\n    '.join(['<p>{}</p>'.format(line) for line in lines])
