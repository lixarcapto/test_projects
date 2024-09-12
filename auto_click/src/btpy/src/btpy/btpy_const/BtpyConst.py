


from .deps_in import*
from ..btpy_checkers.BtpyCheckers import BtpyCheckers
import random
from ..btpy_random.mod.random_choice.random_choice import random_choice

class BtpyConst(BtpyCheckers):

    ALPHABET = ALPHABET_TUPLE

    NUMBER = NUMBER_TUPLE

    HEX = HEX_TUPLE

    SENSE = Sense

    def get_animal_array():
        """
        Array con una lista de animales 
        ordenados alfabeticamente en 
        ingles para pruebas de funciones.
        """
        return ANIMAL_ARRAY
    
    def random_sense():
        return random_choice(
            BtpyConst.SENSE.CARDINAL_DICT)