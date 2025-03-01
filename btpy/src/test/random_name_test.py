


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
    Btpy.set_name_male_path(
        "../btpy/res/name_male_data.xlsx")
    Btpy.set_name_female_path(
        "../btpy/res/name_female_data.xlsx")
    #
    r = Btpy.random_name(
        "nordic",
        "female"
        )
    print(r)
    #
    r = Btpy.random_name(
        "nordic"
        )
    print(r)
    #
    r = Btpy.random_name(
        "nordic",
        "male"
        )
    print(r)
    #
    r = Btpy.random_name()
    print(r)

main()