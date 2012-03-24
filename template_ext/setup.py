#!/usr/bin/python

from distutils.core import setup, Extension

setup(name = '${name}',
	version = '${version}',
	description = '${description}',
	author = '${author}',
	ext_modules=[
		Extension('name', 'source.c') # .c, .h, ...
	]) # put here all *.py files, without the extension

# To build:   			python setup.py build
# To install: 			python setup.py install
# To build archive file: 	python setup.py sdist

