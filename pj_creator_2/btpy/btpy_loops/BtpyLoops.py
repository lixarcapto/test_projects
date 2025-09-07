

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
    
    def repeat_each(INTERVAL_TIME:int, 
            FUNCTION)\
            ->None:
        """
        Repite la función especificada cada 
        cierto intervalo que retorna una flag
        para controlar la repeticion y retorna 
        una flag. Tambien recibe un numero int que 
        indica el numero de repeticiones.
        """
        repeat_each(INTERVAL_TIME, 
            FUNCTION)
        
    def mapp(DATA:list|dict|str, FUNCTION)\
        -> list|dict|str:
        """
        Function that improves the map 
        function to support dict, list and 
        str.
        """
        return mapp(DATA, FUNCTION)
