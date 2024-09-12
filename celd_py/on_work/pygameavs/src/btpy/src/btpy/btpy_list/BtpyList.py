


from .in_deps import*
from ..btpy_const.BtpyConst import BtpyConst

class BtpyList(BtpyConst):

    def get_keys(dict) -> list[str]:
        """
        Funcion para obtener las 
        claves de un diccionario 
        como un array.
        """
        return get_keys(dict)
    
    def true_percentage(array:list[bool])\
            ->float:
        """
        Función que calcula el 
        porcentaje de datos verdaderos 
        de una lista booleana
        """ 
        return true_percentage(array)
    
    def create_list(size:list):
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
