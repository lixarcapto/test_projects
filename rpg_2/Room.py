

from Character import Character

class Room:

    def __init__(self):
        self.character_list = []

    def add_character(self, character):
        self.character_list.append(
            character)

    def update(self):
        self.catch_images()

    def catch_images(self):
        txt = ""
        leng = len(self.character_list)
        char = None
        for i in range(leng):
            txt = ""
            char = self.character_list[i]
            for i2 in range(leng):
                if(i == i2): continue
                txt += self.character_list[i]\
                    .appearance
            char.vision_text = txt