

import sys
import os

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)

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
    box.pack()
    window.start()

main()