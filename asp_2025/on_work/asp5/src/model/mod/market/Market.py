

from .product_keys_const import*

class Market:

    KEYS_CHANGE = ["--", "++", "**"]

    """
        Clase que representa a un mercado de producto y
        todas sus interacciones.
    """
    def __init__(self):
        self.product_map = {}
        self.create_keys_product()

    """
        Funcion que escribe los productos del mercado como
        una lista estadistica.
    """
    # return string
    def write_market(self):
        text = "market information: \n"
        margin = " " * 3
        product = {}
        for k in self.product_map:
            product = self.product_map[k]
            text += margin + k + ": " \
            + str(product["former"]) + "/" \
            + str(product["actual"]) + " " \
            + product["change"] + "\n"
        return text

    """
        Funcion que crea un diccionario predefinido para los
        productos del mercado.
    """
    # return key_value_map
    def create_product_map(self):
        map = {"actual": 0, "former": 0, "change": "**"}
        return map

    """
        Funcion que inicia todos los productos predefinidos del
        mercado en la constante PRODUCT_KEYS_CONST
    """
    def create_keys_product(self):
        for e in PRODUCT_KEYS_CONST:
            self.product_map[e] = self.create_product_map()

    """
        Funcion que pregunta si tiene la cantidad de producto
        indicada.
    """
    # return boolean
    def has(self, key, quantity):
        product = self.product_map[key]
        if product["actual"] >= quantity: return True
        return False

    """
        Funcion que extrae la cantidad de producto indicada.
    """
    # return int
    def extract(self, key, quantity):
        value = self.product_map[key]["actual"]
        self.product_map[key]["actual"] -= quantity
        return value

    def advance_time(self):
        self.save_former()

    """
        Funcion que suma los productos de forma rapida y facil.
    """
    def sum(self, key, quantity):
        self.product_map[key]["actual"] += quantity

    """
        Funcion que guarda los datos del producto anterior
        y analiza si hubo o no incrementos y decrementos.
    """
    def save_former(self):
        product = {}
        for k in self.product_map:
            product = self.product_map[k]
            if(product["actual"] < product["former"]):
                product["change"] = "++"
            elif(product["actual"] == product["former"]):
                product["change"] = "**"
            elif(product["actual"] > product["former"]):
                product["change"] = "--"
            product["former"] = product["actual"]
            self.product_map[k] = product
