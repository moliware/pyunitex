Pyunitex
========

Minimalist Python ctypes wrapper for Unitex_.

Description
...........

Pyunitex is a wrapper for UnitexTool program. So you can use all utilities of which Unitex is composed. You can check them in Unitex documentation_, chapter 12.


Install
.......

To install pyunitex: ::

  easy_install pyunitex

or, if you want to install it from source code: ::

  python setup.py install

For installing pyunitex it's necessary to compile unitex as a shared library and copy it to a shared library search path  (For example: /usr/local/lib/ or /usr/lib/)

Usage
.....

This an example of a typical utility called from command line and how to use it with pyunitex.


Command line: ::

  Convert -s UTF8 file_name -o file_name_converted

Pyunitex: ::

  >>> import pyunitex
  >>> u = pyunitex.Unitex()
  >>> u.Convert('-s', 'UTF8', 'file_name', '-o', 'file_name_converted')

.. _Unitex: http://www-igm.univ-mlv.fr/~unitex/
.. _documentation: http://www-igm.univ-mlv.fr/~unitex/UnitexManual2.1.pdf