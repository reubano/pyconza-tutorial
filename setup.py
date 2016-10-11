#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import sys

from os import path as p

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

sys.dont_write_bytecode = True

setup(
    name='pyconza-tutorial',
    version='0.5.0',
    description='pyconza-tutorial materials',
    author='Reuben Cummings',
    author_email='reubano@gmail.com',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    package_data={'data': ['*.csv', '*.json', '*.xlsx']},
    install_requires=['meza>=0.31.0,<0.32.0'],
    zip_safe=False
)
