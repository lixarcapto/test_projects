



from basic.Basic import Basic

class EyeTypeMapData:

    def __init__(self):
        array = [
            "asian", #ASIATICO
            "round", #EUROPEO
            "nutty", #INDIGENA
            "separated", #MONGOLOIDES Y AFRICANOS
            "together", #JUNTOS
            "droopy"
        ]
        self.INNER = Basic().convertArrayToMap(array)
