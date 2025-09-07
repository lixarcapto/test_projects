


from ..remove_char.remove_char import*
from ..divide_string.divide_string import*
from .split_by_last_string import*


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
    return __cut("from", 
                primal_str, 
                searched_str, 
                last_appearance
    )

def cut_until(primal_str: str, 
             searched_str: str, 
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
    return __cut("until", 
                primal_str, 
                searched_str, 
                last_appearance
    )

def __cut(return_side,
        primal_str: str, 
            searched_str: str, 
          / ,last_appearance:bool = False)\
    -> str:
    index = {"from":1,"until":0}[return_side]
    # valida el string ingresado
    r_string = ""
    if searched_str not in primal_str: 
        return ""
    # en caso de buscar el ultimo
    if(last_appearance):
       r_string = split_by_last_string(
          primal_str, 
          searched_str
       )[index]
    # en caso de buscar el primero
    else:
        # divide el string
        r_string += primal_str\
            .split(searched_str, 1)[index]
    return r_string



