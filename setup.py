# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in lexcru/__init__.py
from lexcru import __version__ as version

setup(
	name='lexcru',
	version=version,
	description='Lexcru App',
	author='FinByz',
	author_email='info@finbyz.tech',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
