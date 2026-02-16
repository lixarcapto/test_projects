


from ..is_iterable.is_iterable import*

def type_iterable(ITERABLE
        :list|tuple|dict|set)-> str:
    """
    TESTED
    Function that returns the data 
    type of the data contained within 
    an iterable if it is an iterable 
    of homogeneous types.
    """
    # valida si ITERABLE es un iterable
    if(not is_iterable(ITERABLE)):
        raise Exception("The parameter ITERABLE is not a valid iterable type.")
    # valida si ITERABLE es mayor que 0
    if(len(ITERABLE) == 0):
        raise Exception("The iterable passed in the ITERABLE parameter has a size of zero, and must be greater than zero.")
    if(isinstance(ITERABLE, dict)):
        ITERABLE = list(ITERABLE.values())
    # funcion final
    last_type:str = ""
    for e in ITERABLE:
        if(last_type == ""):
            last_type = type(e)
            continue
        if(not type(e) == last_type): 
            last_type = ""
            break
        last_type = type(e)
    if(last_type == ""):
        raise Exception("The iterable sent has multiple data types in its elements; therefore a homogeneous type cannot be defined.")
    return last_type