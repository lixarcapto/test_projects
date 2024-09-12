

from ....btpy_random.mod.random_choice.random_choice import*
from ..read_excel_dict.read_excel_dict import*

CACHE_NAMES_DICT = {}
ROUTE_LASTNAME_XLSX = "../res/lastname_data.xlsx"


def random_lastname(culture = ""):
        """
        Función que genera un nombre 
        aleatorio según la cultura y el 
        género especificado.
        culture_keys = ["russian", "american", 
        "english", 
        "arab", "french", "afrikan", 
        "nordic", "indian", "spanish", 
        "turkish", "chinese", "japanese", 
        "polinesian", "italic"]
        """
        # carga un cache con los nombres
        name = ""
        names_list = []
        names_dict = None
        if(CACHE_NAMES_DICT == {}):
            names_dict = read_excel_dict(
                ROUTE_LASTNAME_XLSX)
        # adapta la clave cultura faltante
        if(culture == ""):
            names_list = random_choice(
                names_dict)
        else:
            names_list = names_dict[culture]
        # genera nombre aleatorio
        name =  random_choice(names_list)
        return name