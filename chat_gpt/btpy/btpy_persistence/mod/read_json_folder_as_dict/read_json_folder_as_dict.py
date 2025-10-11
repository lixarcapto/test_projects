

from ..get_files_into.get_files_into import*

def read_json_folder_as_dict(PATH:str)\
        ->dict[str, dict]:
    """
    Funcion que carga una lista de 
    archivos json en la misma carpeta 
    como un diccionario
    de objetos json donde las claves
    de cada par son los nombres de
    los archivos.
    """
    list_:list = get_files_into(
            PATH,
            ".json"
        )
    nested_dict:dict = {}
    dict_:dict = {}
    key:str = ""
    for file_name in list_:
        dict_ = Btpy.read_json_object(
            PATH + file_name
        )
        key = file_name.replace(".json", "")\
            .upper()
        nested_dict[key] = dict_
    return nested_dict