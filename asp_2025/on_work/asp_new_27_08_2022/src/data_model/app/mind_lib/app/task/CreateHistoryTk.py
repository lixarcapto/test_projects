

#task
from data_model.app.mind_lib.app.task.WriteFullName import WriteFullName

from data_model.app.translator_lib.Translator import Translator

class CreateHistoryTk:

    """
        Escribe una descripcion de todos los datos y eventos vividos en un dia
        por esta persona.
    """
    def writeIntroduceHimself(self, mindProduct):
        writeFullName = WriteFullName()
        text = ""
        physicalSelfDescription = mindProduct.getPhysicalSelfDescription()
        visionRegion = mindProduct.getVisionMemories()
        mindProduct.setNeedToIntroduceHimself(False)
        text +=  writeFullName.inner(mindProduct) + " "
        text += "era " + physicalSelfDescription + " "
        text += "que vivia en " + visionRegion + ".\n\n "
        return text

    def inner(self, mindProduct):
        writeFullName = WriteFullName()
        translator = Translator()
        text = ""
        if(mindProduct.getNeedToIntroduceHimself()):
            text += self.writeIntroduceHimself(mindProduct)
        text += mindProduct.getCurrentDateWritten()
        text += writeFullName.inner(mindProduct) + " "
        text += " " + translator.obtainDesition(mindProduct.desition) + " "
        for e in mindProduct.dailyEventList:
            text += e[2]
        text += ".\n\n "
        mindProduct.dailyEventList.clear()
        mindProduct.history.append(text)
        return mindProduct
