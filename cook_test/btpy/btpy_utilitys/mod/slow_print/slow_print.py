

import time

def slow_print(text, speed = 0.4):
    """
    Función que imprime en consola el 
    texto enviado con una Pausa corta 
    tras cada carácter
    """
    if(not type(text) == str):
        text = str(text)
    if(len(text) == 1):
        print(text)
        return None
    for char in text:
        time.sleep(speed)
        print(char, end="", flush=True)