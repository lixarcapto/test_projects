
from .array_to_dict import*

# TESTED
def array_to_dict_test():
    print("--> array_to_dict_test")
    # test numeros
    array = [0, 1, 2]
    r = array_to_dict(array)
    print(r == {"0":None, "1":None, "2":None})

    # test letras
    array = ["a", "b"]
    r = array_to_dict(array, 0)
    print(r == {"a":0, "b":0})

    # test array void
    array = ["hola", "adios"]
    r = array_to_dict(array, "si")
    print(r == {"hola":"si", "adios":"si"})
    
    print("")