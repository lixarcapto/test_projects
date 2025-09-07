



from data_model.core.body.core.system.System import System

class TestSystem:

    def inner(self):
        system = System()
        system.causeDamage("burn", 3)
        for i in range(3):
            system.advanceTime()
        print(system.writeAppearance())
