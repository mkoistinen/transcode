# -*- coding: utf-8 -*-
from invoke import task

BUILDDIR = "build"
PROJECT = "transcode"

PYPI_KEY = "df0e1f093c9e414d94c609a83132611a"
PYPI_SECRET = "9bc5309ddcf04522a8d1e00244de7b81"
PYPI_SOURCE = "pypi.opentherapeutics.net/simple/"

PIP_EXTRA = "--extra-index-url https://{}:{}@{}".format(
    PYPI_KEY,
    PYPI_SECRET,
    PYPI_SOURCE
)


def pip_with_extra(ctx, cmd, *args, **kws):
    if PIP_EXTRA:
        cmd = '{} {}'.format(cmd, PIP_EXTRA)

    ctx.run(cmd, *args, **kws)


@task
def clean(ctx):
    """Removes all the cache files"""
    ctx.run("find . -type d -name __pycache__ | xargs rm -rf")


@task
def install(ctx):
    """Installs the libraries required to run the application"""
    ctx.run("pip install -U pip")
    pip_with_extra(ctx, "pip install -qr requirements/base.txt")


@task(install)
def develop(ctx):
    """Installs all the libraries used for development"""
    pip_with_extra(ctx, "pip install -qr requirements/dev.txt")


@task
def checks(ctx):
    """Runs pep8/flake8 checks on the code"""
    excl = "--exclude='build/,*migrations/*'"
    ctx.run("pep8 {} .".format(excl))
    ctx.run("flake8 {} .".format(excl))


@task
def test(ctx):
    """Runs the tests"""
    ctx.run(
        'PYTHONPATH=`pwd` '
        "py.test --cov-config .coveragerc --cov-report html --cov-report term --cov={}".format(
            PROJECT
        ),
        pty=True
    )

