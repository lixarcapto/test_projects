

from btpy.Btpy import Btpy

class Character:

    last_id = 0

    def __init__(self):
        self.id = 0
        self.name = ""
        self.years_old = 0
        self.gender_k = "female"
        self.history:str = ""
        self.action_k = "interact"
        self.id = Character.last_id
        Character.last_id += 1

    def randomize(self):
        self.id = Btpy.random_name(
            "english",
            "male"
        )

    def advance_time(self):
        self.years_old += 1
