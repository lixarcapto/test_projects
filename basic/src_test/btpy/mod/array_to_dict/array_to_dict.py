


from ...fn.deep import*
from ...fn.valid_list import*

"""
    Function that converts the elements of 
    an array into the keys of a dictionary; 
    with the data sent as an element.
    EXAMPLE:
        array = ['a', 'b', 'c', 'd', 'e']
        r:list = Basic.array_to_dict(array)
        print(r)
    OUTPUT:
        {'a': None, 'b': None, 'c': None, 
        'd': None, 'e': None}
"""
def array_to_dict(array:list, 
        data_type = None)->dict:
    valid_list(array, 1)
    # fill in the dict with data_type 
    # parameter
    dict = {e:data_type for e in array}
    return dict