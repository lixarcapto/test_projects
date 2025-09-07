

from data_model.app.world_lib.app.task.GoOutToMeetPersonTk import GoOutToMeetPersonTk
from data_model.app.world_lib.app.task.MeetAFriendTk import MeetAFriendTk
from data_model.app.world_lib.app.task.HaveSexTk import HaveSexTk
from data_access.DataAccess import DataAccess

class MakeDesitionTk:

    def inner(self, worldProduct):
        desitionData = DataAccess().getPersonData().DESITION
        goOutToMeetPerson = GoOutToMeetPersonTk()
        haveSex = HaveSexTk()
        meetAFriend = MeetAFriendTk()
        region = None
        person = None
        personArray = None
        for y in range(len(worldProduct.regionMatrix.regionMatrix)):
            for x in range(len(worldProduct.regionMatrix.regionMatrix[y])):
                region = worldProduct.regionMatrix.regionMatrix[x][y]
                if(not region.isItInhabited):
                    continue
                personArray = region.personList.getPersonArray()
                for i in range(len(personArray)):
                    person = personArray[i]
                    if(person.getDesition() == desitionData.STAY_AT_HOME):
                        None
                    elif(person.getDesition() == desitionData.TAKE_A_WALK_IN_REGION):
                        None
                    elif(person.getDesition() == desitionData.TRAVEL_TO_ANOTHER_REGION):
                        None
                    elif(person.getDesition() == desitionData.MOVE_HOUSE_OF_REGION):
                        None
                    elif(person.getDesition() == desitionData.GO_SHOPPING):
                        None
                    elif(person.getDesition() == desitionData.GO_OUT_TO_MEET_PEOPLE):
                        worldProduct = goOutToMeetPerson.inner(worldProduct,
                        person.getCodeInt())
                    elif(person.getDesition() == desitionData.GO_TO_WORK):
                        None
                    elif(person.getDesition() == desitionData.GO_HAVE_FUN):
                        None
                    elif(person.getDesition() == desitionData.GO_VISIT_FRIENDS):
                        worldProduct = meetAFriend.inner(worldProduct,
                        person.getCodeInt())
                    elif(person.getDesition() == desitionData.GO_TO_HAVE_SEX):
                        worldProduct = haveSex.inner(worldProduct,
                        person.getCodeInt())
                    personArray[i] = person
                    region.personList.setPersonArray(personArray)
        return worldProduct
