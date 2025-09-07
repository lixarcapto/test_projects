


from ..character.Character import Character
import random
from btpy.src.btpy.Btpy import Btpy
from .society_const import*

def find_closest_lower(DICT, NUMBER):
    """
    funcion que identifique en un 
    diccionario de numeros que numero 
    es el mas cercano inferior al numero 
    enviado retornando su clave.
    """
    claves = sorted(DICT.keys())
    for clave in claves:
        if clave < NUMBER:
            continue
        else:
            if clave > NUMBER and claves.index(clave) > 0:
                return claves[claves.index(clave) - 1]
            else:
                return None



class Society:

    """
    Clase que representa a la sociedad
    donde interactuan los personajes.
    """

    def __init__(self):
        self.society_type:str = ""
        self.character_arr:list[Character] \
            = []
        
    def identify_type(self):
        
        self.society_type \
            = SOCIETY_KEY_DICT[""]

    def create_group(self, quantity:int,
            culture, region_number):
        """
        Crea un grupo de personajes.
        """
        for _ in range(quantity):
            self.create(culture, 
                region_number)
            
    def get_all_character_id(self)\
            ->list[int]:
        """
        Obtiene todos los ID de los
        caracteres en la lista.
        """
        array = []
        char:Character = None
        for char in self.character_arr:
            array.append(char.d.get_id())
        return array

    def makes_interactions(self):
        """
        Proboca interacciones y relaciones
        entre los personajes.
        """
        # obtiene los character outside
        outside_index = []
        char:Character = None
        char_destiny:Character = None
        i_destiny = 0
        for i, char in enumerate(self.character_arr):
            if(char.d.get_is_outside()):
                outside_index.append(i)
        for index in outside_index:#
            char = self.character_arr[index]
            # elige un personaje destino
            # aleatorio
            i_destiny = Btpy.random_choice(
                outside_index)
            char_destiny = self\
                .character_arr[i_destiny]
            # relaciona los personajes
            char.relate(char_destiny)
            char_destiny.relate(char)
            # actualiza los personajes
            self.character_arr[i_destiny]\
                = char_destiny
            self.character_arr[index]\
                = char
            
    def write_narrative(self):
        """
        escribe una vision narrativa
        de los personajes
        """
        txt = "looking at people "
        for e in self.character_arr:
            txt += "you see a "
            txt += e.write_appearance() + ". "
        return txt

    def advance_one_day(self):
        """
        Funcion que avansa un dia en el 
        tiempo para todos los personajes
        de la sociedad.
        """
        for i in range(len(self.character_arr)):
            self.character_arr[i]\
                .advance_one_day()
        self.makes_interactions()

    def create(self, culture, 
            region_number)-> None:
        """
        Crea un personaje nuevo desde cero.
        """
        character = Character()
        character.randomize(culture)
        character.d.set_region_code(
            str(region_number))
        self.character_arr.append(character)

    def size(self):
        """Tamanio actual de la sociedad"""
        return len(self.character_arr)
    
    def get_random(self):
        """
        Obtiene un personaje aleatorio
        en la sociedad.
        """
        index = random.randint(0, 
            self.size() - 1)
        return self.character_arr[index]

    def get_by_id(self, ID:int)->Character:
        """
        Funcion que entrega una copia del
        character con el ID indicado.
        """
        char:Character = None
        for char in self.character_arr:
            if(char.d.get_id() == ID):
                return char
        return None
    
    def set(self, character:Character)->None:
        """
        Funcion que remplaza el character 
        actual por el character enviado.
        """
        ID_searched = character.d.get_id()
        for i, e in enumerate(self.character_arr):
            if(e.d.get_id() == ID_searched):
                self.character_arr[i] \
                    = character
                break

    def has_with_id(self, ID:int)-> bool:
        """
        Funcion que retorna un boolean
        dependiendo si existe el character
        con el ID enviado.
        """
        for char in self.character_arr:
            if(char.d.get_id() == ID):
                return True
                
    def delete_by_id(self, ID:int):
        """
        Elimina un personaje de la lista.
        """
        for i, char in enumerate(self.character_arr):
            if(char.d.get_id() == ID):
                del(self.character_arr[i])
                break

    def get_description(self, ID):
        char = self.get_by_id(ID)
        desc = char.create_description()
        desc.society_characters = self\
            .write_narrative()
        return desc
