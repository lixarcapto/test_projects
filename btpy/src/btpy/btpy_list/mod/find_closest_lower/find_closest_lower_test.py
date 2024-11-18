

from .find_closest_lower import*

def find_closest_lower_test():
    print("--> find_closest_lower")
    r = find_closest_lower(
        {"a":1, "b":3, "c":5}, 4
    )
    print(r == "b")
    print("")