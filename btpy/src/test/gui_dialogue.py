

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
    dialogue = Btpy.Dialog(window)
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