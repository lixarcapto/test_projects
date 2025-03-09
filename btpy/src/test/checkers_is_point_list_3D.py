

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
    r = Btpy.is_point_list_3D(
        [[0,0,0], [100, 100,100], 
            [400, 400, 400]]
    )
    print(r == True)
    # si no es una lista de puntos
    r = Btpy.is_point_list_3D(
        [0,0,0]
    )
    print(r == False)
    # si no es una lista de puntos
    r = Btpy.is_point_list_3D(
        "[0, 0, 0]"
    )
    print(r == False)

main()