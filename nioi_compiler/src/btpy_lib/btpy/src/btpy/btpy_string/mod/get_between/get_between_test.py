


from .get_between import*

def get_between_test():
    #
    print("get_between_test")
    r = get_between("aafbfaaaa", "f", "f")
    print(r == "b")
    #
    r = get_between("aaaaaafbf", "f", "f")
    print(r == "b")
    #
    r = get_between("fbfaaaaa", "f", "f")
    print(r == "b")