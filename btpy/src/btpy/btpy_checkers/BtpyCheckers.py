

from .in_deps import*
from config import*

class BtpyCheckers:

    CONFIG = config

    def is_number(data) -> bool:
        """
        Comprueba si el dato enviado 
        el de un tipo numérico.
        """
        return is_number(data)
    
    def is_error(value)->bool:
        """
        Funcion que analiza si un valor 
        es un error de retorno como  -1, 
        none, void string, void dict o void 
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
    
    def in_range(number: int, range_arr: list)\
        -> bool:
        """
        Function to identify if the input 
        number is contained within the 
        sending range.
        Eg:
        code: print(in_range(5, [4, 6]))
        output: True
        """
        return in_range(number, range_arr)
    
    def are_all_same(array:list)->bool:
        """
        Verifica si todos los elementos 
        de un array son iguales.
        """
        return are_all_same(array)
