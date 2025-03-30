

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
    range_2 = [0, 100]
    bar = Btpy.DataBar(window, "data")
    bar.set_is_horizontal(False)
    bar.set_size(30, 100)
    bar.set_value(range_2)
    bar.pack(3)
    bar2 = Btpy.DataBar(window, "data")
    bar2.set_value(range_2)
    bar2.pack(3)
    btn = Btpy.Button(window, "sum")
    btn.pack()
    def fn(e):
        nonlocal range_2
        print("funciona")
        range_2[0] = Btpy.sum_in_range(
            range_2[0],
            5, 
            [0, 100]
        )
        bar2.set_value(range_2)
        bar.set_value(range_2)
    btn.add_listener("LEFT_CLICK", fn)
    window.start()

main()