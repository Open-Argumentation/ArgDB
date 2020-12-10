#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='argdb',
    description='ArgDB - A Datastore for arguments ',
    long_description=readme,
    license=license,
    author='Simon Wells',
    url='https://github.com/Open-Argumentation/ArgDB',
    author_email='mail@simonwells.org',
    version='0.1',
    packages=find_packages(exclude=('deploy', 'etc', 'examples')),
    install_requires=['tinydb']
)
