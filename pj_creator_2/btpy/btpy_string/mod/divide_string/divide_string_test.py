


from .divide_string import*

def divide_string_test():
    print("divide_string_test")
    r = divide_string(4, "hola mundo")
    print(r == ["hola", " mundo"])
    r = divide_string(5, "hola mundo")
    print(r == ["hola ", "mundo"])