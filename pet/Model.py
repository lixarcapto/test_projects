

from btpy.Btpy import Btpy

class Model:

    MAX_NEEDS = 10

    def __init__(self):
        self.name = ""
        self.memory_text = ""
        self.days = 0
        self.thought_list:list = []
        self.max_days_life = 0
        self.food = 0
        self.water = 0
        self.energy = 0

    def write(self):
        txt = ""
        txt += self.write_thought_list()
        return txt
    
    def write_thought_list(self):
        txt = Btpy.write_as_list(
            self.thought_list,
            ""
        )
        return txt

    def advance_one_day(self):
        self.days += 1
        Btpy.sum_in_range(
            self.food, -1, 
            [0, Model.MAX_NEEDS]
        )
        Btpy.sum_in_range(
            self.water, -1, 
            [0, Model.MAX_NEEDS]
        )
        Btpy.sum_in_range(
            self.energy, -1, 
            [0, Model.MAX_NEEDS]
        )