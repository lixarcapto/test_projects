


from btpy.src.btpy.Btpy import Btpy
from .read_excel_dict_list import*


class Persistence:

    """
    Modulo para obtener datos de alguna
    base de datos.
    """

    SALUTE_DICT = {}
    PATH_RES = "../res/"
    FOLDER_GROUP = "genetic_group"

    def get_salute(CULTURE):
        if(Persistence.SALUTE_DICT == {}):
            Persistence.SALUTE_DICT = Btpy\
            .read_excel_dict(
                "../res/salute_table.xlsx")
        array = Persistence.SALUTE_DICT[CULTURE]
        return Btpy.random_choice(array)
    
    def read_genetic_grups(
            genetic_group_list:list[str])\
                ->dict[dict]:
        path \
            = Persistence.PATH_RES\
            + Persistence.FOLDER_GROUP
        return read_excel_dict_list(path,
            genetic_group_list)
    
