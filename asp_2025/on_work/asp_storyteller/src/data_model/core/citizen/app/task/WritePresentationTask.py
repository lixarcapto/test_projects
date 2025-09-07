



class WritePresentationTask:

    def inner(self, citizenPack):
        text = ""
        text += citizenPack.traitsMap["name"] + " "
        text += citizenPack.traitsMap["second_name"] + " "
        text += citizenPack.traitsMap["lastname"] + " "
        text += citizenPack.traitsMap["second_lastname"] + " "
        text += "also called" + " "
        text += citizenPack.traitsMap["nickname"] + " "
        text += citizenPack.traitsMap["gender"] + " "
        text += "is an" + " "
        text += citizenPack.traitsMap["religion"] + " "
        text += "has " + " "
        text += citizenPack.traitsMap["skin_color"] + " "
        text += "skin " + ", "
        text += citizenPack.traitsMap["eye_type"] + " "
        text += citizenPack.traitsMap["eye_color"] + " "
        text += "eyes" + ", "
        text += citizenPack.traitsMap["hair_type"] + " "
        text += citizenPack.traitsMap["hair_color"] + " "
        text += "hair" + ", "
        text += "talk" + " "
        text += citizenPack.traitsMap["lenguage"] + " "
        text += "write in" + " "
        text += citizenPack.traitsMap["writing"] + " "
        text += "" + " "
        return text
