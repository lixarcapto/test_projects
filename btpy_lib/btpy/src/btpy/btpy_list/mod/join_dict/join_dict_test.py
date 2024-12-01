


from .join_dict import*

def join_dict_test():
    print("--> join_dict_test")

    r = join_dict(
        {"a":0, "b":0},
        {"c":0, "d":0}
    )
    print(r == {"a":0, "b":0, "c":0, "d":0})

    r = join_dict(
        {"a":0, "b":0, "c": 0},
        {"d":0}
    )
    print(r == {"a":0, "b":0, "c":0, "d":0})

    print("")
