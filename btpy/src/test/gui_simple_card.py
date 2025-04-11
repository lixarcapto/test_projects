

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
    card = Btpy.SimpleCard(window,
        "vertical", "Monica")
    card.set_icon(
        "../btpy/res/image/image_500x500/face_girl_1_530x530.png",
        [150, 150]
    )
    card.set_description(
        "ella es una experta en el tema")
    card.grid(0, 0)
    card2 = Btpy.SimpleCard(window,
        "vertical_invert", "Monica")
    card2.set_icon(
        "../btpy/res/image/image_500x500/face_girl_1_530x530.png",
        [150, 150]
    )
    card2.set_description(
        "ella es una experta en el tema")
    card2.grid(0, 1)
    card3 = Btpy.SimpleCard(window,
        "horizontal", "Monica")
    card3.set_icon(
        "../btpy/res/image/image_500x500/face_girl_1_530x530.png",
        [150, 150]
    )
    card3.set_description(
        "ella es una experta en el tema")
    card3.grid(1, 0)
    card4 = Btpy.SimpleCard(window,
        "horizontal_invert", "Monica")
    card4.set_icon(
        "../btpy/res/image/image_500x500/face_girl_1_530x530.png",
        [150, 150]
    )
    card4.set_description(
        "ella es una experta en el tema")
    card4.grid(1, 1)
    window.start()

main()