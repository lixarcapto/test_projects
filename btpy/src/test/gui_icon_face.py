

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
    canvas = Btpy.IconFace(window)
    canvas.pack()
    canvas.set_path_resources(
        "../btpy/res/image/icon_face/"
    )
    canvas.set_face_dict(
        {

            "FACE": "FACE_BLACK",
            "MOUTH": "MOUTH_NORMAL",
            "HAIR": "HAIR_POT_BLACK",
            "NOSE": "NOSE_TYPE_A",
            "EYES": "EYES_ASIAN_NORMAL"

        }
    )
    canvas.paint()
    selector = Btpy.Combobox(window,
        "skin", 
        canvas.get_face_keys_list()
    )
    selector.pack()
    def fn(e):
        canvas.set_face_key(
            selector.get_value())
        canvas.paint()
    selector.add_change_listener(fn)
    window.start()

main()