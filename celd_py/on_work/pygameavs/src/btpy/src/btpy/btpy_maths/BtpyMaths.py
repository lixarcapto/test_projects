

from .in_deps import*
from ..btpy_loops.BtpyLoops import BtpyLoops

class BtpyMaths(BtpyLoops):

    def abs_sum(a_chief:int|float, 
        b:int|float)->int|float:
        """
        Funcion que suma número a otro 
        ignorando los negativos y 
        manteniendo el símbolo del primer 
        número.
        """
        return abs_sum(a_chief, b)
    
    def get_symbol(n:int|float)->int:
        """
        Función que retorna un valor 
        1 o -1 segun el símbolo del 
        número enviado
        """
        return get_symbol(n)
    
    def mid(array:list)->float:
        """
        Función que calcula el
        promedio de los números en
        la matriz enviada.
        """
        return mid(array)
    
    def set_in_range(value: int, 
        range_arr: list)->int:
        """
        Funcion que ajusta un valor en el 
        rango limite enviado.
        """
        return set_in_range(value, 
            range_arr)
    
    def random_probability(porcentage: int)\
    -> bool:
        """
        Funcion que genera un boolean 
        aleatorio basado en el porcentaje 
        enviado.
        """
        return random_probability(
            porcentage)
    
    def vector_sum(array1:list[int], 
        array2:list[int])->list[int]:
        """
        Función que suma los elementos 
        de dos arrays de números en la 
        misma posición del array.
        """
        return vector_sum(array1, array2)
    
    def sum_in_range(value_a:int|float, 
        value_b:int|float, 
        range_arr:list[int|float]):
        """
        Funcion que suma dos valores en 
        un rango limitado, si supera o es 
        inferior al rango se limita a 
        ajustar el limite.
        """
        return sum_in_range(value_a, 
            value_b, range_arr)
    
    def part_from_percent(percent: int, 
        total: int) -> float:
        return part_from_percent(
            percent, total
        )
    
    def percent_from_part(part: int, 
        total: int)-> float:
        return percent_from_part(part, 
            total)
    
    def total_from_part(percent, 
        part: int) -> float:
        return total_from_part(percent, 
            part)
    
    def percent_to_index(percent, limit):
        """
        convierte un porcentaje a un 
        índice dentro de un rango 
        específico.
        """
        return percent_to_index(percent, 
            limit)
    
    def sum_point( 
        old_point:list[int], 
        new_point:list[int], 
        range_x:list[int],
        range_y:list[int]
        ) -> list[int]:
        """
        Función que desplaza un a otro 
        punto sin superar los límites 
        que los ejes enviados como 
        intervalos.
        """
        return sum_point( 
            old_point, 
            new_point, 
            range_x,
            range_y
        )
    
    def whats_range(ranges_named:dict, 
            number:int)->list[str]:
        """
        Función que analiza En qué Rango 
        del diccionario de rangos enviados 
        se encuentra el número enviado 
        retornando la clave que identifica 
        al Rango
        """
        return whats_range(ranges_named, 
            number)
    
    def point_in_space(punto:list[int], 
                   rango_x:list[int], 
                   rango_y:list[int])\
                    ->bool:
        """
        Analiza y verifica si un punto 
        en forma de lista se encuentra 
        dentro de los intervalos de los 
        ejes enviados en x e y.
        """
        return point_in_space(punto, 
            rango_x, rango_y)
    
    def Probability():
        """
        Es un objeto que sirve para 
        calcular probabilidades 
        multiples. Para usarlo deben 
        enviarse con el metodo add
        claves con su probabilidad 
        entera; y el metodo calculate
        generara un resultado basado 
        en esas probabilidades.
        """
        return Probability()
    
    def translade_points(
      lista_puntos, 
      origen_x, 
      origen_y, 
      ancho, 
      alto
    ):
        """
        Traslada una lista de puntos a un 
        nuevo espacio rectangular.
        """
        return translade_points(
            lista_puntos, 
            origen_x, 
            origen_y, 
            ancho, 
            alto
        )
    
    # return point
    def center_square(point:list[int], 
        size_x:int, 
        size_y:int)->list[int]:
        """
        This function calculates the center 
        point of a square represented by 
        a dictionary.
        """
        return center_square(point, size_x, 
            size_y)
    
    def colliding_square(square1:dict[int], 
      square2:dict[int])->bool:
        """
        This function checks if two squares 
        are colliding based on their 
        coordinates and dimensions. By gemini.
        square = {
            "x":location_x
            "y":location_y
            "width":size_x
            "height":size_y
        }
        """
        return colliding_square(square1, 
            square2)
    
    def origin_by_center(point:list[int], 
      size_x:int, size_y:int)->list[int]:
        """
        Encuentra el punto de origen 
        (esquina superior izquierda) 
        de un rectángulo.
        """
        return origin_by_center(point,
            size_x, size_y)