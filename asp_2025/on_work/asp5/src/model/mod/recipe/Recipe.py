


class Recipe:

    """
        Clase que representa un proceso para la creacion
        de un producto.
    """
    def __init__(self, name):
        self.name = name
        self.__goods_required_array = []
        self.__goods_produced_array = []
        self.__services_produced_array = []
        self.__services_required_array = []
        self.__resource_required_array = []
        self.production_days = 0
        None

    # return map
    def create_product_map(self, key, quantity):
        return {"key": key, "quantity": quantity}

    def add_goods_require(self, key, quantity):
        product = self.create_product_map(key, quantity)
        self.__goods_required_array.append(key)

    def add_goods_produced(self, key, quantity):
        product = self.create_product_map(key, quantity)
        self.__goods_produced_array.append(key)

    def add_services_produced(self, key, quantity):
        product = self.create_product_map(key, quantity)
        self.__goods_produced_array.append(key)

    def add_services_required(self, key, quantity):
        product = self.create_product_map(key, quantity)
        self.__goods_produced_array.append(key)

    def add_resource_required(self, key, quantity):
        product = self.create_product_map(key, quantity)
        self.__resource_required_array.append(key)

    def build(self, name):
        None
