


from ..society.Society import Society
import random
from basic_things.basic_things import Basic
from .region_const import*
from .mod.zone_collection.ZoneCollection import ZoneCollection
from .mod.clime_collection.ClimeCollection import ClimeCollection

class Region:

    """
        Clase que representa un estado o region territorial
        de gran extension. Estan subdivididas en distritos
        imaginarios.
    """

    CLIME_COLLECTION = ClimeCollection()
    ZONE_COLLECTION = ZoneCollection()
    DISTRICT_QUANTITY = 10

    def __init__(self, code, location_x, location_y):
        self.society = Society()
        self.is_inhabitated = False
        self.name = ""
        self.type = ""
        self.biome = ""
        self.soil_type = ""
        self.code = code
        self.location_x = location_x
        self.location_y = location_y
        self.relief = ""
        self.clime = "clear"
        self.temperature_code = 0
        self.wind_code = 0
        self.humidity_code = 0
        self.contamination = 0
        self.climatic_zone = 0
        self.is_seismic = False
        self.is_coastal = False

    """
        Funcion que crea un asentamiento de personas en la
        region y una sociedad.
    """
    def inhabitate(self, initial_persons):
        self.is_inhabitated = True
        self.society.new(initial_persons,
            [self.location_y, self.location_x])

    def randomize(self):
        self.relief = Basic.randindex(RELIEF_KEYS_ARRAY)
        self.soil_type = random.choice(SOIL_TYPE_KEYS_ARRAY)

    """
        Funcion que modifica las variables climatologicas segun
        los rangos permitidos por su zona climatica definida.
    """
    def generates_climatology(self):
        zone_index = self.climatic_zone
        zone = Region.ZONE_COLLECTION.get_zone_by_index(zone_index)
        temperature_range = zone.temperature_range_allowed
        self.temperature_code = Basic.randrange(temperature_range)
        wind_range = zone.wind_range_allowed
        self.wind_code = Basic.randrange(wind_range)
        humidity_range = zone.humidity_range_allowed
        self.humidity_code = Basic.randrange(humidity_range)

    """
        Funcion que elige un clima de la lista
        si cumple las condiciones. defineclime siempre
        debe ir antes de generar las variables climaticas,
        para permitir la anticipacion del clima.
        TODO: cambiar el map por un array de climas y
        hacerle un shuffle para añadir aleatoriedad.
    """
    def define_clime(self):
        clime = None
        find_clime = False
        for k in Region.CLIME_COLLECTION.get_keys():
            clime = Region.CLIME_COLLECTION.get(k)
            if(not Basic.in_range(self.humidity_code,
                clime.humidity_range)):
                continue
            if(not Basic.in_range(self.temperature_code,
                clime.temperature_range)):
                continue
            if(not Basic.in_range(self.wind_code,
                clime.wind_range)):
                continue
            """ # para agregar
            if(not self.soil_type \
                    in clime.soil_type_required):
                continue
            if(not self.relief \
                    in clime.relief_required):
                continue
            """
            self.clime = k
            find_clime = True
            break
        # si no encuentra el clima le asigna clear
        if not find_clime: self.clime = "clear"

    """
        Funcion que avansa el tiempo en un dia para la region.
    """
    def advance_time(self):
        if(self.is_inhabitated):
            self.society.advance_time()
        self.define_clime()
        self.generates_climatology()

    """
        Funcion que describe narrativamente el clima de la
        region.
    """
    # return string
    def write_clime_description(self):
        tx = ""
        tx += "it was " + self.clime + " "
        tx += ", the air " \
        + HUMIDITY_KEYS_ARRAY[self.humidity_code] + " "
        tx += " and " \
        + TEMPERATURE_KEYS_ARRAY[self.temperature_code] + " "
        tx += " with " \
        + WIND_KEYS_ARRAY[self.wind_code] + " "
        tx += "winds"
        return tx

    """
        Funcion que describe narrativamente todos los aspectos
        de la region.
    """
    # return string
    def describe(self, player_code):
        tx = ""
        tx += "in the region " + self.name + " "
        tx += self.write_clime_description() + ". "
        tx += "You observe a "
        if self.is_inhabitated:
            tx += self.society.describe(player_code)
        return tx
