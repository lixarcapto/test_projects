

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
    text = Btpy.TextArea(
        window, "write something")
    text.pack()
    text.set_size(10, 5)
    label = Btpy.Label(window)
    label.pack()
    btn = Btpy.Button(window, 
        "is it ready")
    btn.pack()
    def fn(e):
        txt = text.get_value()
        label.set_title(txt)
    btn.add_listener("LEFT_CLICK", fn)
    window.start()

main()