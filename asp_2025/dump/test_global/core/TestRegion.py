


from data_model.core.region.Region import Region

class TestRegion:

    def inner(self):
        region = Region()
        region.randomize()
        print(region.writeInformation())
