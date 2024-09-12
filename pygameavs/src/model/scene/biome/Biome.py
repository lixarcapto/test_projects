


class Biome:

    def __init__(self) -> None:
        self.name = ""
        self.terrain_keys = []
        self.vegetable_keys = []
        self.animal_keys = []

    def create(self, BIOME_KEY):
        match BIOME_KEY:
            case "forest":
                self.create_forest()

    def create_forest(self):
        self.name = "forest"
        self.terrain_keys = []
        self.vegetable_keys = []
        self.animal_keys = []