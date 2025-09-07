

from .GenGroup import GenGroup

class GenGroupCollection:

    """
        Clase que sirve para crear grupos de genes predefinidos
        en una coleccion ordenada y accesible.
    """
    def __init__(self):
        self.gen_group_map = {}
        gen_group_keys = GenGroup().GEN_GROUP_KEYS
        for k in gen_group_keys:
            self.gen_group_map[k] = GenGroup(k)

    def get(self, key):
        return self.gen_group_map[key]

    def get_keys(self):
        return GenGroup.GEN_GROUP_KEYS
