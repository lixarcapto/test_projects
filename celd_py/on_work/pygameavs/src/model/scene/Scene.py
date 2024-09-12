

from .scene_deps import*

class Scene:

    """
     clase qué sirve para gestionar 
     modificar los objetos del escenario.  
     permite  delegar la modificación 
     e iteración de los objetos del 
     escenario global.
    """

    def __init__(self, size_x, 
            size_y) -> None:
        self.name:str = "" 
        self.go_factory = GoFactory()
        self.user_player_dict = {}
        self.gobject_dict:dict = {}
        self.actual_player_id = ""
        self.size_x = size_x
        self.size_y = size_y
        self.init()

    def init(self):
        pass

    def update(self):
        self.update_gobject()
        self.detect_collisions()
        go = self.gobject_dict["cam_main"]
        print(go)

    def set_gobject(self, go:GObject):
        self.gobject_dict[go.id] = go

    def get_gobject(self, id)->GObject:
        return self.gobject_dict[id]
    
    def has_objects(self):
        if(self.gobject_dict == {}):
            return False
        return True
    
    def has_player(self):
        if(self.user_player_dict == {}):
            return False
        return True
    
    """
     función que crea un objeto user 
     Player,  un objeto de cámara 
     player y un objeto character player.
    """
    def create_player(self, id, 
            cam_size_x, cam_size_y):
        # cam player
        cam_id = "cam_" + id
        self.create_gobject(cam_id, 
            "GObject", [0,0], 
            [cam_size_x, cam_size_y])
        # character player
        character_id = "player_" + id
        self.create_gobject(character_id, 
            "GPlayer")
        # user player
        player = UserPlayer()
        player.main_id = character_id
        player.name = id
        player.cam_id = cam_id
        self.actual_player_id = id
        self.user_player_dict[id] = player
    
    def create_gobject(self, id, 
            class_name, point = [0,0],
            size_box = [70, 70]):
        go = self.go_factory.create(
            class_name, 
            id
        )
        go.size_box_x = size_box[0]
        go.size_box_y = size_box[1]
        go.point = point
        self.set_gobject(go)

    def add_go_class(self, class_name, 
        class_reference):
        self.go_factory.add_go_class(
            class_name, 
            class_reference
        )

    def delete_gobject(self, name):
        go = self.gobject_dict[name]
        del(self.gobject_dict[name])

    def detect_collisions(self):
        self.gobject_dict \
        = detect_all_collitions(
            self.gobject_dict)
            
    """
     función que actualiza todos los 
     objetos de la lista
    """
    def update_gobject(self):
        gobject = None
        for k in self.gobject_dict:
            self.gobject_dict[k].update()

    """
     función los datos temporales 
     almacenados de los objetos
    """
    def free(self):
        gobject = None
        for k in self.gobject_dict:
            self.gobject_dict[k].free()
    
    """
     función que obtiene todos los 
     objetos que se encuentran en 
     el área de la cámara con sus 
     puntos de camara traducidos
    """
    def take_screenshot(self):
        object_arr = get_object_to_render(
            self.get_cam_id(), 
            self.gobject_dict)
        return object_arr
    
    def get_cam_id(self):
        id = self.actual_player_id
        player = self.user_player_dict[id]
        return player.cam_id
    
    def get_player_main_id(self):
        id = self.actual_player_id
        player = self.user_player_dict[id]
        return player.main_id
    
    def get_player_id(self):
        return self.actual_player_id
    
    def get_cam_square(self):
        id = self.actual_player_id
        player = self.user_player_dict[id]
        cam_id = player.cam_id
        go = self.get_gobject(cam_id)
        return go.get_box_square()
    
    def set_cam_square(self, square):
        id = self.actual_player_id
        player = self.user_player_dict[id]
        cam_id = player.cam_id
        go = self.get_gobject(cam_id)
        go.set_box_square(square)
        self.set_gobject(go)
    
    def render_bars(self, gobject_arr):
        render = {}
        render_list = []
        for go in gobject_arr:
            # health bar
            bar_dict = create_bar(
                go.health,
                go.health_limit,
                go.point_in_cam,
                go.size_box_x
            )
            render = self.create_render_line(
                bar_dict["point1"],
                bar_dict["point2"],
                5,
                [255, 0, 0]
            )
            render_list.append(render)
        return render_list
    
    def create_render_line(self, 
            point1, point2, width, rgb):
        return {
            "type":"render_line",
            "point1":point1,
            "point2":point2,
            "width":width,
            "rgb":rgb
        }
    
    def create_render_image(self):
        return {
            "type":"render_image",
            "route":"",
            "point":[0, 0]
        }

    """
     Función que renderiza los objetos  
     en la cámara para convertirlos 
     en una lista de objetos gráficos  
     qué enviar a la interfaz gráfica
    """
    def render(self):
        # toma objetos en pantalla
        object_arr = self.take_screenshot()
        # renderiza las imagenes
        render_image_arr = render_gobjects(
            object_arr)
        render_bar_arr = self\
            .render_bars(object_arr)
        render_list = render_image_arr\
         + render_bar_arr
        return render_list
    
    def seek_void_space(self, point_proxi):
        """
        Función que identifica el espacio 
        vacío más cercano al punto enviado 
        En el mapa
        """
        point = [0, 0]
        sum_point_arr = [
            [0, 1],
            [1, 0],
            [1, 1],
            [-1, -1],
            [-1, 0],
            [0, -1]
        ]
        r_point = [0, 0]
        while(True):
            for sum_point in sum_point_arr:
                r_point = Btpy.sum_point(
                    point,
                    sum_point,
                    [0, self.size_x],
                    [0, self.size_y]
                )
                if(not self.__some_is_in(
                    r_point)):
                    return r_point
        raise Exception("not exist space")

    def transform(self, name, family, point):
        self.delete_gobject(name)
        self.spawn(name, family, point)

    def spawn_child(self, name, 
            family, point):
        new_name = name + "_child_" \
        + str(self.__create_unique_code())
        self.spawn(new_name, family, point)

    def sense_change(self, id, key):
        go = self.get_gobject(id)
        go.cardinal_sense = key
        self.set_gobject(go)

    def spawn(self, name, 
            class_name, point):
        """
        Función que aparece un objeto 
        de la clase determinada en un 
        punto Determinado
        """
        go = self.go_factory.create(
            class_name,
            name
        )
        go.point_index = point
        self.insert_go(go)

    def move_in_matrix(self, id, 
            final_point):
        """
        Función que mueve un objeto hacia 
        un Point determinado siempre que 
        el Point no esté ocupado.
        """
        # calcula el destino
        go = self.get_gobject(id)
        destiny_point = Btpy.sum_point(
            go.point, 
            final_point,
            [0, self.size_x], 
            [0, self.size_y]
        )
        square = {
            "x":destiny_point[0],
            "y":destiny_point[1],
            "height":go.size_box_y,
            "width":go.size_box_x
        }
        some_is_in = some_is_in_area(
            square, self.gobject_dict)
        if(some_is_in):
            go.cardinal_sense = "C"
            return None
        go.point = destiny_point
        self.set_gobject(go)
            
    def move_cam(self, point):
        cam_id = self.get_cam_id()
        go_cam = self.get_gobject(cam_id)
        go_cam.point = Btpy.origin_by_center(
            point,
            go_cam.size_box_x,
            go_cam.size_box_y
        )
        self.set_gobject(go_cam)

    def pick_events(self):
        """
        Función que recolecta los eventos 
        desencadenados en los objetos de 
        la lista de objetos y los almacena 
        en la cola de eventos.
        """
        e = None
        event = None
        event_list = []
        for k in self.gobject_dict:
            e = self.gobject_dict[k]
            event_arr = e.pick_event()
            # checkea si obtubo eventos
            if(len(event_arr) > 0):
                for event in event_arr:
                    event_list\
                        .append(event)
        return event_list

    

    

