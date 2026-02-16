

from ....btpy_checkers.mod.is_RGB.is_RGB import*
from ....btpy_checkers.mod.is_hex_color.is_hex_color import*
from ....btpy_transformers.mod.hex_to_RGB.hex_to_RGB import*
from ..color_key_to_hex.color_key_to_hex import*
from ..is_color_key.is_color_key import*

def adapt_rgb(COLOR_ANY:any)\
        ->list[list[int]]:
    """
    Function that adapts color formats 
    to convert them into RGB lists; 
    it can receive color key, hex code, 
    and RGB.
    """
    color = None
    if(is_RGB(COLOR_ANY)):
        color = COLOR_ANY
    elif(is_hex_color(COLOR_ANY)):
        color = hex_to_RGB(
            COLOR_ANY
        )
    elif(is_color_key(COLOR_ANY)):
        hex_ = color_key_to_hex(
            COLOR_ANY)
        color = hex_to_RGB(hex_)
    return color