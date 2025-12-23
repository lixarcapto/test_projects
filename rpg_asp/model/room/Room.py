

from ..character.Character import Character

class Room:

    def __init__(self):
        self.id = 0
        self.character_list:list = []

    def populate(self):
        char = None
        for i in range(5):
            char = Character()
            self.character_list.append(char)

    def advance_time(self):
        leng = len(self.character_list)
        for i in range(leng):
            self.character_list[i]\
                .advance_time()

    def has_character(self, ID):
        leng = len(self.character_list)
        char = None
        for i in range(leng):
            char = self.character_list[i]
            if(char.id == ID):
                return True
        return False

    def get_character(self, ID):
        leng = len(self.character_list)
        char = None
        for i in range(leng):
            char = self.character_list[i]
            if(char.id == ID):
                return char
            
    def set_character(self, character):
        leng = len(self.character_list)
        char = None
        for i in range(leng):
            char = self.character_list[i]
            if(char.id == character.id):
                self.character_list[i]\
                    = character
                break