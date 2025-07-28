
from btpy.Btpy import Btpy
from ItemStore import ItemStore

# para btpy
def list_to_dict(LIST:list, VALUE:any):
    dict_ = {}
    for e in LIST:
        dict_[e] = VALUE
    return dict_

class Character:

    ItemStore = ItemStore()
    MAX_ATTRIBUTE = 15
    MIN_ATTRIBUTE = 1

    ATTRIBUTES_TUPLE:tuple = (
        "ATTACK",
        "DEFENSE",
        "SPEED",
        "DAMAGE_RESISTANCE"
    )

    def __init__(self):
        self.name = ""
        self.category = ""
        self.born_attr:dict = list_to_dict(
            self.ATTRIBUTES_TUPLE, 0
        )
        self.practicing_attr:dict = list_to_dict(
            self.ATTRIBUTES_TUPLE, 0
        )
        self.final_attr:dict = list_to_dict(
            self.ATTRIBUTES_TUPLE, 0
        )
        self.level = 0
        self.damage = 0
        self.shield = 0
        self.item_index = 0
        self.items_list = []
        self.is_dead = False
        self.randomize_attributes()

    def update(self):
        self.check_is_dead()
        self.calculate_attributes()

    def advance_turn(self):
        pass

    def randomize_attributes(self):
        print("randomize attributes")
        for k in self.born_attr:
            self.born_attr[k] = Btpy\
                .rand_range(
                    [Character.MIN_ATTRIBUTE,
                    Character.MAX_ATTRIBUTE]
                )

    def calculate_attributes(self):
        dict_ = {}
        dict_ = Btpy.sum_dict(
            self.born_attr,
            self.practicing_attr
        )
        self.final_attr = Btpy.sum_dict(
            dict_,
            self.get_item()\
                .attributes_dict
        )

    def get_item(self):
        key = "none"
        if(self.items_list == []):
            key == "none"
        else:
            key = self.items_list[
                self.item_index]
        return Character.ItemStore\
            .get_item(key)
    
    def check_is_dead(self):
        damage_r = self.final_attr\
            ["DAMAGE_RESISTANCE"]
        if(self.damage > damage_r):
            self.is_dead = True

    def load_character_dict(self, 
            KEY:str, DICT:dict):
        self.name = KEY
        self.category = DICT["CATEGORY"]
        self.born_attr["ATTACK"] = DICT["ATTACK"]
        self.level = DICT["LEVEL"]
        self.born_attr["DEFENSE"] \
            = DICT["DEFENSE"]
        self.born_attr["DAMAGE_RESISTANCE"]\
            = DICT["DAMAGE_RESISTANCE"]
        self.items_list.append(
            DICT["ITEM_1"]
        )
        self.items_list.append(
            DICT["ITEM_2"]
        )
        self.items_list.append(
            DICT["ITEM_3"]
        )
        self.items_list.append(
            DICT["ITEM_4"]
        )

    def get_item_selected(self)->str:
        if(self.items_list == []):
            return "none"
        return self.items_list\
            [self.item_index]

    def write(self):
        txt = ""
        txt += self.name + " "
        txt += self.category + " "
        txt += "level" + str(self.level) + " "
        txt += "DAMAGE: " + str(self.damage) + "\n "
        txt += "is dead " + str(self.is_dead)
        txt += "=> FINAL STATS: \n"
        txt += Btpy.write_dict_bars(
            self.final_attr, "/")
        txt += "=> ITEM: "
        txt += self.get_item_selected()
        return txt