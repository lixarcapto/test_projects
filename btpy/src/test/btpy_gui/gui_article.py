

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

text = """
Los cuatro hobbits franquearon el ancho umbral de piedra y se
detuvieron, parpadeando. La habitación era larga y baja, iluminada por unas
lámparas que colgaban de las vigas del cielo raso y en la mesa de madera
oscura y pulida había muchas velas altas y amarillas, de llama brillante.
 En el extremo opuesto de la habitación, mirando a la puerta de entrada,
estaba sentada una mujer. Los cabellos rubios le caían en largas ondas sobre
los hombros; llevaba una túnica verde, verde como las cañas jóvenes,
salpicada con cuentas de plata como gotas de rocío y el cinturón era de oro,
labrado como una cadena de azucenas y adornado con ojos de nomeolvides,
azules y claros. A sus pies, en vasijas de cerámica verde y castaña, flotaban
unos lirios de agua, de modo que la mujer parecía entronizada en medio de un
estanque. 
"""

def main():
    window = Btpy.Window("titulo")
    window.set_is_fullscreen(True)
    article = Btpy.Article(window,
        "Articulo")
    article.set_title_article("Titulo")
    article.set_content(text)
    article.set_subtitle("Subtitulo")
    article.pack()
    window.start()

main()