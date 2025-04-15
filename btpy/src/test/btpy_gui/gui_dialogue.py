

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
    dialogue = Btpy.Dialogue(window)
    dialogue.pack()
    res_path = "../btpy/res/image/face/"
    dialogue.load_json_cards(
        "../btpy/res/json/json_cards_test.json"
    )
    dialogue.load_dialogue_txt(
        "../btpy/res/txt/dialogue_test.txt"
    )
    def fn():
        import sys
        sys.exit()
    dialogue.add_end_listener(fn)
    dialogue.start()
    window.start()

main()