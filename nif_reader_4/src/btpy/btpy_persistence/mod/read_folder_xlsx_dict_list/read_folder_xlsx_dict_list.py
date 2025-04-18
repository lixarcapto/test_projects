

from ..read_xlsx_dict_list.read_xlsx_dict_list import*

def read_folder_xlsx_dict_list(path:str,
            name_list:list[str])\
                ->dict[dict]:
        """
        Funcion que lee todos los archivos
        XLSX con los nombres enviados y 
        retorna un dict anidado con los 
        datos.
        """
        gg_dict_nested:dict[dict] = {}
        gg_dict:dict[str] = {}
        final_path:str = ""
        format_file = ".xlsx"
        # carga los XLSX de cada grupo
        for gg_key in name_list:
            final_path = path + "/" \
            + gg_key + format_file
            gg_dict = read_xlsx_dict_list(
                final_path)
            gg_dict_nested[gg_key] \
                = gg_dict
        return gg_dict_nested