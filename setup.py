#!/usr/bin/env python
# (c) 2019 Thomas Deutschmann <whissi@gentoo.org>
# Distributed under the terms of the GNU General Public License v2

from distutils.core import setup

setup(
	name = 'elicense',
	version = '1.0.0',
	author = 'Thomas Deutschmann',
	author_email = 'whissi@gentoo.org',
	url = 'https://github.com/Whissi/elicense',

	packages = [],
	scripts = [
		'elicense'
	],

	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
		'Operating System :: POSIX',
		'Programming Language :: Python',
		'Topic :: System :: Systems Administration'
	]
)
