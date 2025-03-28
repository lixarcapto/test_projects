

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
    date = Btpy.InputDate(window, "date")
    date.set_recomended_years([
        "2000",
        "2001"
    ])
    date.pack()
    btn = Btpy.Button(window, "get date")
    btn.pack()
    label = Btpy.Label(window, "")
    label.pack()
    def fn(e):
        label.set_title(date.get_value())
        print("button event")
    btn.add_listener("LEFT_CLICK", fn)
    window.start()

main()