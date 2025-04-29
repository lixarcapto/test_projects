



from ..game_object.GameObject import GameObject
from ....btpy_checkers.mod.is_colliding_rect.is_colliding_rect import*
from ....btpy_maths.mod.translade_point.translade_point import*

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

    def get_cam_rect(self):
        return { 
            "x":self.cam_point_location[0],
            "y":self.cam_point_location[1],
            "width":self.cam_size_list[0],
            "height":self.cam_size_list[1]
        }

    def capture_object_render(self)->list:
        gobject:GameObject = None
        render_list:list[dict] = []
        cam_rect = self.get_cam_rect()
        is_colliding = False
        for k in self.__game_object_dict:
            gobject = self\
                .__game_object_dict[k]
            is_colliding = is_colliding_rect(
                gobject.get_rect_hitbox(),
                cam_rect
            )
            if(is_colliding):
                render_list.append(
                    gobject.get_render()
                )
        return render_list
    
    def translate_renders(self, render_list):
        for render in render_list:
            render["point"] \
                = translade_point(
                    render["point"],
                    self.cam_point_location
                )
        return render_list
            
    def get_render_list(self)\
            ->list[dict]:
        render_list = self\
            .capture_object_render()
        return self.translate_renders(
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
        is_colliding = False
        for k1 in gog_dict:
            gog_actual = gog_dict[k1]
            for k2 in gog_dict:
                if(k2 == k1): continue
                gog_review = gog_dict[k2]
                is_colliding = gog_review\
                    .detect_collision(
                        gog_actual
                    )
                if(is_colliding):
                    gog_review.add_collision(
                        gog_actual)
                    gog_actual.add_collision(
                        gog_review)
                
        
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