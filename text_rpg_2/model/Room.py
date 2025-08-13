

from btpy.Btpy import Btpy
from .Pj import Pj

class Room:

    def __init__(self):
        self.place_type = "town"
        self.nickname = "beautiful"
        self.pj_list:list = []

    def attack(self, I_ATTACKER, 
            I_OBJETIVE):
        pj_attacker:Pj = self.get_pj(
            I_ATTACKER
        )
        pj_objective:Pj = self.get_pj(
            I_OBJETIVE
        )
        pj_objective.receive_attack(
            pj_attacker.damage
        )
        self.set_pj(pj_attacker)
        self.set_pj(pj_objective)

    def get_room_memory(self, IDX):
        txt = ""
        txt += self.place_type + " " \
            + self.nickname + " "
        for i in range(len(self.pj_list)):
            if(i == IDX): continue
            txt += self.pj_list[i]\
                .write_narrative()
        return txt
    
    def update(self):
        self.record_memorys()

    def record_memorys(self):
        pj = None
        txt = ""
        for i in range(len(self.pj_list)):
            pj = self.pj_list[i]
            txt = self.get_room_memory(i)
            pj.temp_memory = txt
            self.pj_list[i] = pj

    def write(self):
        txt = ""
        for pj in self.pj_list:
            txt += pj.write() + "\n"
        return txt

    def set_pj(self, pj_seek):
        pj = None
        for i in range(len(self.pj_list)):
            pj = self.pj_list[i]
            if(pj.id == pj_seek.ID):
                self.pj_list[i] = pj
                break

    def add_pj(self, pj):
        self.pj_list.append(pj)

    def get_pj(self, ID):
        for pj in self.pj_list:
            if(pj.id == ID):
                return pj
            
    def has_pj(self, ID):
        for pj in self.pj_list:
            if(pj.id == ID):
                return True 
        return False
    
    def extract_pj(self, ID):
        i = 0
        pj_select = None
        for pj in self.pj_list:
            if(pj.id == ID):
                pj_select = pj
                del(self.pj_list[i])
                break
            i += 1
        return pj_select