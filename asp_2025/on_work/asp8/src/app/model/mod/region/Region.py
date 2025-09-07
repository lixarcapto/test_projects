


from ..society.Society import Society
from ..territory.Territory import Territory
from ..memory.Memory import Memory
from ..date_esp.DateEsp import DateEsp
from .region_keys import*
from ..perception.Perception import Perception
from ....persistence.Persistence import Persistence
from btpy.src.btpy.Btpy import Btpy

class Region:

    last_code = 0
    size_region = 3
    REGION_NAMES_DICT = Persistence\
            .read_city_names()

    def __init__(self) -> None:
        self.id = ""
        self.point = [0, 0]
        self.name = ""
        self.relief = 0
        self.soil_type = ""
        self.wind = 0
        self.temperature = 0
        self.humidity = 0
        self.season = ""
        self.territory_matrix = []
        self.perception = Perception()
        self.resources_arr = []
        self.date_esp = DateEsp()
        # genera un codigo unico
        self.get_id_code()
        self.randomize()

    def get_relief(self):
        return RELIEF_ARRAY[self.relief]
    
    def random_name(self):
        return Btpy.random_choice(
            self.REGION_NAMES_DICT["nordic"]
        )

    def write_narrative(self):
        txt = self.date_esp.write_narrative()
        txt += f"{self.name} was a "\
        + f"{self.get_relief()} "\
        + f"with the soil "\
        + f"{self.soil_type}"
        return txt
    
    def update(self):
        # avansa un dia
        self.date_esp.one_more_day()
        territory = None
        for y in range(Region.size_region):
            for x in range(Region.size_region):
                territory = self.territory_matrix[x][y]
                territory.update(
                    self.write_narrative()
                )
                self.territory_matrix[x][y] = territory

    def detect_resources_descriptions(self):
        pass

    def detect_person_description(self):
        pass

    def detect_smells(self):
        pass

    def detect_sounds(self):
        pass

    def create_territory(self):
        territory = None
        matrix = []
        array = []
        for y in range(Region.size_region):
            array = []
            for x in range(Region.size_region):
                array.append(Territory())
            matrix.append(array)
        self.territory_matrix = matrix

    def write_territory(self):
        e = None
        txt = ""
        for y in range(Region.size_region):
            for x in range(Region.size_region):
                e = self\
                    .territory_matrix[x][y]
                txt += e.write()
        return txt
    
    def get_all_person_id(self):
        e = None
        id_arr = []
        person = None
        result = []
        for y in range(Region.size_region):
            for x in range(Region.size_region):
                e = self\
                    .territory_matrix[x][y]
                result = e.society\
                    .get_all_person_id()
                id_arr = id_arr + result
        return id_arr
    
    def get_person(self, id):
        e = None
        person = None
        for y in range(Region.size_region):
            for x in range(Region.size_region):
                e = self\
                    .territory_matrix[x][y]
                person = e.society.get(id)
                if(person == None): continue
                if(person.get_id() == id): 
                    return person
        return None
    
    def has_person(self, id):
        e = None
        person = None
        for y in range(Region.size_region):
            for x in range(Region.size_region):
                e = self\
                    .territory_matrix[x][y]
                if(e.society.has(id)): return True
        return False
    
    def set_person(self, person):
        e = None
        person = None
        for y in range(Region.size_region):
            for x in range(Region.size_region):
                e = self\
                    .territory_matrix[x][y]
                if(e.society.has(person.id)):
                    e.society.set(person)
                    return None
    
    def populate(self, quantity, culture):
        for y in range(Region.size_region):
            for x in range(Region.size_region):
                e = self\
                    .territory_matrix[x][y]
                e.populate(quantity, culture)
                self.territory_matrix[x][y]\
                 = e


    def randomize(self):
        self.create_territory()
        self.name = self.random_name()
        self.soil_type = Btpy.random_choice(
            SOIL_TYPE_ARRAY
        )
        self.relief = Btpy.rand_range(
            [0, len(RELIEF_ARRAY) -1]
        )

    def set_maximum_person(integer):
        Territory.set_maximum_person(
            integer)

    def get_id_code(self):
        self.id = str(Region.last_code)
        Region.last_code += 1

    def write(self):
        txt = ""
        txt += f"REGION:\n"\
        + f"{self.id=}\n"\
        + f"{self.point=}\n"\
        + f"{self.name=}\n"\
        + f"{self.relief=}\n"\
        + f"{self.soil_type=}\n"\
        + f"{self.wind=}\n"\
        + f"{self.temperature=}\n"\
        + f"{self.humidity=}\n\n"\
        + f"{self.write_territory()}\n"
        return txt