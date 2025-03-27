

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
    swiper = Btpy.SwiperImage(window, 
        "animales")
    swiper.pack()
    swiper.set_is_cyclical(True)
    swiper.set_arroy_is_bold(True)
    swiper.set_image_size(300, 300)
    swiper.set_values_list([
        "../btpy/res/image/capture/clam.png",
        "../btpy/res/image/capture/hake.png",
        "../btpy/res/image/capture/octopus.png",
        "../btpy/res/image/capture/sardine.png"
    ])
    window.start()

main()