

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
    print("--> fit_list_test")

    r = Btpy.fit([0, 1, 2], 4)
    print(r == [0, 1, 2, None])

    r = Btpy.fit("abc", 4)
    print(r == "abc ")

    r = Btpy.fit([0, 1, 2, 4], 3)
    print(r == [0, 1, 2])

    print("")

main()