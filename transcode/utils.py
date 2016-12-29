from importlib import import_module


def load_item_from_module(source):
    bits = source.rsplit('.', 1)
    if bits == 1:
        raise ImportError('Incorrect usage: specify a callable with a module')

    mod = import_module(bits[0])
    try:
        return getattr(mod, bits[1])
    except AttributeError:
        raise ImportError('Module "{}"" does not def "{}"'.format(*bits))

