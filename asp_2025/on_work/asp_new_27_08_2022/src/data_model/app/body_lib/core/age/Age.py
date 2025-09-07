




class Age:

    def __init__(self):
        self.age = 0
        self.yearsCounter = 0
        self.daysAge = 0
        self.weeksAge = 0
        self.monthsAge = 0
        self.yearsAge = 0
        self.fulfiledYears = False

    #MODIFIER-------------------------------------------------------------------------------

    def advanceOneDay(self):
        self.daysAge += 1
        if(self.daysAge == 3):
            self.daysAge = 0
            self.weeksAge += 1
        if(self.weeksAge == 1):
            self.weeksAge = 0
            self.monthsAge += 1
        if(self.monthsAge == 3):
            self.monthsAge = 0
            self.yearsAge += 1
            self.yearsCounter += 1
            self.fulfiledYears = True
        if(self.yearsAge == 3):
            self.yearsAge = 0
            self.age += 1

    def isEqualTo(self, age):
        if(age.getAge() != self.getAge()):
            return False
        if(age.getDaysAge() != self.getDaysAge()):
            return False
        if(age.getWeeksAge() != self.getWeeksAge()):
            return False
        if(age.getMonthsAge() != self.getMonthsAge()):
            return False
        if(age.getYearsAge() != self.getYearsAge()):
            return False
        return True

    def checkFulfiledYears(self):
        if(self.fulfiledYears == True):
            self.fulfiledYears = False
            return True
        return False

    def writeAge(self):
        text = ""
        text = " tiene " + str(self.yearsCounter) + " año " + str(self.monthsAge) + " meses"
        text += " " + str(self.weeksAge) + " semanas y " + str(self.daysAge) + " dias"
        return text

    #ACCESSORS-----------------------------------------------------------------------------


    def setAge(self, codeInt):
        self.age = codeInt

    def getAge(self):
        return self.age

    def getDaysAge(self):
        return self.daysAge

    def getWeeksAge(self):
        return self.weeksAge

    def getMonthsAge(self):
        return self.monthsAge

    def getYearsAge(self):
        return self.yearsAge

    def getYearsCounter(self):
        return self.yearsCounter

    #-------------------------------------------------------------------------------------
