#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# cms-booklet - github.com/obag/cms-booklet
# Copyright © 2014 Gabriele Farina <gabr.farina@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from distutils.core import setup
import os

this_path = os.path.dirname(os.path.realpath(__file__))
data_files = []
for (path, dirs, files) in os.walk(os.path.join(this_path, 'templates')):
	rel_path = path[len(this_path)+1:]
	for file in files:
		if file[0] != '.': # Don't copy hidden files
			data_files += [(
				os.path.join('cms-booklet',rel_path),
				[os.path.join(rel_path, file)]
			)]

setup(
	name = 'cms-booklet',
	version = '1.0',
	description = 'cms-booklet: problem statement compiler for CMS (Contest Management System)',
	author = 'Gabriele Farina',
	author_email = 'gabr.farina@gmail.com',

	scripts = ['cms-booklet.py'],
	data_files = data_files
)