

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
    inventory = Btpy.ButtonInventory(
        window, "inventario", [
            "Manzana",
            "Espada",
            "Abrigo",
            "Monedas"
        ])
    inventory.pack()
    inventory.set_content([
            "Manzana",
            "Martillo",
            "Pan",
            "Pañuelo"
        ])
    inventory.set_background_color("green")
    inventory.set_foreground_color("white")
    window.start()

main()