


import time

class Crono:

    """
    Clase que almacena el tiempo 
    actual y retorna la resta del 
    nuevo tiempo en que el llamado
    el método stop
    """
    def __init__(self) -> None:
        self.start_time = time.time()

    def stop(self):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        return elapsed_time