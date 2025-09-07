

from .gen_group_map_const import*

class GenGroup:

    """
        Clase que representa a los grupos geneticos
        y sus caracteristicas unicas.
    """

    GEN_GROUP_KEYS = None

    def __init__(self, key = ""):
        self.key = key
        self.eye_type_array = []
        self.skin_color_array = []
        self.height_code_array = []
        self.hair_type_array = []
        self.hair_color_array = []
        self.eye_color_array = []
        self.is_bald_array = []
        self.has_frekkles_array = []
        self.init(key)

    def init(self, key):
        self.build(key)
        GenGroup.GEN_GROUP_KEYS = GenGroup.create_gen_group_keys()

    def create_gen_group_keys():
        # crea un gen_group si este esta vacio
        if len(GEN_GROUP_MAP) == 0: return None
        array = []
        for k in GEN_GROUP_MAP:
            array.append(k)
        return array

    def load_gen_group_map(self, gen_group_map):
        self.add_eye_type(gen_group_map["eye_type_array"])
        self.add_skin_color(gen_group_map["skin_color_array"])
        self.add_height_code(gen_group_map["height_code_array"])
        self.add_hair_type(gen_group_map["hair_type_array"])
        self.add_hair_color(gen_group_map["hair_color_array"])
        self.add_eye_type(gen_group_map["eye_type_array"])
        self.add_eye_color(gen_group_map["eye_color_array"])
        self.add_is_bald(gen_group_map["is_bald_array"])
        self.add_has_frekkles(gen_group_map["has_frekkles_array"])

    """
        Funcion que crea una genetica predefinida segun la key
        enviada.
    """
    def build(self, key):
        self.load_gen_group_map(GEN_GROUP_MAP[key])

    # para basic_things
    def fuse(self, array_a, array_b):
        for i in range(len(array_a)):
            array_b.append(array_a[i])
        return array_b

    # ACCESORS --------------------------------------------------

    # return string_array
    def get_gen_group_keys():
        return GenGroup.GEN_GROUP_KEYS

    def add_eye_type(self, key_array):
        self.eye_type_array = self.fuse(self.eye_type_array,
            key_array)

    def add_skin_color(self, key_array):
        self.skin_color_array = self.fuse(self.skin_color_array,
            key_array)

    def add_height_code(self, key_array):
        self.height_code_array = self.fuse(self.height_code_array,
            key_array)

    def add_hair_type(self, key_array):
        self.hair_type_array = self.fuse(self.hair_type_array,
            key_array)

    def add_hair_color(self, key_array):
        self.hair_color_array = self.fuse(self.hair_color_array,
            key_array)

    def add_eye_color(self, key_array):
        self.eye_color_array = self.fuse(self.eye_color_array,
            key_array)

    def add_is_bald(self, key_array):
        self.is_bald_array = self.fuse(self.is_bald_array,
            key_array)

    def add_has_frekkles(self, key_array):
        self.has_frekkles_array = self.fuse(self.has_frekkles_array,
            key_array)
