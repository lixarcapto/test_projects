


from data_model.core.citizen_trigger.CitizenTrigger import CitizenTrigger

class HungryTrigger(CitizenTrigger):

    def __init__(self):
        super().__init__()
        self.setKeyName("hungry")
        self._satisfactionKey = "fed_up"
        self._dissatisfactionKey = "hungry"
        self.addMinimumAttributeCondition("feed", 0)
        self.addAttributeEffect("organic_damage", 1, 0)
        self.setCategory("lack")
