


from .filter2 import*

def filter2_test():
    print("--> filter2")
    r = filter2([1, 2, 2, 3, 2], 
        lambda e:e==2)
    print(len(r) == 3)
    r = filter2([1, 2, 2, 3, 2], 
        lambda e:e==2, 2)
    print(len(r) == 2)
    print("")