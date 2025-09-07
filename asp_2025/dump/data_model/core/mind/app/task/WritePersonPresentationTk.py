

from data_access.DataAccess import DataAccess

class WritePersonPresentationTk:

    def inner(self, personProduct, physicalAppearanceText):
        translator = DataAccess().createTranslator()
        text = ""
        text += personProduct.getName() + " " + personProduct.getSecondName() + " "
        text += personProduct.getLastName() + " "
        text += personProduct.getSecondLastName() + " "
        text +=  personProduct.getNickname() + " "
        return text
