

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
    swiper = Btpy.SwiperCard(window, 
        "animales")
    swiper.pack()
    swiper.set_is_cyclical(True)
    swiper.set_arroy_is_bold(True)
    swiper.set_values_list([
        {
            "title": "sardina",
            "path": "../btpy/res/image/capture/sardine.png",
            "description":"en un pez de cardumen"
        },
        {
            "title": "clam",
            "path": "../btpy/res/image/capture/clam.png",
            "description":"es un molusco con concha"
        },
        {
            "title": "octopus",
            "path": "../btpy/res/image/capture/octopus.png",
            "description":"es un molusco predador"
        }
    ])
    window.start()

main()