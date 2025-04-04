

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
    swiper = Btpy.SwiperText(window, 
        "animales")
    swiper.pack()
    swiper.set_is_cyclical(True)
    swiper.set_values_list([
        "perro", "gato", "elefante", 
        "caiman"
    ])
    window.start()

main()