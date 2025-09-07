


from presenter.core.presentation_lib.link.QuestionProduct import QuestionProduct

class RequestMessage:

    def __init__(self):
        self.updateText = ""
        self.questionArray = []
        self.responseArray = []
        self.separatorSymbol = ">"
        self.distanceBetwenMargin = 1
        return

    def config(separatorSymbol, distanceBetwenMargin):
        self.separatorSymbol = separatorSymbol
        self.distanceBetwenMargin = distanceBetwenMargin

    def addQuestion(self, text, optionsArray):
        question = QuestionProduct()
        question.text = text
        question.optionsArray = optionsArray
        self.questionArray.append(question)
