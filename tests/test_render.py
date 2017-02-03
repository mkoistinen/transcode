import pytest
import transcode.conf
import transcode.render

class TestRender:

    def test_basic_default_handlers(self):
        assert transcode.render.render('Hello, World', transcode.conf.HTML_FORMAT)       
        assert transcode.render.render('Hello, World', transcode.conf.SIMPLE_TEXT_FORMAT)
        assert transcode.render.render('Hello, World', transcode.conf.MARKDOWN_FORMAT)   
        assert transcode.render.render('Hello, World', transcode.conf.RST_FORMAT)        

