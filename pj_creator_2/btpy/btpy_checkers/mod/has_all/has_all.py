

from ...mod.is_function.is_function import*
from ...mod.is_iterable.is_iterable import*

def has_all(
        ITERABLE:list|dict|str|tuple|set, 
        FUNCTION:callable)-> bool:
    """
    TESTED
    Function that returns true if
    the checker function applied to all
    the elements of the iterable return
    true when each element is received.
    """
    if(not is_iterable(ITERABLE)):
        raise Exception(f"<!>Error: The parameter ITERABLE is not an iterable type, its type is {type(ITERABLE)}.")
    if(not is_function(FUNCTION)):
        raise Exception(f"<!>Error: The parameter FUNCTION is not a function, its type is {type(FUNCTION)}.")
    if(len(ITERABLE) == 0):
        raise Exception("<!>Error: The parameter ITERABLE sent is empty, so there are no elements to check.")
    data = None
    if(type(ITERABLE) == dict):
        data = ITERABLE.values()
    else:
        data = ITERABLE
    for e in data:
        if(not FUNCTION(e)):
            return False
    return True