

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
    question = Btpy.Questionary(
        window, "question")
    question.pack()
    question.set_questionary_list([
        {
            "question":"Pais mas grande",
            "option_list":["Rusia", "China"]
        },
        {
            "question":"Color del cobre oxidad",
            "option_list":["Verde", "rojo"]
        },
        {
            "question":"Capital de Serbia",
            "option_list":["Belgrado", "Sofia"]
        },
        {
            "question":"Material de construccion antiguo",
            "option_list":["Adobe", "Pladur"]
        } 
    ])
    def fn(answer_list):
        print(answer_list)
    question.add_listener(fn)
    window.start()

main()