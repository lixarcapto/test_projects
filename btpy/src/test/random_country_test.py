

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
    r = ""

    Btpy.set_country_dict_path(
        "../btpy/res/country_dict.xlsx")
    r = Btpy.random_country()

    print(r)

main()