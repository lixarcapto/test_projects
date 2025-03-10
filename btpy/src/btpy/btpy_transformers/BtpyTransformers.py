


from .in_deps import*
from ..btpy_string.BtpyString import BtpyString

class BtpyTransformers(BtpyString):

    """
    static class that is part of 
    the BTPY partial class. It contains 
    functions related to the 
    transformation of different types 
    of data.
    """

    def RGB_to_hex(RGB_OR_RGBA:list[int])\
            ->str:
        """
        TESTED
        Converts an RGB color to its
        hexadecimal representation.
        """
        return RGB_to_hex(RGB_OR_RGBA)
