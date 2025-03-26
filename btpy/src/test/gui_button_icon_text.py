

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
    button = Btpy.ButtonIconText(window, 
        "click aqui")
    button.paint_image("../btpy/res/image/cell.png")
    button.pack()
    button.set_text_position("LEFT")
    button2 = Btpy.ButtonIconText(window, 
        "click aqui")
    button2.paint_image("../btpy/res/image/cell.png")
    button2.pack()
    button2.set_text_position("TOP")
    button3 = Btpy.ButtonIconText(window, 
        "click aqui")
    button3.paint_image("../btpy/res/image/cell.png")
    button3.pack()
    button3.set_text_position("BOTTOM")
    button4 = Btpy.ButtonIconText(window, 
        "click aqui")
    button4.paint_image("../btpy/res/image/cell.png")
    button4.pack()
    button4.set_text_position("RIGHT")
    window.start()

main()