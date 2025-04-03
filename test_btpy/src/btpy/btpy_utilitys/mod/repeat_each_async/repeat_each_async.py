


import threading
import time

def repeat_each_async(
        INTERVAL_TIME:int|float, 
        FUNCTION)->None:
    """
    Repite la función especificada cada 
    cierto intervalo que retorna una flag
    para controlar la repeticion. Si 
    la funcion retorna True se terminaran
    las repeticiones.
    Tambien recibe un numero int que 
    indica el numero de repeticiones.
    Esta funcion repite la callback en 
    un hilo propio asincrono al hilo
    principal.
    """
    def run_repeatedly():
        flag = True
        n = 0
        result = None
        while flag:
            result = FUNCTION(n)
            # permite romper el bucle durante 
            # la ejecucion
            if(result == True):
                flag = False
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