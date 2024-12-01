

from .clean_voids import*

def clean_voids_test():
    print("--> clean_voids_test")

    r = clean_voids(["a", "b", ""])
    print(r == ["a", "b"])

    r = clean_voids([0, 1, None, 2])
    print(r == [0, 1, 2])

    r = clean_voids([[0], [1], [], [2]])
    print(r == [[0], [1], [2]])

    print("")