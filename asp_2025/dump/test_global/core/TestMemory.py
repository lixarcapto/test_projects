



from data_model.core.mind.core.memory.Memory import Memory

class TestMemory:

    def  inner(self):
        memory = Memory()
        for i in range(14):
            memory.addSensation("pain", "circulatory", 4)
        print(memory.writeMemory())
        return
