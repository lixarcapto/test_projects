

from ..hex_dict_const import*

def is_color_key(KEY:str)->bool:
    if(KEY.upper() in HEX_DICT):
        return True
    return False