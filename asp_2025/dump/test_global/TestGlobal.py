


#from data_model.core.world.World import World
from test_global.core.TestBasic import TestBasic
from test_global.core.TestPerson import TestPerson
from test_global.core.TestPersonList import TestPersonList
from test_global.core.TestRegion import TestRegion
from test_global.core.TestWorld import TestWorld
from test_global.core.TestScene import TestScene
from test_global.core.TestBattle import TestBattle
from test_global.core.TestSystem import TestSystem
from test_global.core.TestBody import TestBody
from test_global.core.TestMemory import TestMemory
from test_global.core.TestView import TestView
from test_global.core.TestApplication import TestApplication
from test_global.core.TestSensoryDescription import TestSensoryDescription
from basic.Basic import Basic

class TestGlobal:

    def __init__(self):
        #TestBasic()
        """
        self.world = World()
        self.world.createNewMap()
        self.world.colonizeInitialRegion()
        print(self.world.writeGlobalDescription())
        """
        #testPerson = TestPerson()
        #testPersonList = TestPersonList()
        ##TestRegion().inner()
        #TestWorld().inner()
        #TestScene().inner()
        #TestBattle().inner()
        #TestSystem().inner()
        #TestBody().inner()
        #TestView().inner()
        #TestApplication().inner()
        TestSensoryDescription().inner()
