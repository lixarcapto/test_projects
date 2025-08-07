

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
    point_1 = [0, 0]
    point_2 = [600 ,0]
    canvas.set_brush_color("black")
    rgb = Btpy.random_color()
    print(rgb)
    def fn(n):
        nonlocal point_2, point_1,\
            rgb
        rgb[0] = Btpy.sum_in_range(
            rgb[0],
            1,
            [0, 255]
        )
        rgb[1] = Btpy.sum_in_range(
            rgb[1],
            1,
            [0, 255]
        )
        rgb[2] = Btpy.sum_in_range(
            rgb[2],
            1,
            [0, 255]
        )
        if(rgb == [255, 255, 255]):
            rgb = Btpy.random_color()
        point_1[1] += 1
        point_2[1] += 1
        print(rgb)
        canvas.set_brush_color(rgb)
        canvas.draw_line(point_1, point_2)
    Btpy.repeat_each_async(0.03, fn)
    window.start()

main()