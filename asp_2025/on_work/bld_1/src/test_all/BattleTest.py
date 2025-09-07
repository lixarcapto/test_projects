


from data_model.core.battle.Battle import Battle

class BattleTest:

    def inner(self):
        battle = Battle()
        battle.armyGarrison.personList.createInitialPerson(6)
        battle.armyInvader.personList.createInitialPerson(6)
        battle.advanceTime()
        print(battle.armyInvader.personList.writePersonData())
