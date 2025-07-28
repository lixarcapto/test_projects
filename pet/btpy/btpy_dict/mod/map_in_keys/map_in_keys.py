

from typing import Callable
from ....btpy_checkers.mod.is_function.is_function import*

def map_in_keys(DICT:dict, 
        FUNCTION_PROCESSOR
        :Callable[[str], str])\
        ->dict:
    """
    TESTED
    function that goes through all the 
    keys in a dictionary by applying 
    the sent function.
    """
    if(not isinstance(DICT, dict)):
        raise Exception("The DICT parameter is not a dict type.")
    if(not is_function(FUNCTION_PROCESSOR)):
        raise Exception("The FUNCTION PROCESSOR parameter is not a function type.")
    new_dict:dict = {}
    for k in DICT:
        new_dict[FUNCTION_PROCESSOR(k)] \
            = DICT[k]
    return new_dict