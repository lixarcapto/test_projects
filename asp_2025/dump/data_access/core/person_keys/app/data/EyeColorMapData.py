


from basic.Basic import Basic

class EyeColorMapData:

    def __init__(self):
        array = [
            "gray",
            "black",
            "brown",
            "blue",
            "skyblue",
            "light_brown",
            "red",
            "green"
        ]
        self.INNER = Basic().convertArrayToMap(array)
