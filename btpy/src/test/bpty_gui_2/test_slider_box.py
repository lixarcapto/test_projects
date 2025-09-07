


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
    button = Btpy.Button(
        window.widget, "click"
    )
    button.grid(0, 0)
    sliderbox = Btpy.SliderBox(
        window.widget, "titulo"
    )
    sliderbox.grid(1, 0)
    sliderbox.set_components(
        ["dog", "giraffe", "cat"]
    )
    sliderbox.set_content(
        ["perro", "jirafa", "gato"]
    )
    sliderbox.set_range_for_all(
        [0, 400]
    )
    sliderbox.set_value(
        {"giraffe":133}
    )
    def fn():
        print("change listener")
    sliderbox.add_change_listener(fn)
    sliderbox.set_columns(3)
    def fn(e):
        v = sliderbox.get_value()
        print(v)
    button.add_listener(fn)
    window.start()

main()