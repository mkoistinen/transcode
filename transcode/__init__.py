'''Yet another full for converting various text formats to HTML'''

VERSION = (0, 2, 1)


def get_version():
    return '.'.join(map(str, VERSION))

__version__ = get_version()
