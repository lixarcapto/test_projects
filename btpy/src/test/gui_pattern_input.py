

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
    pattern = Btpy.PatternInput(window,
        "patron", 5)
    pattern.pack()
    pattern.add_listener(
        lambda :print("funciona"))
    pattern.set_key_right([
        1, 2, 3, 4
    ])
    window.start()

main()