


from .map_in_keys import*

def map_in_keys_test():
    print("--> map_in_keys_test")

    r = map_in_keys({"a":0, "b":0},
        lambda e:e + ".")
    
    print(r == {"a.":0, "b.":0})

    print("")