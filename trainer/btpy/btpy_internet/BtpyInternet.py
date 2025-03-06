

from ..btpy_images.BtpyImages import BtpyImages
from .mod.query_to_dict.query_to_dict import*
from .mod.request_open_ai.request_open_ai import*
from .mod.create_server_flask import create_server_flask

class BtpyInternet(BtpyImages):

    def __init__(self) -> None:
        pass

    def create_server_flask(debug, port,
            function):
        return create_server_flask(
            debug, port, function)

    def query_to_dict(QUERY:str)->dict:
        """
        Funcion que convierte una query URL 
        en formato string en un diccionario
        """
        return query_to_dict(QUERY)
    
    def request_open_ai(PROMPT, API_KEY, 
        MAX_TOKENS = 100, 
        MODEL = "gpt-4o-mini"):
        """
        modelo recomendado: gpt-4o-mini
        """
        return request_open_ai(
            PROMPT, 
            API_KEY, 
            MAX_TOKENS, 
            MODEL
        )