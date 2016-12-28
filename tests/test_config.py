import pytest
import transcode.conf

class TestConf:

    def test_load_item(self):
        item = transcode.conf.load_item_from_module(
            'transcode.regex.multiline_splitter'
        )

        assert item.__name__ == 'split'
