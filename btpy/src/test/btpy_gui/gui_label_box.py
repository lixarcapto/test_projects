

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
    box = Btpy.LabelBox(window, 
        "animales", [
            "jirafa",
            "perro",
            "gato",
            "cocodrilo",
            "paloma"
        ])
    box.set_content(
        [
            0, 
            1,
            2,
            3,
            4
        ]
    )
    box.draw_in_direction()
    window.start()

main()