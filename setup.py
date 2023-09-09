#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md', "r", encoding="utf-8") as f:
    long_description = f.read()

exec(open('argdb/version.py').read())

setup(
    name='argdb',
    description='ArgDB - A Datastore for arguments ',
    long_description_content_type="text/markdown",
    long_description=long_description,
    license=license,
    author='Simon Wells',
    url='https://github.com/Open-Argumentation/ArgDB',
    author_email='mail@simonwells.org',
    version=__version__,
    install_requires=['sadface', 'bottle', 'pywebview'],
    setup_requires=['sadface', 'bottle', 'pywebview'],
    packages=find_packages(exclude=('deploy', 'etc', 'examples'))
)
