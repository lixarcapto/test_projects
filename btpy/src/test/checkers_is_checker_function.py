

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
    r = Btpy.is_checker_function(
        lambda e: False)
    print(r == True)
    r = Btpy.is_checker_function(
        lambda e: 1)
    print(r == False)

main()