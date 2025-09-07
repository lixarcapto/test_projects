


from data_model.core.citizen_trigger.CitizenTrigger import CitizenTrigger

class AdvanceTimeTrigger(CitizenTrigger):

    def __init__(self):
        super().__init__()
        self.setKeyName("advance_time")
        self.addAttributeEffect("feed", -1, 0)
        self.addAttributeEffect("hydration", -1, 0)
        self.setCategory("need")
