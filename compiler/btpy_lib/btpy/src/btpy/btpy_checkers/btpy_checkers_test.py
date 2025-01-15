


from .mod.are_all_same.are_all_same_test import*
from .mod.is_point.is_point_test import*
from .mod.is_byte.is_byte127_test import*
from .mod.is_byte.is_byte256_test import*
from .mod.in_range.in_range_test import*
from .mod.is_error.is_error_test import*
from .mod.is_function.is_function_test import*
from .mod.is_rgb.is_rgb_test import*
from .mod.is_number.is_number_test import*

def btpy_checkers_test():
    are_all_same_test()
    is_point_test()
    is_byte256_test()
    is_byte127_test()
    in_range_test()
    is_error_test()
    is_function_test()
    is_rgb_test()
    is_rgba_test()
    is_number_test()