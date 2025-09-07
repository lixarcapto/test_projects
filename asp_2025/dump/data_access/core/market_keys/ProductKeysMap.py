


from basic.Basic import Basic

class ProductKeysMap:

    def __init__(self):
        array = [
            #GOODS
            "chicken_meat",
            "cow_meat",
            "pig_meat",
            "turkey_meat",
            "exotic_meat",
            "wild_meat",
            "blue_fish",
            "white_fish",
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
            #SERVICES
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
        self.INNER = Basic().convertArrayToMap(array)
        return
