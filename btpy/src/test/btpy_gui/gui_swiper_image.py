

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
    swiper = Btpy.SwiperImage(window, 
        "animales")
    swiper.draw_in_direction()
    swiper.set_is_cyclical(True)
    swiper.set_arroy_is_bold(True)
    swiper.set_image_size(300, 300)
    n = 0
    def fn(e):
        nonlocal n
        print(f"activar {n}")
        n += 1
    swiper.add_listener(fn)
    swiper.set_content([
        "../btpy/res/image/capture/clam.png",
        "../btpy/res/image/capture/hake.png",
        "../btpy/res/image/capture/octopus.png",
        "../btpy/res/image/capture/sardine.png"
    ])
    window.start()

main()