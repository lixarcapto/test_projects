


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

    def reset_counter(self)->None:
        self.start_time = time.time()

    def get_seconds_counted(self)\
            ->float:
        """
        Funcion que obtiene el tiempo 
        contado desde la creacion del 
        objeto Crono en segundos.
        """
        end_time = time.time()
        elapsed_time = end_time \
            - self.start_time
        return elapsed_time