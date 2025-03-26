

from .in_deps import*
from ..btpy_transformers.BtpyTransformers import BtpyTransformers
import time
from typing import Callable

class BtpyUtilitys(BtpyTransformers):

    EmotionSim = EmotionSim
    
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
        INTERVAL_TIME:int|float, 
        FUNCTION)->None:
        """
        Repite la función especificada cada 
        cierto intervalo que retorna una flag
        para controlar la repeticion. Si 
        la funcion retorna True se terminaran
        las repeticiones.
        Tambien recibe un numero int que 
        indica el numero de repeticiones.
        Esta funcion repite la callback en 
        un hilo propio asincrono al hilo
        principal.
        """
        return repeat_each_async(
            INTERVAL_TIME, 
            FUNCTION
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
    
    def url_split(url:str)->dict[str]:
        """
        Función que divide una URL 
        retornando un diccionario con las 
        secciones de la URL en claves 
        protocol, domain, route y query
        """
        return url_split(url)
    
    def DesitionThree():
        return DecisionThree()
    
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
    
    def Three():
        return Three()
    
    def Char():
        """
        Esta clase es un tipo de dato 
        character para Python. Sirve 
        para reducir el consumo de datos 
        de los string de un solo char.
        Consiste en un string global que 
        sirve para almacenar chars en 
        cada indice del string.
        """
        return Char()
    
    def create_console_loop(EXIT_KEY: str,
            PIPE_FUNCTION: Callable):
        """
        Esta es una funcion que facilita
        crear un bucle de consola con
        una sola funcion principal que recibe
        las entradas del usuario en texto
        y retorna las salidas de la aplicacion
        en texto. Ejecuta una primera ves
        la funcion como un valor void string para 
        obtener la primera salida de texto.
        El parametro EXIT_KEY indica una clave
        en caso de errores logicos para terminar
        el bucle de la consola.
        """
        return create_console_loop(
            EXIT_KEY,
            PIPE_FUNCTION
        )
    

