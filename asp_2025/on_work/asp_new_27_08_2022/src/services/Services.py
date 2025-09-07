


class Services:

    def __init__(self):
        self.dataModel = DataModelV2()

    def obtainBooleanWithProbability(probability):
        result = random.randint(0, 100)
        if(result < probability):
            return True
        return False
