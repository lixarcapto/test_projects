

from .clime_map_const import*
from .Clime import Clime

class ClimeCollection:

    """
        Clase que crea una coleccion de climas predefinidas
        para obtener de forma rapida.
    """

    CLIME_KEYS_ARRAY = None

    def __init__(self):
        self.clime_map = {}
        clime = None
        for k in CLIME_MAP_CONST:
            clime = Clime()
            clime.load_clime_map(CLIME_MAP_CONST[k])
            self.clime_map[k] = clime
        if(ClimeCollection.CLIME_KEYS_ARRAY == None):
            self.create_clime_keys()

    def create_clime_keys(self):
        array = []
        for k in CLIME_MAP_CONST:
            array.append(k)
        ClimeCollection.CLIME_KEYS_ARRAY = array

    def get(self, key):
        return self.clime_map[key]

    def get_keys(self):
        return ClimeCollection.CLIME_KEYS_ARRAY
