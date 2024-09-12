

import time
from ....btpy_checkers.mod\
    .is_number.is_number import*

def repeat(repetition: int, 
           seconds: int | float, 
           function):
    """
    Funcion de repeticion temporal de una
    funcion en el hilo actual. No crea
    un nuevo hilo.
    """
    if(not type(repetition) == int):
        raise Exception(
            f"repetition is not int "\
            + f"{repetition}")
    if(not is_number(seconds)):
        raise Exception(
            f"seconds is not a number "\
            + f"{seconds}")
    for i in range(repetition):
        time.sleep(seconds)
        function(i)
