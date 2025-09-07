


class Epitaph:

    def __init__(self):
        self.id:int = 0
        self.cause_death_key:str = ""
        self.specific_death:str = ""
        self.full_name:str = ""
        self.culture_key:str = ""
        self.years:int = 0

    def write(self)->str:
        return ""\
            + f"{self.full_name}died with "\
            + f"{self.years} years-old "\
            + f" of {self.specific_death} ({self.cause_death_key}) "