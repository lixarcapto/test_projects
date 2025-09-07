


class Clime:

    def __init__(self):
        self.humidity_range = []
        self.temperature_range = []
        self.wind_range = []
        self.soil_type_required = []
        self.relief_required = []
        self.effect_array = []

    def load_clime_map(self, clime_map):
        self.humidity_range = clime_map["humidity_range"]
        self.temperature_range = clime_map["temperature_range"]
        self.wind_range = clime_map["wind_range"]
        self.soil_type_required = clime_map["soil_type_required"]
        self.relief_required = clime_map["relief_required"]
        self.effect_array = clime_map["effect_array"]
