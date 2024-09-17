


from ....btpy_maths.mod.sum_point.sum_point import*
from ....btpy_maths.mod.colliding_square.colliding_square import*
from ....btpy_const.mod.sense.Sense import Sense

class GObject:

    LAST_ID = 0
    SENSE = Sense

    def __init__(self, ROUTE = "") -> None:
        self.id = ""
        self.location_x:int = 0
        self.location_y:int = 0
        self.route_image:str = ROUTE
        self.stance:str = ""
        self.hit_box_x = 100
        self.hit_box_y = 100
        self.move_arrow = [0, 0]
        self.family:str = ""
        self.colliding_id_buffer = []
        self.create_id()

    def set_move_arrow(self, point):
        self.move_arrow = point

    def collide_with(self, ID)->bool:
        return ID in self\
            .colliding_id_buffer

    def create_id(self):
        self.id = str(self.LAST_ID)
        self.LAST_ID += 1

    def update(self):
        pass

    def get_image_paint_dict(self):
        return {
            "route":self.route_image,
            "point":[
                self.location_y,
                self.location_x
            ]
        }
    
    def free(self):
        self.colliding_id_buffer.clear()

    def move(self, move_point, 
             scenario_size_x, 
             scenario_size_y, 
             gobject_list):
        # si colisiona con otro objeto 
        # salta el codigo
        for gobject in gobject_list:
            if(gobject.id == self.id):
                continue
            if(self.is_colliding(gobject)):
                self.colliding_id_buffer\
                    .append(gobject.id)
                return None
        r_point = sum_point(
            [self.location_x, self.location_y],
            [move_point[0], move_point[1]],
            [0, scenario_size_x],
            [0, scenario_size_y]
        )
        self.location_x = r_point[0]
        self.location_y = r_point[1]

    def set_route_image(self, ROUTE:str):
        self.route_image = ROUTE

    def get_route_image(self):
        return self.route_image

    def set_size_hit_box(self, SIZE_X:int, 
            SIZE_Y:int):
        self.hit_box_x = SIZE_X
        self.hit_box_y = SIZE_Y

    def set_location(self, LOCATION_X:int,
            LOCATION_Y:int):
        self.location_x = LOCATION_X
        self.location_y = LOCATION_Y

    def write(self):
        return ""\
        + f"{self.location_x=}"\
        + f"{self.location_y=}"\
        + f"{self.route_image=}"\
        + f"{self.stance=}"\
        + f"{self.hit_box_x=}"\
        + f"{self.hit_box_y=}"\
        + f"{self.family=}"
    
    def __str__(self):
        return self.write()
    
    def get_square(self):
        return {
            "x":self.location_x,
            "y":self.location_y,
            "width":self.hit_box_x,
            "height":self.hit_box_y
        }
    
    def get_image_dict(self)->dict:
        return {
            "route":self.route_image,
            "point":[self.location_x, 
                     self.location_y]
        }
    
    def is_colliding(self, gobject):
        is_colliding = colliding_square(
            self.get_square(),
            gobject.get_square()
        )
        return is_colliding
        
