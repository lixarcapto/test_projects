

from .in_deps import*
from config import*

class BtpyCheckers:

    CONFIG = config

    def are_all_same(array:list)->bool:
        """
        Checks if all elements
        of an array are equal.
        """
        return are_all_same(array)
    
    def in_range(number: int, range_arr: list)\
        -> bool:
        """
        Function to identify if the input 
        number is contained within the 
        sending range.
        """
        return in_range(number, range_arr)

    def is_number(data) -> bool:
        """
        Checks if the data sent
        is of a numeric type.
        """
        return is_number(data)
    
    def is_error(value)->bool:
        """
        Function that tests whether a value
        is a return error such as -1,
        none, void string, void dict, or void
        array
        """
        return is_error(value)
    
    def is_byte256(data)\
        -> bool:
        """
        función que verifica si el dato 
        enviado es un tipo byte 256
        """
        return is_byte256(data)

    def is_byte127(data)\
        -> bool:
        """
        función que verifica si el dato 
        enviado es un tipo byte 127
        """
        return is_byte127(data)
    
    def is_rgb(data)->bool:
        """
        Checker que verifica si un 
        dato es de tipo rgb lista
        """
        return is_rgb(data)
    
    def is_rgba(data)->bool:
        """
        Checker que verifica si un 
        dato es de tipo rgba lista
        """
        return is_rgba(data)
    
    def is_function(data)->bool:
        """
        Función que verifica si 
        un dato enviado este tipo 
        función retornando verdadero 
        sí lo es y falso si no
        """
        return is_function(data)
    
    def is_point_2d(data)->bool:
        """
        Función que verifica  el dato 
        enviado es un punto 2D
        """
        return is_point_2d(data, 2)


    def is_point_3d(data)->bool:
        """
        Función que verifica  el dato 
        enviado es un punto 3D
        """
        return is_point_3d(data, 3)
    
    
    
