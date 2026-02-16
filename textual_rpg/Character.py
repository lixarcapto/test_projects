

class Character:

    last_id_number = 0

    def __init__(self):
        self.id:int = 0
        self.name = "noname"
        self.life_points = 10
        self.life_turns = 0
        self.is_player = False
        # -------------------------------
        self.create_id()

    def advance_one_turn(self):
        self.life_turns += 1

    def write(self):
        txt = ""
        txt += self.name + " "
        txt += "(" + str(self.id) + ") "
        return txt 

    def create_id(self):
        id_ = Character.last_id_number
        self.id = id_
        Character.last_id_number += 1