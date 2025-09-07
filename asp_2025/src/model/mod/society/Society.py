


from ...mod.citizen.Citizen import Citizen
import random
from .society_constant import*
from btpy.Btpy import Btpy
from ..graveyard.Graveyard import Graveyard

class Society:

    def __init__(self):
        self.citizen_list:list = []
        self.region_point = [0, 0]
        self.__key_size:str = ""

    def set_region_point(self, 
                POINT:list[int]):
        self.region_point = POINT

    def get_key_size(self)->str:
        return self.__key_size

    def __update_size_key(self)->str:
        size:int = self.get_size()
        self.key_size = Btpy.whats_range(
            SOCIETY_SIZE_RANGE_DICT,
            size
        )

    def get_size(self)->int:
        return len(self.citizen_list)
    
    def set_citizen(self, citizen):
        if(self.has_citizen(citizen)):
            self.__replace_citizen(citizen)
        else:
            self.__add_citizen(citizen)

    def __add_citizen(self, citizen:Citizen):
        self.citizen_list.append(citizen)

    def get_citizen_id_list(self)->list[int]:
        """
        Funcion que obtiene una lista
        de todos los numeros ID de los
        citizen en la lista.
        """
        citizen:Citizen = None
        id_list:list[int] = []
        for i in range(self.get_size()):
            citizen = self.citizen_list[i]
            id_list.append(
                citizen.get_id_number()
            )
        return id_list

    def has_citizen(self, citizen_seek
            :Citizen)\
            ->bool:
        """
        Funcion que retorna verdadero
        si existe un citizen con el numero
        indicado y retorna false si no.
        """
        number:int = citizen_seek\
            .get_id_number()
        citizen:Citizen = None
        for i in range(self.get_size()):
            citizen = self\
                .citizen_list[i]
            if(citizen.get_id_number() \
                        == number):
                return True
        return False
    
    def update_let_go_children(self, 
                citizen:Citizen):
        """
        Funcion que verifica si el
        ciudadano tiene verdadero en la
        flag is_a_mother; si lo es 
        entonces si el citizen hijo
        del citizen madre es de rango de 
        edad "adolecent" este añade 
        el citizen hijo como un citizen
        independiente.
        """
        let_go_children:bool = citizen\
            .time_to_let_go_children()
        new_citizen = None
        if(let_go_children):
            new_citizen_list = citizen\
                .let_go_children()
            for new_citizen in new_citizen_list:
                self.set_citizen(
                    new_citizen)
        return citizen
    
    def socialize_citizen(self, 
                citizen_main:Citizen):
        """
        Funcion que ejecuta las 
        interacciones sociales entre todos 
        los ciudadanos de la region.
        """
        citizen_list_ = self\
            .get_citizen_outside()
        main_id = citizen_main\
            .get_id_number()
        for i, citizen in enumerate(
                citizen_list_):
            if(citizen.get_id_number() 
                    == main_id):
                continue
            citizen_list_[i] \
                = citizen_main.socialize(
                    citizen_list_[i]
                )
            self.set_citizen(
                citizen_list_[i])
        return citizen_main
    
    def get_citizen_outside(self):
        """
        Funcion que obtiene una lista
        de los ciudadanos que tienen
        en falso la flag is_inside;
        esto significa que estan 
        al aire libre.
        """
        citizen:Citizen = None
        is_inside:int = 0
        outside_list:list[Citizen] = []
        for i in range(self.get_size()):
            citizen = self.citizen_list[i]
            is_inside = citizen\
                .data.get_is_inside()
            if(not is_inside):
                outside_list.append(
                    citizen) 
        return outside_list
    
    def advance_one_day(self, market,
            is_pay_day:bool, postcard):
        """
        Funcion que avansa un dia
        en el tiempo del simulador para
        todos los ciudadanos en la 
        sociedad.
        """
        market = self.__update_all_citizens(
            market, is_pay_day, postcard)
        self.__update_size_key()
        return market

    def __update_all_citizens(self, 
            market, is_pay_day, postcard):
        """
        Funcion que itera por la lista
        de ciudadanos en la sociedad
        para ejecutar todos sus 
        comportamientos predeterminados
        por ciclo.
        """
        dead_id_list = []
        def fn(citizen):
            nonlocal market
            market = citizen.advance_one_month(
                market, 
                is_pay_day, 
                postcard
            )
            citizen = self\
                .update_let_go_children(
                    citizen
                )
            citizen = self.socialize_citizen(
                citizen)
            if(citizen.data.get_is_dead()):
                dead_id_list.append(
                    citizen.get_id_number()
                )
            return citizen
        self.foreach(fn)
        self.collects_dead_citizens(
            dead_id_list
        )
        return market

    def collects_dead_citizens(self, 
                id_list):
        """
        Funcion que recorre toda 
        la ciudadanos para eliminar a los
        ciudadanos con la flag is_dead
        activada(en verdadero).
        Tambien agrega la informacion
        de cada ciudadano muerto al
        epitafio.
        """
        index_list:list[int] = []
        id_ = 0
        leng = len(self.citizen_list)
        citz = None
        for i in range(leng -1):
            id_ = self.citizen_list[i]\
               .get_id_number()
            if(id_ in id_list):
                citz:Citizen = self\
                    .citizen_list[i]
                self.add_epitaph(citz)
                index_list.append(i)
        # Es importante que realize
        # este ordenamiento de mayor
        # a menor para que no ocurran
        # errores al borrar elementos
        # en la lista.
        index_list.sort(reverse=True)
        for index in index_list:
            del(self.citizen_list[index])

    def add_epitaph(self, citizen:Citizen):
        Graveyard.set_id(
            citizen.data.get_id_number()
        )
        Graveyard.set_cause_death_key(
            citizen.data.get_cause_death_key()
        )
        Graveyard.set_specific_death(
            citizen.data.specific_cause_death
        )
        Graveyard.set_full_name(
            citizen.get_full_name()
        )
        Graveyard.set_culture_key(
            citizen.data.get_culture_key()
        )
        Graveyard.set_year(
            citizen.data.date_asp\
                .get_year()
        )
        Graveyard.save_epitaph()

    def foreach(self, function_argsx1):
        for i in range(self.get_size()):
            self.citizen_list[i] \
                = function_argsx1(
                    self.citizen_list[i]
                )

    def __replace_citizen(self, 
            new_citizen:Citizen):
        """
        Funcion que remplaza la instancia 
        del citizen almacenado con un 
        codigo unico por un nuevo citizen
        con el mismo codigo.
        """
        n = new_citizen.get_id_number()
        citizen:Citizen = None
        for i in range(self.get_size()):
            citizen = self.citizen_list[i]
            if(citizen.get_id_number() == n):
                self.citizen_list[i]\
                    = new_citizen
                
    def get_citizen(self, number:int)\
            ->None:
        """
        Funcion que busca el ciudadano 
        con el numero unico enviado.
        """
        citizen:Citizen = None
        for i in range(self.get_size()):
            citizen = self.citizen_list[i]
            citizen_number = citizen\
                .get_id_number()
            if(citizen_number == number):
                return self.citizen_list[i]
        return None

    def populate_society(self, QUANTITY:int, 
            CULTURE_KEY:str,
            postcard):
        """
        Funcion que crea una cantidad
        de ciudadanos en la lista de la 
        poblacion con la cultura 
        determinada. Las claves de cultura 
        son:
        * "russian",
        * "american",
        * "english",
        * "arab",
        * "french",
        * "afrikan",
        * "nordic",
        * "indian",
        * "spanish",
        * "turkish",
        * "chinese",
        * "japanese",
        * "polinesian",
        * "italic",
        * "slavic",
        * "hebrew"
        """
        self.create_legendary_citizens(
            5, CULTURE_KEY, "female",
            postcard
        )
        self.create_legendary_citizens(
            5, CULTURE_KEY, "male",
            postcard
        )

    def create_legendary_citizens(self, 
            QUANTITY:int, 
            CULTURE_KEY:str, 
            GENDER:str,
            postcard):
        """
        Funcion que crea una cantidad
        de ciudadanos en la lista de la 
        poblacion con la cultura 
        determinada. Las claves de cultura 
        son:
        * "russian",
        * "american",
        * "english",
        * "arab",
        * "french",
        * "afrikan",
        * "nordic",
        * "indian",
        * "spanish",
        * "turkish",
        * "chinese",
        * "japanese",
        * "polinesian",
        * "italic",
        * "slavic",
        * "hebrew"
        """
        citizen = None
        for i in range(QUANTITY):
            citizen = Citizen()
            citizen.data.set_is_legendary(
                True)
            citizen.randomize_legendary(
                CULTURE_KEY,
                GENDER,
                postcard
            )
            citizen.set_origin_region_point(
                self.region_point)
            citizen.set_actual_region_point(
                self.region_point)
            self.citizen_list.append(
                citizen
            )

    def write(self)->str:
        """
        Funcion que escribe un texto
        con al informacion principal
        de todos los ciudadanos en la 
        sociedad.
        """
        txt = ""
        citizen:Citizen = None
        for citizen in self.citizen_list:
            txt += f"{citizen.write()}\n\n"
        return txt

