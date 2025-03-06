


def fit_list(LIST:list, SIZE:int, 
        FILL_TYPE:any = None)->list:
    """
    Function that adjusts the sent list
    to the indicated size.
    """
    new_list = []
    for i in range(SIZE):
        if(i >= len(LIST)):
            new_list.append(FILL_TYPE)
        else:
            new_list.append(LIST[i])
    return new_list