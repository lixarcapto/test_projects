

from btpy.Btpy import Btpy
from moods_dict import moods_dict

class Creature:

    mood_reduction = 1
    max_mood = 30
    

    def __init__(self):
        self.name = "cloud_demon"
        self.group = ""
        self.position = ""
        self.image_name = ""
        self.max_life_time = 0
        self.life_time = 0
        self.mood = 0
        self.food = 0
        self.energy = 0
        self.mood_key = ""
        self.mood_image_dict = {}
        self.pose_time = 0
        self.position_image_dict = {}
        self.callback_behavior = None

    def give_gift(self, quantity):
        self.position = "receiving"
        self.pose_time = 2
        self.mood = Btpy.sum_in_range(
            self.mood, 
            quantity,
            [0, Creature.max_mood]
        )

    def advance_time(self):
        self.reduce_mood()
        self.find_mood_key()
        self.identify_image()

    def find_mood_key(self)->str:
        mood_dict = moods_dict[self.group]
        mood_key = Btpy.whats_range(
            mood_dict,
            self.mood
        )
        self.mood_key = mood_key[0]

    def identify_image(self):
        if(self.position == ""):
            image_name = self.mood_image_dict[
                self.mood_key]
            self.image_name = image_name
        else:
            self.image_name = self\
                .position_image_dict[
                    self.position]
            if(self.pose_time > 0):
                self.pose_time -= 1
            else:
                self.position = ""

    def reduce_mood(self):
        self.mood = Btpy.sum_in_range(
            self.mood, 
            Creature.mood_reduction * -1,
            [0, Creature.max_mood]
        )

    def load_creature_dict(self, DICT):
        self.name = DICT["name"]
        self.group = DICT["group"]
        self.position = DICT["position"]
        self.image_name = DICT["image_name"]
        self.max_life_time = int(DICT["max_life_time"])
        self.life_time = int(DICT["life_time"])
        self.mood = int(DICT["mood"])
        self.food = int(DICT["food"])
        self.energy = int(DICT["energy"])
        self.mood_image_dict = DICT["mood_image_dict"]
        self.position_image_dict = DICT["position_image_dict"]
        