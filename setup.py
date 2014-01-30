#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
wdb
"""
import os
import re
from setuptools import setup

ROOT = os.path.dirname(__file__)
with open(os.path.join(ROOT, 'app', '__init__.py')) as fd:
    __version__ = re.search("__version__ = '([^']+)'", fd.read()).group(1)

options = dict(
    name="butterfly",
    version=__version__,
    description="A sleek web based terminal emulator",
    long_description="See http://github.com/paradoxxxzero/butterfly",
    author="Florian Mounier",
    author_email="paradoxxx.zero@gmail.com",
    url="http://github.com/paradoxxxzero/butterfly",
    license="GPLv3",
    platforms="Any",
    scripts=['butterfly.py'],
    packages=['app'],
    install_requires=["tornado"],
    package_dir={'butterfly': 'app'},
    package_data={
        'app': [
            'static/fonts/*',
            'static/stylesheets/main.css',
            'static/javascripts/term.js/src/term.js',
            'static/javascripts/main.js',
            'templates/index.html'
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Terminals"])

setup(**options)