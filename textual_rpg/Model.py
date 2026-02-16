

from Territory import Territory
from Character import Character

class Model:

    chapter_turns = 50

    def __init__(self):
        self.territory_list = []
        self.book = ""
        self.chapter = 0
        self.turns = 0
        self.turns_for_chapter = 0
        self.player_id = 0
        self.create_map()
        self.new_chapter()

    def create_map(self):
        territory:Territory = None
        for i in range(10):
            territory = Territory()
            self.territory_list\
                .append(territory)
        char = Character()
        char.is_player = True
        self.player_id = char.id
        self.territory_list[0]\
            .add_character(char)
        char = Character()
        self.territory_list[0]\
            .add_character(char)
            
    def write(self):
        return self.book

    def new_chapter(self):
        char = self.territory_list[0]\
            .get_character_by_id(
                self.player_id
            )
        self.book += char.write()

    def update_chapter_counter(self):
        self.turns_for_chapter += 1
        if(self.turns_for_chapter\
                >= Model.chapter_turns):
            self.turns_for_chapter = 0
            self.chapter += 1
            self.new_chapter()

    def advance_one_turn(self):
        self.turns += 1
        self.update_chapter_counter()
        for territory in self.territory_list:
            territory.advance_one_turn()

    def get_character_by_id(self, ID):
        territory:Territory = None
        has_character = False
        for territory in self.territory_list:
            has_character = territory\
                .has_character_by_id(ID)
            if(has_character):
                return territory\
                    .get_character_by_id(ID)
        return None
    
    def replace_character(self, 
            character):
        territory:Territory = None
        has_character = False
        for territory in self.territory_list:
            has_character = territory\
                .has_character_by_id(
                    character.id
                )
            if(has_character):
                return territory\
                    .replace_character(
                       character
                    )
        return None