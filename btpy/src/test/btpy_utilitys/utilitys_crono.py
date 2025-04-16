

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
    crono = Btpy.Crono()
    time.sleep(2)
    r = crono.get_seconds_counted()
    print(r)
    crono.reset_counter()
    time.sleep(2)
    r = crono.get_seconds_counted()
    print(r)

main()