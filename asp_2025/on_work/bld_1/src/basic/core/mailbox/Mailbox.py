



class Mailbox:

    def __init__(self):
        self.actualProcess = ""
        self.counter = 0
        self.text = ""
        self.marginSize = 5
        return

    def start(self, text):
        self.text += "INIT " + text + "():\n"

    def addError(self, text, example):
        self.text += " " * self.marginSize + "<!>Error " + str(self.counter)
        self.text += " with \"\"" + example + "\"\"" + " due to "
        self.text += text + ".\n"
        self.counter += 1

    def addMessage(self, text):
        self.text += + "<!>Error " + str(self.counter)
        self.text += " in " + text + ".\n"
        self.counter += 1

    def obtainMessage(self):
        text = self.text
        self.text = ""
        return text
