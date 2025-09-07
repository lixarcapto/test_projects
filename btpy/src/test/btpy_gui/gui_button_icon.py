

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
    print("ruta de imagenes", os.getcwd())
    root_path = Btpy.get_root()
    window = Btpy.Window("titulo")
    window.set_is_fullscreen(True)
    button = Btpy.ButtonIcon(window, 
        "girl_fishing",
        "./res/cell.png"
    )
    button.draw_in_direction()
    def fn(e):
        print("funciona")
    button.add_listener(fn)
    window.start()

main()