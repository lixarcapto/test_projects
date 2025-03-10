

from ....btpy_checkers.mod.is_function\
    .is_function import*
from ....btpy_checkers.mod.is_iterable.is_iterable import*
from typing import Callable

def count_true_checks(
        ITERABLE:list|str|tuple|set|dict,
        CHECKER_FUNCTION
        :Callable[[any],bool])-> int:
    """
    TESTED
    Function that counts the number of
    checks when going through a
    structure. It works by applying 
    the checker function sent to
    each element of the structure 
    and counting the true results.
    """
    if(not is_iterable(ITERABLE)):
        raise Exception("The parameter ITERABLE is not an iterable, it must be a str, list, tuple, set or dict type.")
    if(not is_function(CHECKER_FUNCTION)):
        raise Exception("The FUNCTION parameter is not a function.")
    n:int = 0
    array:list = []
    type_:str = type(ITERABLE)
    # si no es una funcion checker
    if(not type(CHECKER_FUNCTION(1)) 
            == bool):
        raise Exception(f"<!>Error: CHECKER_FUNCTION must be a checker function type, for example (lambda e:e > 1)")
    # si no es diccionario o una lista
    if((not type_ == dict)
    and (not type_ == list)):
        raise Exception(f"<!>Error: STRUCTURE is not a valid data type is ({type_}), it must be dict or list")
    if(type_ == dict):
        array = ITERABLE.values()
    else:
        array = ITERABLE
    for e in array:
        if(CHECKER_FUNCTION(e)):
            n += 1
    return n