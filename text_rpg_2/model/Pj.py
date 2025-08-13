

from btpy.Btpy import Btpy

class Pj:

    last_id = 0

    def __init__(self):
        self.id = 0
        self.name = ""
        self.damage = 10
        self.life_points = 10
        self.category = ""
        self.age = 15
        self.gender = ""
        self.temp_memory = ""
        self.create_id()

    def receive_attack(self, damage):
        self.life_points = Btpy.sum_in_range(
            self.life_points,
            damage * -1,
            [0, 100]
        )
    
    def create_id(self):
        self.id = Pj.last_id
        Pj.last_id += 1

    def randomize(self):
        if(Btpy.random_bool()):
            self.gender = "female"
        else:
            self.gender = "male"
        self.name = Btpy.random_name(
            "english",
            self.gender
        )

    def write_player(self):
        return self.write_narrative()\
        + self.temp_memory

    def write_narrative(self):
        return "" + "is " + self.name\
        + " " + self.gender + " "\
        + f"(ID : {self.id})"