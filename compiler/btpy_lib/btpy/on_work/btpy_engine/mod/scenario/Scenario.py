

from ..gobject.GObject import GObject

class Scenario:

    """
    Clase que representa un escenario para
    videojuegos o simuladores.
    """

    GObject = GObject

    def __init__(self) -> None:
        self.__gobject_list:GObject = []
        self.__resource_folder = ""
        self.__image_format = "png"
        self.__size_x = 0
        self.__size_y = 0

    # ACCESSORS----------------------------

    def set_resource_folder(self, ROUTE:str):
        self.__resource_folder = ROUTE

    def get_resource_folder(self):
        return self.__resource_folder

    def set_image_format(self, EXTENSION:str):
        self.__image_format = EXTENSION

    def get_image_format(self):
        return self.__image_format

    def get(self, KEY_OBJECT:str)->GObject:
        """
        Obtiene un game object almacenado
        por su clave ID.
        """
        for i, e in enumerate(self.__gobject_list):
            if(e.get_id() == KEY_OBJECT):
                return e
        return None
                
    
    def set(self, GOBJECT:GObject)->None:
        """
        Almacena o remplaza un game 
        object existente.
        """
        if(self.has(GOBJECT.get_id())):
            self.replace(GOBJECT)
        else:
            self.__add(GOBJECT)
        
    def replace(self, GOBJECT:GObject)->None:
        """
        Remplaza un game object existente.
        """
        for i, e in enumerate(self.__gobject_list):
            if(e.get_id() == GOBJECT.get_id()):
                self.__gobject_list[i]\
                    = GOBJECT
                break

    def has(self, KEY_OBJECT:str)->bool:
        """
        Revisa si existe el game object
        con la clave ID enviada.
        """
        for e in self.__gobject_list:
            if(e.get_id() == KEY_OBJECT):
                return True
        return False
    
    # MUTATORS------------------------------

    def set_size(self, 
            SIZE_X:int, SIZE_Y:int)->None:
        """
        Asigna un tamanio maximo 
        al escenario.
        """
        self.__size_x = SIZE_X
        self.__size_y = SIZE_Y

    def render(self)->list[dict]:
        """
        Funcion que genera una lista de 
        imagenes layout en formato
        diccionario. Cada dict tiene 
        este formato:
        {
            "route_array":[]
            "point":[0,0]
        }
        """
        PATH_KEY = "route_array"
        LENG = len(self.__gobject_list)
        go = None
        image_dict_list = []
        image_dict = {}
        for i in range(LENG):
            go = self.__gobject_list[i]
            # obtiene los datos para pintado
            image_dict = go\
                .get_image_layout_dict()
            # completa la ruta de las 
            # imagenes
            image_dict[PATH_KEY] = self\
                .__complete_routes(
                image_dict[PATH_KEY])
            # añade los datos para pintado
            image_dict_list.append(
                image_dict
            )
        return image_dict_list

    def update(self)->None:
        self.__move()
        LENG = len(self.__gobject_list)
        for i in range(LENG):
            self.__gobject_list[i].update()
        self.__free()

    # PRIVATE------------------------------

    def __create_route(self, NAME:str):
        return self.__resource_folder\
            + "/" + NAME + "." \
            + self.__image_format

    def __complete_routes(self, 
            routes_arr):
        route = ""
        array = []
        for e in routes_arr:
            route = self.__create_route(
                e)
            array.append(route)
        return array

    def __free(self)->None:
        for i, go in enumerate(self.__gobject_list):
            go.free()
            self.__gobject_list[i] = go

    def __move(self)->None:
        for i, go in enumerate(self.__gobject_list):
            go.move(
                go.get_vector_arrow(),
                self.__size_x,
                self.__size_y,
                self.__gobject_list
            )
            self.__gobject_list[i] = go

    def __object_clicked_id(self, 
            POINT_CLICKED:list[int])->str:
        LENG = len(self.__gobject_list)
        go = None
        for i in range(LENG):
            go = self.__gobject_list[i]
            if(go.point_is_colliding(
                    POINT_CLICKED)):
                return go.get_id()
        return ""
    
    def __add(self, gobject:GObject)->None:
        self.__gobject_list.append(gobject)