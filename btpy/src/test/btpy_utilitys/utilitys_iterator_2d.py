

import sys
import os

# Obtiene la ruta absoluta del directorio del script actual.
directorio_actual = os.path.dirname(os.path.abspath(__file__))
# Sube dos niveles en la jerarquía de directorios.
directorio_padre = os.path.dirname(directorio_actual)
directorio_abuelo = os.path.dirname(directorio_padre)
# Añade el directorio abuelo al sys.path.
sys.path.append(directorio_abuelo)

import time

from btpy.Btpy import Btpy

def main():
    it2d = Btpy.Iterator2D(
        [
            [4, 3, 2, 1, 0],
            [0, 1, 2, 3, 4]
        ]
    )
    print(it2d.get())
    size = it2d.get_size()
    print("size", size)
    for i in range(size):
        print(it2d.get())
        it2d.next()

main()