

from .in_deps import*

class BtpyCheckers:

    def are_all_same(array:list)->bool:
        """
        Checks if all elements
        of an array are equal.
        """
        return are_all_same(array)
    
    def in_range(NUMBER: int|float, 
            RANGE_ARR_X2: list[int])\
            -> bool:
        """
        TESTED
        Function to identify if the input 
        number is contained within the 
        sending range. The range sent is 
        an integer array where index 0 
        is min and 1 is max.
        """
        return in_range(
            NUMBER, 
            RANGE_ARR_X2
        )

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
    
    def is_byte_256(ANY_DATA : any)\
        -> bool:
        """
        TESTED
        Function that returns true if 
        the data sent is a byte 256 type, 
        that is, an 8-bit integer in the 
        range between 0 and 256.
        """
        return is_byte_256(ANY_DATA)

    def is_byte_127(ANY_DATA : any)\
            -> bool:
        """
        TESTED
        Function that returns true if 
        the data sent is a byte 127 type, 
        that is, an 8-bit integer between 
        the range -127 and 127.
        """
        return is_byte_127(ANY_DATA)
    
    def is_RGB(ANY : any)->bool:
        """
        TESTED
        Checker que verifica si un 
        dato es de tipo rgb lista
        """
        return is_RGB(ANY)
    
    def is_RGBA(ANY:any)->bool:
        """
        TESTED
        Checker que verifica si un 
        dato es de tipo rgba lista o tupla
        """
        return is_RGBA(ANY)
    
    def is_function(ANY : any)->bool:
        """
        TESTED
        Función que verifica si 
        un dato enviado este tipo 
        función retornando verdadero 
        sí lo es y falso si no. Considera
        funciones a las funciones lambda,
        las funciones con nombre y los 
        metodos.
        """
        return is_function(ANY)
    
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
    
    def is_range(RANGE_ARRAY:list[int]):
        """
        TESTED
        Función que devuelve True si los 
        datos enviados son de tipo array 
        de rango.
        """
        return is_range(RANGE_ARRAY)
    
    def is_hex_color(ANY : any):
        """
        TESTED
        Funcion que verifica si una cadena 
        es un color hexadecimal válido.
        """
        return is_hex_color(ANY)
    
    
    
