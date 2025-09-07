



from .ClimaticZone import ClimaticZone

class ZoneCollection:

    """
        Clase que contiene una coleccion de zonas climaticas
        predefinidas en un diccionario.
    """
    def __init__(self):
        self.zone_map = {}
        # crea un mapa de la zona climatica
        for e in ClimaticZone.CLIMATIC_ZONE_ARRAY:
            self.zone_map[e] = ClimaticZone(e)

    def get_zone(self, key):
        return self.zone_map[key]

    def get_zone_by_index(self, index):
        key = ClimaticZone.CLIMATIC_ZONE_ARRAY[index]
        return self.zone_map[key]

    def get_quantity_zones(self):
        return ClimaticZone.get_quantity_zones()
