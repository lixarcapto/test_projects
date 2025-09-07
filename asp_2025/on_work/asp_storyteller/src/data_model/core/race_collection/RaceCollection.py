



from data_model.core.race_collection.app.entities.RaceNordic import RaceNordic
from data_model.core.race_collection.app.entities.RaceMediterranean import RaceMediterranean

class RaceCollection:

    def __init__(self):
        self.inner = dict()
        self.addRace(RaceNordic())
        self.addRace(RaceMediterranean())
        return

    def getRace(self, keyName):
        return self.inner[keyName]

    def addRace(self, race):
        self.inner[race.keyName] = race
