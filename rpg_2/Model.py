

from Room import Room
from Character import Character

class Model:

    def __init__(self):
        self.room_matrix:Room = []
        self.__init_matrix()

    def create_character(self):
        return Character()

    def add_character(self, 
            character, point):
        self.room_matrix\
            [point[0]][point[1]]\
                .add_character(character)

    def update(self):
        leng = len(self.room_matrix)
        for y in range(leng):
            for x in range(len(self.room_matrix[y])):
                self.room_matrix[y][x]\
                    .update()

    def __init_matrix(self):
        room = None
        size = 10
        list_ = []
        for y in range(size):
            list_ = []
            for x in range(size):
                room = Room()
                list_.append(room)
            self.room_matrix.append(list_)
                
