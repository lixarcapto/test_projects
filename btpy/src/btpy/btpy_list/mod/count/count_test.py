

from .count import count

def count_test():
    print("--> count_test")

    r = count([0, 1, 1, 1], lambda e:e==1)
    print(r == 3)

    r = count([0, 3, 4, 3], lambda e:e!=3)
    print(r == 2)

    r = count([1], lambda e:e==1)
    print(r == 1)

    print("")