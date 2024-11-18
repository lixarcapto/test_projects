


from .max_dict import*

def max_dict_test():
    print("--> max_dict_test")

    r = max_dict({"a":1, "b":2, "c":3})
    print(r == "c")

    r = max_dict({"a":5, "b":5, "c":3})
    print(r == "a")

    r = max_dict({"a":-6, "b":8, "c":5})
    print(r == "b")

    print("")