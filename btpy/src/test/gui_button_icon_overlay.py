

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
    button.set_size(200, 200)
    button.set_text("Click Aqui")
    button.set_path("../btpy/res/image/image_500x500/loli_anime_kawaii_257_500x500.png")
    label = Btpy.Label(window)
    label.pack()
    n = 0
    def fn(e):
        nonlocal n
        n += 1
        label.set_title(f"clicks {n}")
    button.add_listener(fn)
    button.pack()
    window.start()

main()