

"""
Function that applies the strip function 
to all strings in a string array.
"""
def strip_array(array:list[str])\
        ->list[str]:
    for i in range(len(array)):
        array[i] = array[i].strip()
    return array