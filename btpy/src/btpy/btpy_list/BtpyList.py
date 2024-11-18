


from .in_deps import*
from ..btpy_images.BtpyImages import BtpyImages

class BtpyList(BtpyImages):

    MatrixIterator = MatrixIterator
    
    def true_percentage(array:list[bool])\
            ->float:
        """
        Función que calcula el 
        porcentaje de datos verdaderos 
        de una lista booleana
        """ 
        return true_percentage(array)
    
    def create_list(size:list)->list:
        """
        función que genera una lista con 
        los tamaños determinados ya 
        inicializada con valores None;  
        los tamaños deben enviarse como 
        una lista de máximo 3 de largo de 
        números enteros Qué indican en este 
        orden el tamaño en y, x y z.
        """
        return create_list(size)
    
    def array_to_dict(array:list, 
        data_type = None)->dict:
        """
        Function that converts the elements 
        of an array into the keys of a 
        dictionary; with the data sent 
        as an element.
        """
        return array_to_dict(array, 
            data_type)
    
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
    
    def write(send_list:list)->str:
        return write(send_list)
    
    def seek_one(array:list, condition)\
        ->int|float|str|dict|list:
        """
        Función que busca un elemento por 
        la condición enviada en la lista.
        """
        return seek_one(array, condition)
    
    def seek_all(array:list, condition)->list:
        """
        función que busca todos los 
        elementos por la condición enviada 
        en la lista.
        """
        return filter2(array, condition)
    
    def filter2(DATA:list|dict, CONDITION, 
        QUANTITY:int = -1)->list:
        """
        función que busca la cantidad 
        determinada de elementos por la 
        condición enviada en la lista
        """
        return filter2(DATA, CONDITION,
            QUANTITY)
    
    def clean_voids(ARRAY)->list:
        """
        Función que crea un nuevo 
        eliminando todos los valores 
        None y void
        """
        return clean_voids(ARRAY)
    
    def join_dict(DICT_A:dict, 
            DICT_B:dict)->dict:
        """
        function that combines two 
        dictionaries into one.
        """
        return join_dict(DICT_A, DICT_B)
    
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
    
    def fit_list(LIST, SIZE, 
        FILL_TYPE = None)->list:
        """
        Funcion que ajusta la lista enviada 
        al tamaño indicado.
        """
        return fit_list(LIST, SIZE, 
            FILL_TYPE)
    
    def count(STRUCTURE:list|dict, CHECKER)\
        -> int:
        """
        Funcion que cuenta el numero de 
        verificaciones con una funcion 
        checker enviada.
        """
        return count(STRUCTURE, CHECKER)
    
    def find_value(DICT:dict, DATA)->str:
        """
        Busca la clave del valor enviado
        en el diccionario.
        """
        return find_value(DICT, DATA)

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
