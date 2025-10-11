


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
    button = Btpy.Button(window.widget,
        "button")
    button.pack()
    switchbox = Btpy.SwitchImageBox(
        window.widget, "titulo"
    )
    switchbox.pack()
    switchbox.set_components(3)
    switchbox.set_seleted_image_path(
        "./res/light_on.png"
    )
    switchbox.set_unseleted_image_path(
        "./res/light_off.png"
    )
    def fn():
        print(switchbox.get_values())
    button.add_listener(fn)
    window.start()

main()