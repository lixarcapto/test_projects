

from btpy.src.btpy.Btpy import Btpy

class GObject:

    UNIQUE_CODE = 0

    def __init__(self, id = "") -> None:
        # STATS ----------------------------
        self.energy_frac = [0, 0]
        self.life_limit = 0
        self.energy_limit = 0
        self.speed = 70
        self.health = 10
        #
        # RESOURCES ------------------------
        self.life_time = 0
        self.energy = 0
        self.acceleration = 0
        self.health_limit = 10
        # REGISTER
        self.was_free = False
        # SUBCRIPTIONS ---------------------
        self.is_player = False
        self.is_movile = False
        self.is_a_walker = False
        self.is_mortal = False
        # indica si esta en pantalla
        self.is_in_cam = False
        self.is_destructible = False
        self.has_focus_cam = False
        self.keyboard_movement = False
        # indica si detecta colisiones
        self.is_collidable = False
        #
        # IDENTIFIERS -----------------------
        self.id = id
        self.family = ""
        self.mode = ""
        #
        # PHYSIC_PROPERTYS ------------------
        self.point = [0, 0]
        self.mid_point = [0, 0]
        self.cardinal_sense = "C"
        self.size_box_x = 0
        self.size_box_y = 0
        #
        # GRAPHIC PROPERTYS -----------------
        self.layout = 0
        # punto en la pantalla traducido
        self.point_in_cam = [0, 0]
        self.image_layout = []
        self.__image_route = ""
        #
        # BUFFERS ---------------------------
        self.event_buffer = []
        self.colition_id_arr = []
        #
        # OTHERS ---------------------------
        # si no indica un ID
        if(id == ""):
            self.id = self.get_unique_code()
        self.set_image_route(
            "../res/image/red_square_70x70.png"
        )

    # ACCESSORS -----------------------------

    def write(self):
        txt = ""
        txt += f"{self.id=}\n"\
        + f"{self.point=}\n"\
        + f"{self.size_box_x=}\n"\
        + f"{self.size_box_y=}\n"\
        + f"{self.__image_route=}\n"\
        + f"{self.is_in_cam=}\n"\
        + f"{self.was_free=}\n"\
        + f"{self.point_in_cam=}\n"
        txt += "colition id: \n"
        for e in self.colition_id_arr:
            txt += e + ", "
        return txt
    
    def __str__(self):
        return self.write()

    def set_box_square(self, square):
        self.size_box_x = square["width"]
        self.size_box_y = square["height"]
        self.point = [square["x"], 
                      square["y"]]

    def randomize_destiny(self):
        sense = Btpy.sense()
        r = list(sense.CARDINAL_DICT.keys())
        sense_key = Btpy.random_choice(r)
        self.cardinal_sense = sense_key

    def stop_move(self):
        self.cardinal_sense = "C"

    def set_image_route(self, route:str):
        Btpy.check_path(route, ".png")
        r = Btpy.image_size(route)
        self.size_box_x = r["x"]
        self.size_box_y = r["y"]
        self.__image_route = route


    def get_image_route(self):
        return self.__image_route
    
    def get_box_square(self)->dict[int]:
        return {
        'x': self.point[0], 
        'y': self.point[1], 
        'width': self.size_box_x, 
        'height': self.size_box_y
        }

    def get_destiny_point(self):
        sense = Btpy.sense()
        key = self.cardinal_sense
        sum_point = sense.CARDINAL_DICT[key]
        # calcula velocidad + direccion
        final_point = list(map(
            lambda e:e*self.speed, sum_point))
        return final_point
    
    def get_mid_point(self):
        self.calculate_center()
        return self.mid_point

    def collided_with_id(self, name)->None:
        if(name in self.colition_id_arr):
            return True
        return False

    def get_unique_code(self):
        code = GObject.UNIQUE_CODE
        GObject.UNIQUE_CODE += 1
        return code
    
    def get_collision_id(self):
        return self.colition_id_arr

    def add_colition_id(self, name):
        self.colition_id_arr.append(name)

    def clear_colition(self):
        self.colition_id_arr.clear()

    def sum_health(self, value):
        self.health = Btpy.sum_in_range(
            self.health,
            value, 
            [0, self.health_limit]
        )

    def set_is_mortal(self, fraction):
        self.is_mortal = True
        self.life_time = fraction[0]
        self.life_limit = fraction[1]

    def add_event(self, event):
        self.event_buffer.append(event)

    def pick_event(self)->list[list]:
        event_list = self.event_buffer.copy()
        self.event_buffer.clear()
        return event_list

    def launch_move(self, id):
        point = self.get_destiny_point()
        event = ["move", id, point]
        self.add_event(event)

    def launch_move_cam(self):
        event = ["move_cam", self.point]
        self.add_event(event)

    def launch_sense_change(self, key):
        event = ["sense_change", self.id, key]
        self.add_event(event)

    def advance_age(self):
        self.life_time += 1
        if(self.life_time>= self.life_limit):
            self.launch_die()

    def launch_die(self):
        event = ["kill", self.id]
        self.add_event(event)

    def launch_transform(self, family_new_object):
        event = [
            "transform", 
            self.id, 
            family_new_object,
            self.point_index
        ]
        self.add_event(event)

    def update(self): 
        self.was_free = False
        if(self.is_mortal):
            self.advance_age()
            if(self.health <= 0):
                self.launch_die()
            self.sum_health(-1)
        if(self.is_a_walker):
            self.randomize_destiny()
            self.launch_move(self.id)
        if(self.is_movile):
            self.launch_move(self.id)
        if(self.has_focus_cam):
            self.launch_move_cam()
        self.calculate_center()
        

    def calculate_center(self):
        square = self.get_box_square()
        self.mid_point = Btpy.center_square(
            [square["x"], square["y"]],
            square["width"],
            square["height"])

    def free(self):
        self.clear_colition()
        self.is_in_cam = False
        self.stop_move()
        self.was_free = True

    def move_index(self, point):
        for i in range(len(point)):
            self.point[i] += point[i]
    
    def to_pod_image(self) -> dict:
        paint_order = {
        "type": "image",
        "route" : self.src_image,
        "point": self.point,
        }
        return paint_order