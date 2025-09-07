



from data_model.core.world.World import World

class TestWorld:

    def inner(self):
        world = World()
        world.createNewMap()
        world.colonizeInitialRegion()
        return
