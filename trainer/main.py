

import sys
import os
import webbrowser

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)

from btpy.Btpy import Btpy
from create_path_bot import*
from make_pyautogui_click import*
import webbrowser
import time

def execute_bot(point_list):
    url = "https://www.facebook.com/"
    webbrowser.open_new(url)
    time.sleep(3.5)
    make_pyautogui_click(
        point_list)
    
def write(text):
    # Escribe el texto
    pyautogui.write("Python PyAutoGUI")
    # Simula la pulsación de la tecla Enter (opcional)
    pyautogui.press("enter")

def main():
    create_path_bot()
    #execute_bot([[768, 701]])
    #write("hola buenos dias")

main()