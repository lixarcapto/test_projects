

from typing import Callable
import os


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
    output:str = ""
    user_input:str = ""
    __clean_console()
    output = PIPE_FUNCTION("")
    while(True):
        print(output)
        user_input = input()
        if(EXIT_KEY == user_input):
            break
        output = PIPE_FUNCTION(
            user_input)
        __clean_console()

def __clean_console():
    """Limpia la consola según el sistema operativo."""
    os_name = os.name
    if os_name == 'posix':  # macOS y Linux
        os.system('clear')
    elif os_name == 'nt':  # Windows
        os.system('cls')
    else:
        print('\n' * 100)