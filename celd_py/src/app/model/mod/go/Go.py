

from btpy.src.btpy.Btpy import Btpy

class Go:

    SIZE_IMAGE = 70

    def __init__(self, id) -> None:
        self.id = id
        self.image_src_arr:list[str] = []
        self.group = ""
        self.class_name = ""
        self.event_buffer = []
        self.point = [0, 0]
        self.set_image_layout(
            "../res/image/go_pj_70x70.png")
        
    def update(self):
        point = self.random_move(self.point)
        self.launch_move(point)
        
    def collect_event(self):
        event_list = self.event_buffer
        self.event_buffer.clear()
        return event_list
    
    def random_move(self, point, factor = 1):
        sense_dict = Btpy.sense()
        point_sense = Btpy.random_choice(
            sense_dict.CARDINAL_DICT)
        point_sense = list(map(
            lambda e: e*factor,
            point_sense))
        point = Btpy.vector_sum(point, 
            point_sense)
        return point
        
    def launch_move(self, point):
        event = ["move", self.id, point]
        self.event_buffer.append(event)

    def set_image_layout(self, route):
        self.image_src_arr.append(route)

    def new_render_image(self, route, point):
        return {
            "type":"image",
            "route":route,
            "point": self.calcule_point_final(
                point
            )
        }
    
    def calcule_point_final(self, point):
        return list(map(
            lambda e: e * Go.SIZE_IMAGE,
            point
        ))
    
    def render(self, point):
        render_list = []
        render = {}
        # renderiza la imagen en capas
        for route in self.image_src_arr:
            render = self.new_render_image(
                route, 
                point
            )
            render_list.append(render)
        return render_list
    
    def write(self):
        txt = f"{self.id=}\n"
        txt += f"{self.image_src_arr=}\n"
        txt += f"{self.group=}\n"
        txt += f"{self.class_name=}\n"
        return txt