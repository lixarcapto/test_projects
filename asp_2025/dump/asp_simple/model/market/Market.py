



class Market:

    """
    Clase que representa al mercado de 
    productos. Utiliza un sistema de
    almacenamiento de variables tipo 
    int estaticas. NO usa diccionarios
    ni listas porque es mucha memoria
    RAM para tantas regiones.
    """

    def __init__(self):
        self.food:int = 0
        self.meat:int = 0 
        self.water:int = 0
        self.delicacies:int = 0 
        self.vegetables:int = 0 
        self.paper:int = 0 
        self.soap:int = 0 
        self.electricity:int = 0 
        self.gas:int = 0 
        self.wood:int = 0 
        self.gasoline:int = 0 
        self.jar:int = 0

    def write(self)->str:
        return "" \
        + f"{self.food=}\n" \
        + f"{self.meat=}\n" \
        + f"{self.water=}\n" \
        + f"{self.delicacies=}\n" \
        + f"{self.vegetables=}\n" \
        + f"{self.paper=}\n" \
        + f"{self.soap=}\n" \
        + f"{self.electricity=}\n" \
        + f"{self.gas=}\n" \
        + f"{self.wood=}\n" \
        + f"{self.gasoline=}\n" \
        + ""

    def sum_value(self, KEY:str, VALUE:int):
        match KEY:
            case "food": 
                self.food += VALUE
            case "meat": 
                self.meat += VALUE
            case "water": 
                self.water += VALUE
            case "delicacies": 
                self.delicacies += VALUE
            case "vegetables": 
                self.vegetables += VALUE
            case "paper": 
                self.paper += VALUE
            case "soap": 
                self.soap += VALUE
            case "electricity": 
                self.electricity += VALUE
            case "gas": 
                self.gas += VALUE
            case "wood": 
                self.wood += VALUE
            case "gasoline": 
                self.gasoline += VALUE
            case "containers": 
                self.jar += VALUE

