

class WriteFullName:

    def inner(self, personProduct):
        text = ""
        text += personProduct.getName() + " "
        text += personProduct.getSecondName() + " "
        text += personProduct.getLastName() + " "
        text += personProduct.getSecondLastName() + " "
        text += personProduct.getNickname()
        return text
