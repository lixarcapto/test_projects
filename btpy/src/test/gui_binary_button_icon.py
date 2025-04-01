

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
    button = Btpy.BinaryButtonIcon(window, 
        "girl_fishing",
        "../btpy/res/image/capture/girl_fishing_kawaii.png",
        "../btpy/res/image/capture/octopus.png"
    )
    button.pack()
    button.set_size(300, 300)
    window.start()

main()