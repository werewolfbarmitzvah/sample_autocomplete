#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sampleautocomplete',  # Required

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    version='1.0.0',
    description='A sample autocomplete test project',
    packages=find_packages(exclude=['tests', 'misc', 'spec']),
    install_requires=['requests',
                      'PyHamcrest',
                      'bravado',
                      'pytest'],
)
