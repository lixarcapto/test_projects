
from btpy.Btpy import Btpy

class Go:

    """
    Clase que representa a un objeto de 
    juego o escenario para una escena.
    su abreviación go es de Game object.
    """
    def __init__(self, name) -> None:
        self.point_index:list[int] = [0, 0]
        self.name:str = name
        self.src_image:str = ""
        self.event_buffer = []
        self.resistance_frac = [0,0]
        self.layout = 0
        self.image_layout = []
        self.family = ""
        self.mode = ""
        self.is_a_walker = False
        self.is_mortal = False
        self.is_the_star = False
        self.cardinal_sense = "c"
        self.resource_kval = ["", 0]
        self.colition_names_arr = []
        self.life_frac = [0, 10]
        self.energy_frac = [0, 0]
        self.food_frac = [0, 0]

    def consume_resource_kval(self, kval):
        match kval[0]:
            case "food":
                self.food_frac[0] += kval[1]

    def add_colition_name(self, name):
        self.colition_names_arr.append(name)

    def set_is_mortal(self, fraction):
        self.is_mortal = True
        self.life_frac = fraction

    def add_event(self, event):
        self.event_buffer.append(event)

    def pick_event(self)->list[list]:
        event_list = self.event_buffer.copy()
        self.event_buffer.clear()
        return event_list
    
    def launch_focus_cam(self):
        event = ["focus_cam", 
                 self.point_index]
        self.add_event(event)
    
    def launch_move(self, id, point):
        event = ["move", id, point]
        self.add_event(event)

    def advance_age(self):
        self.life_frac[0] += 1
        if(self.life_frac[0] 
           == self.life_frac[1]):
            self.launch_die()

    def launch_die(self):
        event = ["kill", self.name]
        self.add_event(event)

    def launch_transform(self, family_new_object):
        event = [
            "transform", 
            self.name, 
            family_new_object,
            self.point_index
        ]
        self.add_event(event)

    def update(self): 
        if(self.is_mortal):
            self.advance_age()
        if(self.is_a_walker):
            point = Btpy.random_point([-1, 1])
            self.launch_move(self.name, point)
        if(self.is_the_star):
            self.launch_focus_cam()
        pass

    def move_index(self, point):
        for i in range(len(point)):
            self.point_index[i] += point[i]

    def write(self):
        txt = ""
        txt += f"{self.point_index=}\n"
        txt += f"{self.name=}\n"
        txt += f"{self.src_image=}\n"
        return txt
    
    def to_pod_image(self) -> dict:
        paint_order = {
        "type": "image",
        "route" : self.src_image,
        "point": self.point_index,
        }
        return paint_order