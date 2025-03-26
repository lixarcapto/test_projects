

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
    button = Btpy.Button(window, "click")
    button.pack()
    def fn():
        print("right")
    button.add_listener("RIGHT_CLICK", 
            fn)
    def fn():
        print("left")
    button.add_listener("LEFT_CLICK", 
            fn)
    def fn():
        print("wheel")
    button.add_listener("WHEEL_CLICK", 
            fn)
    def fn():
        print("leave")
    button.add_listener("MOUSE_LEAVE", 
            fn)
    def fn():
        print("over")
    button.add_listener("MOUSE_OVER", 
            fn)
    window.start()

main()