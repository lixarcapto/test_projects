

import os

def input_choose(QUESTION:str, 
        LIST:list[str])->str:
    """
    Funcion que hace al usuario una 
    pregunta de seleccion multiple;
    el usuario debe responder con 
    un numero en un rango de 1 a 
    indeterminado segun el tamaño de 
    la lista enviada. La funcion
    retorna el elemento string de la 
    lista elegido. 
    La funcion corrige al 
    usuario si ingresa una opcion
    incorrecta y repite la pregunta.
    *  QUESTION: Es la pregunta a 
       realizar.
    *  LIST: Es la lista de opciones 
       a elegir.
    """
    # ------------------------------------
    # VALIDACION DE ENTRADAS 
    if(not isinstance(QUESTION, str)):
        raise Exception(
        """the QUESTION argument is 
        not a string"""
        )
    if(not isinstance(LIST, list)):
        raise Exception(
        "the LIST argument is not a list"
        )
    for e in LIST:
        if(not isinstance(e, str)):
            raise Exception(
            """the LIST argument is 
            not a list of strings"""
            )
    # ------------------------------------
    # VARIABLES
    is_right_answer:bool = False
    input_:str = ""
    index:int = 0
    MARGIN_SIZE:int = 2
    margin:str = " " * MARGIN_SIZE
    error_message:str = ""
    txt:str = ""
    # -----------------------------------
    # FUNCION PRINCIPAL
    while(not is_right_answer):
        os.system('cls')
        txt = error_message
        txt += QUESTION + ":\n"
        n = 1
        for e in LIST:
            txt += f"{margin}{n}) " 
            txt += e + "\n"
            n += 1
        input_ = input(txt)
        if(input_.isnumeric()):
            index = int(input_)
            if(len(LIST) >= index
            and index > 0):
                is_right_answer = True
            else:
                error_message = input_\
                    + " does not exist as an option\n"
        else:
            error_message = input_\
                + " it is not a number\n"
    return LIST[index -1]