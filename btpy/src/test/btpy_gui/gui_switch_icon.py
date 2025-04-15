

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
    button = Btpy.SwitchIcon(window, 
        "girl_fishing",
        "../btpy/res/image/capture/girl_fishing_kawaii.png",
        "../btpy/res/image/capture/octopus.png"
    )
    button.pack()
    button.set_size(300, 300)
    def fn(e):
        print("valor " + str(button.get_value()))
    button.add_listener(fn)
    button.set_title("chica pescando")
    window.start()

main()