

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
    label = Btpy.LabelImage(window,
        "../btpy/res/image/image_400x400/loli_anime_kawaii_231_400x400.png")
    label.pack()
    label.set_path_image("../btpy/res/image/image_400x400/loli_anime_kawaii_231_400x400.png")
    label.set_size(300, 300)
    window.start()

main()