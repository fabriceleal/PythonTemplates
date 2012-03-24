PythonTemplates
===============
Python template system for generating the skeleton of a Python package / Python C extension project.

"Special" Vars:
	name: the name of the package / extension
	version: version of the package / extension
	author: the author(s) of the package / extension
	description: description of the package / extension


Usage:
	./make.py module_name module_version module_author module_description out_dir template_dir
	

Templates:

	/template
	- Skeleton for a Python package project


	/template_ext
	- Skeleton for a Python C extension project
