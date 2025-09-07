

from .is_point import*

def is_point_test():
    print("--> is_point_test")
    r = is_point_2d([0, 0])
    print(r == True)
    r = is_point_2d([10000, 0])
    print(r == True)
    r = is_point_2d([0])
    print(r == False)
    r = is_point_2d([0, 0, 0])
    print(r == False)
    r = is_point_2d("[0, 0]")
    print(r == False)
