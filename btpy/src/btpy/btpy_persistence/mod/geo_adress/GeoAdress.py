


class GeoAdress():
    def __init__(self):
        self.continent = ""
        self.country = ""
        self.region =  ""
        self.district = ""
        self.parcel_code = ""

    def write(self):
        return ""\
        + self.region + " "\
        + self.country + " "\
        + self.continent + " "\
        + self.district + " "\
        + self.parcel_code
    
    def __str__(self):
        return self.write()