

from Character import Character

class Territory:

    def __init__(self):
        self.character_list = []

    def advance_one_turn(self):
        char:Character = None 
        for char in self.character_list:
            char.advance_one_turn()

    def add_character(self, 
            new_character:Character):
        self.character_list.append(
            new_character
        )

    def replace_character(self, 
            new_character:Character):
        char:Character = None
        leng = len(self.character_list)
        for i in range(leng):
            if(self.character_list[i].id\
               == new_character.id):
                self.character_list[i]\
                    = new_character
                break

    def has_character_by_id(self, ID):
        char:Character = None
        for char in self.character_list:
            if(char.id == ID):
                return True
        return False

    def get_character_by_id(self, ID):
        char:Character = None
        for char in self.character_list:
            if(char.id == ID):
                return char
        return None