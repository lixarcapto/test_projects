


from .in_deps import*
from ..btpy_internet.BtpyInternet import BtpyInternet
from typing import Callable

class BtpyList(BtpyInternet):

    """
    Modulo estatico de herramientas
    para trabajar con listas.
    """

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
    
    def filter(
            ITERABLE:list|tuple|dict
            |set|str, 
            CHECKER_FUNCTION
            :Callable[[any], bool])\
            ->list[any]:
        """
        TESTED
        Filter function that obtains all 
        elements of an iterable that meet 
        a given condition. The given 
        condition is defined by the checker 
        function passed; the checker 
        function must receive the data 
        type of the iterable with a single 
        parameter and return a boolean.
        """
        return filter(ITERABLE, CHECKER_FUNCTION)
    
    def write(send_list:list)->str:
        return write(send_list)
    
    def clean_voids(ARRAY : list)->list:
        """
        TESTED
        Función que crea un nuevo array
        eliminando todos los valores de 
        tipo None y void como void 
        string "", void array [], y 
        void dict {}
        """
        return clean_voids(ARRAY)
    
    def fit(ORDERDER_ITERABLE
            :list|tuple|str, 
            SIZE:int)->list:
        """
        Function that adjusts the sent list
        to the indicated size.
        """
        return fit(ORDERDER_ITERABLE, SIZE)
