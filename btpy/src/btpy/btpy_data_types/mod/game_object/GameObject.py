

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

    def __init__(self, ID:str = ""):
        self.last_number_id += 1
        self.point_location\
            :list[int] = [0, 0]
        self.point_motion\
            :list[int] = [0, 0]
        self.pose_key:str = ""
        self.group_key:str = ""
        self.__image_list_dict = {}
        self.__image_list_key:str = ""
        self.__iterator_image = Iterator()
        self.__iterator_image\
            .set_is_cycle(True)
        self.__box_size_list\
            :list[int] = [0, 0]
        self.behavior_dict:dict = {}
        self.colliding_id_set:set = set()
        self.is_colliding = False
        # CALLS -------------------------
        self.set_id(ID)

    # -----------------------------------

    # PUBLIC -----------------------------

    def set_box_size(self, WIDTH:int, 
            HEIGHT:int)->None:
        self.__box_size_list \
            = [WIDTH, HEIGHT]

    def get_id(self)->str:
        return self.__id

    def set_id(self, ID:str)->None:
        """
        Funcion que crea un identificador
        unico para llamar al objeto
        desde el escenario. Si el ID es 
        void string crea uno automatica-
        mente.
        """
        if(ID == ""):
            self.__id = str(self\
                .last_number_id)
        else:
            self.__id = ID

    # PUBLIC STATIC
    def set_scenario_size(scenario_list):
        GameObject.scenario_width \
            = scenario_list[0]
        GameObject.scenario_height \
            = scenario_list[1]

    def add_behavior(self, KEY:str,
            FUNCTION_ARGS_X1:callable)\
            ->None:
        self.behavior_dict[KEY] \
            = FUNCTION_ARGS_X1
        
    def get_render(self)->dict:
        return {
            "image_key": self\
                .__iterator_image.get(),
            "point": self.point_location
        }
        
    def set_image_list(self, 
                KEY:str, 
                IMAGE_LIST:list[str])\
                ->None:
        if(isinstance(IMAGE_LIST, list)):
            self.__image_list_dict[KEY]\
                = IMAGE_LIST
        elif(isinstance(IMAGE_LIST, str)):
            self.__image_list_dict[KEY]\
                = [IMAGE_LIST]
        if(self.__image_list_key == ""):
            self.set_image_list_key(KEY)
        
    def next_image(self):
        if(self.__image_list_key == ""):
            return None
        self.__iterator_image.next()
        
    def set_image_list_key(self, KEY:str)\
                ->None:
        self.__image_list_key = KEY
        image_list = self\
            .__image_list_dict[KEY]
        self.__iterator_image\
            .set_list(image_list)

    def get_rect_box(self)->dict:
        return { 
            "x":self.point_location[0],
            "y":self.point_location[1],
            "width":self.__box_size_list[0],
            "height":self.__box_size_list[1]
        }
    
    def get_future_rect_box(self)->dict:
        """
        Crea un rect box del hitbox del
        objeto que predice el movimiento
        futuro del objeto para detectar
        la colision antes de que se mueva.
        Esto evita que se atasque con
        el otro objeto colisionable.
        """
        point = self.get_next_move_point()
        return { 
            "x":point[0],
            "y":point[1],
            "width":self.__box_size_list[0],
            "height":self.__box_size_list[1]
        }
        
    def detect_collision(self,
            game_object)->bool:
        return is_colliding_rect(
                self.get_future_rect_box(),
                game_object.get_rect_box()
            )
    
    def add_collision(self, game_object):
        self.is_colliding = True
        self.colliding_id_set.add(
            game_object.get_id()
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
        self.next_image()
        if(self.is_colliding):
            self.point_motion = [0, 0]
        else:
            self.__move_object()

    def __move_object(self):
        self.point_location = self\
            .get_next_move_point()

    def get_next_move_point(self)\
            ->list[int]:
        point = [0, 0]
        point[0] \
            = sum_in_range(
                self.point_location[0],
                self.point_motion[0],
                [0, self.scenario_width]
            )
        point[1] = sum_in_range(
            self.point_location[1],
            self.point_motion[1],
            [0, self.scenario_height]
        )
        return point

    def free(self)->None:
        self.is_colliding = False
        self.colliding_id_set = set()

    # ----------------------------------------

    # PRIVATE ------------------------------

