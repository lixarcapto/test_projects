

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
    time = Btpy.Time(1, 0)
    time2 = Btpy.Time(4, 0)
    time.substract_time(time2)
    print("hora almacenada",
        time.get_time())
    print("hora actual",
        time.get_actual_hour())
    print("hora string",
        time.get_time_string())

main()