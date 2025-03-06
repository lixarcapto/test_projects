

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
    r = Btpy.is_hex_color("#2596be")
    print(r == True)
    #
    r = Btpy.is_hex_color("#873e23")
    print(r == True)
    #
    r = Btpy.is_hex_color("#993300")
    print(r == True)
    #
    r = Btpy.is_hex_color("")
    print(r == False)
    #
    r = Btpy.is_hex_color("993300")
    print(r == False)
    #

main()