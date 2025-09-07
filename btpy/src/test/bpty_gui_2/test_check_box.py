


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
    btn = Btpy.Button(
        window.widget, "click")
    btn.set_font_size(15)
    btn.grid(1, 0)
    radio_box = Btpy.CheckBox(
        window.widget, "animales")
    radio_box.grid(0, 0)
    radio_box.set_components(
        ["jirafa", "perro", "rata"]
    )
    def fn():
        print(radio_box.get_value())
    radio_box.add_change_listener(fn)
    def fn():
        v = radio_box.get_value()
        print(v)
        radio_box.set_value(["jirafa"])
    btn.add_listener(fn)
    window.start()

main()