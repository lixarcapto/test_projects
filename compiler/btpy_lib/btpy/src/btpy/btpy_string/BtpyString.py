

from .in_deps import*
from ..btpy_red.BtpyRed import BtpyRed

class BtpyString(BtpyRed):

    def charat(string:str, index:int) -> str:
        """
        # return char
        Funcion que extrae una letra 
        del string en un index 
        especifico usando slicing.
        """
        return charat(string, index)
    
    def compare_strings(
        strig_primal:str, 
        string_to_compare:str)\
        ->float|int:
        """
        Funcion que calcula las similitudes
        dos strings a partir de sus caracteres 
        similares y su posicion en la cadena; 
        despues hace una media entre ambos
        porcentajes.
        """
        return compare_strings(
            strig_primal,
            string_to_compare
        )
    
    def cut_from(primal_str: str, 
             searched_str: str, 
          / ,last_appearance:bool = False)\
            -> str:
        """
        Funcion que corta el string enviado 
        desde el string indicado 
        returnando la primera parte del 
        string. Si no encuentra el carácter 
        indicado retorna un String void.
        last_appearance: buscara la ultima 
        aparicion
        """
        return cut_from(primal_str,
                        searched_str,
                        last_appearance)
    
    def cut_until(primal_str: str, 
             searched_str: str, 
          / ,last_appearance:bool = False)\
            -> str:
        """
        Funcion que corta el string enviado 
        hasta donde aparece el string 
        indicado returnando la primera 
        parte del string. Si no encuentra 
        el carácter indicado retorna un 
        String void. last_appearance: 
        buscara la ultima aparicion 
        """
        return cut_until(
                primal_str, 
                searched_str, 
                last_appearance
        )
    
    def divide_string(index:int, string:str)\
        -> list[str]:
        """
        Funcion que divide un string en el
        indice indicado.
        """
        return divide_string(index, string)
    
    def remove_char(string:str, index:int)\
        ->str:
        """
        Función que elimina un carácter 
        de un String por su índice
        """
        return remove_char(string, index)
    
    def normalize(text: str) -> str:
        """
        Funcion que elimina las mayúsculas, 
        espacios extra y tildes de un texto.
        """
        return normalize(text)
    
    def get_words(text:str)->list[str]:
        """
        Función que divide un texto en 
        palabras separando por puntuación 
        y espacios
        """
        return get_words(text)
    
    def get_between(base:str, start:str,
        end:str) -> str:
        """
        Funcion que tome todo el string que 
        siguen despues de un string hasta llegar 
        al caracter indicado.
        """
        return get_between(base, 
            start, end)
    
    def insert_string(index:int, 
        base_string:str, 
        new_string:str) -> str:
        """
        Funcion que sirve para añadir 
        un string  antes de la pocision 
        indicada en el string enviado.
        """
        return insert_string(
            index, 
            base_string,
            new_string
        )
    
    def get_description(string:str,
        separator_string:str, 
        range_string_array:str)->list[str]:
        """
        Funcion que extrae de un string 
        una lista de elementos separadas 
        por el separator string; iniciando 
        desde el init_string hasta el 
        end_string.
        """
        return get_description(
            string, 
            separator_string, 
            range_string_array)
    
    def remove_strings(STRING_PRIMAL:str,
            TO_REMOVE_LIST:list[str])->str:
        return remove_strings(STRING_PRIMAL,
            TO_REMOVE_LIST)
    
    def sort_text( TEXT, LIMIT_CHAR_IN_LINE):
        """
        Funcion que ordena el texto para 
        cortar correctamente las palabras 
        finales
        """
        return sort_text(TEXT, 
            LIMIT_CHAR_IN_LINE)
    
    def replace_with_dict(TEXT:str, 
            TRANSLATE_DICT:dict[str])->str:
        return replace_with_dict(TEXT, 
            TRANSLATE_DICT)
    
    def get_symbols(TEXT):
        return get_symbols(TEXT)
    
    def remove_between(cadena, inicio, fin):
        return remove_between(
            cadena, inicio, fin)