

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