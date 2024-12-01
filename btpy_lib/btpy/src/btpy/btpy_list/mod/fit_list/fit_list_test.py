


from .fit_list import*

def fit_list_test():
    print("--> fit_list_test")

    r = fit_list([0, 1, 2], 4)
    print(r == [0, 1, 2, None])

    r = fit_list([0, 1, 2], 4, 3)
    print(r == [0, 1, 2, 3])

    r = fit_list([0, 1, 2, 4], 3)
    print(r == [0, 1, 2])

    print("")