


from .find_value import*

def find_value_test():
    print("--> find_value_test")
    r = find_value(
        {"a":1, "b":2, "c":3}, 1)
    print(r == "a")
    r = find_value(
        {"a":1, "b":2, "c":3}, 2)
    print(r == "b")
    print("")
