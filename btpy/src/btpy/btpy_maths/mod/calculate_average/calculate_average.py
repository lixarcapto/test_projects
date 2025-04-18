

from ....btpy_checkers.mod.instanceof_iterable.instanceof_iterable import*

def calculate_average(
        ITERABLE:list[int|float]
        |tuple[int|float]
        |dict[str, int|float]
        |set[int|float])->int|float:
    """
    TESTED
    Function that calculates the
    average of the numbers in the
    submitted iterable.
    """
    if((not instanceof_iterable(
            ITERABLE, int))
    and (not instanceof_iterable(
            ITERABLE, float))):
        raise Exception(f"<!>Error: parameter ITERABLE is not an iterable integer or float.")
    if(isinstance(ITERABLE, dict)):
        ITERABLE = list(ITERABLE.values())
    sum_number:int = 0
    for e in ITERABLE:
        sum_number += e
    return sum_number / len(ITERABLE)




