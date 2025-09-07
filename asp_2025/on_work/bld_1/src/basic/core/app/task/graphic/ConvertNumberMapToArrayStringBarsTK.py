



class ConvertNumberMapToArrayStringBarsTK:

    """
        Convierte un array de numeros en una pintura de barras para cmd.
    """

    def inner(self, map, quantityLow,
    quantityMid, spacesToBar, mode):
        text = ""
        lineSymbol = "/"
        colorBarLines = "white"
        colorLow = "red"
        colorMid = "yellow"
        colorHigh = "green"
        if(mode == "<"):
            colorLow = "red"
            colorHigh = "green"
        elif(mode == ">"):
            colorLow = "green"
            colorHigh = "red"
        key = ""
        array = []
        for e in map.keys():
            key = self.fullfillText(e, spacesToBar)
            text = ""
            text += key
            if(map[e] <= quantityLow):
                text += self.colorString(colorBarLines, colorLow)
            elif(map[e] > quantityLow
            and map[e] <= quantityMid):
                text += self.colorString(colorBarLines, colorMid)
            elif(map[e] > quantityMid):
                text += self.colorString(colorBarLines, colorHigh)
            text += lineSymbol * map[e]
            text += self.colorString("white", "black")
            text += " " + str(map[e])
            array.append(text)
        return array
