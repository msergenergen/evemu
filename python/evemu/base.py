import ctypes
from ctypes.util import find_library
import os

from evemu import const


class EvEmuBase(object):
    """
    A base wrapper class for the evemu functions, accessed via ctypes.
    """
    def __init__(self, library=""):
        if not library:
            library = const.LIB
        self._lib = ctypes.CDLL(library, use_errno=True)
        self._libc = ctypes.CDLL(find_library("c"))

    def get_c_errno(self):
        return ctypes.get_errno()

    def get_c_error(self):
        return os.strerror(ctypes.get_errno())

    def get_c_lib(self):
        return self._libc

    def get_lib(self):
        return self._lib
