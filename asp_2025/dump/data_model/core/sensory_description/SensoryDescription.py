


from data_model.core.sensory_description.core.thing.Thing import Thing

class SensoryDescription:

    def __init__(self):
        self.date = None
        self.thingArray = []

    def createThing(self):
        return Thing()

    def addThing(self, thing):
        self.thingArray.append(thing)

    def writeDescription(self):
        text = ""
        for e in self.thingArray:
            text += e.writeThing()
        return text
