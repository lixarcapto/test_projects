


from .in_deps import*
from ..btpy_persistence.BtpyPersistence \
    import BtpyPersistence

class BtpyRandom(BtpyPersistence):

    # return element
    def random_choice(array: list):
        """
        Funcion wrapper para mejorar 
        choice de random library añadiendo 
        la posibilidad de randomizar 
        elementos de diccionarios.
        """
        return random_choice(array)
    
    def random_bool() -> bool:
        """
        Función que genera un dato boolean 
        aleatorio
        """
        return random_bool()
    
    def randint_list(size: int, 
            range_array: list[int]) \
            -> list[int]:
        return randint_list(size, 
            range_array)
    
    def random_without(range_arr: int, 
        repeated_int_ar: list,
        /, is_exclusive:bool = False
        ) -> int:
        """
        Funcion que genera un numero 
        aleatorio en el rango sin 
        repetir los numeros enviados 
        en la lista indicando si es 
        exclusivo o no.
        """
        return random_without(
            range_arr, 
            repeated_int_ar, 
            is_exclusive)
    
    def random_polygon(quantity:int, 
            range_ar:list[int])\
            ->list[list[int]]:
        """
        Función que genera una lista 
        al de puntos aleatorios es la 
        cantidad indicada dentro del 
        Rango enviado
        """
        return random_polygon(quantity, 
            range_ar)
    
    def random_polyline(quantity:int, 
            range_ar:list[int]|list[float])\
            -> list[list[int] \
            |list[list[float]]]:
        """
        Función que genera un polígono de 
        líneas aleatorio en el rango enviado 
        con el número de líneas indicado.
        """
        return random_polyline(quantity, 
            range_ar)
    
    def random_ip()->str:
        return random_ip()
    
    def random_mac():
        return random_mac()
    
    def random_phone(country:str)->str:
        return random_phone(country)
    
    def random_color():
        return random_color()
    
    def random_uniques(quantity:int, 
        range_arr:list[int])\
        ->list[int]:
        """
        función que genera una lista de 
        números aleatorios en un rango 
        sin repetir.
        """
        return random_uniques(quantity, 
            range_arr)
    
    def random_str(SIZE:int, 
            STRING:str)->str:
        """
        Genera un texto aleatorio de la 
        longitud especificada utilizando 
        los caracteres proporcionados.
        """
        return random_str(SIZE, STRING)
    
    def around(NUMBER, LIMIT)->int:
        return around(NUMBER, LIMIT)
    
    def rand_range(RANGE_ARR:list[int])->int:
        return rand_range(RANGE_ARR)
    
    import random

    def random_multi_probabilities(
            PROBABILITY_LIST: list) -> str:
        """
        Elige una clave de una lista de pares 
        [clave, valor] aleatoriamente,
        basado en los porcentajes de 
        probabilidad proporcionados en 
        los valores.
        Las probabilidades deben sumar 100.
        """
        return random_multi_probabilities(
            PROBABILITY_LIST
        )