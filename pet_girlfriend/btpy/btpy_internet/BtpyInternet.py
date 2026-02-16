

from ..btpy_images.BtpyImages import BtpyImages
from .mod.query_to_dict.query_to_dict import*
from .mod.request_open_ai.request_open_ai import*
from .mod.create_server_flask import create_server_flask
from ..init_html_gui import init_html_gui

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
    
    def init_html_gui(MODEL_API, 
            PATH_HTML:str, 
            PORT:int = 5000):
        """
        XXX: No funciona, no carga los 
        archivos estaticos de las paginas
        webs; solo carga el index.html.
        
        Esta funcion inicia directamente
        una interface del navegador en local
        utilizando un servidor flask y 
        un archivo index.html. Para que 
        funcione debe instalarse la libreria
        Flask, debe crearse una carpeta 
        templates en la raiz de la aplicacion
        y en su interior debe tener un index.html
        valido. La ruta relativa del index
        debe enviarse como PATH_HTML.
        El parametro API_Model recibe una clase
        que debe contener como parametro 
        un metodo request que reciba json 
        y retorne json; el json recibido es
        el json de la request, y el json
        retornado es el json de la response.
        """
        init_html_gui(MODEL_API, 
            PATH_HTML, 
            PORT)
    
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
    
