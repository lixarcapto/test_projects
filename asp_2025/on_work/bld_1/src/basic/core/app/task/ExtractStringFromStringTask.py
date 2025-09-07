


import random

class ExtractStringFromStringTask:

    def __init__(self):
        self.messagesOnHold = ""

    def inner(self, text, textToFind, endKey):
        indexInit = text.find(textToFind)
        char = ""
        i = indexInit + len(textToFind)
        result = ""
        textFinal = ""
        nameError = "<!>Error extractFromString()"
        if(len(text) < 2):
            self.messagesOnHold += nameError + " text less than 2 [" + text + "]."
            return ""
        if(len(text) < 1):
            self.messagesOnHold += nameError + " textToFind less than 1 [" + textToFind + "]."
            return ""
        while(i < len(text)):
            char = text[i:i + 1]
            if(char == endKey):
                result = textFinal
                break
            textFinal += char
            if(endKey == "*//"
            and i == len(text) -1):
                result = textFinal
                break
            if(len(text)-1 == i):
                self.messagesOnHold += nameError + " not has endkey  [" + endKey + "]."
                return ""
            i += 1
            if(i > 1000):
                self.messagesOnHold += nameError + " limit iteration " + str(i) + "."
                result = ""
                break
        return result
