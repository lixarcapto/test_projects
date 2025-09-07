


from basic.core.app.task.logic.IsANumberTK import IsANumberTK

class AreAllThoseNumbersTK:

    def inner(self, text):
        letter = ""
        if(len(text) == 1):
            if(not IsANumberTK().inner(text)):
                return False
            return True
        for i in range(len(text)):
            letter = text[i:i+1]
            if(not IsANumberTK().inner(letter)):
                return False
        return True
