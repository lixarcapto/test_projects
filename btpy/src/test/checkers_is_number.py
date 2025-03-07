

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
    array = []
    print("-> is_number_test")
    r = Btpy.is_number(5)
    print(r == True)
    r = Btpy.is_number(0.4)
    print(r == True)
    r = Btpy.is_number("5")
    print(r == False)

main()