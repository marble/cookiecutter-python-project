#!/usr/bin/env python3

# https://ianhopkinson.org.uk/2022/02/understanding-setup-py-setup-cfg-and-pyproject-toml-in-python/
# https://daveshawley.medium.com/safely-using-setup-cfg-for-metadata-1babbe54c108

import pkg_resources
import setuptools

if __name__ == "__main__":
    pkg_resources.require('setuptools>=39.2')
    setuptools.setup()
