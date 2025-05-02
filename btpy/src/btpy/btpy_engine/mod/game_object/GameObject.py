

from ....btpy_maths.mod\
    .sum_in_range.sum_in_range import*
from ....btpy_maths.mod.vector_sum\
    .vector_sum import*
from ....btpy_checkers.mod\
    .is_colliding_rect.is_colliding_rect import*
from ....btpy_const.mod.sense.Sense import Sense
from ....btpy_utilitys.mod.iterator.Iterator import Iterator
from ....btpy_maths.mod.vector_sum.vector_sum import*
from ....btpy_maths.mod.adjusts_to_threshold.adjusts_to_threshold import*
from ....btpy_const.mod.sense.Sense import Sense
import random

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
    acceleration_factor:float = 0.2

    def __init__(self, ID:str = ""):
        # IDENTITY ------------------------
        self.__id:str = ""
        self.__key_class:str = ""
        self.__group_key:str = ""
        # ---------------------------------
        # SPACE PROPERTIES ----------------
        self.__location_point\
            :list[int] = [0, 0]
        self.__mass:int = 4
        self.__speed_point\
            :list[int] = [0, 0]
        # TODO: indica un eje Z para
        # colisiones.
        self.__z_axis:int = 0
        self.__hitbox_size_list\
            :list[int] = [50, 50]
        # ---------------------------------
        # BEHAVIOR FLAGS ------------------
        self.__stance_key:str = ""
        self.__is_alive:bool = True
        self.__is_mortal:bool = False
        self.__has_cam_focus:bool \
            = False 
        self.__has_acceleration:bool \
            = False
        self.__has_air_resistance\
            :bool = False
        self.__is_destructible:bool = False
        self.__has_gravity:bool = False
        self.__is_a_walker:bool = False
        # is_solid indica si el objeto
        # se detendra ante las colisiones.
        self.__is_solid:bool = True
        # is_collidable indica si el
        # objeto detectara las colisiones.
        self.__is_collidable:bool = True
        # ---------------------------------
        # BEHAVIOR VALUES -----------------
        self.__life_time:int = 0
        self.__health:int = 0
        self.__maximum_lifespan:int = 0
        self.__pixel_weight:int = 5
        self.__acceleration_point\
            :list[int] = [0, 0]
        self.air_resistance = 1
        # ---------------------------------
        # INNER ENGINE PROPERTIES ----------
        self.is_colliding:bool = False
        self.behavior_dict:dict = {}
        self.__event_list = []
        # los event del event list son
        # dict con la clave name y 
        # las demas son claves para 
        # el evento asociadas.
        # ---------------------------------
        # GRAPHIC PROPERTIES --------------
        # layer indica la capa de
        # renderizado del objeto.
        self.__layer:int = 0
        self.__animation_list_dict:dict = {}
        self.__image_list_key:str = ""
        # este iterador sirve para 
        # crear el sistema de animaciones
        self.__iterator_image = Iterator()
        self.__iterator_image\
            .set_is_cycle(True)
        # ---------------------------------
        # I don't know what this is
        self.colliding_id_set:set = set()
        # CALLS -------------------------
        self.set_id(ID)
        # --------------------------------

    # -----------------------------------

    # PUBLIC -----------------------------

    def set_is_a_walker(self, BOOL:bool)\
            ->None:
        """
        Funcion que asigna un 
        comportamiento de caminante tonto
        al objeto. Esto significa que el
        objeto se movera en una direccion
        aleatoria siempre que este
        detenido o por detenerse.
        """
        self.__is_a_walker = BOOL

    def get_is_a_walker(self)->bool:
        return self.__is_a_walker

    def get_has_air_resistance(self):
        return self.__has_air_resistance
    
    def set_has_air_resistance(self, 
                BOOL:bool):
        self.__has_air_resistance = BOOL

    def extract_event_list(self):
        event_list = self.__event_list
        self.__event_list = []
        return event_list
    
    def launch_spawn(self, KEY_CLASS):
        event = {
            "TYPE":"SPAWN",
            "ID":self.get_id(),
            "KEY_CLASS":KEY_CLASS
        }
        self.__event_list.append(event)

    def set_mass(self, PIXEL_MASS:int)\
            ->None:
        self.__mass = PIXEL_MASS

    def get_mass(self)->int:
        return self.__mass

    def set_is_destructible(self, 
            BOOL_VALUE:bool)->bool:
        self.__is_destructible = BOOL_VALUE
    
    def get_is_destructible(self)->bool:
        return self.__is_destructible
    
    def set_health(self, 
            HEALTH_POINTS:int)->None:
        self.__health = HEALTH_POINTS

    def get_health(self)->int:
        return self.__health

    def set_stance_key(self,
            STANCE_KEY:str):
        """
        Funcion que asigna una clave de 
        estado de tipo stance o postura;
        esta clave sirve para manejar
        estados del objeto.
        """
        self.__stance_key = STANCE_KEY

    def get_stance_key(self)->str:
        return self.__stance_key

    def set_key_class(self, KEY:str)->None:
        """
        Funcion que asigna una clave que
        identifica a la clase de gameobject
        a la que pertenece.
        """
        self.__key_class = KEY

    def get_key_class(self)->str:
        return self.__key_class

    def get_speed_point(self)->list[int]:
        return self.__speed_point

    def set_has_acceleration(self,
            BOOL:bool)  \
            ->None:
        self.__has_acceleration = BOOL

    def get_has_acceleration(self)->bool:
        return self.__has_acceleration
    
    def get_acceleration_point(self)\
            ->list[int]:
        return self.__acceleration_point

    def set_has_gravity(self, BOOL:bool)\
            ->None:
        self.__has_gravity = BOOL

    def get_has_gravity(self)->bool:
        return self.__has_gravity

    def set_pixel_weight(self, 
            PIXEL_SIZE:int)->None:
        self.__pixel_weight = PIXEL_SIZE

    def get_pixel_weight(self)->int:
        return self.__pixel_weight

    def get_speed_point(self)\
            ->list[int]:
        return self.__speed_point

    def set_has_cam_focus(self,
            BOOL:bool)->None:
        self.__has_cam_focus = BOOL

    def get_has_cam_focus(self)->bool:
        return self.__has_cam_focus

    def set_group_key(self, GROUP_KEY:str)\
            ->None:
        """
        Funcion que asigna una clave de 
        grupo que sirve para clasificar
        los gameobject en grupos.
        """
        self.__group_key = GROUP_KEY\
            .upper()
    
    def get_group_key(self)->str:
        return self.__group_key

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

    def is_stopped(self)->bool:
        STOPPING_SPEED = 3
        speed_p = self.__speed_point
        if(speed_p[0] <= STOPPING_SPEED
        and speed_p[1] <= STOPPING_SPEED):
            return True
        return False  

    def simulate_random_walk(self, speed):
        if(not self.is_stopped()):
            return None
        sense_key_list = list(Sense\
            .CARDINAL_DICT.keys())
        sense_k = random.choice(
            sense_key_list
        )
        p_sense = Sense.CARDINAL_DICT\
            [sense_k]
        p_result = list(map(
            lambda e:e*speed, 
            p_sense
        ))
        self.sum_force(p_result)

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
        self.__location_point = POINT_LIST

    def get_location(self)->list[int]:
        return self.__location_point.copy()

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
            "point": self.__location_point
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
            "x":self.__location_point[0],
            "y":self.__location_point[1],
            "width":self.__hitbox_size_list[0],
            "height":self.__hitbox_size_list[1]
        }

    def detect_collision(self,
            game_object)->bool:
        return is_colliding_rect(
                self.__get_future_rect_hitbox(),
                game_object.get_rect_hitbox()
            )
    
    def add_border_collision(self, 
            BORDER_KEY):
        self.is_colliding = True
        self.colliding_id_set.add(
            BORDER_KEY)
        
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
        
    def sum_force(self, 
            vector_list:list[int]):
        self.__speed_point = vector_sum(
            self.__speed_point, vector_list)
        # calcula la aceleracion
        accel_p:list[int] = [0, 0]
        accel_p[0] = round(
            self.__speed_point[0] 
            / self.__mass)
        accel_p[1] = round(
            self.__speed_point[1] 
            / self.__mass)
        self.__acceleration_point = accel_p

    def update(self):
        self.__next_animation_frame()
        if(self.__is_mortal):
            self.__simulate_lifespan()
        if(self.__has_gravity):
            self.__simulate_gravity()
        if(self.__has_acceleration):
            self.__simulate_acceleration()
        if(self.__has_air_resistance):
            self.__simulate_air_resistance()
        if(self.__is_destructible):
            self.__simulate_destruction()
        if(self.__is_a_walker):
            self.simulate_random_walk(3)
        if(self.is_colliding
        and self.__is_collidable):
            self.__stop_movement()
        else:
            self.__move_object()

    def free(self)->None:
        self.is_colliding = False
        self.colliding_id_set = set()

    # ------------------------------------

    # PRIVATE ----------------------------

    def __next_animation_frame(self)->None:
        """
        Funcion que avansa a la siguiente
        imagen(Frame) de la lista de 
        imagenes de la animacion 
        seleccionada actualmente.
        """
        if(self.__image_list_key == ""):
            return None
        self.__iterator_image.next()

    def __simulate_gravity(self):
        force = [0, self.__pixel_weight]
        self.sum_force(force)

    def __simulate_destruction(self):
        if(self.__health <= 0):
            self.__is_alive = False
        
    def __get_future_rect_hitbox(self)\
            ->dict:
        """
        Crea un rect box del hitbox del
        objeto que predice el movimiento
        futuro del objeto para detectar
        la colision antes de que se mueva.
        Esto evita que se atasque con
        el otro objeto colisionable.
        """
        point = self.__get_next_move_point()
        return { 
            "x":point[0],
            "y":point[1],
            "width":self.__hitbox_size_list[0],
            "height":self.__hitbox_size_list[1]
        }

    def __simulate_lifespan(self):
        self.__life_time = sum_in_range(
            self.__life_time,
            +1,
            [0, self.__maximum_lifespan]
        )
        if(self.__life_time \
                == self.__maximum_lifespan):
            self.__is_alive = False

    def __move_object(self):
        future_point = self\
            .__get_next_move_point()
        collides_with_border = self\
            .__collides_width_border(
                future_point)
        if(not collides_with_border):
            self.__location_point \
                = future_point
        else:
            self.__stop_movement()

    def __simulate_air_resistance(self):
        self.__speed_point = self\
            .__apply_air_resistence_in_point(
                self.__speed_point
            )
        self.__acceleration_point = self\
            .__apply_air_resistence_in_point(
                self.__acceleration_point
            )

    def __apply_air_resistence_in_point(self,
                POINT):
        new_point = [0, 0]
        new_point[0] = adjusts_to_threshold(
            POINT[0],
            self.air_resistance,
            0
        )
        new_point[1] = adjusts_to_threshold(
            POINT[1],
            self.air_resistance,
            0
        )
        return new_point


    def __collides_width_border(self,
                future_point:list[int]):
        if(self.scenario_width 
           == future_point[0]):
            self.add_border_collision(
                "BORDER_RIGHT"
            )
            return True
        elif(0 == future_point[0]):
            self.add_border_collision(
                "BORDER_LEFT"
            )
            return True
        elif(self.scenario_height
                == future_point[1]):
            self.add_border_collision(
                "BORDER_DOWN"
            )
            return True
        elif(0 == future_point[1]):
            self.add_border_collision(
                "BORDER_TOP"
            )
            return True
        return False
        
    def __stop_movement(self):
        self.__speed_point = [0, 0]
        self.__acceleration_point = [0, 0]

    def __simulate_acceleration(self):
        self.__speed_point\
            = vector_sum(
                self.__speed_point,
                self.__acceleration_point
            )
        accel_p = self.__acceleration_point
        accel_p[0] += round(
            accel_p[0] \
            * self.acceleration_factor
        )
        accel_p[1] += round(
            accel_p[1] \
            * self.acceleration_factor
        )
        self.__acceleration_point = accel_p

    def __get_next_move_point(self)\
            ->list[int]:
        point = [0, 0]
        point[0] \
            = sum_in_range(
                self.__location_point[0],
                self.__speed_point[0],
                [0, self.scenario_width]
            )
        point[1] = sum_in_range(
            self.__location_point[1],
            self.__speed_point[1],
            [0, self.scenario_height]
        )
        return point

    # ----------------------------------------

    # PRIVATE ------------------------------

