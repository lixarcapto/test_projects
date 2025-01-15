


from .merge_as_dict import*

def merge_as_dict_test():
    print("--> merge_as_dict_test")

    r = merge_as_dict(
        ["a","b","c"], [0, 1, 2])
    print(r == {"a":0,"b":1,"c":2})

    try:
        r = merge_as_dict(
        ["a","b","c"], [0, 1, 2, 3])
    except Exception:
        print(True)
    else:
        print(False)
    
    print("")