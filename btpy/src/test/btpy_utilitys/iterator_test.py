

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
    animals = Btpy.get_animal_array()
    it = Btpy.Iterator(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
    while(it.has_next()):
        #if(it.get() == 7): it.extract()
        print(it.get())
        it.next()
    it.set_is_reverse(True)
    while(it.has_next()):
        print(it.get())
        it.next()

main()