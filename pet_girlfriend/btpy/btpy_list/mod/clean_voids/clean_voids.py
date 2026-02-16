


def clean_voids(ITERABLE : list|tuple|set)\
        ->list:
    """
    Function that creates a new array
    by removing all values ​​of type
    None and void such as void string "",
    void array [], and void set {}
    """
    if(not isinstance(ITERABLE, list)
    and not isinstance(ITERABLE, tuple)
    and not isinstance(ITERABLE, set)):
        raise Exception("the ITERABLE parameter is not a valid type, it must be list, set or tuple.")
    new_array:list = []
    for i in range(len(ITERABLE)):
        if(ITERABLE[i] == None): continue
        if(ITERABLE[i] == ""): continue
        if(ITERABLE[i] == []): continue
        if(ITERABLE[i] == {}): continue
        new_array.append(ITERABLE[i])
    return new_array