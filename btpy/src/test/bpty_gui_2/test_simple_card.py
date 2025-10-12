


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
    card = Btpy.Card(window.widget, "")
    card.pack()
    card.set_title("titulo")
    card.set_path_image(
        "./res/chica_ingeniera.png",
        [300, 300]
    )
    card.set_description("texto")
    window.start()

main()