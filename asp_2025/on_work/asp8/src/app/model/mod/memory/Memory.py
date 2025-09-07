

from ..date_esp.DateEsp import DateEsp

class Memory:

    def __init__(self) -> None:
        self.date = DateEsp()
        self.place_name = ""
        self.region_code = ""
        self.territory_code = ""
        self.territory_name = ""
        self.relief = 0
        self.clime = ""
        self.temperature = 0
        self.humidity = 0
        self.soil_type = ""
        self.sounds_arr = []
        self.smell_arr = []
        self.resources_arr = []
        self.person_description_dict = {}

    def write_narrative(self):
        txt = ""
        return txt
    
    def write_date(self):
        return self.date.write_narrative()

    def write(self):
        txt = ""
        txt += f"{self.place_name=}\n"
        txt += f"{self.region_code=}\n"
        txt += f"{self.territory_code=}\n"
        txt += f"{self.territory_name=}\n"
        txt += f"{self.relief=}\n"
        txt += f"{self.clime=}\n"
        txt += f"{self.temperature=}\n"
        txt += f"{self.humidity=}\n"
        txt += f"{self.soil_type=}\n"
        txt += f"{self.sounds_arr=}\n"
        txt += f"{self.smell_arr=}\n"
        txt += f"{self.resources_arr=}\n"
        txt += f"{self.person_description_dict=}\n"
        return txt