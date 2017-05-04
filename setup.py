#!/usr/bin/env python

from distutils.core import setup

setup(
    name='OTXv2',
    version='1.1',
    description='AlienVault OTX API',
    author='AlienVault Team',
    author_email='otx@alienvault.com',
    url='https://github.com/AlienVault-Labs/OTX-Python-SDK',
    download_url='https://github.com/AlienVault-Labs/OTX-Python-SDK/tarball/1.1.0',
    py_modules=['OTXv2', 'IndicatorYypes','PatchPulse'],
    install_requires=['simplejson', 'requests']
)
