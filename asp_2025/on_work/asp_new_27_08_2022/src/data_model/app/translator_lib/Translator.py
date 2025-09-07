


import data_model.app.translator_lib.app.PersonTranslateData as PersonTranslateData
import data_model.app.translator_lib.app.RegionTranslateData as RegionTranslateData

class Translator:

    def __init__(self):
        self.personTranslate = PersonTranslateData.PersonTranslateData()
        self.regionTranslate = RegionTranslateData.RegionTranslateData()
        return

    def obtainRelief(self, number):
        return self.regionTranslate.reliefArray[number]

    def obtainTypeSoil(self, number):
        return self.regionTranslate.typeSoilArray[number]

    def obtainBiome(self, number):
        return self.regionTranslate.biomeArray[number]

    def obtainTemperatureRegime(self, number):
        return self.regionTranslate.temperatureRegimeArray[number]

    def obtainWindRegime(self, number):
        return self.regionTranslate.windRegimeArray[number]

    def obtainWeight(self, number):
        return self.personTranslate.weightArray[number]

    def obtainHeight(self, number):
        return self.personTranslate.heightArray[number]

    def obtainSkinColor(self, number):
        return self.personTranslate.skinColorArray[number]

    def obtainAge(self, number, gender):
        size = len(self.personTranslate.ageArray)
        if(gender == 0):
            return self.personTranslate.AGE_TO_MALES_TEXT_ARRAY[number]
        elif(gender == 1):
            return self.personTranslate.AGE_TO_FEMALES_TEXT_ARRAY[number]
        elif(gender == 3):
            return self.personTranslate.AGE_TO_HERMAFRODITE_MALES_TEXT_ARRAY[number]
        elif(gender == 4):
            return self.personTranslate.AGE_TO_HERMAFRODITE_FEMALES_TEXT_ARRAY[number]
        return text

    def obtainSexualOrientation(self, number):
        return self.personTranslate.ORIENTATION_TEXT_ARRAY[number]

    def obtainArticle(self, number):
        return self.personTranslate.ARTICLE_TEXT_ARRAY[number]

    def obtainCulture(self, number):
        return self.personTranslate.cultureArray[number]

    def obtainPronoums(self, number):
        return self.personTranslate.pronoumsArray[number]

    def obtainHealthState(self, number):
        return self.personTranslate.healthStateArray[number]

    def obtainDesition(self, number):
        if(number >= len(self.personTranslate.DESITION_ARRAY)):
            return ""
        else:
            return self.personTranslate.DESITION_ARRAY[number]

    def obtainDesitionConsequence(self, number):
        return self.personTranslate.desitionConsequenceArray[number]

    def obtainEyeColor(self, number):
        return self.personTranslate.eyeColor[number]

    def obtainHairColor(self, number):
        return self.personTranslate.hairColor[number]

    def obtainEyeType(self, number):
        return self.personTranslate.eyeTypeArray[number]

    def obtainPersonMoodUsing(self, number):
        return self.personTranslate.PERSON_MOOD_TEXT_ARRAY[number]

    def obtainHairStyle(self, number):
        return self.personTranslate.HAIR_STYLE_TEXT_ARRAY[number]

    def obtainFacialHairStyle(self, number):
        return self.personTranslate.FACIAL_HAIR_STYLE_TEXT_ARRAY[number]

    def obtainDayName(self, number):
        return self.regionTranslate.DAY_NAME_TEXT_ARRAY[number]

    def obtainMonthName(self, number):
        return self.regionTranslate.MONTH_TEXT_ARRAY[number]

    def obtainCulture(self, number):
        return self.personTranslate.CULTURE_NAMES_TEXT_ARRAY[number]
