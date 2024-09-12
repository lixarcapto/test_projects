


from .get_keys import*

def get_keys_test():
    print("--> get_keys_test")
    dict = {"a":0, "b":0, "c":0}
    r = get_keys(dict)
    print(r == ["a", "b", "c"])
