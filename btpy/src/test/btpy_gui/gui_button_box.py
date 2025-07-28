

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
    box = Btpy.ButtonBox(window, False,
     "frutas"
    )
    box.set_icon_path("./res/cell.png")
    box.set_title("mejor un titulo")
    box.set_components(4, 1)
    box.set_content(
        ["manzana", "pera", "uvas", "mora"]
    )
    box.pack()
    def fn(key):
        print(key)
    box.add_single_listener(fn)
    #
    box2 = Btpy.ButtonBox(window, False,
     "frutas"
    )
    box2.set_icon_path("./res/cell.png")
    box2.set_title("mejor un titulo")
    box2.set_components(4, 4)
    box2.set_content(
        ["manzana", "pera", 
         "uvas", "mora", "platano"]
    )
    box2.pack()
    box2.set_background_color(
        "#FF0000")
    box2.set_foreground_color(
        "#ffff00"
    )
    def fn(e):
        print("funciona el listener")
    box2.add_listener_to(2, fn)
    window.start()

main()