

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
    time = Btpy.Date(26, 10, 2023)
    time2 = Btpy.Date(1, 1, 1)
    print("numeric date",
        time.get_numeric_british_date())
    print("days", time2.convert_to_days())
    time.sum_date_time(time2)
    print("british date",
        time.get_british_date())
    print("numeric date",
        time.get_numeric_british_date())

main()