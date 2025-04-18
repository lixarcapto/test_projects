



def get_between(base:str, start:str,
        end:str) -> str:
    """
    Funcion que tome todo el string que 
    siguen despues de un string hasta llegar 
    al caracter indicado. Si no encuentra
    el string retorna un valor string void.
    """
    #
    init_index = base.find(start)
    if init_index == -1:
      return ""
    end_index = base.find(end,
        init_index +
        len(start))
    if end_index == -1:
      return ""
    new_string = base[init_index + len(start):end_index]
    return new_string

def has_between(base:str, start:str,
        end:str) -> bool:
    init_index = base.find(start)
    if init_index == -1:
      return False
    end_index = base.find(end,
        init_index +
        len(start))
    if end_index == -1:
      return False
    return True