


import random

CACHE_LASTNAMES_DICT:dict = {}

def random_lastname(
          read_excel_dict,
          LASTNAMES_PATH : str,
          CULTURE : str = "")-> str:
        """
        Función que genera un apellido
        aleatorio segun la cultura
        determinada.
        Las culturas son:
        * "russian" 
        * "american" 
        * "english"
        * "arab"
        * "french"
        * "afrikan"
        * "nordic"
        * "indian"
        * "spanish"
        * "turkish"
        * "chinese"
        * "japanese"
        * "polinesian"
        * "italic"
        """
        # carga un cache con los nombres
        name:str = ""
        names_list:list = []
        names_dict:dict = None
        # carga un cache con los apellidos
        # para evitar una relectura
        # constante de los archivos excel.
        global CACHE_LASTNAMES_DICT
        if(CACHE_LASTNAMES_DICT == {}):
            CACHE_LASTNAMES_DICT \
                = read_excel_dict(
                    LASTNAMES_PATH)
        names_dict = CACHE_LASTNAMES_DICT
        # adapta la clave cultura faltante
        if(CULTURE == ""):
            key:str = random.choice(
                list(names_dict.keys()))
            names_list = names_dict[key]
        else:
            names_list = names_dict[CULTURE]
        # genera nombre aleatorio
        name =  random.choice(names_list)
        return name