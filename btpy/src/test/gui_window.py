

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
    window = Btpy.WindowNav("titulo")
    window.set_is_fullscreen(True)
    window.set_path_image(
        "../btpy/res/image/chica_en_la_puerta.png"
    )
    button = Btpy.Button(window, "click")
    button.pack()
    window.start()
    

main()