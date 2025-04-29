



from ..game_object.GameObject import GameObject
from ....btpy_checkers.mod.is_colliding_rect.is_colliding_rect import*
from ....btpy_maths.mod.translade_point.translade_point import*
from .sort_numbers_dict_descending import*

class Scenario:

    """
    Clase que sirve como escenario
    conteniendo datos del espacio
    bidimensional y una lista de los
    game objects que contienen.
    """

    def __init__(self):
        self.__game_object_dict:dict = {}
        self.__width:int = 0
        self.__height:int = 0
        self.cam_size_list = [300, 300]
        self.cam_point_location = [0, 0]

    # ------------------------------------

    # PUBLIC ------------------------------

    def set_cam_location(self, POINT):
        self.cam_point_location = POINT

    def center_cam_in(self, POINT):
        p_size = self.cam_size_list
        point_r = [0, 0]
        point_r[0] = POINT[0] \
            - round(p_size[0] / 2)
        point_r[1] = POINT[1] \
            - round(p_size[1] / 2)
        self.set_cam_location(point_r)

    def set_cam_size(self, SIZE_LIST):
        self.cam_size_list = SIZE_LIST

    def get_size_list(self)->list:
        return [
            self.__width, 
            self.__height
        ]

    def set_size(self, WIDTH:int, 
            HEIGHT:int)->None:
        self.__width = WIDTH
        self.__height = HEIGHT
        GameObject.set_scenario_size(
            [WIDTH, HEIGHT]
        )
    
    def set_gobject(self, 
            GAME_OBJECT:GameObject)->None:
        id_ = GAME_OBJECT.get_id()
        self.__game_object_dict\
            [id_] = GAME_OBJECT
    
    def has_gobject(self, KEY:str)\
            ->None:
        if(KEY in self.__game_object_dict):
            return True
        return False
        
    def remove_gobject(self, KEY:str):
        del(self.__game_object_dict[KEY])

    def get_gobject(self, KEY:str):
        return self.__game_object_dict[KEY]
    
    def update(self)->None:
        gobject:GameObject = None
        self.detect_all_collisions()
        for k in self.__game_object_dict:
            gobject = self  \
                .__game_object_dict[k]
            gobject.update()
        self.__execute_all_behaviors()
        self.free_gobject()

    def __get_cam_rect(self):
        return { 
            "x":self.cam_point_location[0],
            "y":self.cam_point_location[1],
            "width":self.cam_size_list[0],
            "height":self.cam_size_list[1]
        }

    def __detect_objects_on_cam(self)->list:
        gobject:GameObject = None
        objects_list:list[GameObject] = []
        cam_rect = self.__get_cam_rect()
        is_colliding = False
        for k in self.__game_object_dict:
            gobject = self\
                .__game_object_dict[k]
            is_colliding = is_colliding_rect(
                gobject.get_rect_hitbox(),
                cam_rect
            )
            if(is_colliding):
                objects_list.append(
                    gobject
                )
        return objects_list
    
    def __capture_render_objects(self,
            gobject_list):
        # obtener un diccionario con las 
        # capas de los objetos.
        layer_dict = {}
        render_list:list[dict] = []
        i = 0
        for gobject in gobject_list:
            layer_dict[str(i)]\
                = gobject.get_layer()
            i += 1
        key_list = sort_numbers_dict_descending(
            layer_dict
        )
        # renderiza los objetos en el
        # orden determinado por sus capas.
        render:dict = {}
        for key in key_list:
            render = gobject_list[int(key)]\
                .get_render()
            render_list.append(render)
        return render_list
    
    def __translate_renders(self, render_list):
        for render in render_list:
            render["point"] \
                = translade_point(
                    render["point"],
                    self.cam_point_location
                )
        return render_list
            
    def get_render_list(self)\
            ->list[dict]:
        gobject_list = self\
            .__detect_objects_on_cam()
        render_list = self\
            .__capture_render_objects(
                gobject_list
            )
        return self.__translate_renders(
            render_list
        )
    
    def detect_all_collisions(self):
        """
        Funcion que realiza una busqueda
        por todos los gameobject en el 
        scenario detectando cuales
        colisionaron y agregando los datos
        de la colision a cada gameobject.
        """
        gobject:GameObject = None
        gog_dict = self.__game_object_dict
        gog_actual:GameObject = None
        gog_review:GameObject = None
        is_colliding:bool = False
        is_collidable:bool = False
        for k1 in gog_dict:
            gog_actual = gog_dict[k1]
            is_collidable = gog_actual\
                .get_is_collidable()
            # ignora los objetos con
            # la propiedad is_collidable
            # en False
            if(not is_collidable):
                continue
            for k2 in gog_dict:
                if(k2 == k1): continue
                gog_review = gog_dict[k2]
                self.__activate_collisions(
                    gog_actual,
                    gog_review
                )
                
        
    def __activate_collisions(self, 
            gobject_1, gobject_2):
        is_colliding = gobject_1\
            .detect_collision(
                gobject_2
            )
        if(is_colliding):
            gobject_1.add_collision(
                    gobject_2
            )
            gobject_2.add_collision(
                gobject_1
            )

    def free_gobject(self):
        """
        Funcion que libera los datos
        temporales del objeto en cada 
        ciclo del motor, como los datos
        de colisiones.
        """
        gobject:GameObject = None
        for k in self.__game_object_dict:
            gobject = self\
                .__game_object_dict[k]
            gobject.free()
    
    # -------------------------------------
    
    # PRIVATE -----------------------------
    
    def __execute_all_behaviors(self):
        gobject:GameObject = None
        for k in self.__game_object_dict:
            gobject = self\
                .__game_object_dict[k]
            self.__execute_behaviors(
                    gobject)

    def __execute_behaviors(self, 
            game_object:callable):
        fn = None
        for k in game_object.behavior_dict:
            fn = game_object.behavior_dict\
                [k]
            fn(game_object)