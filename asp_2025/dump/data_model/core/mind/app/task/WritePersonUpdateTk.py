

from data_model.core.mind.app.task.mental_task.GetMoodNameTk import GetMoodNameTk
from data_access.DataAccess import DataAccess

class WritePersonUpdateTk:

    def writeThoughts(self, personProduct):
        text = ""
        for e in personProduct.psychologicalTraits.thoughtsArray:
            text += e.remimber
        return text

    def inner(self, personProduct):
        getMoodName = GetMoodNameTk()
        translator = DataAccess().createTranslator()
        text = ""
        moodValue = 0
        if(personProduct.body.isDeath):
            text += " murio por " + personProduct.traits.causeOfDeath
        else:
            moodValue = getMoodName.inner(personProduct.psychologicalTraits.moodValue)
            text += " se sentia " + translator.obtainPersonMoodUsing(moodValue) + " por "
            text += self.writeThoughts(personProduct)
        return text
