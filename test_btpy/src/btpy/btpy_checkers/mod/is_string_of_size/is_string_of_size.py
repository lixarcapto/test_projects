



def is_string_of_size(ANY_DATA:any, 
        SIZE:int)-> bool:
    """
    Function that returns true if 
    the data sent is a string of the 
    indicated size; and returns false
    if it is not.
    """
    if(not isinstance(ANY_DATA, str)):
        return False
    if(not len(ANY_DATA) == SIZE):
        return False
    return True