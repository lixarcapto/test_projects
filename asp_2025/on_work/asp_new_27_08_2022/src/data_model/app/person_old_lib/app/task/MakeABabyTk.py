




class MakeABabyTk:

    """
        Crea un producto bebe que sera almacenado en el cuerpo de la madre, este contara
        con apellido, relacion padre y madre y un cuerpo propio.
    """
    def inner(self, personProductMom, personProductDad):
        embryo = personProductMom.inner.personBody.embryo
        embryo.relationList.addRelation(0, personA.traits.getCodeInt(), "mother")
        embryo.relationList.addRelation(0, personB.traits.getCodeInt(), "father")
        personProductMom.inner.personBody.embryo = embryo
        secondName = personA.traits.getSecondName()
        embryo.traits.setSecondName(secondName)
        lastName = personB.traits.getLastName()
        embryo.traits.setLastName(lastName)
        array = []
        array.append(personProductA)
        array.append(personProductB)
        return array
