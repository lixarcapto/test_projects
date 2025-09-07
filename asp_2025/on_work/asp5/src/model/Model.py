


from .mod.world.World import World

class Model:

    def __init__(self):
        self.player_code = 0
        self.world = World()
        self.is_first_turn = True
        self.world.new([20, 20])
        self.world.randomize_settlements(15)
        self.player_code = self.world.randomize_player_code()

    def advance_time(self):
        self.world.advance_time()

    def describe_player(self):
        person = self.world.get_person_by_code(self.player_code)
        text = "you are " + person.write_presentation() + ". "
        text += person.describe_appearance()
        return text

    def describe_player_vision(self):
        person = self.world.get_person_by_code(self.player_code)
        region = self.world.get_region_by_person(person)
        return region.describe(self.player_code)

    def write(self):
        text = ""
        if(self.is_first_turn):
            text += self.describe_player() + ".\n"
            self.is_first_turn = False
        text += self.describe_player_vision()
        return text
