

from typing import Callable
from ....btpy_checkers.mod.is_iterable.is_iterable import*
from ....btpy_checkers.mod.is_function.is_function import*

def filter(
        ITERABLE:list|tuple|dict|set|str, 
        CHECKER_FUNCTION
        :Callable[[any], bool])\
        ->list[any]:
    """
    TESTED
    Filter function that obtains all 
    elements of an iterable that meet 
    a given condition. The given 
    condition is defined by the checker 
    function passed; the checker 
    function must receive the data 
    type of the iterable with a single 
    parameter and return a boolean.
    """
    if(not is_iterable(ITERABLE)):
        raise Exception("The ITERABLE parameter is not an iterable, it must be a list, dict, tuple, or set type.")
    if(not is_function(CHECKER_FUNCTION)):
        raise Exception("The FUNCTION parameter is not a function, it must be a function type such as a lambda function, named function, or method.")
    if(isinstance(ITERABLE, dict)):
        ITERABLE = ITERABLE.values()
    new_array:list = []
    for e in ITERABLE:
        if(CHECKER_FUNCTION(e)):
            new_array.append(e)
    return new_array