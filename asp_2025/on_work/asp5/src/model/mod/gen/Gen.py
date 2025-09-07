

from basic_things.basic_things import Basic
from .GenConstants import GenConstants
from .mod.gen_group_collection.GenGroupCollection \
    import GenGroupCollection
import random

class Gen:

    GEN_GROUP_COLLECTION = None
    GEN_CONSTANTS = GenConstants

    def __init__(self):
        # appearance
        self.gen_group = ""
        self.eye_type = ""
        self.skin_color = ""
        self.maximum_height_code = 0
        self.hair_type = ""
        self.hair_color = ""
        self.eye_color = ""
        self.is_bald = False
        self.has_frekkles = False
        if(Gen.GEN_GROUP_COLLECTION == None):
            Gen.GEN_GROUP_COLLECTION = GenGroupCollection()

    def randomize(self, key):
        gp = Gen.GEN_GROUP_COLLECTION.get(key)
        self.gen_group = key
        self.eye_type = random.choice(gp.eye_type_array)
        self.skin_color = random.choice(gp.skin_color_array)
        self.maximum_height_code = random.choice(gp.height_code_array)
        self.hair_type = random.choice(gp.hair_type_array)
        self.hair_color = random.choice(gp.hair_color_array)
        self.eye_color = random.choice(gp.eye_color_array)
        self.is_bald = random.choice(gp.is_bald_array)
        self.has_frekkles = random.choice(gp.has_frekkles_array)

    """
        Funcion que genera una nueva genetica a
        partir de dos geneticas diferentes.
    """
    def creates_new_gen(self, gen):
        new_gen = Gen()
        self.data.gen_father = gen_father
        self.data.gen_mother = gen_mother
        new_gen.eye_type = random \
            .choice([self.eye_type, gen.eye_type])
        new_gen.skin_color = random \
            .choice([self.skin_color, gen.skin_color])
        new_gen.maximum_height_code = random.choice([self.maximum_height_code,
            gen.maximum_height_code])
        new_gen.hair_type = random.choice([self.hair_type, gen.hair_type])
        new_gen.hair_color = random.choice([self.hair_color, gen.hair_color])
        new_gen.eye_color = random.choice([self.eye_color, gen.eye_color])
        new_gen.is_bald = random.choice([self.is_bald, gen.is_bald])
        new_gen.has_frekkles = random.choice([self.has_frekkles, gen.has_frekkles])
        return new_gen
