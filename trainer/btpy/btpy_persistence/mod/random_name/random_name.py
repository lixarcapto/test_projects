



import random

CACHE_NAMES_FEMALE_DICT:dict = {}
CACHE_NAMES_MALE_DICT:dict = {}
cache_exist:bool = False

def random_name(
            read_excel_dict,
            PATH_NAME_MALE_XLSX,
            PATH_NAME_FEMALE_XLSX, 
            culture:str = "",
            gender:str = "")->str:
        """
        Función que genera un nombre 
        aleatorio según la cultura y el 
        género especificado. 
        Los generos son:
        * "female"
        * "male"
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
        # carga un cache para almacenar
        # los nombres leidos del archivo
        # excel evitando recargas 
        # constantes
        global CACHE_NAMES_MALE_DICT
        global CACHE_NAMES_FEMALE_DICT
        global cache_exist
        if(not cache_exist):
            cache_exist = True
            CACHE_NAMES_MALE_DICT \
                = read_excel_dict(
                    PATH_NAME_MALE_XLSX)
            CACHE_NAMES_FEMALE_DICT  \
                = read_excel_dict(
                    PATH_NAME_FEMALE_XLSX)
        names_dict:dict = {}
        # adapta el param gender
        if(gender == ""):
            gender = random.choice(
                ["male", "female"])
        if(gender == "male"):
            names_dict = CACHE_NAMES_MALE_DICT
        elif(gender == "female"):
            names_dict = CACHE_NAMES_FEMALE_DICT
        # adapta el param culture 
        # randomizandolo
        if(culture == ""):
            # obtiene la clave de la lista
            # de nombres
            k = random.choice(
                list(names_dict.keys()))
            # carga la lista de nombres
            names_list = names_dict[k]
        else:
            names_list = names_dict[culture]
        # genera nombre aleatorio
        name =  random.choice(names_list)
        return name