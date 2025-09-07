


from data_access.core.biome_collection.Biome import Biome

class NoneBOM(Biome):

    def __init__(self):
        super().__init__()
        self.setKey("none")
        self.setBaseSoilType("ground")
        self.addSoilType("sand", 5)
        self.addResource("pine-forest", 5)
        return
