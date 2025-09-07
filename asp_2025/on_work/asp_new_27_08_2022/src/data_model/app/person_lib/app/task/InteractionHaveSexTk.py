



class InteractionHaveSexTk:

    #tienen sexo dos veces una para cada uno
    def inner(self, personProductA, personProductB):
        personArray = None
        personArray = personProductB.body.haveSex(personProductA.body)
        personProductB.body = personArray[0]
        personProductA.body = personArray[1]
        personArray = personProductA.body.haveSex(personProductB.body)
        personProductA.body = personArray[0]
        personProductB.body = personArray[1]
        array = []
        array.append(personProductA)
        array.append(personProductB)
        return array
