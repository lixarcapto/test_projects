


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
    print("--> is_error_test")
    print(Btpy.is_error_return(None) == True)
    print(Btpy.is_error_return([]) == True)
    print(Btpy.is_error_return({}) == True)
    print(Btpy.is_error_return("") == True)

main()