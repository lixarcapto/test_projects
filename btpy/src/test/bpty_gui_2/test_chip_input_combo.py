


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
    btn = Btpy.Button(window.widget)
    btn.grid(0, 0)
    chip = Btpy.ChipInputCombo(
        window.widget)
    chip.grid(1, 0)
    chip.set_components([
        "perro", "jirafa", "rata", "rana"
    ])
    chip.set_content([
        "dog", "jirafa", "rat", "frog"
    ])
    def fn(e):
        r = chip.get_value()
        print(r)
    btn.add_listener(fn)
    window.start()

main()