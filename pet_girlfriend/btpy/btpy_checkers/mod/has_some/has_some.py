

from ...mod.is_function.is_function import*
from ...mod.is_iterable.is_iterable import*

def has_some(
        ITERABLE:list|dict|str|tuple|set, 
        FUNCTION:callable)->bool:
    """
    TESTED
    Function that returns true if 
    the verification function applied 
    to all elements returns false in 
    any case.
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
        if(FUNCTION(e)):
            return True
    return False