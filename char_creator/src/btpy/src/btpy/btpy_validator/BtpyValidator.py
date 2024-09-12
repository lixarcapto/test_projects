


from .in_deps import*
from ..btpy_utilitys.BtpyUtilitys import BtpyUtilitys

class BtpyValidator(BtpyUtilitys):

    def valid_string(data: str, 
        min_size = -1, /,
        is_strict:bool = False)->None:
        """
        funcion para validar la cadena 
        enviada; esto valida si la cadena 
        es una cadena, no esta vacia y 
        es mayor que el minimo (opcional)
        """
        valid_string(data, min_size, 
            is_strict)
        
    def valid_index(index: int, array: list)\
        ->None:
        """
        Funcion estricta de validacion para
        indices de arrays. Envia el array 
        a verificar.
        """
        valid_index(index, array)

    def valid_list(array:list, 
        deep_int:int = -1) ->None:
        """
        Función que valida una lista 
        enviada si es lista, si no es 
        void y si tiene la profundidad 
        indicada[opcional]
        """
        return valid_list(array, deep_int)