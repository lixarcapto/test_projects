


from basic.Basic import Basic

class MindKeysData:

    #INNER SENSATION
    def getSensationKeysMap(self):
        array = [
            #negative
            "pain",
            "nauseas",
            "cold",
            "heat",
            "paralysis", #incapacidad de mover
            "irritation",
            "fatigue",
            "dryness",
            "tremors",
            "burning",
            "pressure"
            #positive
            "caress",
            "tickle",
            "touch",
            "hypersensitivity",
            ""
        ]
        return Basic().convertArrayToMap(array)

    def getSoundKeysMap(self):
        array = [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        return Basic().convertArrayToMap(array)

    def getImageKeysMap(self):
        array = [
            #REGION -------------------------
            #relief------------------------------------------
            "deep_sea", #1
            "low_sea", #2
            "depression", #3
            "plain", #4
            "plateau", #6
            "mountain", #7
            "pick", #8
            #soil type---------------------------------------------
            "ground",
            "gravel",
            "rocks",
            "sand",
            "clay",
            "coal",
            "limestone",
            "salt",
            "peat",
            "concrete",
            #sun location-----------------------------------
            "dawnty",
            "sunsety",
            "duskty",
            "darkty"
            #skycolor------------------------------------------
            "reddish_sky",
            #cuando hay neblina o nubes por el atardecer o el amanacer
            "yellowish_sky",
            #cuando hay vientos o lluvias en el desierto durante el dia
            "bluish_sky", #tarde de dia despejado
            "whitish_cloudy_sky", #tarde de dia nublado
            "brown_sky", #por contaminacion urbana en el dia
            "starry_black_sky",
            #visible en lugares altos, sin urbanizacion por la noche
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        return Basic().convertArrayToMap(array)

    def getSussoKeysMap(self):
        array = [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        return Basic().convertArrayToMap(array)

    #tacto
    def getExternalSensationsKeysMap(self):
        array = [
            "cold",
            "heat",
            "burning",
            "rough",
            "smooth",
            "sticky",
            "wet",
            "grainy",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ]
        return Basic().convertArrayToMap(array)
