

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
    lcolor = Btpy.LabelColor(window,
        "personas", "red")
    lcolor.draw_in_direction()
    lcolor2 = Btpy.LabelColor(window,
        "animales", "blue")
    lcolor2.draw_in_direction()
    window.start()

main()