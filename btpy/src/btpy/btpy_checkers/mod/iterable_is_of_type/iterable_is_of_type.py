

from ..is_iterable.is_iterable import*

def iterable_is_of_type(
        ITERABLE:list|set|tuple|dict, 
        KEY_TYPE)-> bool:
    """
    TESTED
    Function that returns true if
    all elements of the iterable
    are the same type of data sent
    in the KEY_TYPE parameter.
    """
    if(not is_iterable(ITERABLE)):
        return False
    if(isinstance(ITERABLE, dict)):
        ITERABLE = list(ITERABLE.values())
    for e in ITERABLE:
        if not isinstance(e, KEY_TYPE):
            return False
    return True