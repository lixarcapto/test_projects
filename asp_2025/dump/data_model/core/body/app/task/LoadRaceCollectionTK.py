


from data_access.DataAccess import DataAccess
from data_model.core.body.core.race.Race import Race
from basic.Basic import Basic

class LoadRaceCollectionTK:

    def inner(self):
        self.raceCollectionArray = DataAccess().getRaceCollectionArray()
        raceArray = []
        race = None
        for e in self.raceCollectionArray:
            race = Race()
            race.convertMatrixToRace(e)
            raceArray.append(race)
        return raceArray
