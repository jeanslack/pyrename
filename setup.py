#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# First release: Monday, July 7 10:00:47 2014
# 
#########################################################
# Name: setup.py
# Porpose: script for building pyrename and package for install
# Platform: Gnu/Linux
# Writer: jeanslack <jeanlucperni@gmail.com>
# Copyright: (c) 2015 jeanslack <jeanlucperni@gmail.com>
# license: GPL3
# Rev (01) September 24 2014
# Rev (02) January 21 2015
#########################################################

from distutils.core import setup
from setuptools import setup
import platform
from glob import glob
import sys
import os

VERSION = '0.9'
LICENSE = 'Gnu GPL3 (See LICENSE)'
DESCRIPTION = 'Command line Batch renamer for Unix and Unix like OS'

LONG_DESCRIPTION = """Pyrename is written entirely in python, 
It uses the command line (cli) and from 
the options is also available with sequential 
numbering. Each process is applied separately 
or renaming the files or folders.
"""
URL = 'https://github.com/jeanslack/pyrename'

 
def glob_files(pattern):
	"""
	this is a simple function for globbing that iterate 
	for list files in dir
	"""
	
	return [f for f in glob(pattern) if os.path.isfile(f)]



def LINUX_SLACKWARE(id_distro, id_version):
	
	
	setup(name = 'pyrename',
		version = VERSION,
		description = DESCRIPTION,
		long_description = LONG_DESCRIPTION,
		author = 'Gianluca Pernigotto',
		author_email = 'jeanlucperni@gmail.com',
		url = URL,
		license = LICENSE,
		platforms = ['Gnu/Linux (%s %s)' % (id_distro, id_version)],
		packages = ['renamerpack'],
		scripts = ['pyrename'],
		)

def LINUX_DEBIAN_UBUNTU(id_distro, id_version):
	"""
		------------------------------------------------
		setup build pyrename debian package
		------------------------------------------------
		
		TOOLS: 
		apt-get install python-all python-stdeb fakeroot

		USAGE: 
		- for generate both source and binary packages :
			python setup.py --command-packages=stdeb.command bdist_deb
			
		- Or you can generate source packages only :
			python setup.py --command-packages=stdeb.command sdist_dsc
			
		RESOURCES:
		- look at there for major info:
			https://pypi.python.org/pypi/stdeb
			http://shallowsky.com/blog/programming/python-debian-packages-w-stdeb.html
	"""
	
	# this is DATA_FILE structure: 
	# ('dir/file destination of the data', ['dir/file on current place sources']
	# even path must be relative-path
	DATA_FILES = [
		('share/man/man1', ['man/pyrename.1.gz']),
		('share/man/it/man1', ['man/it/pyrename.1.gz'])
				]
	
	DEPENDENCIES = ['python >=2.6']
	
	setup(name = 'pyrename',
		version = VERSION,
		description = DESCRIPTION,
		long_description = LONG_DESCRIPTION,
		author = 'Gianluca Pernigotto',
		author_email = 'jeanlucperni@gmail.com',
		url = URL,
		license = LICENSE,
		platforms = ['Gnu/Linux (%s %s)' % (id_distro, id_version)],
		packages = ['renamerpack'],
		scripts = ['pyrename'],
		data_files = DATA_FILES,
		install_requires = DEPENDENCIES,
		)

	
##################################################

if sys.platform.startswith('linux2'):
	
	dist_name = platform.linux_distribution()[0]
	dist_version = platform.linux_distribution()[1]
	
	if dist_name == 'Slackware ':
		LINUX_SLACKWARE(dist_name, dist_version)
		
	elif dist_name == 'debian' or dist_name == 'Ubuntu':
		LINUX_DEBIAN_UBUNTU(dist_name, dist_version)
		
	else:
		print 'this platform is not yet implemented: %s %s' % (dist_name, dist_version)
		

else:
	print 'OS not supported'
###################################################
