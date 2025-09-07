


from data_model.core.citizen_trigger.app.entities.FeedTrigger import FeedTrigger
from data_model.core.citizen_trigger.app.entities.HungryTrigger import HungryTrigger
from data_model.core.citizen_trigger.app.entities.AdvanceTimeTrigger import AdvanceTimeTrigger

class CollectionCitizenTrigger:

    def __init__(self):
        self.inner = dict()
        self.addItem(FeedTrigger())
        self.addItem(HungryTrigger())
        self.addItem(AdvanceTimeTrigger())
        return

    def addItem(self, citizenTrigger):
        self.inner[citizenTrigger.getKeyName()] = citizenTrigger
