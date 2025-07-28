

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
    point_2 = [300 ,0]
    degree = 0
    def fn(n):
        nonlocal degree, point_1
        canvas.repaint()
        canvas.draw_path_image(
            point_1,
            "./res/solar.png",
            degree
        )
        point_1[1] += 2
        degree += 5
        if(n >= 100):
            return True
    Btpy.repeat_each_async(0.16, fn)
    window.start()

main()