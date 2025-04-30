

from ....btpy_maths.mod\
    .sum_in_range.sum_in_range import*
from ....btpy_maths.mod.vector_sum\
    .vector_sum import*
from ....btpy_checkers.mod\
    .is_colliding_rect.is_colliding_rect import*
from ....btpy_const.mod.sense.Sense import Sense
from ....btpy_utilitys.mod.iterator.Iterator import Iterator

class GameObject:

    """
    Esta clase sirve para crear un 
    gameobject; un gameboject es un 
    objeto con volumen que puede
    desplazarse y ocupar espacio en un
    escenario de simulacion(Scenario).
    """

    default_image_path:str = ""
    scenario_width:int = 0
    scenario_height:int = 0
    last_number_id:int = 0

    def __init__(self, ID:str = ""):
        self.__id:str = ""
        self.point_location\
            :list[int] = [0, 0]
        self.point_motion\
            :list[int] = [0, 0]
        self.key_class:str = ""
        self.pose_key:str = ""
        self.group_key:str = ""
        # TODO: indica un eje Z para
        # colisiones.
        self.__z_axis = 0
        # layer indica la capa de
        # renderizado del objeto.
        self.__layer:int = 0
        self.__animation_list_dict = {}
        self.__image_list_key:str = ""
        # este iterador sirve para 
        # crear el sistema de animaciones
        self.__iterator_image = Iterator()
        self.__iterator_image\
            .set_is_cycle(True)
        self.__hitbox_size_list\
            :list[int] = [50, 50]
        self.behavior_dict:dict = {}
        self.colliding_id_set:set = set()
        self.__is_alive = True
        self.__is_mortal = False
        self.__maximum_lifespan:int = 0
        self.__life_time:int = 0
        self.is_colliding = False
        # is_solid indica si el objeto
        # se detendra ante las colisiones.
        self.__is_solid:bool = True
        # is_collidable indica si el
        # objeto detectara las colisiones.
        self.__is_collidable:bool = True
        # CALLS -------------------------
        self.set_id(ID)

    # -----------------------------------

    # PUBLIC -----------------------------

    def get_is_alive(self)->bool:
        """
        Indica si el objeto se encuentra
        vivo actualmente; si es false
        sera destruido por el motor
        al terminar el ciclo.
        """
        return self.__is_alive

    def set_is_mortal(self, BOOL:bool,
            MAXIMUM_LIFESPAN:int = 0):
        """
        Esta funcion asigna la propiedad
        is_mortal al objeto; esta propiedad
        indica que el objeto morira al 
        llegar a su tiempo de vida maximo.
        El tiempo inicial de vida es cero.
        """
        self.__is_mortal = BOOL
        self.__life_time = 0
        self.set_maximum_lifespan(
            MAXIMUM_LIFESPAN
        )
        

    def get_is_mortal(self)->bool:
        return self.__is_mortal

    def set_maximum_lifespan(self, 
            LIFESPAN:int):
        self.__maximum_lifespan = LIFESPAN

    def get_maximum_lifespan(self)->int:
        return self.__maximum_lifespan
    
    def get_life_time(self)->int:
        return self.__life_time

    def set_layer(self, LAYER_NUMBER:int):
        """
        Funcion que asigna una capa de 
        dibujado al objeto para designar
        un orden de renderizado.
        """
        self.__layer = LAYER_NUMBER

    def get_layer(self)->int:
        return self.__layer

    def set_is_collidable(self, BOOL:bool)\
            ->None:
        """
        Funcion que asigna un estado
        is_collidable al objeto. Si este
        estado es verdadero el objeto
        podra colisionar con otros objetos
        y almacenar las colisiones; pero
        no sera detenido por la colision.
        """
        self.__is_collidable = BOOL

    def get_is_collidable(self)->bool:
        return self.__is_collidable

    def set_is_solid(self, BOOL:bool)\
            ->None:
        """
        Funcion que asigna un estado 
        de solido al objeto; esto 
        hace que el objeto se detenga
        ante las colisiones. Si se asigna
        como solido obligatoriamente sera
        asignado como is_collidable para 
        que funcione la propiedad.
        """
        self.__is_solid = BOOL
        if(self.__is_solid):
            self.set_is_collidable = True

    def get_is_solid(self)->bool:
        return self.__is_solid

    def set_location(self, POINT_LIST):
        self.point_location = POINT_LIST

    def get_location(self)->list[int]:
        return self.point_location.copy()

    def set_hitbox_size(self, WIDTH:int, 
            HEIGHT:int)->None:
        """
        Funcion que ajusta un tamaño
        determinado al hitbox o area
        de colision en forma
        de una lista numerica de tamaño
        x2.
        """
        self.__hitbox_size_list \
            = [WIDTH, HEIGHT]
        
    def get_hitbox_size(self)->list[int]:
        """
        Funcion que obtiene el tamaño 
        del hitbox del objeto en forma
        de una lista numerica de tamaño
        x2.
        """
        return self.__hitbox_size_list

    def get_id(self)->str:
        """
        Funcion que obtiene el ID unico
        del gameobject.
        """
        return self.__id

    def set_id(self, ID:str)->None:
        """
        Funcion que crea un identificador
        unico para llamar al objeto
        desde el escenario. Si el ID es 
        void string crea uno automatica-
        mente.
        """
        if(ID == ""):
            self.__id = str(GameObject\
                .last_number_id)
            GameObject.last_number_id += 1
        else:
            self.__id = ID

    # PUBLIC STATIC
    def set_scenario_size(
            RANGE_LIST_SIZE:list[int])\
            ->None:
        """
        Funcion que ajusta un tamaño
        determinado al scenario donde
        se desplazan los gameobject.
        """
        GameObject.scenario_width \
            = RANGE_LIST_SIZE[0]
        GameObject.scenario_height \
            = RANGE_LIST_SIZE[1]

    def add_behavior(self, KEY:str,
            FUNCTION_ARGS_X1:callable)\
            ->None:
        """
        Funcion que agrega un 
        comportamiento a el objeto
        utilizando una callback que 
        recibe como argumento una instancia
        de este mismo objeto que puede
        ser modificada.
        """
        self.behavior_dict[KEY] \
            = FUNCTION_ARGS_X1
        
    def get_render(self)->dict:
        leng = self.__iterator_image\
            .get_size()
        image_key:str = ""
        if(leng != 0):
            image_key = self\
                .__iterator_image.get()
        else:
            image_key = self\
                .default_image_path
        return {
            "image_key": image_key,
            "point": self.point_location
        }
        
    def set_animation_list(self, 
                KEY:str, 
                IMAGE_LIST:list[str])\
                ->None:
        """
        Funcion que asigna una lista 
        de rutas de imagenes que seran
        utilizadas como una animacion
        al renderizar el objeto. Cada
        ciclo del motor desplazara la 
        imagen actual en la lista en 
        un ciclo infinito. La clave sirve
        para identificar la animacion 
        y poder cambiarla cuando se desee.
        """
        if(isinstance(IMAGE_LIST, list)):
            self.__animation_list_dict[KEY]\
                = IMAGE_LIST
        elif(isinstance(IMAGE_LIST, str)):
            self.__animation_list_dict[KEY]\
                = [IMAGE_LIST]
        if(self.__image_list_key == ""):
            self.select_actual_animation(KEY)
        
    def next_animation_frame(self)->None:
        """
        Funcion que avansa a la siguiente
        imagen(Frame) de la lista de 
        imagenes de la animacion 
        seleccionada actualmente.
        """
        if(self.__image_list_key == ""):
            return None
        self.__iterator_image.next()
        
    def select_actual_animation(self, 
            KEY:str)\
            ->None:
        """
        Funcion que selecciona una de 
        las animaciones almacenadas
        en el objeto para reproducirla.
        La animation inicia desde el
        primer frame de la nueva
        animacion.
        """
        self.__image_list_key = KEY
        image_list = self\
            .__animation_list_dict[KEY]
        self.__iterator_image\
            .set_list(image_list)

    def get_rect_hitbox(self)->dict[int]:
        """
        Funcion que obtiene un 
        rectangulo en formato
        diccionario con los datos 
        del hitbox del objeto.
        """
        return { 
            "x":self.point_location[0],
            "y":self.point_location[1],
            "width":self.__hitbox_size_list[0],
            "height":self.__hitbox_size_list[1]
        }
    
    def get_future_rect_hitbox(self)->dict:
        """
        Crea un rect box del hitbox del
        objeto que predice el movimiento
        futuro del objeto para detectar
        la colision antes de que se mueva.
        Esto evita que se atasque con
        el otro objeto colisionable.
        """
        point = self.get_next_move_point()
        return { 
            "x":point[0],
            "y":point[1],
            "width":self.__hitbox_size_list[0],
            "height":self.__hitbox_size_list[1]
        }
        
    def detect_collision(self,
            game_object)->bool:
        return is_colliding_rect(
                self.get_future_rect_hitbox(),
                game_object.get_rect_hitbox()
            )
    
    def add_collision(self, game_object):
        self.is_colliding = True
        self.colliding_id_set.add(
            game_object.get_id()
        )

    def move_left(self, speed):
        self.sum_force([speed *-1, 0])

    def move_right(self, speed:int):
        self.sum_force([speed, 0])

    def move_up(self, speed:int):
        self.sum_force([0, speed *-1])

    def move_down(self, speed:int):
        self.sum_force([0, speed])
        
    def sum_force(self, vector_list:list[int]):
        self.point_motion = vector_sum(
            self.point_motion, vector_list)

    def advance_lifespan(self):
        self.__life_time = sum_in_range(
            self.__life_time,
            +1,
            [0, self.__maximum_lifespan]
        )
        if(self.__life_time \
                == self.__maximum_lifespan):
            self.__is_alive = False

    def update(self):
        self.next_animation_frame()
        if(self.__is_mortal):
            self.advance_lifespan()
        if(self.is_colliding
        and self.__is_collidable):
            self.point_motion = [0, 0]
        else:
            self.__move_object()

    def __move_object(self):
        self.point_location = self\
            .get_next_move_point()

    def get_next_move_point(self)\
            ->list[int]:
        point = [0, 0]
        point[0] \
            = sum_in_range(
                self.point_location[0],
                self.point_motion[0],
                [0, self.scenario_width]
            )
        point[1] = sum_in_range(
            self.point_location[1],
            self.point_motion[1],
            [0, self.scenario_height]
        )
        return point

    def free(self)->None:
        self.is_colliding = False
        self.colliding_id_set = set()

    # ----------------------------------------

    # PRIVATE ------------------------------

