#!/usr/bin/python

import os 
from string import Template
from pprint import pprint
import sys

try:

	d = {}
	outdirectory    = './out'
	template_folder = './template'
	
	# Parse command line args here
	args = sys.argv[1:]

	try:
		if len(args) != 6:
			raise Exception('Invalid number of arguments (%d), expected 6' % (len(args)))

		# Build d from args
		d['name']        = args[0]
		d['version']     = args[1]
		d['author']      = args[2]
		d['description'] = args[3]

		if args[4] != None and args[4] != '':
			outdirectory    = args[4]
		if args[5] != None and args[5] != '':
			template_folder = args[5]		

	except: 
	        print "Exception parsing command line args."
		print "Usage: %s <module_name> <module_version> <module_author> <module_description> <out_dir> <template_dir>" % (sys.argv[0])
        	raise

	def walk_callback(arg, directory, files):
		for f in files:
			inp = None
			out = None
			# Parse file 
			try:
				print "Processing %s at directory %s" % (f, directory)
				
				full_f = os.path.normpath(os.path.join(directory, f))

				if os.path.isfile(full_f):
					inp = open(full_f, 'r')
			
					t_name = Template(f)
				        t_content = Template(inp.read())

					# Perform transformations
					t_name    = t_name.substitute(d)
					t_content = t_content.substitute(d)
				
					# Generate full path for the output file
					full_t_name = os.path.normpath(os.path.join(outdirectory, t_name))
					
					# Ugly, horrendous and non-portable way of taking out the filename from a filename's full path
					full_dir_name = '/'.join(full_t_name.split('/')[:-1])

					# Create the dir if it doesn't exists
					if not os.path.exists(full_dir_name):
						os.makedirs(full_dir_name, 0777) # Hardcoded chmod ... no problem, right?
				
					# Open and write transformed content in the output file (create if not exists)
					out = open(full_t_name, 'w')
					out.write(t_content)			
				else:
					pass # TODO: Create directory
			except Exception, e:
				print "Exception parsing file '%s' at directory '%s'" % (f, directory)
				raise
			finally:
				# Close files
				if inp != None:
					inp.close()
				if out != None:
					out.close()
		# for
	# def walk_callback

	os.path.walk(template_folder, walk_callback, None)
	
except Exception, e:
	print "Error processing templates, check below for detailed exception info.\n"
	pprint(sys.exc_info())
