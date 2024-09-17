

from .in_deps import*
from ..btpy_list.BtpyList import BtpyList

class BtpyLoops(BtpyList):

    def mapp(array:dict|list, 
        function)\
        ->dict|list:
        """
        Funcion mapper mejorada para 
        permitir el recorrido de arrays 
        y diccionarios de cualquier 
        profundidad.
        """
        return mapp(array, function)
    
    def repeat(repetition: int, 
           seconds: int | float, 
           function):
        """
        Funcion de repeticion temporal 
        de una funcion en el hilo 
        actual. No crea un nuevo hilo.
        """
        repeat(repetition, seconds, 
            function)
    
    def has_all(array:list, function):
        """
        Función que itera sobre los 
        elementos del array enviado 
        buscando si todos los elementos 
        del array retornan true a la 
        función enviada.
        """
        return has_all(array, function)
    
    def has_none(array:list, function)->bool:
        """
        Función que itera sobre los 
        elementos del array enviado 
        buscando si ninguno de los 
        elementos del array retornan 
        true a la función enviada.
        """
        return has_none(array, function)
    
    def has_some(array:list, 
            function)->bool:
        """
        Función que itera sobre los 
        elementos del array enviado 
        buscando si alguno de los 
        elementos del array retornan 
        true a la función enviada.
        """
        return has_some(array, function)
    
    def repeat_each(INTERVAL_TIME:int, 
            FUNCTION,  
            REPETITIONS:int|float = -1)\
            ->None:
        """
        Repite la función especificada cada 
        cierto intervalo que retorna una flag
        para controlar la repeticion y retorna 
        una flag. Tambien recibe un numero int que 
        indica el numero de repeticiones.
        """
        repeat_each(INTERVAL_TIME, FUNCTION, 
            REPETITIONS)
