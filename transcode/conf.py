HTML_FORMAT        = 'HTML' 
SIMPLE_TEXT_FORMAT = 'TEXT'
MARKDOWN_FORMAT    = 'MARK'
RST_FORMAT         = 'REST'

DEFAULT_CONFIG = {
    HTML_FORMAT : {
        'transcoder': 'transcode.render.render_html',
        'kwargs': {},
        'args': ()
    },
    SIMPLE_TEXT_FORMAT : {
        'transcoder': 'transcode.render.render_simple',
        'kwargs': {},
        'args': ()
    },
    MARKDOWN_FORMAT : {
        'transcoder': 'transcode.render.render_markdown',
        'kwargs': {},
        'args': ()
    },
    RST_FORMAT : {
        'transcoder': 'transcode.render.render_restructuredtext',
        'kwargs': {},
        'args': ()
    },
}

_config_db = {}

def load_config(cfg=None):
    global _config_db
    from transcode.utils import load_item_from_module
    cfg = cfg or DEFAULT_CONFIG
    cfg_id = id(cfg)
    
    if cfg_id not in _config_db:
        type_error_msg = 'transcoder type must be a callable'
        for key, dct in cfg.items():
            xcoder = dct['transcoder']
            if isinstance(xcoder, str):
                xcoder = load_item_from_module(xcoder)
            elif not callable(xcoder):
                raise TypeError(type_error_msg)
            cfg[key]['transcoder'] = xcoder

        _config_db[cfg_id] = cfg

    return _config_db[cfg_id]


def get_transcoder(format, cfg=None):
    handler = load_config(cfg)[format]
    return (
        handler['transcoder'],
        handler.get('args', ()),
        handler.get('kwargs', {})
    )
