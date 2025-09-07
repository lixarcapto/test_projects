


import threading
import time


def repeat_in_thread(interval:int, 
        limit, action)->None:
    """
    Función que repite una acción 
    enviada en un intervalo de 
    segundos usando un hilo propio.
    """
    n = 0
    def run_repeatedly():
        n = 0
        while True:
            action()  # Execute the action
            time.sleep(interval)  
            # Wait for the specified 
            # interval
            if(n == limit): break
            n += 1
        n = n
    # Create a thread to run the action 
    # repeatedly
    thread = threading.Thread(\
        target=run_repeatedly)
    thread.daemon = True  
    # Set the thread as a daemon 
    # to avoid blocking main thread exit
    thread.start()