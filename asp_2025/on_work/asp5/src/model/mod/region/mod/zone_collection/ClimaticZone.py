


class ClimaticZone:

    CLIMATIC_ZONE_ARRAY = [
        "north_polar_zone",
        "north_cold_zone",
        "north_tempered_zone",
        "north_arid_zone",
        "tropic_zone",
        "south_arid_zone",
        "south_tempered_zone",
        "south_cold_zone",
        "south_polar_zone"
    ]

    """
        Clase que representa las caracteristicas
        posibles de una zona climatica del mapa.
    """
    def __init__(self, key):
        self.key = key
        self.wind_range_allowed = [0, 4]
        self.temperature_range_allowed = [0, 4]
        self.humidity_range_allowed = [0, 4]
        self.soil_type_allowed = []
        self.build(key)

    def get_quantity_zones():
        return len(ClimaticZone.CLIMATIC_ZONE_ARRAY)

    def add_wind_range(self, range):
        self.wind_range_allowed = range

    def add_temperature_range(self, range):
        self.temperature_range_allowed = range

    def add_humidity_range(self, range):
        self.humidity_range_allowed = range

    """
        Funcion que crea una zona climatica predefinida.
    """
    def build(self, key):
        if("north_polar_zone" == key):
            self.add_wind_range([3, 4])
            self.add_temperature_range([0, 1])
            self.add_humidity_range([3, 4])
        elif("north_cold_zone" == key):
            self.add_wind_range([2, 4])
            self.add_temperature_range([0, 3])
            self.add_humidity_range([2, 4])
        elif("north_tempered_zone" == key):
            self.add_wind_range([3, 4])
            self.add_temperature_range([1, 4])
            self.add_humidity_range([2, 4])
        elif("north_arid_zone" == key):
            self.add_wind_range([0, 4])
            self.add_temperature_range([2, 4])
            self.add_humidity_range([0, 3])
        elif("tropic_zone" == key):
            self.add_wind_range([3, 4])
            self.add_temperature_range([4, 4])
            self.add_humidity_range([3, 4])
        elif("south_arid_zone" == key):
            self.add_wind_range([0, 0])
            self.add_temperature_range([3, 4])
            self.add_humidity_range([0, 1])
        elif("south_tempered_zone" == key):
            self.add_wind_range([3, 4])
            self.add_temperature_range([2, 4])
            self.add_humidity_range([0, 4])
        elif("south_cold_zone" == key):
            self.add_wind_range([0, 3])
            self.add_temperature_range([1, 3])
            self.add_humidity_range([1, 4])
        elif("south_polar_zone" == key):
            self.add_wind_range([3, 4])
            self.add_temperature_range([0, 1])
            self.add_humidity_range([0, 4])
