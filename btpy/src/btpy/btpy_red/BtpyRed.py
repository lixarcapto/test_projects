

from ..btpy_random.BtpyRandom import BtpyRandom
from .mod.query_to_dict.query_to_dict import*

class BtpyRed(BtpyRandom):

    def __init__(self) -> None:
        pass

    def query_to_dict(QUERY:str)->dict:
        """
        Funcion que convierte una query URL 
        en formato string en un diccionario
        """
        return query_to_dict(QUERY)