


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
    
    def map_in_keys(DICT:dict, 
            FUNCTION_PROCESSOR
            :Callable[[str], str])\
            ->dict:
        """
        TEST
        Function that goes through all the 
        keys in a dictionary by applying 
        the sent function.
        """
        return map_in_keys(DICT, 
            FUNCTION_PROCESSOR)
    
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
    
    def max_key(NUMBER_DICT
            :dict[str, int|float])\
            ->str:
        """
        TESTED
        Function that finds the maximum 
        value in a dictionary and returns 
        the key of that value. If there 
        are two equal values, it uses the 
        one that is first in the dictionary 
        order.
        """
        return max_key(NUMBER_DICT)
    
    def min_key(NUMBER_DICT
            :dict[str, int|float])\
            ->str:
        """
        TESTED
        Function that finds the minimum 
        value in a dictionary and returns 
        the key of that value. If there 
        are two equal values, it uses the 
        one that is first in the dictionary 
        order.
        """
        return min_key(NUMBER_DICT)
    
    

    
