

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
    label = Btpy.LabelImage(window,
        "../btpy/res/image/image_400x400/loli_anime_kawaii_231_400x400.png")
    label.pack()
    label.set_path_image("../btpy/res/image/image_400x400/loli_anime_kawaii_231_400x400.png")
    label.set_size(300, 300)
    window.start()

main()