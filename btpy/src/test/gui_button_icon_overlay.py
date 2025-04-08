

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
    button.pack()
    window.start()

main()