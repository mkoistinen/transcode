import pytest
import transcode.utils

class TestConf:

    def test_load_item(self):
        item = transcode.utils.load_item_from_module(
            'transcode.regex.multiline_splitter'
        )

        assert item.__name__ == 'split'
