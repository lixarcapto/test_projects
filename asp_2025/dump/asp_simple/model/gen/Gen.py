


from .appearance_const import*

class Gen:

    """
    Clase que representa las 
    características físicas genéticas 
    heredables.  sirve para simular 
    la herencia de características 
    genéticas y las mezclas genéticas 
    en Los herederos de los personajes.
    El objetivo es que se puedan crear
    genes a partir del grupo genetico; 
    y los genes se mesclen al crear
    nuevos personajes.
    """

    def __init__(self):
        self.__maximum_size:int = 0
        self.__skin_color:str = ""
        self.__eye_color:str = ""
        self.__eye_type:str = ""
        self.__hair_type:str = ""
        self.__hair_color:str = ""

    def get_maximum_size(self)->int:
        return self.__maximum_size
    
    def set_maximum_size(self,
            MAXIMUM_SIZE:int):
        self.__maximum_size = MAXIMUM_SIZE

    def get_skin_color(self)->str:
        return self.__skin_color
    
    def set_skin_color(self, SKIN_COLOR:str):
        self.__skin_color = SKIN_COLOR

    def get_eye_color(self)->str:
        return self.__eye_color
    
    def set_eye_color(self, EYE_COLOR:str):
        self.__eye_color = EYE_COLOR

    def get_eye_type(self)->str:
        return self.__eye_type
    
    def set_eye_type(self, EYE_TYPE:str):
        self.__eye_type = EYE_TYPE

    def get_hair_type(self)->str:
        return self.__hair_type
    
    def set_hair_type(self, HAIR_TYPE:str):
        self.__hair_type = HAIR_TYPE

    def get_hair_color(self)->str:
        return self.__hair_color
    
    def set_hair_color(self, HAIR_COLOR:str):
        self.__hair_color = HAIR_COLOR

