
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

    
    
    def launch_focus_cam(self):
        event = ["focus_cam", 
                 self.point_index]
        self.add_event(event)
    
    