




class FullfillTextTask:

    def inner(self, text, size):
        sizeMaximum = size
        if(len(text) < sizeMaximum):
            spacesRemaining = sizeMaximum - len(text)
            addText = " " * spacesRemaining
            text += addText
        if(len(text) > sizeMaximum):
            text = text[0:sizeMaximum]
        return text
