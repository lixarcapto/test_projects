

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
    crono = Btpy.Crono()
    time.sleep(2)
    r = crono.get_seconds_counted()
    print(r)
    crono.reset_counter()
    time.sleep(2)
    r = crono.get_seconds_counted()
    print(r)

main()