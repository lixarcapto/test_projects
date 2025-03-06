

from .count_true_checks import count_true_checks

def count_test():
    print("--> count_test")

    r = count_true_checks([0, 1, 1, 1], lambda e:e==1)
    print(r == 3)

    r = count_true_checks([0, 3, 4, 3], lambda e:e!=3)
    print(r == 2)

    r = count_true_checks([1], lambda e:e==1)
    print(r == 1)

    print("")