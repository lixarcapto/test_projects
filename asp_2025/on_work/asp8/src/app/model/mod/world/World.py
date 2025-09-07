

from ..region.Region import Region

class World:


    def __init__(self) -> None:
        self.size_x = 0
        self.size_y = 0
        self.init_person = 10
        self.default_culture = "extreme_north"
        self.set_maximum_person(40)
        self.__region_matrix:list = []

    def set_maximum_person(self, integer):
        Region.set_maximum_person(integer)

    def create_map(self, size_x, size_y):
        matrix = []
        array = []
        self.size_x = size_x
        self.size_y = size_y
        for y in range(size_y):
            array = []
            for x in range(size_x):
                array.append(Region())
            matrix.append(array)
        self.__region_matrix = matrix
        self.randomize()

    def get_all_person_id(self):
        region = None
        id_arr = []
        result = []
        for y in range(self.size_y):
            for x in range(self.size_x):
                region = self.__region_matrix\
                    [x][y]
                result = region\
                    .get_all_person_id()
                id_arr = id_arr + result
        return id_arr
    
    def update(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                self.__region_matrix\
                    [x][y].update()

    def get_person(self, id):
        region = None
        person = None
        for y in range(self.size_y):
            for x in range(self.size_x):
                region = self.__region_matrix\
                    [x][y]
                person = region.get_person(id)
                if(person == None): continue
                if(person.get_id() == id):
                    return person
        return person
    
    def set_person(self, person):
        region = None
        person = None
        for y in range(self.size_y):
            for x in range(self.size_x):
                region = self.__region_matrix\
                    [x][y]
                if(region.has_person(id)):
                    region.set(person)
                    return None
        

    def randomize(self):
        region = None
        for y in range(self.size_y):
            for x in range(self.size_x):
                region = self.__region_matrix\
                    [x][y]
                region.randomize()
                region.populate(self.init_person,
                    self.default_culture)

    def write(self):
        txt = ""
        region = None
        for y in range(self.size_y):
            for x in range(self.size_x):
                region = self.__region_matrix\
                    [x][y]
                txt += f"{region.write()}\n"
        return txt

                