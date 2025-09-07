
import data_model.app.person.PersonProduct as PersonProduct

class Person:

    def __init__(self):
        self.product = PersonProduct.PersonProduct()

    def writeData(self):
        textStr = ""
        textStr += self.product.name + " " + self.product.secondName
        textStr += " " + self.product.lastName + " " + self.product.secondLastName
        textStr += " tambien conocido como " + self.product.nickName
        return textStr
