

from ....btpy_maths.mod\
    .sum_in_range.sum_in_range import*
from ....btpy_maths.mod.vector_sum\
    .vector_sum import*
from ....btpy_checkers.mod\
    .is_colliding_rect.is_colliding_rect import*
from ....btpy_const.mod.sense.Sense import Sense
from ....btpy_utilitys.mod.iterator.Iterator import Iterator

class GameObject:

    scenario_width:int = 0
    scenario_height:int = 0
    last_number_id:int = 0

    def set_scenario_size(scenario_list):
        GameObject.scenario_width \
            = scenario_list[0]
        GameObject.scenario_height \
            = scenario_list[1]

    def __init__(self):
        self.number_id = self\
            .last_number_id
        self.last_number_id += 1
        self.point_location\
            :list[int] = [0, 0]
        self.point_motion\
            :list[int] = [0, 0]
        self.pose_key:str = ""
        self.group_key:str = ""
        self.__image_key_list:list[str] = []
        self.index_image:int = 0
        self.box_size_list\
            :list[int] = [0, 0]
        
    def add_image_key(self, IMAGE_KEY:str)\
            ->None:
        """
        Funcion que agrega una imagen a
        la lista de imagenes.
        """
        # validators
        if(not isinstance(IMAGE_KEY, str)):
            raise Exception(
                "IMAGE_KEY is not a string type")
        self.__image_key_list.append(
            IMAGE_KEY)
        
    def clean_image_key_list(self)->None:
        self.__image_key_list = []
        
    def set_image_key_list(self, 
                IMAGE_KEY_LIST:list[str])\
                ->None:
        self.__image_key_list \
            = IMAGE_KEY_LIST

    def get_rect_box(self)->dict:
        return { 
            "x":self.point_location[0],
            "y":self.point_location[1],
            "width":self.box_size_list[0],
            "height":self.box_size_list[1]
        }
        
    def is_colliding(self,
            game_object)->bool:
        return is_colliding_rect(
            self.get_rect_box(),
            game_object.get_rect_box()
        )
    
    def move_left(self, speed):
        self.sum_force([speed *-1, 0])

    def move_right(self, speed:int):
        self.sum_force([speed, 0])

    def move_up(self, speed:int):
        self.sum_force([0, speed *-1])

    def move_down(self, speed:int):
        self.sum_force([0, speed])
        
    def sum_force(self, vector_list:list[int]):
        self.point_motion = vector_sum(
            self.point_motion, vector_list)
        
    def update(self):
        self.point_location[0] \
            = sum_in_range(
                self.point_location[0],
                self.point_motion[0],
                [0, self.scenario_width]
            )
        self.point_location[1] = sum_in_range(
            self.point_location[1],
            self.point_motion[1],
            [0, self.scenario_height]
        )

