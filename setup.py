# -*- coding: utf-8 -*-
from distutils.core import setup

import pyunitex

setup(name = 'pyunitex',
      version = '0.1',
      description = 'Minimalist Python ctypes wrapper for Unitex',
      author = pyunitex.__author__,
      author_email = pyunitex.__email__,
      url = 'https://github.com/moliware/pyunitex',
      packages = ['pyunitex'],
      classifiers = ('Development Status :: 5 - Production/Stable',
                     'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                     'Natural Language :: English',
                     'Operating System :: POSIX',
                     'Operating System :: Microsoft',
                     'Programming Language :: Python :: 2.5',
                     'Programming Language :: Python :: 2.6',
                     'Programming Language :: Python :: 2.7',
      ),
)
