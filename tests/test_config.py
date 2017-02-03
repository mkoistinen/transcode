import pytest
import transcode.conf
import transcode.render

def my_callback(source, *args, **kws):
    pass



CFG_GOOD = {
    'TEXT': {'transcoder': my_callback},
}

CFG_BAD = {
    'MARK': {'transcoder': 42}
}

class TestConf:

    def test_default_config(self):
        for fmt, expected in (
            (transcode.conf.HTML_FORMAT, transcode.render.render_html),
            (transcode.conf.SIMPLE_TEXT_FORMAT, transcode.render.render_simple),
            (transcode.conf.MARKDOWN_FORMAT, transcode.render.render_markdown),
            (transcode.conf.RST_FORMAT, transcode.render.render_restructuredtext),
        ):
            handler, args, kwargs = transcode.conf.get_transcoder(fmt)
            assert handler is expected

    def test_config_with_actual_callback(self):
        handler, args, kwargs = transcode.conf.get_transcoder('TEXT', CFG_GOOD)
        assert handler == my_callback
        assert args == ()
        assert kwargs == {}

    def test_config_with_bad_callback(self):
        try:
            transcode.conf.load_config(CFG_BAD)
        except TypeError:
            assert True
        else:
            assert False

