


from data_access.core.biome_collection.app.entities.NoneBOM import NoneBOM

class BiomeCollection:

    def __init__(self):
        self.inner = dict()
        return

    def getBiome(self, key):
        return self.inner[key]

    def addBiome(self, biome):
        self.biome[biome.getKey()] = biome

    def size(self):
        return len(self.inner)
