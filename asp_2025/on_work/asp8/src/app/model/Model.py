

from .mod.world.World import World
from ..persistence.Persistence import Persistence
from btpy.src.btpy.Btpy import Btpy
from .mod.user.User import User

class Model:

    

    def __init__(self) -> None:
        # config map
        self.size_map_x = 10
        self.size_map_y = 10
        self.user_dict = {}
        self.world = World()
        
    def create_user(self, nickename):
        user = User(nickename)
        self.user_dict[nickename] = user

    def select_new_person(self, nickname):
        user = self.user_dict[nickname]
        id_arr = self.world\
            .get_all_person_id()
        user.person_id = Btpy.random_choice(
            id_arr)
        
    def update(self):
        self.world.update()

    def render(self, nickname):
        user = self.user_dict[nickname]
        person = self.world.get_person(
            user.person_id)
        return person.narrative_write()
    
    def take_desition(self, nickname, key):
        user = self.user_dict[nickname]
        person = self.world.get_person(
            user.person_id)
        person.take_desition(key)
        self.world.set_person(person)
    
    def create_map(self):
        self.world.create_map(
            self.size_map_x, self.size_map_y)
        
    def write(self):
        return self.world.write()

    