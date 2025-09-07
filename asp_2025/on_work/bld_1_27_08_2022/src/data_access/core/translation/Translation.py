


from data_access.core.translation.app.data.ResourcesTranslation import ResourcesTranslation
from basic.Basic import Basic

class Translation:

    def __init__(self):
        return

    def translateSoilType(self, codeInt):
        array = [
            "tierra ",
            "grava  ",
            "arena  ",
            "turba  ",
            "sal    ",
            "caliza ",
            "roca   ",
            "arcilla",
            "pavimen",
            "humus  ",
            "cenizas",
            "limo   "
        ]
        return array[codeInt]

    def translateBuildingType(self, codeInt):
        array = [
            "       ", #0
            "basketr", #1
            "lumberj", #2
            "mine   ", #3
            "quarry ", #4
            "well   ", #5
            "house  ", #6
            "weavers", #7
            "sawmill", #8
            "foresth", #9
            "", #10
            "", #11
            "", #12
            "", #13
            "", #14
            "", #15
            #FARMS
            "flaxf  ", #16
            "wheatf ", #17
            "mintf  ", #18
            "cornf  ", #19
            "milletf", #20
            "", #21
            "", #22
            "", #23
            "", #24
            "", #25
            "", #26
            "", #27
            "", #28
            "", #29
            "", #30
            "", #31
            "", #32
            "", #33
            "", #34
            #LIVESTOCKING
            "sheep r", #35
            "cow r  ", #36
            "chicken", #37
            "turkey ", #38
            "horse r", #39
            "pig r  ", #40
            "goat r ", #41
            "elephan", #42
            "duck r ", #43
            "donkeyr", #44
            "", #45
            "", #46
            "", #47
            "", #48
            "", #49
            "", #50
            "", #51
            "", #52
            "", #53
            "", #54
            "", #55
            "", #56
            "", #57
            "", #58
            "", #59
            "", #60
            "", #61
            "", #62
            "", #63
            "", #64
            "", #65
            "", #66
            "", #67
            "", #68
            "", #69
            "", #70
            "", #71
            "", #72
            "", #73
            "", #74
            "", #75
            "" #76
        ]
        return array[codeInt]

    def translateResourceType(self, codeInt):
        text = ResourcesTranslation().inner[codeInt]
        text = Basic().fullfillText(text, 7)
        return text
