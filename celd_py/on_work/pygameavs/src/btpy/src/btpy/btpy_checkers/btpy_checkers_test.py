


from .mod.is_point.is_point_test import*
from .mod.is_byte.is_byte127_test import*
from .mod.is_byte.is_byte256_test import*

def btpy_checkers_test():
    is_point_test()
    is_byte256_test()
    is_byte127_test()