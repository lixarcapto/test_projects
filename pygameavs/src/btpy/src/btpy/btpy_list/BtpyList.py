


from .in_deps import*
from ..btpy_gui.BtpyGui import BtpyGui

class BtpyList(BtpyGui):
    
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
    
    def MatrixIterator(list)->MatrixIterator:
        return MatrixIterator(list)
    
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
        return seek_all(array, condition)
    
    def seek_number(array:list, number:int, 
        condition)->list:
        """
        función que busca la cantidad 
        determinada de elementos por la 
        condición enviada en la lista
        """
        return seek_number(array, number, 
            condition)
    
    def clean_voids(ARRAY)->list:
        """
        Función que crea un nuevo 
        eliminando todos los valores 
        None y void
        """
        return clean_voids(ARRAY)

