


def is_function(ANY_DATA : any)->bool:
    """
    TESTED
    Function that returns true if 
    the data sent is of function 
    type and returns false if it 
    is not. Lambda functions, named 
    functions, and methods are 
    considered functions.
    """
    if(hasattr(ANY_DATA, "__name__")):
        return True
    return False