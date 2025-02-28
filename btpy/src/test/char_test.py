

import sys
import os

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)

from btpy.btpy_utilitys.mod.char.Char import Char

def main():
    char = Char("x")
    test_basic()
    memory_test()

def test_basic():
    char = Char("x")
    print(char.get() == "x")

def memory_test():
    char_list = []
    for i in range(1000):
        char_list.append(Char("x"))
    weight_string = 0
    string_list = []
    for i in range(1000):
        string_list.append("x")
        weight_string += sys.getsizeof("x")
    print("weighs " + str(Char.get_size_of()) 
          + " bytes with 1000 chars x")
    print("weighs " + str(weight_string) 
          + " bytes with 1000 strings x")

main()