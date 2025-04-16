

import sys
import os

# Obtiene la ruta absoluta del directorio del script actual.
directorio_actual = os.path.dirname(os.path.abspath(__file__))
# Sube dos niveles en la jerarquía de directorios.
directorio_padre = os.path.dirname(directorio_actual)
directorio_abuelo = os.path.dirname(directorio_padre)
# Añade el directorio abuelo al sys.path.
sys.path.append(directorio_abuelo)

from btpy.Btpy import Btpy

def main(): 
    number = Btpy.LimitNumber(4, [3, 6])
    print(number.get() == 4)
    number.set(7)
    print(number.get() == 6)
    number = Btpy.LimitNumber(8, [3, 6])
    print(number.get() == 6)
    number = Btpy.LimitNumber(0, [0, 3])
    number.sum(3)
    print(number.get() == 3)
    number = Btpy.LimitNumber(0, [0, 3])
    number.sum(4)
    print(number.get() == 3)
    number = Btpy.LimitNumber(0, [0, 3])
    number.sum(-2)
    print(number.get() == 0)
    number = Btpy.LimitNumber(0, [0, 3])
    number.set(4)
    print(number.get() == 3)
    number = Btpy.LimitNumber(1.5, 
            [1.2, 1.7])
    number.set(2)
    print(number.get() == 1.7)
    number = Btpy.LimitNumber(1.5, 
            [1.2, 1.7])
    number.sum(0.9)
    print(number.get() == 1.7)
    number = Btpy.LimitNumber(6, [2, 6])
    number.set_range_arr([2, 4])
    print(number.get() == 4)

main()