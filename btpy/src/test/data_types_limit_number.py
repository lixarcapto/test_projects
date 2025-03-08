

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
    number = Btpy.LimitNumber(4, [3, 6])
    print(number.get() == 4)
    number.set(7)
    print(number.get() == 6)
    number = Btpy.LimitNumber(8, [3, 6])
    print(number.get() == 6)

main()