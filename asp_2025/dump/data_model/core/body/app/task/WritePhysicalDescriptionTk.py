


from data_access.DataAccess import DataAccess

class WritePhysicalDescriptionTk:

    def inner(self, bodyProduct):
        translator = DataAccess().createTranslator()
        genes = bodyProduct.getGenesThis()
        text = ""
        text += translator.obtainArticle(bodyProduct.getGender()) + " "
        text += translator.obtainAge(bodyProduct.getAgeCode(), bodyProduct.getGender()) + " "
        if(bodyProduct.getIsPregnant() and bodyProduct.getPregnantTime() >= 3):
            text += " embarazada "
        text += translator.obtainWeight(bodyProduct.getWeight()) + " "
        text += translator.obtainHeight(bodyProduct.getHeight()) + " "
        text += "de piel " + translator.obtainSkinColor(genes.getSkinColor()) + ", "
        text += "con pelo " + translator.obtainHairType(genes.getHairType()) + " "
        text += "" + translator.obtainFacialHairStyle(bodyProduct.getFacialHairStyle()) + " "
        text +=  "de color " + translator.obtainHairColor(genes.getHairColor()) + " "
        text += "y los ojos " + translator.obtainEyeType(genes.getEyeType()) + " "
        text += "de color " + translator.obtainEyeColor(genes.getEyeColor())
        return text
