


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
    
    def sum_dict(DICT_1:dict[str, int],
             DICT_2:dict[str, int])->dict:
        """
        Funcion que permite sumar dos 
        diccionarios de numeros.
        """
        return sum_dict(DICT_1, DICT_2)

    def contains_dict(
            CONTAINER:dict[str, int],
            CONTENT:dict[str, int])->bool:
        """
        Funcion que verifica si un diccionario
        contiene las cantidades de otro 
        diccionario.
        """
        return contains_dict(
            CONTAINER, 
            CONTENT
        )
    
    def substract_dict(MINUEND:dict, 
        SUBTRANDH:dict)->dict:
        """
        Funcion que resta un diccinario
        de numeros a otro diccionario de
        numeros.
        """
        return substract_dict(
            MINUEND,
            SUBTRANDH
        )
    
    def natural_substract_dict(
            MINUEND:dict, 
            SUBTRANDH:dict)->dict:
        """
        Funcion que resta un diccinario
        de numeros a otro diccionario de
        numeros.
        """
        return natural_substract_dict(
            MINUEND,
            SUBTRANDH
        )
    
    def witch_dict_contains_it(
            nested_dict:dict[str, dict], 
            content:dict[str, int])->str:
        """
        Funcion que identifica que 
        diccionario de un diccionario 
        anidado contiene un diccionario 
        numerico
        """
        return witch_dict_contains_it(
            nested_dict,
            content
        )

    def dict_number_are_equal(
        DICT_1:dict[str, int], 
        DICT_2:dict[str, int])->bool:
        """
        Funcion que identifica si dos 
        diccionarios numericos son iguales
        ignorando los valores 0.
        """
        return dict_number_are_equal(
            DICT_1,
            DICT_2
        )

    def identify_dict_number(
            NESTED_DICT:dict[dict], 
            DICT_NEW:dict[str, int])->str:
        """
        Funcion que identifica la clave de
        un diccionario numerico que sea 
        igual al diccionario numerico 
        enviado. Ignora los valores 0.
        """
        return identify_dict_number(
            NESTED_DICT,
            DICT_NEW
        )
    

    
