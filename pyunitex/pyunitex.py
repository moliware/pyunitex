""" Minimalist Python ctypes wrapper for Unitex

author: Miguel Olivares <miguel@moliware.com>

"""
import ctypes
import os

# Load library
unitex_lib = 'libunitex.so' if os.name == 'posix' else 'unitex.dll'
unitex = ctypes.cdll.LoadLibrary(unitex_lib)

class Unitex(object):
    """ Create a callable class for an operation"""
    def __getattr__(self, operation):
        """ Return an operation class """
        return UnitexOperation(operation)

class UnitexOperation(object):
    """ Execute any operation of UnitexTool"""
    def __init__(self, operation):
        """ It's allowed every operation of UnitexTool """
        self.operation = operation

    def __call__(self, *params):
        """ Execute operation """
        # Build argv
        params_list = ["UnitexTool", self.operation] + list(params)
        argv_type = ctypes.c_char_p * len(params_list)
        argv = argv_type(*params_list)
        # Build argc
        argc = ctypes.c_int(len(argv))

        return unitex.main_UnitexTool(argc, argv)

