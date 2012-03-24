#!/usr/bin/python

from distutils.core import setup

setup(name = '{name}',
	version = '{version}',
	description = '{description}',
	author = '{author}',
	py_modules=['']) # put here all *.py files, without the extension

# To build:   			python setup.py build
# To install: 			python setup.py install
# To build archive file: 	python setup.py sdist

