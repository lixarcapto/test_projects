

from btpy.Btpy import Btpy

class Character:

    blueprint_dict = {

    }
    path_dictionary:dict = {
        "neftare":
            "./res/image/neftare.png",
        "gomer":
            "./res/image/gomer.png",
        "gaze":
            "./res/image/gaze.png",
        "soul":
            "./res/image/soul.png"
    }
    image_key_list = [
        "gomer",
        "neftare",
        "gaze",
        "soul"
    ]

    def __init__(self):
        self.id_number = 0
        self.name = ""
        self.nickname = ""
        self.age = 0
        self.demon_type = ""
        self.group = ""
        self.image_key = "neftare"
        self.pose_key = ""
        self.life = 5
        self.max_life = 5
        self.is_dead = False
        self.life_remaining = 0
        self.experience = 0
        self.armor = 0
        self.attack = 1
        self.randomize()

    def randomize(self):
        self.name = Btpy.random_name(
            "afrikan"
        )
        self.demon_type = Btpy\
            .random_choice(
                self.image_key_list
            )
        print(self.demon_type)
        self.image_key = self.demon_type
        blueprint = self.blueprint_dict\
            [self.demon_type]
        self.attack = blueprint["attack"]
        self.life = blueprint["life"]
        self.max_life = blueprint["life"]
        self.life_remaining = blueprint\
            ["life_time"]

    def advance_time(self):
        self.life_remaining = Btpy\
            .sum_in_range(
                self.life_remaining,
                -1,
                [0, 100]
            )
        if(self.life_remaining == 0):
            self.life = 0
        if(self.life == 0):
            self.is_dead = True

    def get_image_path(self, KEY):
        return self.path_dictionary[KEY]

    def get_render(self)->dict:
        return {
            "title_text":self.name,
            "range_bar":[
                self.life,
                self.max_life
            ],
            "attack":self.attack,
            "character_text":self.write(),
            "path_image":self
                .get_image_path(
                    self.image_key)
        }

    def write(self):
        return ""\
        + f"{self.name=} \n"\
        + f"{self.nickname=} \n"\
        + f"{self.age=} \n"\
        + f"{self.group=} \n"\
        + f"{self.image_key=} \n"\
        + f"{self.pose_key=} \n"\
        + f"{self.life=} \n"\
        + f"{self.attack=} \n"\
        + f"{self.armor=} \n"\
        + f"{self.experience=} \n"\
        + f"{self.life_remaining=} \n"

    def receive_attack(self, 
            character):
        attack = character.attack
        self.life = Btpy.sum_in_range(
            self.life,
            attack * -1, 
            [0, self.max_life]
        )