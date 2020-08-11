# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2020 Philip Howard for Pimoroni Ltd
#
# SPDX-License-Identifier: MIT

"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pimoroni-circuitpython-mics6814",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="Driver for the MICS6814 Gas sensor",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/pimoroni/Pimoroni_CircuitPython_MICS6814",
    # Author details
    author="Philip Howard",
    author_email="phil@pimoroni.com",
    install_requires=["Adafruit-Blinka",],
    license="MIT",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Hardware",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    keywords="adafruit blinka circuitpython micropython mics6814",
    py_modules=["pimoroni_mics6814"],
)
