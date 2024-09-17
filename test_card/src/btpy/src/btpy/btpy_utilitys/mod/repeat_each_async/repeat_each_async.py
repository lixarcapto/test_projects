


import threading
import time


def repeat_each_async(
        INTERVAL_TIME:int, 
        FUNCTION,  
        REPETITIONS:int|float = -1)->None:
    """
    Repite la función especificada en 
    un thread propio cada cierto intervalo 
    que retorna una flag para controlar la 
    repeticion. Tambien 
    recibe un numero int que 
    indica el numero de repeticiones.
    """
    def run_repeatedly():
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
            if(REPETITIONS > 0):
                if(n >= REPETITIONS -1):
                    break
            time.sleep(INTERVAL_TIME)
            n += 1
    # Create a thread to run the action 
    # repeatedly
    thread = threading.Thread(\
        target=run_repeatedly)
    thread.daemon = True  
    # Set the thread as a daemon 
    # to avoid blocking main thread exit
    thread.start()