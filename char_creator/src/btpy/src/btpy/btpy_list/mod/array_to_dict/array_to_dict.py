


from ....btpy_utilitys.mod.deep.deep import*
from ....btpy_validator.mod.valid_list.valid_list import*

"""
Function that converts the elements of 
an array into the keys of a dictionary; 
with the data sent as an element.
"""
def array_to_dict(array:list, 
        data_type = None)->dict:
    valid_list(array, 1)
    # fill in the dict with data_type 
    # parameter
    dict = {e:data_type for e in array}
    return dict