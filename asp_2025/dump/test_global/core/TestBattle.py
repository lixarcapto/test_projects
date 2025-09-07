


from data_model.core.general.core.date.Date import Date
from data_model.core.battle.Battle import Battle

class TestBattle:

    def inner(self):
        userInput = ""
        textOutput = ""
        battle = Battle()
        while(not battle.combatIsEnd):
            userInput = input()
            if(userInput == "f" or userInput == "end"):
                break
            battle.advanceOneDay(Date(), "", "", "")
            textOutput = battle.writeBattleStage()
            print(textOutput)
        return
