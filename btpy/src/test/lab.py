

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
    cadena2 = "123a5"
    resultado6 = all(caracter.isdigit() for caracter in cadena2)
    print(f"¿Todos los caracteres de la cadena2 son digitos? {resultado6}") #False

main()