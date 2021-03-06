import os
import sys
import codecs
from setuptools import setup, find_packages


app = __import__('transcode')
VERSION = app.get_version()
DESCRIPTION = app.__doc__
HERE = os.path.dirname(__file__)

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit(0)


def read(*files):
    content = ''
    for f in files:
        content += codecs.open(os.path.join(HERE, f), 'r').read()
    return content


setup(
    name='transcode',
    url='https://github.com/OpenTherapeutics/transcode',
    author='Open Therapeutics',
    author_email='david@opentherapeutics.org',
    description=DESCRIPTION,
    version=VERSION,
    long_description=read('README.rst'),
    platforms=['any'],
    license='MIT License',
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.rst'],
    },
    install_requires=read("requirements/base.txt"),
)
