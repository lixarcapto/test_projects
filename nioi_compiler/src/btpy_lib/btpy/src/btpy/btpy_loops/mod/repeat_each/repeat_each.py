

import time
from ....btpy_checkers.mod\
    .is_number.is_number import*

def repeat_each(INTERVAL_TIME:int, 
        FUNCTION,  
        REPETITIONS:int|float = -1)->None:
    """
    Repite la función especificada cada 
    cierto intervalo que retorna una flag
    para controlar la repeticion. 
    Tambien recibe un numero int que 
    indica el numero de repeticiones.
    """
    if(not type(REPETITIONS) == int):
        raise Exception(
            f"REPETITIONS is not int "\
            + f"{REPETITIONS}")
    if(not is_number(INTERVAL_TIME)):
        raise Exception(
            f"INTERVAL_TIME is not a number "\
            + f"{INTERVAL_TIME}")
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