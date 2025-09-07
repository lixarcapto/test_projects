


from data_model.core.world.World import World
from data_model.core.market.Market import Market

class WorldTest:

    def inner(self):
        world = World()
        world.createNewMap()
        world.advanceTime()
        return
