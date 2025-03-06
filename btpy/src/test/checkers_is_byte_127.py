


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
    print("--> is_byte127_test")
    #
    r = Btpy.is_byte_127(100)
    print(r == True)
    #
    r = Btpy.is_byte_127(126)
    print(r == True)
    #
    r = Btpy.is_byte_127(-126)
    print(r == True)
    #
    r = Btpy.is_byte_127(127)
    print(r == False)
    #
    r = Btpy.is_byte_127(-127)
    print(r == False)
    #
    r = Btpy.is_byte_127(0)
    print(r == True)
    #
    r = Btpy.is_byte_127(-100)
    print(r == True)
    #
    r = Btpy.is_byte_127(256)
    print(r == False)
    #
    r = Btpy.is_byte_127(-256)
    print(r == False)
    #
    r = Btpy.is_byte_127("100")
    print(r == False)
    #

main()