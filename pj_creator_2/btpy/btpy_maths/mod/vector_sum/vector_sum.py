

from ....btpy_checkers.mod.instanceof_iterable.instanceof_iterable import*

def vector_sum(
        ARRAY_1:list[int|float]|
        tuple[int|float], 
        ARRAY_2:list[int|float]|
        tuple[int|float])\
        ->list[int|float]:
    """
    TESTED
    Function that adds the elements
    of two arrays of numbers in the 
    same position of the array.
    """
    if(not isinstance(ARRAY_1, list)
    and not isinstance(ARRAY_1, tuple)):
        raise Exception(f"<!>Error: The parameter ARRAY_1 is not a valid type, it must be a list or tuple type.")
    if(not isinstance(ARRAY_2, list)
    and not isinstance(ARRAY_2, tuple)):
        raise Exception(f"<!>Error: The parameter ARRAY_2 is not a valid type, it must be a list or tuple type.")
    if((not instanceof_iterable(
            ARRAY_1, int))
    and (not instanceof_iterable(
            ARRAY_1, float))):
        raise Exception(f"<!>Error: parameter ARRAY_1 is not an iterable integer or float.")
    if((not instanceof_iterable(
            ARRAY_2, int))
    and (not instanceof_iterable(
            ARRAY_2, float))):
        raise Exception(f"<!>Error: parameter ARRAY_2 is not an iterable integer or float.")
    if(len(ARRAY_1) != len(ARRAY_2)):
        raise Exception(f"<!>Error: The parameter ARRAY_1 and the ARRAY_2 do not have the same size, therefore the vector sum cannot be calculated.")
    new_array:list[int|float] = ARRAY_1\
        .copy()
    for i in range(len(ARRAY_1)):
        new_array[i] += ARRAY_2[i]
    return new_array

