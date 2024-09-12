

from .is_byte import*

def is_byte127_test():
    print("--> is_byte127_test")
    r = is_byte127(100)
    print(r == True)
    r = is_byte127(-100)
    print(r == True)
    r = is_byte127(256)
    print(r == False)
    r = is_byte127(-256)
    print(r == False)
    r = is_byte127("100")
    print(r == False)