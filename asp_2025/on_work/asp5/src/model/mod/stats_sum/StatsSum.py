


from basic_things.basic_things import Basic

class StatsSum:

    """
        Clase que sirve para crear conjuntos de estadisticas
        totales que se pueden usar para calcular estadisticas
        nuevas; usando el total como base para sumar nuevos
        puntos y calcular un porcentaje
    """
    def __init__(self):
        self.stats_map = {}
        self.to_calcule_stats_array = []
        self.total = 0
        self.part = 0

    def calcule(self):
        self.calcule_total()
        self.calcule_stats()
        if self.part == 0: return 0
        percent = Basic.calcule_percent_from_part( \
            self.part, self.total)
        part_percent = round(percent)
        return part_percent

    # return int
    def calcule_stats(self):
        self.part = 0
        for stat_key in self.to_calcule_stats_array:
            #if not stat_key in self.stats_map: continue
            self.part += self.stats_map[stat_key]
        self.to_calcule_stats_array.clear()

    def calcule_total(self):
        self.total = 0
        for k in self.stats_map:
            self.total += self.stats_map[k]

    def sum_stat(self, key):
        self.to_calcule_stats_array.append(key)

    def new_stat(self, key, value = 1):
        self.stats_map[key] = value
