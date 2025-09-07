


class GeneticGroup():

    """
    Clase que almacena los datos 
    embebidos para los grupos genéticos.  
    """

    def __init__(self, NAME:str):
        self.name:str = NAME
        self.maximum_size_arr:list[int] = []
        self.skin_color_arr:list[str] = []
        self.eye_color_arr:list[str] = []
        self.eye_type_arr:list[str] = []
        self.hair_type_arr:list[str] = []
        self.hair_color_arr:list[str] = []

    def add_skin_color(self, ARRAY:list[str]):
        self.skin_color_arr \
            = self.skin_color_arr + ARRAY
        
    def add_eye_color(self, ARRAY:list[str]):
        self.eye_color_arr \
            = self.eye_color_arr + ARRAY

    def add_maximum_size(self, ARRAY:list[int]):
        self.maximum_size_arr \
            = self.maximum_size_arr + ARRAY

    def add_eye_type(self, ARRAY:list[str]):
        self.eye_type_arr \
            = self.eye_type_arr + ARRAY

    def add_hair_type(self, ARRAY:list[str]):
        self.hair_type_arr \
            = self.hair_type_arr + ARRAY

    def add_hair_color(self, ARRAY:list[str]):
        self.hair_color_arr \
            = self.hair_color_arr + ARRAY