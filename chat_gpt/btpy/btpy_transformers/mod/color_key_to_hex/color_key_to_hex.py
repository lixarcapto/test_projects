

from ....btpy_dict.mod.key_of.key_of import*
from ..hex_dict_const import*


def color_key_to_hex(KEY:set)->str:
    """
    function that converts a color 
    key into a hex code.
    """
    return HEX_DICT[KEY.upper()]

def hex_to_color_key(HEX_CODE:str)->str:
    """
    Function that converts a hex 
    code into a color key.
    """
    return key_of(HEX_CODE)