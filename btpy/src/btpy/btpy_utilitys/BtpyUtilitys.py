

from .in_deps import*
from ..btpy_string.BtpyString import BtpyString
import time

class BtpyUtilitys(BtpyString):

    Scenario = Scenario
    
    def deep(array:list) -> int:
        """
        Funcion que analiza la 
        profundidad de un array 
        retornando su nivel de 
        profundidad como un int, 
        si no es array retornara 0.
        TODO: Mejorar para que analize 
        tambien diccionarios.
        """
        return deep(array)
    
    def slow_print(text, speed = 0.4):
        """
        Función que imprime en consola el 
        texto enviado con una Pausa corta 
        tras cada carácter
        """
        slow_print(text, speed)

    def max_key(dict_of_numbers:dict)->str:
        """
        Calcula la clave mas alta en 
        un diccionario de numeros.
        """
        return max_key(dict_of_numbers)
    
    def min_key(dict_of_numbers:dict)->str:
        """
        Calcula la clave mas baja en 
        un diccionario de numeros.
        """
        return min_key(dict_of_numbers)
    
    def count_repeats(array:list)\
        ->dict[int]:
        """
        Función que cuenta el número 
        repeticiones de un dato en el 
        array enviado, retornando un 
        diccionario con la información 
        resultante.
        """
        return count_repeats(array)
    
    def print_test(function)->None:
        """
        Función decoradora para decorar 
        funciones de test que recibe 
        un array por referencia para 
        almacenar resultados boolean 
        que calculará al final de la 
        función mostrando un porcentaje 
        de verdaderos en consola; 
        además de mostrar al inicio 
        el nombre de la función como 
        título en consola.
        """
        return print_test(function)
    
    def request_input(
            request_dict:list[str])\
            -> dict:
        """
        iterador con un dict que 
        solicita una serie de datos 
        utilizando un bucle indefinido 
        con un input para retornar un dict
        """
        return request_input(request_dict)
    
    def new_thread(function):
        """
        Decorador para crear de forma 
        fácil y ágil nuevos hilos.
        """
        return new_thread(function)
    
    def polygon_matrix(size_celd, 
      size_x, size_y):
        return polygon_matrix(
            size_celd, size_x, size_y)
    
    def repeat_each_async(
            INTERVAL_TIME:int, 
            FUNCTION,  
            REPETITIONS:int|float = -1)->None:
        """
        Función que repite una acción 
        enviada en un intervalo de 
        segundos usando un hilo propio.
        """
        return repeat_each_async(
            INTERVAL_TIME, 
            FUNCTION, 
            REPETITIONS
            )
    
    def route_in_dict(seek_string:str,
            dict:dict[dict]) ->list[str]:
        """
        Función que busca en profundidad 
        una serie de claves ordenadas 
        por profundidad a través de 
        diccionarios de diccionarios 
        anidados.
        """
        return route_in_dict(seek_string, 
            dict)
    
    def Crono():
        """
        Clase que almacena el tiempo 
        actual y retorna la resta del 
        nuevo tiempo en que el llamado
        el método stop
        """
        return Crono()
    
    def pause(SECONDS):
        time.sleep(SECONDS)
    
    def clean_console():
        clean_console()

    def Iterator(array, /,
                 is_cycle = False):
        """
        Clase iterador para representar
        un recorredor de arrays que 
        almacena los indices tras cada 
        iteracion. para usarlo solo deben 
        llamarse a su metodo next dentro 
        del condicional del bucle y tomar 
        sus elementos con get.
        """
        return Iterator(array, is_cycle)
    
    def counter_call(limit):
        """
        Clase especilizada para 
        contar de forma agil un numero 
        de llamadas. Se utiliza llamando 
        al metodo is_end en un condicional, 
        con cada llamada sumara un numero 
        hasta llegar al limite indicado,
        una vez alcanzado el limite se 
        formateara.
        """
        return CounterCall(limit)
    
    def LimitNumber(number, range_arr):
        return LimitNumber(number, 
            range_arr)

    def Switch(state = False):
        """
        Clase interruptor para realizar 
        cambios automaticos a variables 
        boolean con cada llamada. Para 
        usarla solo debe crearse un 
        objeto con un nombre estilo
        boolean y comprobarlo con 
        is_true().
        **NOTE**
        La variable rcy es una variable 
        reciclada, para evitar creaciones 
        constantes en los bucles.
        """
        return Switch(state)
    
    def url_split(url:str)->dict[str]:
        """
        Función que divide una URL 
        retornando un diccionario con las 
        secciones de la URL en claves 
        protocol, domain, route y query
        """
        return url_split(url)
    
    def RelatedDict()->RelatedDict:
        """
            Esta clase es un diccionario 
        especial que permite busquedas 
        de claves relacionadas. Su 
        estructura es un diccionario 
        de nodos que contienen claves.
            Para usarlo debes asignar con 
        set una clave multiple separada 
        con dos puntos :, y un dato.
        pueden modificarse los datos con 
        set(key, dato) y obtener el dato 
        con get(key)
        """
        return RelatedDict(
            similar_percent = 70)
    
    def DesitionThree():
        return DecisionThree()
    
    def rgb_to_hex(rgb_list:list)->str:
        """
        Convierte un color RGB en su 
        representación hexadecimal.
        """
        return rgb_to_hex(rgb_list)
    
    def UniqueInt():
        return UniqueInt()
    
    def call_after(SECONDS:int|float, FUNCTION):
        """
        Ejecuta una función en un hilo 
        separado después de un tiempo 
        determinado.
        """
        return call_after(SECONDS, FUNCTION)
    
    def Duplicate(VALUE):
        return Duplicate(VALUE)
    
    def print_in(TEXT:str)->None:
        print_in(TEXT)

    def GObject(ROUTE)->GObject:
        return GObject(ROUTE)
    
    def to_json_string(objeto):
        """
        Convierte un objeto Python en una 
        cadena JSON
        """
        return to_json_string(objeto)
    
    def since_json_string(json_string):
        """
        Convierte una cadena JSON en 
        un objeto Python
        """
        return since_json_string(json_string)
    
    def DateEspecial():
        return DateEspecial()
