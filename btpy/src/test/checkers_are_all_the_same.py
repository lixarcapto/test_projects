


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
    r = Btpy.are_all_the_same([0, 1, 0])
    print(r == False)
    r = Btpy.are_all_the_same([0, 0, 0])
    print(r == True)
    r = Btpy.are_all_the_same([0])
    print(r == True)

main()
