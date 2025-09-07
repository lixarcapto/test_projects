

from data_model.app.translator_lib.Translator import Translator

class WritePersonPresentationTk:

    def inner(self, personProduct, physicalAppearanceText):
        translator = Translator()
        text = ""
        text += personProduct.getName() + " " + personProduct.getSecondName() + " "
        text += personProduct.getLastName() + " "
        text += personProduct.getSecondLastName() + " "
        text +=  personProduct.getNickname() + " "
        return text
