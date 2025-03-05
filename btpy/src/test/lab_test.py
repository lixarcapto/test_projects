

import sys
import os

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)

from ClickTrainer import ClickTrainer
import pyautogui
import time

def make_pyautogui_click(POINT):
    """
    Simula clics en una lista de 
    coordenadas.
    """
    try:
        for x, y in POINT:
            pyautogui.click(x, y)
            print(f"Clic simulado en ({x}, {y})")
            time.sleep(1)  # Espera 1 segundo entre clics
    except pyautogui.FailSafeException:
        print("El mouse se movió a una esquina de la pantalla. Deteniendo la simulación.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")





def main():
    make_pyautogui_click([[1060, 685]])
    #trainer = ClickTrainer()

main()