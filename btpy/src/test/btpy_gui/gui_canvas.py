

import sys
import os

# Obtiene la ruta absoluta del directorio del script actual.
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Sube dos niveles en la jerarquía de directorios.
directorio_padre = os.path.dirname(directorio_actual)
directorio_abuelo = os.path.dirname(directorio_padre)

# Añade el directorio abuelo al sys.path.
sys.path.append(directorio_abuelo)

from btpy.Btpy import Btpy

def main():
    window = Btpy.Window("titulo")
    window.set_is_fullscreen(True)
    
    canvas = Btpy.Canvas(window, "title")
    canvas.pack()
    canvas.set_size(600, 600)
    canvas.draw_image([0, 0],"../btpy/res/image/feto_100x100.png")
    last_point = [0, 0]
    is_first = True
    def fn(event):
        nonlocal last_point
        nonlocal is_first
        point = canvas.get_point_cursor()
        if(is_first):
            is_first = False
            canvas.draw_point(point)
            last_point = point
        canvas.draw_line(
            last_point,
            point)
        last_point = point
        print("draw_point")
    canvas.add_right_click_listener(fn)
    window.start()

main()