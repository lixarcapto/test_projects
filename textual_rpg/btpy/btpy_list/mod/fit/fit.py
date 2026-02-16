

from ....btpy_checkers.mod.is_iterable.is_iterable import*

def fit(ORDERDER_ITERABLE:list|tuple|str, 
        SIZE:int)->list:
    """
    Function that adjusts the sent list
    to the indicated size.
    """
    if(not isinstance(SIZE, int)):
        raise Exception("The SIZE parameter is not an int type.")
    if(isinstance(ORDERDER_ITERABLE, list)
    or isinstance(ORDERDER_ITERABLE, tuple)):
        return __fit_list(
            ORDERDER_ITERABLE, SIZE, None)
    if(isinstance(ORDERDER_ITERABLE, str)):
        return __fit_string(ORDERDER_ITERABLE, SIZE)
    raise Exception("the parameter ITERABLE ORDERED is not a valid iterable type, it must be list, str or tuple")
 
def __fit_list(LIST:list, SIZE:int, 
        FILL_DATA:any)->list:
    new_list = []
    for i in range(SIZE):
        if(i >= len(LIST)):
            new_list.append(FILL_DATA)
        else:
            new_list.append(LIST[i])
    return new_list

def __fit_string(STRING:str, SIZE:int)\
        ->str:
    str_list = __fit_list(
        list(STRING), SIZE, " ")
    return "".join(str_list)

