


import urllib.parse
from urllib.parse import urlparse, parse_qs

def query_to_dict(QUERY:str)->dict:
    """
    Funcion que convierte una query URL 
    en formato string en un diccionario
    """
    message = urllib.parse.unquote(QUERY)
    message = parse_qs(message)
    dictionary = {}
    for k in message:
        dictionary[k] = message[k][0]
    return dictionary