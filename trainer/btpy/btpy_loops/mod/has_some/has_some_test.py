


from .has_some import*

def has_some_test():
    print("--> has_some_test")
    r = has_some([1, 1, 2], lambda e:e==2)
    print(r == True)
    print("")