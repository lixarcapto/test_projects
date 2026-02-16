


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
    
    def hex_to_RGB(HEX_COLOR:str)->list[int]:
        """
        Convierte un color en formato 
        hexadecimal (como #RRGGBB o #RRGGBBAA) 
        a una lista RGB.
        """
        return hex_to_RGB(HEX_COLOR)

    def string_number_list_to_list(STRING:str)\
            ->list[int]:
        return string_number_list_to_list(STRING)

    def color_key_to_hex(KEY:set)->str:
        """
        function that converts a color 
        key into a hex code.
        """
        return color_key_to_hex(KEY)
    
    def hex_to_color_key(HEX_CODE:str)->str:
        """
        Function that converts a hex 
        code into a color key.
        """
        return hex_to_color_key(HEX_CODE)
    
    def is_color_key(KEY:str)->bool:
        return is_color_key(KEY)
    
    def adapt_rgb(COLOR_ANY:any)\
            ->list[list[int]]:
        """
        Function that adapts color formats 
        to convert them into RGB lists; 
        it can receive color key, hex code, 
        and RGB.
        """
        return adapt_rgb(COLOR_ANY)