


from is_function import*

def main():
    print("--> is_function_test")
    # 
    # si es una funcion lambda
    r = is_function(lambda :1)
    print(r == True)
    #
    # si es un numero
    r = is_function(1)
    print(r == False)
    #
    # si es una clase
    class A:
        def __init__(self) -> None:
            pass
    print(is_function(A()) == False)
    #
    # si es un metodo
    class A:
        def __init__(self) -> None:
            pass
        def method():
            return None
    object_ = A()
    r = is_function(object_.method)
    print(r == True)
    #
    # si es una funcion nombrada
    def fn():
        return 1
    print(is_function(fn) == True)
    #

main()
