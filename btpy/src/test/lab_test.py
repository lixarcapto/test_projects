

import sys
import os

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)

from btpy.Btpy import Btpy

import pyautogui
import time

def simular_clics(coordenadas):
    """
    Simula clics en una lista de coordenadas.

    Args:
        coordenadas (list): Una lista de tuplas (x, y) que representan las coordenadas de los clics.
    """
    try:
        for x, y in coordenadas:
            pyautogui.click(x, y)
            print(f"Clic simulado en ({x}, {y})")
            time.sleep(1)  # Espera 1 segundo entre clics
    except pyautogui.FailSafeException:
        print("El mouse se movió a una esquina de la pantalla. Deteniendo la simulación.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def main():
    

main()