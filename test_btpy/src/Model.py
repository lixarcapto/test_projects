

from btpy.Btpy import Btpy
import copy
from Creature import Creature

class Model:

    CREATURE_LIST = []
    PATH_TRANSLATOR = {
        "talitha_adult_normal": "./res/image/demon/talitha/talitha_adult_normal_250x250.png",
        "talitha_adult_angry": "./res/image/demon/talitha/talitha_adult_angry_250x250.png",
        "talitha_adult_happy": "./res/image/demon/talitha/talitha_adult_happy_250x250.png",
        "talitha_adult_receiving": "./res/image/demon/talitha/talitha_adult_receiving_250x250.png",
    }

    def __init__(self):
        self.creature:Creature = None
        self.flag_duplicate = None
        self.loop_time_seconds = 2
        self.load_creature_list()
        self.init_model_loop()

    def give_gift(self):
        self.creature.give_gift(5)
    
    def init_model_loop(self):
        def fn(n):
            self.advance_time()
        self.flag_duplicate = Btpy\
            .repeat_each_async(
                self.loop_time_seconds, 
                fn
            )

    def advance_time(self):
        if(self.creature != None):
            self.creature.advance_time()

    def get_render(self):
        return {
            "title": self.creature.name,
            "path": Model.PATH_TRANSLATOR[
                self.creature.image_name],
            "description": ""
        }

    def random_creature(self):
        creature = Btpy.random_choice(
            Model.CREATURE_LIST)
        self.creature = copy\
            .deepcopy(creature)

    def load_creature_list(self):
        creature_dict = Btpy\
            .read_json_object(
                "./res/json/creatures_list.json"
            )
        creature = None
        for dict_ in creature_dict:
            creature = Creature()
            creature.load_creature_dict(
                dict_)
            Model.CREATURE_LIST.append(
                creature)
            
    
