

import sys
import os

# Obtiene la ruta absoluta del directorio del script actual.
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Sube dos niveles en la jerarquía de directorios.
directorio_padre = os.path.dirname(directorio_actual)
directorio_abuelo = os.path.dirname(directorio_padre)

# Añade el directorio abuelo al sys.path.
sys.path.append(directorio_abuelo)

from btpy.Btpy import Btpy

def main():
    window = Btpy.Window("titulo")
    window.set_is_fullscreen(True)
    range_2 = [0, 100]
    bar = Btpy.DataBar(window, "data")
    bar.set_is_horizontal(False)
    bar.set_size(30, 100)
    bar.set_value([30, 100])
    bar.pack()
    bar2 = Btpy.DataBar(window, "data")
    bar2.set_value([30, 100])
    bar2.pack()
    window.start()

main()