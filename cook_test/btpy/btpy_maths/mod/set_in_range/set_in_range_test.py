

from .set_in_range import*

def set_in_range_test():
    print("set_in_range_test")
    r = set_in_range(5, [4, 6])
    print(r == 5)
    r = set_in_range(10, [4, 6])
    print(r == 6)
    r = set_in_range(3, [4, 6])
    print(r == 4)
