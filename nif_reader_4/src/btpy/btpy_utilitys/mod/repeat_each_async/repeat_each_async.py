


import threading
import time
from ....btpy_utilitys.mod.duplicate.Duplicate import Duplicate

class FlagAsync:

    """
    Este objeto sirve para controlar
    la ejecucion del repetidor
    asincrono en segundo plano. Puedes
    detener el thread llamando al metodo
    stop y saber si esta activo llamando
    al metodo get_is_active.
    """

    def __init__(self):
        self.__bool:bool = True

    def get_is_active(self)->bool:
        """
        Indica si el thread esta activo
        ejecutandose.
        """
        return self.__bool

    def stop(self)->None:
        """
        Detiene el thread que se esta
        ejecutando en segundo plano.
        """
        self.__bool = False

def repeat_each_async(
        INTERVAL_TIME:int|float, 
        FUNCTION)->FlagAsync:
    """
    Repite la función especificada cada 
    cierto intervalo de forma asincrona. Si 
    la funcion retorna True se terminaran
    las repeticiones.
    Tambien recibe un numero int que 
    indica el numero de repeticiones.
    Esta funcion repite la callback en 
    un hilo propio asincrono al hilo
    principal.
    Retorna un objeto llamado FlagAsync 
    que tiene un metodo stop para
    detener el hilo, y un metodo 
    get_is_active para saber su estado.
    """
    flag = FlagAsync()
    def run_repeatedly():
        nonlocal INTERVAL_TIME
        nonlocal flag
        n = 0
        result = None
        while flag.get_is_active():
            # permite romper el bucle durante 
            # la ejecucion
            time.sleep(INTERVAL_TIME)
            result = FUNCTION(n)
            if(result == True):
                flag.stop()
            n += 1
    # Create a thread to run the action 
    # repeatedly
    thread = threading.Thread(\
        target=run_repeatedly)
    thread.daemon = True
    # Set the thread as a daemon 
    # to avoid blocking main thread exit
    thread.start()
    return flag