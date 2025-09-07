


from data_model.app.translator_lib.Translator import Translator

class WritePhysicalDescriptionTk:

    def inner(self, bodyProduct):
        translator = Translator()
        text = ""
        text += translator.obtainArticle(bodyProduct.getGender()) + " "
        text += translator.obtainAge(bodyProduct.getAgeCode(), bodyProduct.getGender()) + " "
        if(bodyProduct.getIsPregnant() and bodyProduct.getPregnantTime() >= 3):
            text += " embarazada "
        text += translator.obtainWeight(bodyProduct.getWeight()) + " "
        text += translator.obtainHeight(bodyProduct.getHeight()) + " "
        text += "de piel " + translator.obtainSkinColor(bodyProduct.getSkinColor()) + ", "
        text += "con " + translator.obtainHairStyle(bodyProduct.getHairStyle()) + " "
        text += "" + translator.obtainFacialHairStyle(bodyProduct.getFacialHairStyle()) + " "
        text +=  "de color " + translator.obtainHairColor(bodyProduct.getHairColor()) + " "
        text += "y los ojos " + translator.obtainEyeType(bodyProduct.getEyeType()) + " "
        text += "de color " + translator.obtainEyeColor(bodyProduct.getEyeColor())
        return text
