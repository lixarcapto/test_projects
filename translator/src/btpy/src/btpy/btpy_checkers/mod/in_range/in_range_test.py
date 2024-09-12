

from .in_range import*

def in_range_test():
    print("--> in_range_test")
    r = in_range(1, [0, 2])
    print(r == True)
    r = in_range(0, [0, 2])
    print(r == True)
    r = in_range(2, [0, 2])
    print(r == True)
    r = in_range(-1, [0, 2])
    print(r == False)
    r = in_range(3, [0, 2])
    print(r == False)
