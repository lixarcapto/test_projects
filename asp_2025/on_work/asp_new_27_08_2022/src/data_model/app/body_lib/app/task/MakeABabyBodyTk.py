

from data_model.app.body_lib.app.product.PersonBodyProduct import PersonBodyProduct

class MakeABabyBodyTk:

    """
        Crea un embryon mesclando genetica del padre y madre y retornando
        un bodyProduct
    """
    def inner(self, personBodyMom, personBodyDad):
        embryo = PersonBodyProduct()
        if(random.randint(0, 1) == 0):
            embryo.setEyeType(personA.inner.getEyeType())
        else:
            embryo.setEyeType(personB.inner.getEyeType())
        if(random.randint(0, 1) == 0):
            embryo.setHairType(personA.inner.getHairType())
        else:
            embryo.setHairType(personB.inner.getHairType())
        if(random.randint(0, 1) == 0):
            embryo.setEyeColor(personA.inner.getEyeColor())
        else:
            embryo.setEyeColor(personB.inner.getEyeColor())
        if(random.randint(0, 1) == 0):
            embryo.setHairType(personA.inner.getHairType())
        else:
            embryo.setHairType(personB.inner.getHairType())
        if(random.randint(0, 1) == 0):
            embryo.setSkinColor(personA.inner.getSkinColor())
        else:
            embryo.setSkinColor(personB.inner.getSkinColor())
        if(random.randint(0, 1) == 0):
            embryo.setHeight(personA.inner.getHeight())
        else:
            embryo.setHeight(personB.inner.getHeight())
        if(random.randint(0, 1) == 0):
            embryo.setCaste(personA.inner.getCaste())
        else:
            embryo.setCaste(personB.inner.getCaste())
        if(random.randint(0, 1) == 0):
            embryo.setGender(personA.PERSON_KEYS.SEX.MALE)
        else:
            embryo.setGender(personA.PERSON_KEYS.SEX.FEMALE)
        personBodyMom.embryo = embryo
        personBodyMom.isPregnant = True
        personBodyMom.inner.embryo = embryo
        array = []
        array.append(personBodyMom)
        array.append(personBodyDad)
        return array
