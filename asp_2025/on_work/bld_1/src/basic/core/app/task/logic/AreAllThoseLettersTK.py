


from basic.core.app.task.logic.IsALetterTK import IsALetterTK

class AreAllThoseLettersTK:

    def inner(self, text):
        letter = ""
        if(len(text) == 1):
            if(not IsALetterTK().inner(text)):
                return False
            return True
        for i in range(len(text)):
            letter = text[i:i+1]
            if(not IsALetterTK().inner(letter)):
                return False
        return True
