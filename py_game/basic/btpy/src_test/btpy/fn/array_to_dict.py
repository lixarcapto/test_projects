


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
    # valid the parameter array
    if(not type(array) == list): 
        txt = f"array parameter is not array "
        txt += "type {array}"
        raise Exception(txt)
    # fill in the dict with data_type parameter
    dict = {e:data_type for e in array}
    return dict