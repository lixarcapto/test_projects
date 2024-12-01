

from btpy.Btpy import Btpy
from tkupg.Tkupg import Tkupg
from ..go_factory.GoFactory import GoFactory

class SceneMatrix:

    """
    Clase que simula un escenario de un 
    motor de escenario para la librería 
    GAMS.
    """

    COMMAND_LIST = [
        ["move", "id", "point"]
    ]

    def __init__(self, size_x, size_y) -> None:
        self.name:str = ""
        self.go_factory = GoFactory()
        self.unique_code = 0
        self.go_dict:dict = {}
        self.space = None
        self.quantity_celds = 0
        self.event_queue = []
        self.size_celd = 100
        self.cam_size = 6
        self.cam_location = [0, 0]
        # funciones
        self.set_space_ranges(size_x, size_y)

    # ACCESSORS ------------------------------

    """
    Función que asigna los rangos del 
    espacio dimensional del escenario.
    """
    def set_space_ranges(self, 
            size_x, size_y):
        self.space = Btpy.range_space()
        self.space.range_y = [0, size_y]
        self.space.range_x = [0, size_x]

    def set_cam_expansion(self, 
        point:list[int])->None:
        if(not Btpy.is_point(point, 2)):
            raise Exception(
            f"is not a point {point}"
            )
        self.cam_rectangle = [[0,0], point]

    def get_cam_square(self):
        return self.cam_rectangle

    def set_size_celd(self, size:int):
         self.size_celd = size

    def add_go_class(self, class_name, 
        class_reference):
        SceneMatrix.CLASS_COLLECTION\
            [class_name] = class_reference

    # MUTATORS ----------------------------

    def create_go(self, id, 
            class_name, point = [0,0]):
        go = self.go_factory.create(
            class_name, 
            id
        )
        go.point_index = point
        self.insert_go(go)

    def insert_go(self, go):
        """
        Función que inserta en el mapa objetos 
        Go encontrando puntos vacío cercanos 
        al punto enviado.
        """
        point = go.point_index
        if(not self.__some_is_in(point)):
            go.point_index = point
            self.__set_go(go)
            return None
        void_point = self.__seek_void_space(
            point)
        go.point_index = void_point
        self.__set_go(go)

    def update(self):
        """
        Función que actualiza el escenario
        a la vez que retorna la camara del 
        escenario renderizado.
        """
        self.__update_objects()
        self.__pick_events()
        self.__process_event()
    
    # PRIVATE ------------------------------

    def __create_unique_code(self):
        n = self.unique_code
        self.unique_code += 1
        return n

    def __process_event(self):
        """
        Función selectora que procesa los 
        eventos almacenados en la cola de 
        eventos.
        """
        print(f"self.event_queue {self.event_queue}")
        for event in self.event_queue:
            if(event[0] == "move"):
                self.__move_in_matrix(
                    event[1],
                    event[2]
                )
            if(event[0] == "focus_cam"):
                self.__move_cam(
                    event[1]
                )
        # solo para kill
        for event in self.event_queue:
            if(event[0] == "kill"):
                self.__delete_go(event[1])
            elif(event[0] == "transform"):
                self.__transform(
                    event[1],
                    event[2],
                    event[3]
                )
        self.event_queue.clear()

    # para basic things
    def origen_to_rectangle(self, 
                origen_point, 
                size):
        point = origen_point.copy()
        point[0] += size
        point[1] += size
        return point

    # FIXME: la camara no se mueve bien
    def __move_cam(self, point_sum):
        point_expansion = self\
            .origen_to_rectangle(
                self.cam_location,
                self.cam_size
            )
        square = Btpy.center_square_by_point(
            point_sum,
            self.cam_location,
            point_expansion,
            self.cam_size
        )
        print(f"{square=}/{point_sum=}")
        self.cam_rectangle = square
    
    def __transform(self, name, family, point):
        self.__delete_go(name)
        self.__spawn(name, family, point)

    def __spawn_child(self, name, 
            family, point):
        new_name = name + "_child_" \
        + str(self.__create_unique_code())
        self.__spawn(new_name, family, point)

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

    def __update_objects(self):
        """
        Función que recorre los objetos de 
        la lista de objetos para actualizarlos
        """
        for k in self.go_dict:
            self.go_dict[k].update()
            print(self.go_dict[k].write())
        
    def __pick_events(self):
        """
        Función que recolecta los eventos 
        desencadenados en los objetos de 
        la lista de objetos y los almacena 
        en la cola de eventos.
        """
        e = None
        event = None
        for k in self.go_dict:
            e = self.go_dict[k]
            event_arr = e.pick_event()
            # checkea si obtubo eventos
            if(len(event_arr) > 0):
                for event in event_arr:
                    self.event_queue\
                        .append(event)

    def render(self)->list[dict]:
        """
        Función que recorre los objetos 
        del escenario llamando a su método 
        to_pod_image encargado de 
        prerrenderizar los objetos al 
        formato de objetos gráficos paint 
        order dictionary de imagenes POD 
        Image.
        # TODO: añadir la cam y que solo
        prerrenderize el scenario de la cam
        """
        # renderiza objetos
        pod_array = self.capture_frame()
        # renderiza una matrix de lineas
        # para el tablero de celdas
        poly_matrix = Btpy.polygon_matrix(
            self.size_celd, 
            self.cam_size,
            self.cam_size
        )
        pod_poly = Tkupg.pod_polygon_line(
            poly_matrix)
        # retorna el formato renderizado
        pod_array.append(pod_poly)
        return pod_array
    
    def capture_frame(self):
        """
        Función que renderiza todos los 
        objetos que se encuentran en el 
        espacio determinado por la 
        expansión de la cámara.
        """
        go = None
        pod_array = []
        pod = None
        is_in_space = False
        for k in self.go_dict:
            go = self.go_dict[k]
            is_in_space = Btpy\
                .point_in_space(
                go.point_index,
                [self.cam_location[0], 
                 self.cam_location[0] + self.cam_size],
                [self.cam_location[1], 
                 self.cam_location[1] + self.cam_size])
            if(is_in_space):
                pod = go.to_pod_image()
                pod_array.append(pod)
                # ajusta la locacion
                pod["point"] = Btpy.map(
                    pod["point"].copy(),
                    lambda e:abs(e*self.size_celd)
                )
        return pod_array
    
    def __move_in_matrix(self, id, sum_point):
        """
        Función que mueve un objeto hacia 
        un Point determinado siempre que 
        el Point no esté ocupado.
        """
        # calcula el destino
        go = self.__get_go(id)
        destiny_point = Btpy.move_point(
            go.point_index, 
            sum_point,
            self.space.range_x, 
            self.space.range_y
        )
        # verifica si el destino esta vacio
        if(self.__some_is_in(destiny_point)):
            # detectar colision con el fallo
            go_destiny = self.__get_go_in(destiny_point)
            if(go_destiny
               .family == "resource"):
                go_destiny.launch_die()
                self.__set_go(go_destiny)
            return None
        go.point_index = destiny_point
        self.__set_go(go)
        
    def __get_go_in(self, point):
        e = None
        for k in self.go_dict:
            e = self.go_dict[k]
            if(e.point_index == point):
                return e
    
    def __get_go(self, name):
        return self.go_dict[name]
    
    def __delete_go(self, name):
        del(self.go_dict[name])

    def __some_is_in(self, point):
        """
        Función que busca en el 
        diccionario si algún objeto se 
        encuentra en el punto de la matriz.
        """
        e = None
        for k in self.go_dict:
            e = self.go_dict[k]
            if(e.point_index == point):
                return True
        return False

    def __set_go(self, go):
        self.go_dict[go.name] = go

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
                r_point = Btpy.move_point(
                    point,
                    sum_point,
                    self.space.range_x,
                    self.space.range_y
                )
                if(not self.__some_is_in(
                    r_point)):
                    return r_point
        raise Exception("not exist space")
            

    
