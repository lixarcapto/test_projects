


from ..region.Region import Region
from ...mod.citizen.Citizen import Citizen
from btpy.Btpy import Btpy
from .world_const import*

class World:

    QUANTITY_ZONES:int = 10
    HEIGHT_ZONES:int = 1
    INITIAL_TOWNS:int = 1

    def __init__(self):
        self.height:int \
            = World.HEIGHT_ZONES \
            * World.QUANTITY_ZONES
        self.width:int = self.height\
            + round(self.height * 0.5)
        self.quantity_regions:int \
            = self.height * self.width
        self.region_matrix:list[list] = []
        self.region_selected_point\
            :list[int] = []
        
    def get_config_data_dict(self)->dict:
        return {
            "RANGE_INITIAL_TOWNS":
                [
                    MIN_INITIAL_TOWNS,
                    MAX_INITIAL_TOWNS
                ],
            "RANGE_HEIGHT_ZONES":
                [
                    MIN_HEIGHT_ZONES,
                    MAX_HEIGHT_ZONES
                ]
        }
        
    def set_region_selected_point(self, 
                POINT:list[int]):
        """
        Selecciona una region del mapa
        por su coordenada.
        """
        self.region_selected_point = POINT

    def get_region_selected_point(self):
        """
        Obtiene la coordenada de la 
        actual region del mapa 
        seleccionada.
        """
        return self.region_selected_point

    def advance_one_month(self):
        for k in range(3):
            Region.date_asp\
                .advance_one_day()
        def fn(e):
            e.advance_one_month()
            return e
        self.foreach(fn)

    def get_citizen_id_list(self)->list[int]:
        """
        Funcion que obtiene una lista
        de todos los numeros ID de los
        citizen en el world.
        """
        id_list:list[int] = []
        region:Region = None
        for y in range(self.height):
            for x in range(self.width):
                region = self.region_matrix\
                        [x][y]
                if(not region.is_populated):
                    continue
                id_list = id_list + region\
                    .get_citizen_id_list()
        return id_list
    
    def get_citizen_quantity(self)->int:
        """
        Funcion que obtiene la cantidad
        de ciudadanos en todo el mundo.
        """
        id_list:list[int] = []
        region:Region = None
        size:int = 0
        for y in range(self.height):
            for x in range(self.width):
                region = self.region_matrix\
                        [x][y]
                if(not region.is_populated):
                    continue
                size += region.society\
                    .get_size()
        return size

    def get_citizen_id_in_region(self, 
                POINT:list[int])->list[str]:    
        region:Region = self.region_matrix\
                        [POINT[0]][POINT[1]]
        return region.get_citizen_id_list()

    def get_random_region_list(self, 
                quantity):
        region_n_list = Btpy.random_uniques(
            quantity,
            [0, self.quantity_regions]
        )
        return region_n_list

    def populate_world(self):
        region:Region = None
        i = 0
        import random
        citizen = Citizen()
        list_ = citizen.data\
            .get_culture_key_list()
        random.shuffle(list_)
        it_cultures = Btpy.Iterator(list_)
        region_n_list = self\
            .get_random_region_list(
                World.INITIAL_TOWNS -1
            )
        for y in range(self.height):
            for x in range(self.width):
                region = self.region_matrix\
                        [x][y]
                if(i in region_n_list):
                    region.populate(
                        it_cultures.get()
                    )
                    it_cultures.next()
                if(not it_cultures\
                            .has_next()):
                    return None
                self.region_matrix\
                        [x][y] = region
                i += 1

    def set_citizen(self, citizen):
        region:Region = None
        has_citizen = False
        id_number = citizen.get_id_number()
        for y in range(self.height):
            for x in range(self.width):
                region = self.region_matrix\
                        [x][y]
                if(not region.is_populated):
                    continue
                has_citizen = region.society\
                    .has_citizen(citizen)
                if(has_citizen):
                    region.society\
                        .set_citizen(
                            citizen)
                return None
                self.region_matrix\
                        [x][y] = region

    def get_citizen(self, ID_NUMBER):
        region:Region = None
        citizen = None
        for y in range(self.height):
            for x in range(self.width):
                region = self.region_matrix\
                        [x][y]
                if(not region.is_populated):
                    continue
                citizen = region.society\
                    .get_citizen(ID_NUMBER)
                if(citizen == None):
                    continue
                return citizen
                self.region_matrix\
                        [x][y] = region

    def new_world(self):
        self.create_region_matrix()
        self.populate_world()

    def get_region_by_point(self, POINT):
        return self.region_matrix\
            [POINT[0]][POINT[1]]

    def get_region(self, NUMBER):
        region:Region = None
        n = 0
        for y in range(self.height):
            for x in range(self.width):
                if(NUMBER == n):
                    return self\
                        .region_matrix[x][y]
                n += 1

    def write(self):
        txt = ""
        txt += f"{self.width=}\n"
        txt += f"{self.height=}\n"
        txt += f"{self.quantity_regions=}\n"
        region:Region = None
        for y in range(self.height):
            for x in range(self.width):
                region = self\
                    .region_matrix[x][y]
                txt += f"{region.write()}\n" 
        return txt
        
    def foreach(self, function_argsx1):
        for y in range(self.height):
            for x in range(self.width):
                self.region_matrix[x][y]\
                    = function_argsx1(
                        self.region_matrix\
                            [x][y]
                    )

    def set_region(self, region:Region):
        n = 0
        new_number = region.unique_number
        for y in range(self.height):
            for x in range(self.width):
                if(new_number == n):
                    self.region_matrix\
                        [x][y] = region
                    return None
                n += 1

    def create_region_matrix(self):
        list_:list = []
        matrix:list = []
        n:int = 0
        # create matrix
        for x in range(self.width):
            list_ = []
            for y in range(self.height):
                list_.append(None)
            matrix.append(list_)
        #
        n:int = 0
        zone_number:int = 0
        zone_counter:int = 0
        region = None
        for y in range(self.height):
            for x in range(self.width):
                region = Region(
                    n, x, y)
                region.latitudinal_zone \
                    = zone_number
                region.randomize()
                n += 1
                matrix[x][y] = region
            if(zone_counter 
                    == World.HEIGHT_ZONES):
                zone_counter = 0
                zone_number += 1
            else:
                zone_counter += 1
        self.region_matrix = matrix

    def render_square_matrix(self, 
            cam_point:list[int], 
            cam_size:int)\
            ->list[str]:
        render_matrix = []
        render_layout = []
        render_row = []
        region = None
        for y in range(cam_point[1], 
                self.height):
            if(y == self.height):
                break
            render_row = []
            for x in range(cam_point[0],
                    self.width):
                if(x == self.width):
                    break
                render_layout = []
                region = self.region_matrix\
                    [x][y]
                render_layout = region\
                    .render_square_layout()
                render_row.append(
                    render_layout)
            render_matrix.append(
                render_row
            )
        return render_matrix


