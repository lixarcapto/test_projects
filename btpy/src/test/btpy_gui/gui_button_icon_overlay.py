

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
    button = Btpy.ButtonIconOverlay(window)
    button.set_title("Click Aqui")
    button.set_size(150, 150)
    button.set_path_image("../btpy/res/image/image_500x500/loli_anime_kawaii_257_500x500.png")
    n = 0
    def fn(e):
        nonlocal n
        n += 1
        button.set_title(f"clicks {n}")
    button.add_listener(fn)
    button.draw_in_direction()
    window.start()

main()