

from .in_deps import*
from .out_deps import*

class Btpy:

    """
    Módulo de funcionalidades básicas para 
    mejorar la experiencia de desarrollo 
    en python.
    """

    def random_bool() -> bool:
        """
        Función que genera un dato boolean 
        aleatorio
        """
        return random_bool()
    
    def random_choice(array):
        return random_choice(array)
    
    def random_without(range: int, 
        repeated_int_ar: list,
        is_exclusive:bool = False
        ) -> int:
        return random_without(
            range, 
            repeated_int_ar, 
            is_exclusive
        )
    
    def random_probability(porcentage: int)\
          -> bool:
        return random_probability(porcentage)
    
    def repeat(repetition: int, 
           seconds: int, 
           function):
        repeat(repetition, 
           seconds, 
           function)
        
    # return array or dict
    def map(array, function):
        return mapp(array, function)
    
    def iterator(array, 
                 is_cycle = False):
        return Iterator(array, is_cycle)
    
    def get_abc_tuple():
        return ABC_TUPLE
    
    def get_number_tuple():
        return NUMBER_TUPLE
    
    def get_animal_array():
        return ANIMAL_ARRAY
    
    def get_vegetable_dict():
        return VEGETABLE_DICT
    
    def init_array(range, value = None):
        return init_array(range, value)

    def calculate_mid(array:list) ->float:
        """
        Función que calcula el
        promedio de los números en
        la matriz enviada.
        """
        return __calculate_mid(array)
    
    def deep(array) -> int:
        return deep(array)
    
    def key_by_index(dict, index: int) \
        -> str:
        return key_by_index(dict, int)
    
    # return string_list
    def get_keys(dict) -> list:
        return get_keys(dict)
    
    """
    Function to identify if the input 
    number is contained within the 
    sending range.
    Ex:
        code: print(in_range(5, [4, 6]))
        output: True
    """
    def in_range(number: int, range: list)\
        -> bool:
        return in_range(number, range)
    
    def part_from_percent(percent: int, 
        total: int) -> float:
        return part_from_percent(percent, 
            total)
    
    def percent_from_part(part: int, 
        total: int)-> float:
        return percent_from_part(part, 
            total)
    
    def total_from_part(percent, 
        part: int) -> float:
        return total_from_part(percent, 
            part)
    
    """
    function to validate the sent string; 
    this validates if the string is a 
    string, is not empty and is greater 
    than the minimum (optional)
    """
    def valid_string(data: str, 
             min_size = -1,
             is_strict = False):
        valid_string(data, min_size, is_strict)

    def randint_list(size: int, 
        range_arr: list) -> list:
        return randint_list(int, range_arr)
    
    # return number
    def set_inrange(value: int, 
            range_arr: list):
        return set_inrange(value, range_arr)
    
    # return number
    def sum_in_range(value_a, value_b, 
                    range_arr):
        return sum_in_range(value_a, 
            value_b, range_arr)
    
    def dict_to_array(dict) -> list:
        return dict_to_array(dict)
    
    # not return
    def valid_index(index: int, leng: int):
        return valid_index(index, leng)
    
    # return element type
    def sum_array(array):
        return sum_array(array)
    
    def percent_to_index(percent, limit):
        return percent_to_index(percent, 
                    limit)
    
    # useless
    def fuse(array_a, array_b) -> list:
        return fuse(array_a, array_b)
    
    def is_error(value):
        return is_error(value)
    
    # return int
    def random_without_repeat(range_arr, 
        repeated_int_ar,
        is_exclusive = False):
        return random_without_repeat(
            range_arr, 
            repeated_int_ar,
            is_exclusive)
    
    def random_ip():
        return random_ip()
    
    def missing_numbers(number_list):
        return missing_numbers(number_list)
    
    def switch():
        return Switch()
    
    def counter_call(limit: int):
        return CounterCall(limit)
    
    def probability():
        return Probability()
    
    # return int
    def compare_strings(strig_primal, 
            string_to_compare):
        return compare_strings(strig_primal, 
            string_to_compare)
    
    def related_dict(similar_percent: int = 70):
        return RelatedDict(similar_percent)
    
    def charat(string:str, index:int) -> str:
        return charat(string, index)
    
    def cut_from(string: str, caracter: str, 
        / ,last_appearance:bool = False)\
            -> str:
        """
        Funcion que corta el string enviado 
        desde donde aparece el string indicado 
        returnando la primera parte del string.
        Si no encuentra el carácter indicado 
        retorna un String void.
        last_appearance: buscara la ultima 
        aparicion
        """
        return cut_from(string, caracter, 
            last_appearance)
    
    def cut_until(string: str, caracter: str, 
        / ,last_appearance:bool = False)\
            -> str:
        """
        Funcion que corta el string enviado 
        hasta donde aparece el string indicado 
        returnando la primera parte del string.
        Si no encuentra el carácter indicado 
        retorna un String void.
        last_appearance: buscara la ultima 
        aparicion 
        """
        return cut_until(string, caracter, 
                last_appearance)
    
    # return string_array
    def divide_string(index:int, string:str)\
        -> list:
        return divide_string(index, string)
    
    # return string
    def next_word(text: str, 
            searched_string: str):
        return next_word(text, 
            searched_string)
    
    def get_between(base:str, start:str,
        end:str) -> str:
        return get_between(base, start, end)
    
    def insert_string(index:int, base_string:str, 
        new_string:str) -> str:
        return insert_string(index,
            base_string, new_string)
    
    def normalize(text: str) -> str:
        return normalize(text)
    
    def split_by(string, dividers_arr: list):
        return split_by(string, dividers_arr)
    
    def simil_search(array:list, element:str, 
        required_percent:int) -> str:
        return simil_search(array, element, 
                required_percent)
    
    def get_description(string,
        separator_string, range_string_array):
        return get_description(
            string,
            separator_string, 
            range_string_array
            )
    
    """
    Function that converts the elements of 
    an array into the keys of a dictionary; 
    with the data sent as an element.
    EXAMPLE:
        array = ['a', 'b', 'c', 'd', 'e']
        result:list = Basic.array_to_dict(array)
        print(result)
    OUTPUT:
        {'a': None, 'b': None, 'c': None, 
        'd': None, 'e': None}
    """
    def array_to_dict(array:list, 
    data_type = None)->dict:
        return array_to_dict(array, 
            data_type)
    
    """
    Function that returns an element of 
    the array if the sent function returns 
    true. If the element does not exist, 
    it returns a value of none.
    EXAMPLES: 
    """
    def seek(function, array:list) ->list:
        return seek(function, array)
    
    """
    Function that applies the strip function 
    to all strings in a string array.
    """
    def strip_array(array:list[str])\
        ->list[str]:
        return strip_array(array)
    
    """
    function that replaces an element of the 
    sent array with the new element, looking 
    for an element that returns true in the 
    sent function.
    """
    def update(function, array:list, element)\
        ->list:
        return update(function, array, element)
    
    def whats_ranges(ranges_named:dict, 
            number:int)->list[str]:
        return whats_ranges(ranges_named,
                number)
    
    def count_keys(keys_array:list[str])\
        ->dict[int]:
        return count_keys(keys_array)
    
    # upgrade
    def layout_image(name_image_arr:\
            list[str] = []):
        return LayoutImage(name_image_arr)
    
    # upgrade
    def motion_image(self, name = ""):
        return MotionImage(name)
    
    def crono():
        return Crono()
    
    def pause(seconds:int):
        time.sleep(seconds)
    
    def splitip(text:str, divider:str)\
            ->list[str]:
        return splitip(text, divider)
    
    def repeat_in_thread(interval:int, 
        action, limit:int = -1)->None:
        return repeat_in_thread(interval,
            action, limit)
    
    def route_in_nested_dict(seek_string:str,
        dict:dict[dict]) ->list[str]:
        return route_in_nested_dict(
            seek_string, dict)

    def random_point(range_ar:list[int])\
            ->list[int]:
        """
        Función que genera un punto Aleatorio 
        en el rango enviado. El formato de punto 
        es un array numerico 2x.
        """
        return random_point(range_ar)

    def random_polygon(quantity:int, 
            range_ar:list[int])\
            ->list[list[int]]:
        """
        Función que genera una lista al de puntos 
        aleatorios en la cantidad indicada dentro 
        del Rango enviado
        """
        return random_polygon(quantity, 
            range_ar)
    
    def random_polygon_line(quantity:int, 
            range_ar:list[int]|list[float])\
            -> list[list[int] \
            |list[list[float]]]:
        """
        Función que genera un polígono de 
        líneas aleatorio en el rango enviado 
        con el número de líneas indicado.
        """
        return random_polygon_line(quantity, 
            range_ar)

    # useless por f format que es mas rapido
    def enclose(symbol, text):
        return symbol + text + symbol
    
    def randindex(array):
        return random.randint(0,
            len(array) -1)

    def randrange(range_arr):
        return random.randint(range_arr[0], 
                range_arr[1])
    
    def clean_console():
        os.system ("cls")

    # upgrade
    def date_manager()->DateManager:
        return DateManager()
    
    def has_all(array, function):
        return has_all(array, function)

    def has_some(array, function):
        return has_some(array, function)
    
    def has_none(array, function):
        return has_none(array, function)
    
    def new_thread(function):
        return new_thread(function)
    
    def range_space():
        return RangeSpace()
    
    # return point
    def move_point( 
        old_point:list[int], 
        new_point:list[int], 
        range_x:list[int],
        range_y:list[int]
    ) -> list[int]:
        return sum_point(old_point, 
            new_point, range_x, range_y)
    
    def is_number(data) -> bool:
        return is_number(data)
    
    # mejorar
    def resize_image(route, range_arr)->str:
        return resize_image(route, range_arr)
    
    def is_byte(data)-> bool:
        return is_byte(data)
    
    def is_rgb(data):
        return is_rgb(data)
    
    def is_rgba(data):
        return is_rgba(data)
    
    def raise_error(text:str, data, 
            correction:str)->None:
        """
        Función que lanza una excepción de 
        forma más ordenada mostrando el dato 
        enviado y una solución al final.
        """
        return raise_error(text, data, 
            correction)
    
    """
    Función que valida una lista enviada 
    si es lista, si no es void y si tiene 
    la profundidad indicada[opcional]
    """
    def valid_list(array:list, 
        deep_int:int = -1) ->None:
        valid_index(array, deep_int)

    """
    Decorador para ejecutar test e 
    imprimirlos en consola de forma 
    ordenada
    """
    def printtest(function):
        def wrapper():
            print(f"init test {function.__name__}()")
            function()
            print("succesfull test")
        return wrapper
    
    """
    iterador con un dict que solicita 
    una serie de datos utilizando un bucle 
    indefinido con un input para retornar un dict
    """
    def request_input(request_dict:list[str]):
        return request_input(request_dict)
    
    def vector_sum(array1:list[int], 
        array2:list[int])->list[int]:
        """
        Función que suma los elementos 
        de dos arrays de números en la 
        misma posición del array.
        """
        return vector_sum(array1, array2)
    
    def polygon_matrix(size_celd, 
      size_x, size_y):
        return polygon_matrix(size_celd, 
        size_x, size_y)
    
    def url_split(url:str)->dict[str]:
        """
        Función que divide una URL 
        retornando un diccionario con las 
        secciones de la URL en claves 
        protocol, domain, route y query
        """
        return url_split(url)
    
    def point_in_space(punto:list[int], 
                   rango_x:list[int], 
                   rango_y:list[int])\
                    ->bool:
        return point_in_space(
            punto,
            rango_x, 
            rango_y
        )
    
    def is_point(self, data, dimension):
        if(not type(data) == list):
            return False
        if(not len(data) == dimension):
            return False
        for e in data:
            if(not type(e) == int 
            or not type(e) == float):
                return False
        return True
    
    def center_square_by_point(
        punto_a_centrar, 
        esquina_superior_derecha, 
        esquina_inferior_izquierda,
        size_square
        ):
        return center_square_by_point(
            punto_a_centrar, 
            esquina_superior_derecha, 
            esquina_inferior_izquierda,
            size_square
        )
    
    def positive(number:int|float)\
        ->int|float:
        """
        Función de que convierte 
        el número recibido en el número 
        positivo más cercano.
        """
        return positive(number)
    
    def is_even(number: int|float)->bool:
        """
        Comprueba si un número es par 
        retornando un booleano.
        """
        return is_even(number)
    
    def is_prime(number:int)->bool:
        """
        Comprueba si un número es primo 
        retornando un booleano.
        """
        return is_prime(number)
    
    def is_point(data, size:int):
        return is_point(data, size)
    
    def rectangle_to_space(
            top_left, 
            bottom_right)->list[int]:

        """
        Calcula el tamaño de los lados de un rectángulo conociendo sus esquinas superior izquierda e inferior derecha.

        Args:
            top_left: Tupla (x, y) que representa el punto superior izquierdo del rectángulo.
            bottom_right: Tupla (x, y) que representa el punto inferior derecho del rectángulo.

        Returns:
            Tupla (ancho, alto) que representa el ancho y el alto del rectángulo.
        """
        x_axe = abs(bottom_right[0] - top_left[0])
        y_axe = abs(bottom_right[1] - top_left[1])
        return [x_axe, y_axe]

