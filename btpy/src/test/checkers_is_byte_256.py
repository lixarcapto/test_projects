

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
    #
    r = Btpy.is_byte_256(255)
    print(r == True)
    #
    r = Btpy.is_byte_256(0)
    print(r == True)
    #
    r = Btpy.is_byte_256(256)
    print(r == False)
    #
    r = Btpy.is_byte_256(255.0)
    print(r == False)
    #
    r = Btpy.is_byte_256("255")
    print(r == False)
    #
    r = Btpy.is_byte_256(-1)
    print(r == False)
    #


main()