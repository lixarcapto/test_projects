


from ..region.Region import Region
import random

class World:

    INITIAL_PERSONS = 12
    ZONE_SIZE = 3
    QUANTITY_ZONES = 8
    WORLD_SIZE_X = 0
    WORLD_SIZE_Y = 0
    QUANTITY_REGIONS = 0

    def __init__(self):
        self.region_matrix = [[]]
        self.calcule_world_data()

    def calcule_world_data(self):
        World.WORLD_SIZE_Y = World.ZONE_SIZE * World.QUANTITY_ZONES
        middle_x = World.WORLD_SIZE_Y // 2
        World.WORLD_SIZE_X = World.WORLD_SIZE_Y + middle_x
        World.QUANTITY_REGIONS = World.WORLD_SIZE_X \
        * World.WORLD_SIZE_Y

    def randomize_settlements(self, quantity):
        code_settlements_array = []
        number = 0
        for i in range(quantity):
            number = random.randint(0, quantity)
            code_settlements_array.append(number)
        region = None
        for code in code_settlements_array:
            region = self.get_region_by_code(code)
            region.inhabitate(World.INITIAL_PERSONS)
            self.set_region(region)

    # return int
    def randomize_player_code(self):
        persons_array = []
        region = None
        person = None
        for y in range(World.WORLD_SIZE_Y):
            for x in range(World.WORLD_SIZE_X):
                region = self.region_matrix[y][x]
                if (region.is_inhabitated):
                    for e in region.society.person_array:
                        persons_array.append(e)
        person_random = random.choice(persons_array)
        return person_random.data.code

    def advance_time(self):
        region = None
        person = None
        for y in range(World.WORLD_SIZE_Y):
            for x in range(World.WORLD_SIZE_X):
                region = self.region_matrix[y][x]
                region.advance_time()
                self.region_matrix[y][x] = region

    # return Person
    def get_person_by_code(self, code):
        region = None
        person = None
        for y in range(World.WORLD_SIZE_Y):
            for x in range(World.WORLD_SIZE_X):
                region = self.region_matrix[y][x]
                if (region.is_inhabitated):
                    person = region.society \
                        .get_person_by_code(code)
                    if not person == None: return person

    def set_person(self, person):
        coordinate = person.coordinate_array
        self.region_matrix[coordinate[0]][coordinate[1]]

    # return Region
    def get_region_by_code(self, code):
        region = None
        for y in range(World.WORLD_SIZE_Y):
            for x in range(World.WORLD_SIZE_X):
                region = self.region_matrix[y][x]
                if (region.code == code):
                    return region

    # return Region
    def get_region_by_coordinate(self, coordinate_array):
        y = coordinate_array[0]
        x = coordinate_array[1]
        return self.region_matrix[y][x]

    # return Region
    def get_region_by_person(self, person):
        y = person.coordinate_array[0]
        x = person.coordinate_array[1]
        return self.region_matrix[y][x]

    def set_region(self, region):
        y = region.location_y
        x = region.location_x
        self.region_matrix[y][x] = region

    def new(self, size_array):
        region = None
        self.size_y = size_array[0]
        self.size_x = size_array[1]
        zone_size = World.ZONE_SIZE
        actual_zone = 0
        counter_zone = 0
        self.quantity_regions = self.size_y * self.size_x
        n = 0
        for y in range(World.WORLD_SIZE_Y):
            self.region_matrix.append([])
            for x in range(World.WORLD_SIZE_X):
                region = Region(n, x, y)
                region.climatic_zone = actual_zone
                self.region_matrix[y].append(region)
                n += 1
                if(counter_zone == zone_size):
                    counter_zone = 0
                    actual_zone += 1
            counter_zone += 1
