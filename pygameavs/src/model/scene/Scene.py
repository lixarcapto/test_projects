

from .scene_deps import*

class Scene:

    """
     clase qué sirve para gestionar 
     modificar los objetos del escenario.  
     permite  delegar la modificación 
     e iteración de los objetos del 
     escenario global.
    """

    def __init__(self) -> None:
        self.name:str = "" 
        self.go_factory = GoFactory()
        self.user_player_dict = {}
        self.gobject_dict:dict = {}
        self.actual_player_id = ""
        self.size_celd = 70
        self.celd_number_x = 0
        self.celd_number_y = 0
        self.size_map_x = 0
        self.size_map_y = 0
        self.__init()
        print("REPORT: init scenario")

    # PUBLIC ACCESSORS ----------------------

    def set_size_map(self, size_x, size_y):
        self.size_map_x = size_x
        self.size_map_y = size_y

    def set_celd_numbers(self, x, y):
        self.celd_number_x = x
        self.celd_number_y = y

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
    
    def get_cam_id(self)->str:
        ID = self.actual_player_id
        player = self.user_player_dict[ID]
        return player.cam_id
    
    def get_player_main_id(self)->str:
        ID = self.actual_player_id
        player = self.user_player_dict[ID]
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

    # PUBLIC MUTATORS -----------------------

    def update(self):
        self.__update_gobject()
        self.__detect_collisions()
        go = self.gobject_dict["cam_main"]
        print(go)

    def create_map(self):
        self.randomize()

    def randomize(self):
        print("REPORT: randomize init")
        CELD_SIZE = 70
        point_index = [0, 0]
        has_object = False
        print(f"REPORT: {self.celd_number_y}/{self.celd_number_x} from randomize")
        for y in range(self.celd_number_y):
            for x in range(self.celd_number_x):
                has_object = Btpy\
                    .random_probability(70)
                if(has_object):
                    self.create_gobject(
                        f"{y}_{x}_three",
                        "GVegetable",
                        point_index.copy(),
                        [CELD_SIZE, CELD_SIZE]
                    )
                point_index[0] += CELD_SIZE
            point_index[1] += CELD_SIZE


    """
     Función que renderiza los objetos  
     en la cámara para convertirlos 
     en una lista de objetos gráficos  
     qué enviar a la interfaz gráfica
    """
    def render(self):
        # toma objetos en pantalla
        object_arr = self.__take_screenshot()
        # renderiza las imagenes
        render_image_arr = render_gobjects(
            object_arr)
        render_bar_arr = self\
            .__render_bars(object_arr)
        render_list = render_image_arr\
         + render_bar_arr
        return render_list

    def create_player(self, ID:str, 
            CAM_SIZE_X:int|float, 
            CAM_SIZE_Y:int|float)->None:
        """
        Función que crea un objeto user 
        Player,  un objeto de cámara 
        player y un objeto character player.
        """
        cam_id = self.__create_cam(ID, 
            CAM_SIZE_X, CAM_SIZE_Y)
        character_id = self\
            .__create_go_player(ID)
        # user player
        player = UserPlayer()
        player.main_id = character_id
        player.name = ID
        player.cam_id = cam_id
        self.actual_player_id = ID
        self.user_player_dict[ID] = player

    def create_gobject(self, ID:str, 
            CLASS_NAME:str, 
            POINT:list[int] = [0,0],
            SIZE_BOX:list[int] = [70, 70])\
            ->None:
        go = self.go_factory.create(
            CLASS_NAME, 
            ID
        )
        go.size_box_x = SIZE_BOX[0]
        go.size_box_y = SIZE_BOX[1]
        go.point = POINT
        self.set_gobject(go)

    def add_go_class(self, CLASS_NAME:str, 
        class_reference)->None:
        self.go_factory.add_go_class(
            CLASS_NAME, 
            class_reference
        )

    def delete_gobject(self, ID:str)->None:
        del(self.gobject_dict[ID])

    
    def free(self)->None:
        """
        Función que limpia los datos 
        temporales almacenados de los 
        objetos
        """
        gobject = None
        for k in self.gobject_dict:
            self.gobject_dict[k].free()

    def effect_transform(self, EVENT):
        self.__transform(
            EVENT[1],
            EVENT[2],
            EVENT[3]
        )

    def effect_sense_change(self, EVENT):
        self.__sense_change(
            EVENT[1],
            EVENT[2]
        )

    def effect_move(self, EVENT):
        self.__move_in_matrix(
            EVENT[1],
            EVENT[2]
        )

    def effect_move_cam(self, EVENT):
        self.__move_cam(
            EVENT[1]
        )

    def effect_kill(self, ID):
        self.delete_gobject(ID)

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

    # PRIVATE --------------------------------

    def __init(self)->None:
        pass

    def __create_go_player(self, ID):
        # character player
        character_id = "player_" + ID
        self.create_gobject(character_id, 
            "GPlayer")
        return character_id

    def __create_cam(self, ID, SIZE_X, 
            SIZE_Y)->str:
        # cam player
        cam_id = "cam_" + ID
        self.create_gobject(cam_id, 
            "GObject", [0,0], 
            [SIZE_X, SIZE_Y])
        return cam_id
    
    def __detect_collisions(self):
        self.gobject_dict \
        = detect_all_collitions(
            self.gobject_dict)
            
    """
     función que actualiza todos los 
     objetos de la lista
    """
    def __update_gobject(self):
        for k in self.gobject_dict:
            self.gobject_dict[k].update()

    """
     función que obtiene todos los 
     objetos que se encuentran en 
     el área de la cámara con sus 
     puntos de camara traducidos
    """
    def __take_screenshot(self)->list:
        object_arr = get_object_to_render(
            self.get_cam_id(), 
            self.gobject_dict)
        return object_arr
    
    def __render_bars(self, gobject_arr):
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
            render = self.__create_render_line(
                bar_dict["point1"],
                bar_dict["point2"],
                5,
                [255, 0, 0]
            )
            render_list.append(render)
        return render_list
    
    def __create_render_line(self, 
            point1, point2, width, rgb):
        return {
            "type":"line",
            "point1":point1,
            "point2":point2,
            "width":width,
            "rgb":rgb
        }
    
    def __create_render_image(self):
        return {
            "type":"render_image",
            "route":"",
            "point":[0, 0]
        }

    def __seek_void_space(self, point_proxi):
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

    def __transform(self, name, family, 
            point):
        self.delete_gobject(name)
        self.__spawn(name, family, point)

    def __spawn_child(self, name, 
            family, point):
        new_name = name + "_child_" \
        + str(self.__create_unique_code())
        self.__spawn(new_name, family, point)

    def __sense_change(self, id, key):
        go = self.get_gobject(id)
        go.cardinal_sense = key
        self.set_gobject(go)

    def __spawn(self, name, 
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

    def detect_AWSD(self, data):
        # si no existen players lo ignora
        if(not self.has_player()):
            return None
        player_id = self\
            .get_player_main_id()
        match data:
            case "w":
                self.__sense_change(
                    player_id, "N")
            case "a":
                self.__sense_change(
                    player_id,"E")
            case "d":
                self.__sense_change(
                    player_id,"W")
            case "s":
                self.__sense_change(
                    player_id,"S")

    def __move_in_matrix(self, id, 
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
            [0, self.size_map_x], 
            [0, self.size_map_x]
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
            
    def __move_cam(self, point):
        cam_id = self.get_cam_id()
        go_cam = self.get_gobject(cam_id)
        go_cam.point = Btpy.origin_by_center(
            point,
            go_cam.size_box_x,
            go_cam.size_box_y
        )
        self.set_gobject(go_cam)

    

    

