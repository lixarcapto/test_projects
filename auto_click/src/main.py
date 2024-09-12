
import pyautogui
import time
from pynput.keyboard import Listener
from pynput import keyboard
import threading
import sys
import pynput.mouse as mouse
from btpy.src.btpy.Btpy import Btpy
from threading import Thread

class Model:

    def __init__(self) -> None:
        self.button_key = 'left'
        self.time_skip = 2
        self.sensibility = 1
        self.is_on = Btpy.Duplicate(True)

    def start(self):
        self.init_escape_listener()
        self.init_mouse_listener()
        self.init_button_press()

    def init_button_press(self):
        def action(n):
            if(not mouse_moved(self.sensibility)):
                print("do_click")
                pyautogui.click(
                    button=self.button_key)
            else:
                print("not_click")
                time.sleep(self.time_skip)
            if(not self.is_on.get()): 
                sys.exit(0)
        repeat_each(1, action, 30)
        """
        hilo1 = threading.Thread(
            target=thread_2, 
            args=("Hilo 1",)
        )
        hilo1.start()
        """

    def init_escape_listener(self):
        def on_press(key):
            if key == keyboard.Key.esc:
                print('El usuario presionó Escape')
                self.is_on.set(False)
                sys.exit(0)
                return False
        # Create and start the keyboard listener in a separate thread
        keyboard_listener = keyboard.Listener(
            on_press=on_press)
        listener_thread = Thread(
            target=keyboard_listener.start)
        listener_thread.start()

    def init_mouse_listener(self):
        def on_click(x, y, button, pressed):
            if button == mouse.Button.right and pressed:
                print('El usuario hizo clic derecho')
                self.button_key = "right"
            elif button == mouse.Button.left and pressed:
                print('El usuario hizo clic izquierdo')
                self.button_key = "left"
        # Create and start the mouse listener in a separate thread
        mouse_listener = mouse.Listener(
            on_click=on_click)
        mouse_thread = Thread(
            target=mouse_listener.start)
        mouse_thread.start()

def main():
    print("init...")
    #
    model = Model()
    model.start()


def mouse_moved(sensibilidad=5):
    """
    Detecta si el mouse se 
    ha movido más allá de un umbral 
    de sensibilidad.
    """
    posicion_actual = pyautogui.position()
    time.sleep(0.1)  
    # Pequeña pausa para permitir el 
    # movimiento del mouse
    nueva_posicion = pyautogui.position()
    # Calcula la distancia euclidiana entre las dos posiciones
    distancia = ((nueva_posicion[0] \
        - posicion_actual[0])**2 \
        + (nueva_posicion[1] \
        - posicion_actual[1])**2)**0.5
    return distancia > sensibilidad
    
def autoclick(intervalo):
    """
    Simula un clic derecho del mouse en 
    la posición actual cada 'intervalo' 
    segundos.
    intervalo (int): Número de segundos 
    entre cada clic.
    """
    while True:
        pyautogui.click(button='right')
        time.sleep(intervalo)

# añadir la funcion como patron
def repeat_each(INTERVAL_TIME:int, FUNCTION,  
        REPETITIONS:int|float = -1):
    """
    Repite la función especificada cada 
    cierto intervalo que retorna una flag
    para controlar la repeticion y retorna 
    una flag. Tambien recibe un numero int que 
    indica el numero de repeticiones.
    """
    flag = True
    n = 0
    result = None
    while flag:
        result = FUNCTION(n)
        # permite romper el bucle durante 
        # la ejecucion
        if(not type(result) == bool):
            flag = True
        else:
            flag = result
        # permite añadir un limite
        if(not REPETITIONS == -1
        or not REPETITIONS == 0):
            if(n >= REPETITIONS -1):
                break
        time.sleep(INTERVAL_TIME)
        n += 1

main()