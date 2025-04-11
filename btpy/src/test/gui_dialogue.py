

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
    dialogue.set_character_card_dict(
        {
            "title": "Monica",
            "description": "",
            "path": res_path + "face_girl_1.png"
        }
    )
    dialogue.set_character_card_dict(
        {
            "title": "Antonia",
            "description": "",
            "path": res_path + "face_girl_2.png"
        }
    )
    dialogue.set_dialog_list([
        {
            "title": "Antonia", 
            "description": "Que haces monica?"
        },
        {
            "title": "Monica", 
            "description": "Solo pasaba a divertirme"
        },
        {
            "title": "Antonia", 
            "description": "Vete de aqui"
        },
        {
            "title": "Monica", 
            "description": "No quiero"
        }
    ])
    def fn():
        import sys
        sys.exit()
    dialogue.add_end_listener(fn)
    dialogue.start()
    window.start()

main()