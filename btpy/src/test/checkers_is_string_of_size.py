


import sys
import os

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)

from btpy.Btpy import Btpy

def main():
    print("-- is string of 4 size")
    r = Btpy.is_string_of_size("lion", 4)
    print(r == True)
    print("-- is not string")
    r = Btpy.is_string_of_size(4, 4)
    print(r == False)
    print("-- string has not size 4")
    r = Btpy.is_string_of_size("lizard", 4)
    print(r == False)
    print("-- string is void")
    r = Btpy.is_string_of_size("", 0)
    print(r == True)

main()