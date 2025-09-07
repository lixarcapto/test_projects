


from ..region.Region import Region
from btpy.src.btpy.Btpy import Btpy

class World:

    """
    Clase que representa a todo el planeta
    con multiples regiones.
    """

    HEIGHT = 20
    DEFAULT_CULTURE = "spanish"
    SETTLER_NUMBER = 10

    def __init__(self):
        self.size_y = 0
        self.size_x = 0
        self.total_regions = 0
        self.region_matrix:list = []
        self.create_world()
        self.colonize_regions()

    def colonize_regions(self):
        print("colonize_regions")
        to_colonize_arr = Btpy\
            .random_uniques(
                30,
                [0, self.total_regions]
            )
        print(f"{to_colonize_arr=}")
        region:Region = None
        for n in to_colonize_arr:
            region = self\
                .get_region_by_number(n)
            region.occupy(self.SETTLER_NUMBER, 
                self.DEFAULT_CULTURE)
            self.set_region(region)
        print("end colonize_regions")

    def get_region_by_number(self, number):
        print(f"get_region_by_number {number}")
        region:Region = None
        for y in range(self.size_y):
            for x in range(self.size_x):
                region = self\
                    .region_matrix[y][x]
                if(region.d.get_number()\
                    == number):
                    return region
        return None
                
    def get_region_by_index(self, y, x):
        """
        Obtiene la region indicada por 
        sus indices X e Y
        """
        return self.region_matrix[y][x]

    def set_region(self, region:Region):
        """
        Actualiza la region enviada
        en el mapa.
        """
        x = region.d.get_point_index()[0]
        y = region.d.get_point_index()[1]
        self.region_matrix[y][x] = region

    def get_all_character_id(self):
        """
        Busca los codigos de ID de todas
        las personas en el mundo y las
        retorna como una lista.
        """
        id_arr = []
        person = None
        array = []
        region:Region = None
        for y in range(self.size_y):
            for x in range(self.size_x):
                region = self\
                    .region_matrix[y][x]
                if(not region.d\
                   .get_is_inhabited()):
                    continue
                array = region\
                    .get_all_character_id()
                id_arr = id_arr + array
        return id_arr
    
    def advance_one_day(self):
        region:Region = None
        for y in range(self.size_y):
            for x in range(self.size_x):
                region = self\
                    .region_matrix[y][x]
                region.advance_one_day()
                self.region_matrix[y][x] \
                    = region
    
    def randomize_person_id(self):
        print("randomize_person_id")
        id_arr = self.get_all_character_id()
        print(id_arr)
        return Btpy.random_choice(id_arr)

    def get_person(self, person_id):
        """
        Busca una persona con el ID indicado
        por todo el mundo.
        """
        region:Region = None
        person = None
        for y in range(self.size_y):
            for x in range(self.size_x):
                region = self\
                    .region_matrix[y][x]
                if(not region.d.get_is_inhabited()):
                    continue
                person = region.d.society\
                    .get_by_id(person_id)
                if(person != None):
                    return person
        return None
    
    def get_description(self, person_id):
        """
        Busca una persona con el ID indicado
        por todo el mundo.
        """
        region:Region = None
        for y in range(self.size_y):
            for x in range(self.size_x):
                region = self\
                    .region_matrix[y][x]
                if(not region.d.get_is_inhabited()):
                    continue
                has_person = region\
                    .has_person(person_id)
                if(has_person):
                    return region\
                        .get_description(
                            person_id)
        return None

    def set_person(self, person_id):
        pass

    def create_world(self)->None:
        """
        Crea un mapa de regiones desde
        cero calculando los tamaños a 
        partir de la altura predeterminada.
        """
        print("World.create_world")
        # calcula los tamaños
        self.size_y = self.HEIGHT
        self.size_x = self.HEIGHT * 2
        self.total_regions = self.size_x \
            * self.size_y
        # crea la matriz de region
        region = None
        n = 0
        for y in range(self.size_y):
            self.region_matrix.append([])
            for x in range(self.size_x):
                region = Region()
                region.d.set_number(n)
                region.d.set_point_index(
                    [x, y])
                self.region_matrix[y]\
                    .append(region)
                n += 1
            