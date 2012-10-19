#!/usr/bin/python

import logging
import os
import sys

cwd = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(cwd, '..'))
src = os.path.join(project_root, 'src')
templates = os.path.join(project_root, 'templates')
static = os.path.join(project_root, 'static')

print __file__
print cwd
print src
print templates
print static
