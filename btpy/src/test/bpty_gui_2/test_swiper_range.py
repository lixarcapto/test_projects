


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
    btn = Btpy.Button(
        window.widget, "click")
    swiper = Btpy.SwiperRange(
        window.widget,
        "swiper"
    )
    swiper.set_content([1, 100])
    swiper.grid(0, 0)
    swiper.set_is_visible_range(False)
    def fn():
        print(swiper.get_value())
    swiper.add_change_listener(fn)
    window.start()

main()