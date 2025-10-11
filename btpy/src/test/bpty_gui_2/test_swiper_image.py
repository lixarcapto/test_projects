


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
    swiper = Btpy.SwiperImage(
        window.widget,
        "imagenes")
    swiper.pack()
    swiper.set_content(
        [
            "./res/chica_normal_3.png",
            "./res/chica_pirata_1.png",
            "./res/chica_pirata_1.png",
            "./res/chica_pirata_1.png"
        ]
    )
    swiper.set_resize([300, 300])
    window.start()

main()