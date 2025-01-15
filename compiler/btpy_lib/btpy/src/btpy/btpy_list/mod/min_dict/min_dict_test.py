


from .min_dict import*

def min_dict_test():
    print("--> min_dict_test")

    r = min_dict(
        {"a":1, "b":2, "c":3})
    print(r == "a")

    r = min_dict(
        {"a":9, "b":0, "c":1})
    print(r == "b")

    r = min_dict(
        {"a":-1, "b":4, "c":0})
    print(r == "a")

    print("")
    