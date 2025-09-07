

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
    # vertical -----------------------------
    card = Btpy.SimpleCard(window,
        "vertical", True)
    card.set_title("chica normal 1")
    card.set_icon(
        "./res/chica_normal_3.png",
        [150, 150]
    )
    card.set_description(
        "ella es una experta en el tema")
    card.draw_in_grid(0, 0)
    # vertical invert ---------------------
    card2 = Btpy.SimpleCard(window,
        "vertical_invert", True)
    card2.set_icon(
        "./res/chica_normal_3.png",
        [150, 150]
    )
    card2.set_description(
        "ella es una experta en el tema")
    card2.draw_in_grid(0, 1)
    # horizontal --------------------------
    card3 = Btpy.SimpleCard(window,
        "horizontal", True)
    card3.set_icon(
        "./res/chica_normal_3.png",
        [150, 150]
    )
    card3.set_description(
        "ella es una experta en el tema")
    card3.draw_in_grid(1, 0)
    # horizontal invert --------------------
    card4 = Btpy.SimpleCard(window,
        "horizontal_invert", True)
    card4.set_icon(
        "./res/chica_normal_3.png",
        [150, 150]
    )
    card4.set_description(
        "ella es una experta en el tema")
    card4.draw_in_grid(1, 1)
    window.start()

main()