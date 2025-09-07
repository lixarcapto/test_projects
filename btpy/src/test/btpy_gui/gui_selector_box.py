

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
    selector_box = Btpy.SelectorBox(
        window, 
        False,
            "animal favorito"
    )
    selector_box.set_components(5, 1)
    selector_box.set_content(
        [
                "gato",
                "tortuga",
                "perro",
                "oso",
                "lagartija"
            ]
    )
    selector_box.draw_in_direction()
    button = Btpy.Button(window, 
            "get value")
    button.draw_in_direction()
    label = Btpy.Label(window)
    label.draw_in_direction()
    def fn(e):
        label.set_title(
            selector_box.get_value())
    button.add_listener(fn)
    window.start()

main()