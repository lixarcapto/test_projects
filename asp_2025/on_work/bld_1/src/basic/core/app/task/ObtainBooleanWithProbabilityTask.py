



class ObtainBooleanWithProbabilityTask:

    def obtainBooleanWithProbability(self, probability):
        result = random.randint(0, 100)
        if(result < probability):
            return True
        return False
