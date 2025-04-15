


from ....btpy_maths.mod.percent\
    .percent_from_part import*
from ....btpy_list.mod.count_true_checks.count_true_checks import*

class Tester:

    """
    Clase que permite almacenar resultados
    de test en tipos boolean con su titulo
    y calcular porcetages de exito
    facilmente.
    """

    def __init__(self, NAME) -> None:
        self.name = NAME
        self.__bool_dict = {}

    def set_test(self, NAME, RESULT):
        self.__bool_dict[NAME] = RESULT

    def write(self):
        number = count_true_checks(
            self.__bool_dict,
            lambda e:e == False
        )
        size = len(self.__bool_dict)
        percent = percent_from_part(
                number, 
                size
        )
        percent = round(percent)
        txt = f"{self.name} : {percent}%\n"
        for k in self.__bool_dict:
            txt += f"{k} = "
            if(self.__bool_dict[k]):
                txt += "success"
            else: 
                txt += "fail"
            txt += "\n"
        return txt

    def __str__(self):
        return self.write()