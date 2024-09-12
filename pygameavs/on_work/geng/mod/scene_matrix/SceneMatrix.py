

from btpy.Btpy import Btpy
from tkupg.Tkupg import Tkupg
from .....src.go_factory.GoFactory import GoFactory

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
    
    

    def __update_objects(self):
        """
        Función que recorre los objetos de 
        la lista de objetos para actualizarlos
        """
        for k in self.go_dict:
            self.go_dict[k].update()
            print(self.go_dict[k].write())
        
    

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
    
    
    
    def __get_go(self, name):
        return self.go_dict[name]
    
    def __delete_go(self, name):
        del(self.go_dict[name])

    def __set_go(self, go):
        self.go_dict[go.name] = go

    
            

    
