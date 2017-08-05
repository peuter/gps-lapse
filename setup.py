#!/usr/bin/env python3
# This file is part of the GPS-lapse project.
#
#  https://github.com/peuter/gps-lapse
#
# Copyright:
#  (C) 2017 Tobias Bräutigam, Germany
#
# See the LICENSE file in the project's top-level directory for details.

import os
from setuptools import setup, find_packages
from sphinx.setup_command import BuildDoc
cmdclass = {'build_sphinx': BuildDoc}

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES')).read()

setup(
    name="gpsl",
    version="0.0.1",
    author="Tobias Bräutigam",
    author_email="tbraeutigam@gmail.com",
    description="GPS time-lapse video creator",
    license="Apache-2.0",
    keywords="GPS timelapse video map overlay",
    url="https://github.com/peuter/gps-lapse",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "Topic :: Multimedia :: Video :: Conversion"
        'Environment :: Console',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3"
    ],
    setup_requires=[
        'sphinx'
    ],
    tests_require=[],
    install_requires=[
        'exifread',
        'gpxpy',
        'colorlog'
    ],
    entry_points="""
        [console_scripts]
        gps-lapse = gpsl.main:main
        
        [gpsl.gps.parsers]
        gpx = gpsl.gps.gpx:GPXParser

    """
)
