

from .Room import Room
from .Pj import Pj

class Scenario:

    def __init__(self):
        self.room_list:Room = []
        self.idx_room = 0
        self.player_id = 0
        self.create_scenario()

    def write_player(self):
        pj = self.get_pj(self.player_id)
        return pj.write_narrative()
    
    def move_player(self, idx):
        self.move_pj(
            self.player_id,
            idx
        )

    def get_pj(self, id_pj):
        leng = len(self.room_list)
        room = None
        pj = None
        for i in range(leng):
            room = self.room_list[i]
            if(room.has_pj(id_pj)):
                return self.room_list[i]\
                    .get_pj(id_pj)
        return None

    def create_scenario(self):
        for i in range(10):
            self.room_list.append(Room())
        player = Pj()
        player.randomize()
        self.player_id = player.id
        self.room_list[0].add_pj(player)

    def update(self):
        leng = len(self.room_list)
        for i in range(leng):
            self.room_list[i].update()

    def attack_pj(self, id_attacker,
            id_objetive):
        i_room = self.get_region_pj(
            id_attacker
        )
        self.room_list[i_room].attack(
            id_attacker,
            id_objetive
        )

    def get_region_pj(self, ID):
        leng = len(self.room_list)
        room = None
        pj = None
        for i in range(leng):
            room = self.room_list[i]
            if(room.has_pj(ID)):
                return i
        return -1

    def move_pj(self, id_pj, idx_destiny):
        leng = len(self.room_list)
        room = None
        pj = None
        for i in range(leng):
            room = self.room_list[i]
            if(room.has_pj(id_pj)):
                pj = self.room_list[i]\
                    .extract_pj(id_pj)
                break
        self.room_list[idx_destiny]\
            .add_pj(pj)