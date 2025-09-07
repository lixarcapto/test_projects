


#PDT
#interfaces
from data_model.app.body_lib.PersonBody import PersonBody
from data_model.app.person_list_lib.core.person_information.PersonInformation import PersonInformation
from data_model.app.person_list_lib.core.person_needs.PersonNeeds import PersonNeeds
from data_model.app.person_list_lib.core.person_interest.PersonInterest import PersonInterest
from data_model.app.person_list_lib.core.person_inventory.PersonInventory import PersonInventory
from data_model.app.person_list_lib.core.person_skills.PersonSkills import PersonSkills
from data_model.app.person_list_lib.core.psychological_traits.PsychologicalTraits import PsychologicalTraits
from data_model.app.person_list_lib.core.relation_list.RelationList import RelationList
#
from data_model.app.person_list_lib.core.thought.Thought import Thought
from data_model.app.market_lib.core.goods.Goods import Goods
from data_access.DataAccess import DataAccess

class PersonProduct:

    def __init__(self):
        #constant
        self.PERSON_KEYS = DataAccess().getPersonData()
        self.GOODS = DataAccess().getGoodsKeysData()
        #
        self.inventory = PersonInventory()
        #

    #person information ------------------------------------------------------------------------------



    #-------------------------------------------------------------------------------------------------



    def extractGoods(self, typeCode):
        for i in range(len(self.inventory.inventoryArray)):
            if(self.inventory.inventoryArray[i].typeCode == typeCode):
                return self.inventory.inventoryArray
        return None

    def addGoods(goodsProduct):
        self.inventory.inventoryArray.append(goodsProduct)

    def addHistory(self, text):
        self.psychologicalTraits.history.append(text)

    def addThought(self, thoughtType, text):
        thought = ThoughtProduct()
        thought.thoughtType = thoughtType
        thought.remimber = text
        self.psychologicalTraits.thoughtsArray.append(thought)
