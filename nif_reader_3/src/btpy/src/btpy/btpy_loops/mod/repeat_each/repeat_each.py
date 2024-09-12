

import time

def repeat_each(INTERVAL_TIME:int, 
        FUNCTION,  
        REPETITIONS:int|float = -1)->None:
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