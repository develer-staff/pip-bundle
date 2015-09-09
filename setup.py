#!/usr/bin/env python

from codecs import open
from os import path
from setuptools import setup, find_packages
import json

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open('.releng.json', 'r') as f:
    version = json.load(f)['version']

setup(
    name='pip-bundle',
    version=version,
    description='Bundle all pip dependencies in a single tarball',
    long_description=long_description,
    url='https://github.com/develersrl/pip-bundle',
    install_requires=['argparse'],
    author='Lorenzo Villani',
    author_email='lvillani@develer.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Build Tools',
    ],
    keywords='pip bundle',
    scripts=['pip-bundle']
)
