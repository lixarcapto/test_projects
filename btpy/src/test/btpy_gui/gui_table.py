

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
    table = Btpy.Table(window, False,
        "tabla")
    table.pack()
    table.set_components(2)
    table.set_row_dict({
        "nombres":["juan", "alvaro", "pedro"],
        "nombres_ingles":["Jhon", "Erick", 
                "Steven"]
    })
    table.draw_components()
    window.start()

main()