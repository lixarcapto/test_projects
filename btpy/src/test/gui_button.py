

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
    def fn(e):
        print("right")
    button.add_listener("RIGHT_CLICK", 
            fn)
    def fn(e):
        print("left")
    button.add_listener("LEFT_CLICK", 
            fn)
    def fn(e):
        print("wheel")
    button.add_listener("WHEEL_CLICK", 
            fn)
    def fn(e):
        print("leave")
    button.add_listener("MOUSE_LEAVE", 
            fn)
    def fn(e):
        print("over")
    button.add_listener("MOUSE_OVER", 
            fn)
    frame = Btpy.Frame(window)
    frame.pack()
    button_2 = Btpy.Button(frame, "innerbutton")
    button_2.pack()
    button_2.add_listener("LEFT_CLICK",
        lambda e:print("left click"))
    window.start()

main()