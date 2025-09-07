


from data_access.DataAccess import DataAccess
from basic.Basic import Basic

class GetMoodNameTk:

    def inner(self, mood):
        personMoodMatrix = DataAccess().getPersonMoodMatrix()
        personMoodMap = Basic().convertMatrixToMap(personMoodMatrix)
        if(mood >= -20):
            return personMoodMap["desperate"]
        elif(mood >= -15):
            return personMoodMap["depressed"]
        elif(mood >= -10):
            return personMoodMap["anxious"]
        elif(mood >= -5):
            return personMoodMap["steady"]
        elif(mood >= -0):
            return personMoodMap["well"]
        elif(mood >= 5):
            return personMoodMap["pleased"]
        elif(mood >= 10):
            return personMoodMap["cheerfull"]
        elif(mood >= 15):
            return personMoodMap["happy"]
        elif(mood >= 20):
            return personMoodMap["rapt"]
