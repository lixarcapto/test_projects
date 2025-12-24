


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
    box = Btpy.ButtonBox(
        window.widget, "box"
    )
    box.set_components(
        ["gato", "perro", "raton"]
    )
    box.grid(0, 0)
    box.add_listener_to(
        0, lambda :print("gato")
    )
    box.add_single_listener(
        lambda e:print(e)
    )
    window.start()

main()