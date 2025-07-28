

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
    char = Btpy.CharacterWidget(
        window, "title")
    char.pack()
    char.canvas.draw_image_layers(
        [0, 0],
        [
            "./res/character/skin_pale.png",
            "./res/character/hair_straight_blonde.png",
            "./res/character/eyes_slanted_blue.png",
            "./res/character/nose_small.png",
            "./res/character/mouth_serious.png",
        ]
    )
    window.start()

main()