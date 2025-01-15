


from .has_all import*

def has_all_test():
    print("--> has_all_test")
    r = has_all([1, 1, 1], lambda e:e == 1)
    print(r == True)
    r = has_all([1, 1, 2], lambda e:e == 1)
    print(r == False)
    print("")