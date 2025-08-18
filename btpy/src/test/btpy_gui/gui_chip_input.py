

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
    button = Btpy.Button(window, "end")
    button.pack()
    inventory = Btpy.ChipInput(
        window, "inventario", [
            "Manzana",
            "Espada",
            "Abrigo",
            "Monedas"
        ])
    inventory.pack()
    inventory.set_components([
            "Manzana",
            "Martillo",
            "Pan",
            "Pañuelo"
        ])
    inventory.set_content([
            "a",
            "b",
            "c",
            "d"
        ])
    def fn(e):
        r = inventory.get_value()
        print(r)
        inventory.set_value(["Martillo"])
    button.add_listener(fn)
    window.start()

main()