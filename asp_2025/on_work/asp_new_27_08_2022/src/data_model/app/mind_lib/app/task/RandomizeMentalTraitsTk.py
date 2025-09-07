


from data_model.app.mind_lib.app.task.RandomizeLastnameTk import RandomizeLastnameTk
from data_model.app.mind_lib.app.task.RandomizeNameTk import RandomizeNameTk

class RandomizeMentalTraitsTk:

    def inner(self, mindProduct, culture, gender):
        randomizeName = RandomizeNameTk()
        randomizeLastname = RandomizeLastnameTk()
        mindProduct.setCulture(culture)
        mindProduct.setName(randomizeName.inner(mindProduct.getCulture(), gender))
        mindProduct.setSecondName(randomizeName.inner(mindProduct.getCulture(), gender))
        mindProduct.setLastName(randomizeLastname.inner(mindProduct.getCulture(),
        mindProduct.getCaste()))
        mindProduct.setSecondLastName(randomizeLastname.inner(mindProduct.getCulture(),
        mindProduct.getCaste()))
        return mindProduct
