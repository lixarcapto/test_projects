

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
    box = Btpy.ButtonBox(window,
     "frutas"
    )
    box.set_icon_path("./res/cell.png")
    box.set_title("mejor un titulo")
    list_ = ["manzana", "pera", "uvas", "mora"]
    box.set_components(list_)
    box.draw_in_direction()
    def fn(key):
        print(key)
    box.add_single_listener(fn)
    window.start()

main()