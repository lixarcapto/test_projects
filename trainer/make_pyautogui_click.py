


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