# pydmtx - Python wrapper for libdmtx
#
# Copyright (C) 2006 Dan Watson
# Copyright (C) 2007, 2008, 2009 Mike Laughton
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

# $Id$

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension
import os

include_dirs = ['/usr/local/include']
if 'DMTX_INCLUDE_DIR' in os.environ:
    include_dirs = [os.path.expandvars(os.path.expanduser(os.environ['DMTX_INCLUDE_DIR']))] + include_dirs
    
library_dirs = ['/usr/local/lib']
if 'DMTX_LIBRARY_DIR' in os.environ:
    library_dirs = [os.path.expandvars(os.path.expanduser(os.environ['DMTX_LIBRARY_DIR']))] + library_dirs

mod = Extension( '_pydmtx',
                 include_dirs = include_dirs,
                 library_dirs = library_dirs,
                 libraries = ['dmtx'],
                 sources = ['pydmtxmodule.c'] )

setup( name = 'pydmtx',
       version = '0.1',
       description = 'A thin wrapper around libdmtx',
       py_modules = ['pydmtx'],
       ext_modules = [mod] )
