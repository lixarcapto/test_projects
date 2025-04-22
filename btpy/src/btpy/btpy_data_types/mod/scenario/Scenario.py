



from ..game_object.GameObject import GameObject

class Scenario:

    """
    Clase que sirve como escenario
    conteniendo datos del espacio
    bidimensional y una lista de los
    game objects que contienen.
    """

    def __init__(self):
        self.__game_object_dict:dict = {}
        self.__width = 0
        self.__height = 0

    # ------------------------------------

    # PUBLIC ------------------------------

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
        return self.__game_object_list[KEY]
    
    def update(self)->None:
        gobject:GameObject = None
        self.detect_all_collisions()
        for k in self.__game_object_dict:
            gobject = self  \
                .__game_object_dict[k]
            gobject.update()
        self.__execute_all_behaviors()
        self.free_gobject()
            
    def get_render_list(self)\
            ->list[dict]:
        gobject:GameObject = None
        render_list:list[dict] = []
        for k in self.__game_object_dict:
            gobject = self\
                .__game_object_dict[k]
            render_list.append(
                gobject.get_render())
        return render_list
    
    def detect_all_collisions(self):
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