

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
    result = Btpy.read_animation_folder(
        "./res/animation_folder/"
    )
    print(result)
    window = Btpy.Window("animation")
    window.set_size(1000, 700)
    label = Btpy.LabelImage(window)
    label.pack()
    iterator = Btpy.Iterator(
        result,
        True
    )
    def fn(n):
        iterator.next()
        label.set_path_image(
            iterator.get())
    flag = Btpy.repeat_each_async(1.4, fn)
    window.start()

main()