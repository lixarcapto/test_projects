



from data_access.core.translator.app.data.PhysicalTraitsTextData import PhysicalTraitsTextData
from data_access.core.translator.app.data.MentalTextData import MentalTextData
from data_access.core.translator.app.data.RegionTextData import RegionTextData

class Translator:

    def __init__(self):
        return

#--- PHYSICAL ------------------------------------------------------------------

    def obtainSkinColor(self, vInt):
        return PhysicalTraitsTextData().SKIN_COLOR_TEXT_ARRAY[vInt]

    def obtainNoseType(self, vInt):
        return PhysicalTraitsTextData().NOSE_TYPE_TEXT_ARRAY[vInt]

    def obtainEyeType(self, vInt):
        return PhysicalTraitsTextData().EYE_TYPE_TEXT_ARRAY[vInt]

    def obtainEyeColor(self, vInt):
        return PhysicalTraitsTextData().EYE_COLOR_TEXT_ARRAY[vInt]

    def obtainJawType(self, vInt):
        return PhysicalTraitsTextData().JAW_TYPE_TEXT_ARRAY[vInt]

    def obtainHeight(self, vInt):
        return PhysicalTraitsTextData().HEIGHT_TEXT_ARRAY[vInt]

    def obtainMuscle(self, vInt):
        return PhysicalTraitsTextData().MUSCLE_TEXT_ARRAY[vInt]

    def obtainHairColor(self, vInt):
        return PhysicalTraitsTextData().HAIR_COLOR_TEXT_ARRAY[vInt]

    def obtainFreckles(self, vInt):
        return PhysicalTraitsTextData().FRECKLES_TYPE_TEXT_ARRAY[vInt]

    def obtainHairType(self, vInt):
        return PhysicalTraitsTextData().HAIR_TYPE_TEXT_ARRAY[vInt]

    def obtainHairStyle(self, vInt):
        return PhysicalTraitsTextData().HAIR_STYLE_TEXT_ARRAY[vInt]

    def obtainFacialHairStyle(self, vInt):
        return PhysicalTraitsTextData().FACIAL_HAIR_TEXT_ARRAY[vInt]

    def obtainWeight(self, vInt):
        return PhysicalTraitsTextData().WEIGHT_TEXT_ARRAY[vInt]

    def obtainSexualOrientation(self, number):
        return MentalTextData().ORIENTATION_TEXT_ARRAY[number]

    def obtainArticle(self, number):
        return PhysicalTraitsTextData().ARTICLE_TEXT_ARRAY[number]

    def obtainPronoums(self, number):
        return PhysicalTraitsTextData().PRONOUMS_TEXT_ARRAY[number]

    def obtainHealthState(self, number):
        return PhysicalTraitsTextData().HEALTH_STATE_DATA[number]

    def obtainOrganType(self, number):
        return PhysicalTraitsTextData().ORGAN_TYPE_TEXT_ARRAY[number]

    def obtainAge(self, number, gender):
        if(gender == 0):
            return PhysicalTraitsTextData().AGE_TO_MALES_TEXT_ARRAY[number]
        elif(gender == 1):
            return PhysicalTraitsTextData().AGE_TO_FEMALES_TEXT_ARRAY[number]
        return text

#--- REGION ----------------------------------------------------------------------

    def obtainRelief(self, number):
        return RegionTextData().RELIEF_TEXT_ARRAY[number]

    def obtainTypeSoil(self, number):
        return RegionTextData().TYPE_SOIL_TEXT_ARRAY[number]

    def obtainBiome(self, number):
        return RegionTextData().BIOME_TEXT_ARRAY[number]

    def obtainTemperatureRegime(self, number):
        return RegionTextData().TEMPERATURE_REGIME_TEXT_ARRAY[number]

    def obtainWindRegime(self, number):
        return RegionTextData().WIND_REGIME_TEXT_ARRAY[number]

    def obtainDayName(self, number):
        return RegionTextData().DAY_NAME_TEXT_ARRAY[number]

    def obtainMonthName(self, number):
        return RegionTextData().MONTH_TEXT_ARRAY[number]

    def obtainCulture(self, number):
        return RegionTextData().CULTURE_NAMES_TEXT_ARRAY[number]

#---   -----------------------------------------------------------------------------

    def obtainCulture(self, number):
        return MentalTextData().CULTURE_TEXT_ARRAY[number]

    def obtainSensationsType(self, number):
        return MentalTextData().SENSATIONS_TYPE_TEXT_ARRAY[number]

    def obtainExternalSensationsType(self, number):
        return MentalTextData().EXTERNAL_SENSATIONS_TYPE_TEXT_ARRAY[number]

    def obtainImageType(self, number):
        return MentalTextData().IMAGE_TYPE_TEXT_ARRAY[number]

    def obtainDesition(self, number):
        if(number >= len(MentalTextData().DESITION_ARRAY)):
            return ""
        else:
            return MentalTextData().DESITION_ARRAY[number]

    def obtainPersonMood(self, number):
        return MentalTextData().PERSON_MOOD_TEXT_ARRAY[number]

    def obtainPersonMood(self, number):
        return MentalTextData().IMAGE_TYPE_TEXT_ARRAY[number]
