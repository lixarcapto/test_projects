


from .is_error import*

def is_error_test():
    print("--> is_error_test")
    print(is_error(-1) == True)
    print(is_error(None) == True)
    print(is_error([]) == True)
    print(is_error({}) == True)
    print(is_error("") == True)