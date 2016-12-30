import string
import pytest
import transcode.utils as xutils

class TestUtils:

    def test_load_item(self):
        item = xutils.load_item_from_module(
            'transcode.regex.multiline_splitter'
        )

        assert item.__name__ == 'split'

    def test_bad_load(self):
        with pytest.raises(ImportError):
            item = xutils.load_item_from_module('string')

        with pytest.raises(AttributeError):
            attr = '_'.join(list(string.ascii_letters))
            item = xutils.load_item_from_module('string.{}'.format(attr))

        with pytest.raises(TypeError):
            item = xutils.load_item_from_module('string.ascii_letters')
