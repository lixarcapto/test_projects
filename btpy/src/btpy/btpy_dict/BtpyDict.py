


from ..btpy_data_types.BtpyDataTypes import BtpyDataTypes
from .in_deps import*

class BtpyDict(BtpyDataTypes):

    def key_of(DICT:dict, VALUE:any)->str:
        """
        TESTED
        Function that searches for the 
        key associated with the value 
        sent in the dictionary.
        """
        return key_of(DICT, VALUE)
    
    def merge_as_dict(KEYS_LIST:list, 
            VALUES_LIST:list)->dict:
        """
        Funcion que crea un diccionario 
        utilizando dos listas.
        """
        return merge_as_dict(KEYS_LIST, 
            VALUES_LIST)
    
    def map_in_keys(OLD_DICT:dict, function)\
            ->dict:
        """
        function that goes through all the 
        keys in a dictionary by applying 
        the sent function.
        """
        return map_in_keys(OLD_DICT, 
            function)
    
    def find_closest_lower(DICT:dict, 
            NUMBER:int|float):
        """
        funcion que identifique en un 
        diccionario de numeros que numero 
        es el mas cercano inferior al numero 
        enviado retornando su clave.
        """
        return find_closest_lower(DICT, 
                NUMBER)
    
    def max_dict(dict:dict[int|float])\
            ->int|float:
        """
        Calcula el valor máximo en un 
        diccionario.
        """
        return max_dict(dict)
    
    def min_dict(dict:dict[int|float])\
            ->int|float:
        """
        Calcula la clave del valor mínimo 
        en un diccionario.
        """
        return min_dict(dict)
    
    

    
