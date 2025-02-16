


from .is_function import*

def is_function_test():
    print("--> is_function_test")
    print(is_function(lambda :1) == True)
    print(is_function(1) == False)
    class A:
        def __init__(self) -> None:
            pass
    print(is_function(A()) == False)
    def fn():
        return 1
    print(is_function(fn) == True)
