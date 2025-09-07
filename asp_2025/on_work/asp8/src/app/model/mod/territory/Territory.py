


from ..society.Society import Society

class Territory:

    last_code = 0

    def __init__(self) -> None:
        self.id = ""
        self.name = ""
        self.society = Society()
        self.create_id()

    def update(self, region_description):
        self.society.update(
            region_description)

    def create_id(self):
        self.id = Territory.last_code
        Territory.last_code += 1

    def set_maximum_person(integer):
        Society.MAXIMUM = integer

    def randomize(self):
        pass

    def populate(self, person_number, culture):
        self.society.randomize(person_number, 
            culture)

    def write(self):
        txt = ""
        txt += f"TERRITORY:\n"\
        + f"{self.id=}\n"\
        + f"{self.resource=}\n\n"\
        + f"{self.society.write()}\n"
        return txt