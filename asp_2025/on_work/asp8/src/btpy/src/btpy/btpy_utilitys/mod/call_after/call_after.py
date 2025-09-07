

import time
import threading

class Duplicate:
    def __init__(self, value = None) -> None:
        self.value = value

def call_after(SECONDS:int|float, CALL_BACK):
    """
    Ejecuta una función en un hilo 
    separado después de un tiempo 
    determinado. Retorna un objeto duplicate
    con un atributo value de la referencia del
    retorno de la funcion.
    """
    duplicate = Duplicate()
    def _wrapper():
        time.sleep(SECONDS)
        nonlocal duplicate 
        duplicate.value = CALL_BACK()
    thread = threading.Thread(target=_wrapper)
    thread.start()
    return duplicate