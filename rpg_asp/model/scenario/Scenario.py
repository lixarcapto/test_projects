

from ..room.Room import Room

class Scenario:

    def __init__(self):
        self.room_list = []
        room = None
        for i in range(10):
            room = Room()
            room.id = i
            self.room_list.append(room)

    def populate_room(self, NUMBER):
        self.room_list[NUMBER].populate()

    def get_character(self, ID):
        room:Room = None
        for i in range(len(self.room_list)):
            room = self.room_list[i]
            if(room.has_character(ID)):
                return room.get_character(ID)
            
    def advance_time(self):
        for i in range(len(self.room_list)):
            self.room_list[i].advance_time()