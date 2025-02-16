


from ....btpy_maths.mod.sum_point.sum_point import*
from ....btpy_maths.mod.colliding_square.colliding_square import*
from ....btpy_const.mod.sense.Sense import Sense
from ....btpy_maths.mod.point_in_space.point_in_space import*
from ....btpy_maths.mod.square_to_space.square_to_space import*
from ..animation.Animation import Animation

class GObject:

    """
    Esta clase representa a un game object
    para utilizar en simuladores y
    videojuegos.
    """

    last_id = 0
    SENSE = Sense

    def __init__(self, ID:str = "") -> None:
        self.__id = ""
        self.__location_x:int = 0
        self.__location_y:int = 0
        self.animation = Animation()
        self.stance:str = ""
        self.__hit_box_x = 100
        self.__hit_box_y = 100
        self.__move_arrow = [0, 0]
        self.family:str = ""
        self.__colliding_id_buffer = []
        if(ID == ""):
            self.__create_id()
        print(f"ID {self.__id}")

    # ACCESORS -----------------------------

    def get_id(self):
        return self.__id
    
    def set_id(self, ID:str):
        self.__id = ID

    def set_location(self, POINT):
        self.__location_x = POINT[0]
        self.__location_y = POINT[1]

    def get_location(self)->list[int|float]:
        return [self.__location_x, 
                self.__location_y]
    
    def set_hitbox_size(self, SIZE_X,
            SIZE_Y):
        self.__hit_box_x = SIZE_X
        self.__hit_box_y = SIZE_Y

    def get_hitbox_size_x(self):
        return self.__hit_box_x
    
    def get_hitbox_size_y(self):
        return self.__hit_box_y
    
    def add_image_layout(self, 
            ROUTE:list[str])\
            ->None:
        if(not type(ROUTE) == list):
            self.animation\
                .add_image_layout([ROUTE])
        else:
            self.animation\
                .add_image_layout(ROUTE)

    def get_image_layout(self)->list[str]:
        return self.animation\
            .get_image_layout()
    
    def set_vector_arrow(self, POINT):
        self.__move_arrow = POINT

    def get_vector_arrow(self):
        return self.__move_arrow

    # MUTATORS ----------------------------

    def set_move_arrow(self, point):
        self.__move_arrow = point

    def collide_with(self, ID)->bool:
        return ID in self\
            .__colliding_id_buffer

    def __create_id(self):
        self.__id = str(GObject.last_id)
        GObject.last_id += 1

    def update(self):
        """
        Funcion que debe ser llamada
        para añadir nuevas funciones
        de actualizacion.
        """
        self.animation.next()
        pass
    
    def free(self):
        self.__colliding_id_buffer.clear()

    def move(self, move_point, 
             scenario_size_x, 
             scenario_size_y, 
             gobject_list):
        # si colisiona con otro objeto 
        # salta el codigo
        for gobject in gobject_list:
            if(gobject.get_id() == self.__id):
                continue
            if(self.square_is_colliding(gobject)):
                self.__colliding_id_buffer\
                    .append(gobject.get_id())
                print("is colliding")
                return None
        r_point = sum_point(
            [self.__location_x, self.__location_y],
            [move_point[0], move_point[1]],
            [0, scenario_size_x],
            [0, scenario_size_y]
        )
        self.__location_x = r_point[0]
        self.__location_y = r_point[1]

    def write(self):
        return ""\
        + f"{self.__location_x=}"\
        + f"{self.__location_y=}"\
        + f"{self.__route_image=}"\
        + f"{self.stance=}"\
        + f"{self.__hit_box_x=}"\
        + f"{self.__hit_box_y=}"\
        + f"{self.family=}"
    
    def __str__(self):
        return self.write()
    
    def get_square(self):
        return {
            "x":self.__location_x,
            "y":self.__location_y,
            "width":self.__hit_box_x,
            "height":self.__hit_box_y
        }
    
    def get_image_layout_dict(self):
        return {
            "route_array":self.get_image_layout(),
            "point":[self.__location_x, 
                     self.__location_y]
        }
    
    def square_is_colliding(self, gobject):
        is_colliding = colliding_square(
            self.get_square(),
            gobject.get_square()
        )
        return is_colliding

    def point_is_colliding(self, POINT):
        location = [self.__location_x, 
            self.__location_y]
        space = square_to_space(
            location,
            self.__hit_box_x,
            self.__hit_box_y
        )
        return point_in_space(
            POINT,
            space["range_x"],
            space["range_y"]
        )
        
        
