

from ....btpy_string.mod.cut_from.cut_from import*


def url_split(url:str)->dict[str]:
    """
    Función que divide una URL 
    retornando un diccionario con las 
    secciones de la URL en claves 
    protocol, domain, route y query
    """
    #
    dict = {
        "protocol":"",
        "domain":"",
        "route":"",
        "query":""
    }
    # extraer protocolo
    dict["protocol"] = cut_until(url, "://")
    # extraer dominio
    temp = cut_from(url, "://")
    temp = cut_until(temp, "/")
    dict["domain"] = temp
    # extraer la ruta
    temp = cut_from(url, "://")
    temp = cut_from(temp, "/")
    # si tiene query
    if("?" in temp):
        dict["route"] = cut_until(temp, "?")
        dict["query"] = cut_from(url, "?")
    else: 
        dict["route"] = temp
    return dict