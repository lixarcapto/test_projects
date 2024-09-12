
from .array_to_dict import*
from ...Btpy import Btpy

@Btpy.printtest
def array_to_dict_test():
    # test numeros
    array = [0, 1, 2, 3]
    dict = array_to_dict(array)
    print(dict)
    # test letras
    array = ["a", "b", "c", "d"]
    dict = array_to_dict(array)
    print(dict)
    # test array void
    array = ["hola", "adios"]
    dict = array_to_dict(array)
    print(dict)