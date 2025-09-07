


from data_access.core.translation.app.data.ResourcesTranslation import ResourcesTranslation
from basic.Basic import Basic

class Translation:

    def __init__(self):
        self.SIZE_TEXT = 10
        return

    def translateRelief(self, codeInt):
        array = [
            "w", #0
            "=", #1
            "U", #2
            "~", #3
            "Δ", #4
            "m", #5
            "A"  #6
        ]
        text = ResourcesTranslation().inner[codeInt]
        return array[codeInt]

    def translateSoilType(self, codeInt):
        array = [
            "ground",
            "gravel",
            "sand",
            "peat",
            "salt",
            "limestone",
            "rock",
            "clay",
            "paved",
            "humus",
            "ash",
            "loamy",
            "sweet water",
            "saltwater",
            "tar"
        ]
        text = ResourcesTranslation().inner[codeInt]
        return array[codeInt]

    def translateBuildingType(self, codeInt):
        array = [
            "", #0
            "basketry", #1
            "lumberjack-house", #2
            "mine", #3
            "quarry", #4
            "well", #5
            "house", #6
            "weavers-workshop", #7
            "sawmill", #8
            "forest-house", #9
            "craft-workshop", #10
            "windmill", #11
            "bottling-station", #12
            "10", #13
            "11", #14
            "12", #15
            #FARMS
            "farm", #16
            "18", #17
            "19", #18
            "20", #19
            "21", #20
            "13", #21
            "14", #22
            "15", #23
            "16", #24
            "17", #25
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
            "sheep-ranch", #35
            "ranch", #36
            "chicken-ranch", #37
            "", #38
            "horse-ranch", #39
            "", #40
            "", #41
            "elephant-ranch", #42
            "duck-ranch", #43
            "", #44
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
        text = ResourcesTranslation().inner[codeInt]
        return array[codeInt]

    def translateResourceType(self, codeInt):
        text = ResourcesTranslation().inner[codeInt]
        return text
