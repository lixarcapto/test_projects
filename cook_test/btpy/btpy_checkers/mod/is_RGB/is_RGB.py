

from ..is_byte_256.is_byte_256 import*

def is_RGB(ANY_DATA : any)->bool:
    """
    TESTED
    function that returns true if the 
    data sent is an array in RGB format, 
    that is, an array of integers of 
    rank 256 of size x3. If it is not, 
    it returns false.
    """
    if(not type(ANY_DATA) == list): 
        return False
    if(not len(ANY_DATA) == 3): 
        return False
    for e in ANY_DATA:
        if(not is_byte_256(e)): 
            return False
    return True
