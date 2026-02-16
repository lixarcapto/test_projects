

from ..get_files_into.get_files_into import*

def read_animation_folder(PATH)\
        ->list[str]:
    """
    Funcion que lee obtiene las 
    rutas ordenadas en una lista de 
    cada frame de un animation folder
    formato; este formato consiste en
    carpetas de imagenes para crear
    una animacion que solo tienen de nombre
    el orden de dibujado como un entero 
    del 0 al 100
    """
    names_list = get_files_into(PATH)
    index_list:list[int] = []
    only_name = ""
    name:str = ""
    index:int = 0
    extension = names_list[0]\
        .split(".")[1]
    for name in names_list:
        only_name = name.replace(
            f".{extension}", "")
        index = int(only_name)
        index_list.append(index)
    index_list.sort()
    path_list = []
    path = ""
    for index in index_list:
        path = f"{PATH}{index}.{extension}"
        path_list.append(path)
    return path_list
    
