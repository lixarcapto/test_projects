

import time
from ....btpy_checkers.mod\
    .is_number.is_number import*

def repeat_each(INTERVAL_TIME:int, 
        FUNCTION)->None:
    """
    Repite la función especificada cada 
    cierto intervalo que retorna una flag
    para controlar la repeticion. Si 
    la funcion retorna True se terminaran
    las repeticiones.
    Tambien recibe un numero int que 
    indica el numero de repeticiones.
    """
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
        if(result == True):
            flag = False
        else:
            flag = True
        time.sleep(INTERVAL_TIME)
        n += 1