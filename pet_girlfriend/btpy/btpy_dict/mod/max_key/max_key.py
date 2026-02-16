


from ....btpy_checkers.mod.instanceof_iterable.instanceof_iterable import*

def max_key(NUMBER_DICT
        :dict[str, int|float])\
        ->str:
    """
    TESTED
    Function that finds the maximum 
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
    max_value:int|float = 0.0
    for v in NUMBER_DICT.values():
        if((max_value is None) 
        or (v > max_value)):
            max_value = v
    for k in NUMBER_DICT:
        if(NUMBER_DICT[k] == max_value):
            return k
    return ""

