from importlib import import_module


def load_item_from_module(source):
    bits = source.rsplit('.', 1)
    if len(bits) == 1:
        raise ImportError('Incorrect usage: specify a callable with a module')

    mod = import_module(bits[0])
    try:
        attr = getattr(mod, bits[1])
    except AttributeError:
        raise AttributeError('Module "{}"" does not def "{}"'.format(*bits))

    if not callable(attr):
        raise TypeError('module item must be callable')

    return attr

