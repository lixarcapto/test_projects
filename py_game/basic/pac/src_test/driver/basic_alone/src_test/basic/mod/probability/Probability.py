

import random

class Probability:

    """
        Es un objeto que sirve para calcular probabilidades
        multiples. Para usarlo deben enviarse con el metodo add
        claves con su probabilidad entera; y el metodo calculate
        generara un resultado basado en esas probabilidades.
    """

    def __init__(self):
        self.matrix = []
        None

    """
        Añade una nueva probabilidad al calculador; esta
        debe contener una clave string y un porcentaje integer.
    """
    def add(self, key, porcentage):
        probability = {}
        probability["key"] = key
        probability["porcentage"] = porcentage
        self.matrix.append(probability)

    """
        Es una funcion que elije una clave basada en las
        probabilidades enviadas anteriormente.
        Si el resultado esta fuera de las probabilidades calculadas
        retornara una clave none; si esta por encima de las
        probabilidades enviara un error.
    """
    def calculate(self):
        TOTAL = 100
        key_none = "none"
        key_result = ""
        result_index = random.randint(0, TOTAL)
        array_probability = []
        # comprobar si el limite es 100
        counter = 0
        for e in self.matrix:
            counter += e["porcentage"]
        if(counter > TOTAL):
            print("/Error: porcentaje es mayor a 100 ")
            return key_none
        for e in self.matrix:
            for i in range(e["porcentage"]):
                array_probability.append(e["key"])
        while(len(array_probability) < TOTAL):
            array_probability.append(key_none)
        key_result = array_probability[result_index -1]
        return key_result