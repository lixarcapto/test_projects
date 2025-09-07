

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
    combobox = Btpy.Combobox(window, 
            True,
            "animal favorito"
    )
    combobox.set_components(
        [
                "gato",
                "tortuga",
                "perro",
                "oso",
                "lagartija"
        ]
    )
    combobox.set_content(
        [
                "gato**",
                "tortuga**",
                "perro**",
                "oso**",
                "lagartija**"
        ]
    )
    combobox.draw_in_direction()
    def fn(e):
        print(combobox.get_value())
    combobox.add_change_listener(fn)
    window.start()

main()