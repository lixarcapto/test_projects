




from data_model.core.sensory_description.SensoryDescription import SensoryDescription

class TestSensoryDescription:

    def inner(self):
        sensoryDescription = SensoryDescription()
        thing = sensoryDescription.createThing()
        thing.define("san juan", "region")
        thing.addImage("ground", 6)
        thing.addImage("ground", 6)
        thing.addImage("ground", 6)
        thing.addImage("ground", 6)
        thing.addImage("ground", 6)
        thing.addImage("ground", 6)
        thing.addExternalSensation("rough", 6)
        sensoryDescription.addThing(thing)
        print(sensoryDescription.writeDescription())
