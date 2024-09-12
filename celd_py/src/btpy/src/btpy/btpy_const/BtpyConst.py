


from .deps_in import*
from ..btpy_checkers.BtpyCheckers import BtpyCheckers

class BtpyConst(BtpyCheckers):

    ALPHABET = ALPHABET_TUPLE

    NUMBER = NUMBER_TUPLE

    HEX = HEX_TUPLE

    def get_animal_array():
        """
        Array con una lista de animales 
        ordenados alfabeticamente en 
        ingles para pruebas de funciones.
        """
        return ANIMAL_ARRAY