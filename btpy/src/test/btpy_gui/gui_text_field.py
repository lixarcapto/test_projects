

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
    field = Btpy.TextField(window,
        "campo")
    field.set_shadow_text("nombre")
    field.pack()
    field2 = Btpy.TextField(window,
        "campo")
    field2.set_right_input()
    field2.pack()
    field3 = Btpy.TextField(window,
        "campo")
    field3.set_wrong_input()
    field3.pack()
    window.start()

main()