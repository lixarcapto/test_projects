

from ....btpy_checkers.mod.instanceof_iterable.instanceof_iterable import*

def min_key(NUMBER_DICT
        :dict[str, int|float])\
        ->str:
    """
    TESTED
    Function that finds the minimum 
    value in a dictionary and returns 
    the key of that value. If there 
    are two equal values, it uses the 
    one that is first in the dictionary 
    order.
    """
    if(not isinstance(NUMBER_DICT, dict)):
        raise Exception("The parameter NUMBER_DICT is not a dict type.")
    if((not instanceof_iterable(
            NUMBER_DICT, int))
    and (not instanceof_iterable(
            NUMBER_DICT, float))):
        raise Exception("The parameter NUMBER_DICT is not an iterable with elements of type int or float.")
    min_value:int|float = None
    min_key:str = ""
    for k, v in NUMBER_DICT.items():
        if ((min_value is None) 
        or (v < min_value)):
            min_value = v
            min_key = k
    return min_key