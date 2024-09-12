


def is_byte(data)-> bool:
    if(not type(data) == int): return False
    if(data >= 257): return False
    if(data < 0): return False
    return True