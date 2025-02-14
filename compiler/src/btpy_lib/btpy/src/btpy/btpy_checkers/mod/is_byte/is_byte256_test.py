

from .is_byte import*

def is_byte256_test():
    print("--> is_byte256_test")
    r = is_byte256(5)
    print(r == True)
    r = is_byte256(255)
    print(r == True)
    r = is_byte256(256)
    print(r == False)
    r = is_byte256(-2)
    print(r == False)
    r = is_byte256("6")
    print(r == False)