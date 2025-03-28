

import sys
import os

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)
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