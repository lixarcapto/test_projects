



class Market:

    """
    Esta clase representa a un almacen
    de productos que pueden adquirir
    y consumir los personajes.
    """

    PRODUCT_LIST:list[str] = [
        # PRODUCTS
        "FOOD",
        "WATER",
        "HOUSES",
        "CARS",
        "FAT",
        "FABRICS",
        "FIBERS",
        "WOOD",
        "GAS",
        "TOOLS",
        "SALT",
        "VINEGAR",
        "FERTILIZER",
        "MEDICINES",
        "PAPER",
        # WORKS SERVICES
        "FARM",
        "RANCH",
        # WORKS OFFERT
        "TRAINEE",
        "CHEF",
        "PEASANT",
        "WOODSMAN",
        "SOLDIER",
        "BUILDER",
        "WORKER",
        "TEACHER",
        "SAILOR",
        "ARTIST",
        "TAILOR",
        "DOCTOR",
        "CHEMICAL",
        "MECHANIC",
        "BOSS",
        "CLERK",
        "LAWYER",
        "CRIMINAL",
        "DRIVING",
        "TRADER",
        "PRIEST",
        "ASSISTANT",
        "PILOT",
        "ELECTRICIAN"
    ]

    def __init__(self):
        self.product_dict:dict[int] = {}
        self.demand_dict:dict[int] = {}
        self.last_demand_dict:dict[int] = {}
        for k in Market.PRODUCT_LIST:
            self.product_dict[k] = 1000
            self.demand_dict[k] = 0
            self.last_demand_dict[k] = 0

    def render_dict_number(self)->dict[int]:
        dict_ = {}
        for k in self.product_dict:
            dict_[k] = str(self.product_dict[k])\
            + f" ( {str(self.last_demand_dict[k])} )"
        return dict_

    def write(self)->str:
        """
        Funcion que escribe una 
        representacion textual de las 
        variables del mercado.
        """
        txt = "Market:\n"
        n = 0
        for k in self.product_dict:
            txt += f"{n}). {k} = {self.product_dict[k]}\n"
            n += 1
        txt += "\n"
        return txt

    def advance_one_day(self):
        self.last_demand_dict\
            = self.demand_dict
        for k in self.demand_dict:
            self.demand_dict[k] = 0

    def sum_product(self, KEY:str, SUM:int)\
            ->None:
        """
        Funcion que suma una cantidad 
        al producto determinado.
        """
        self.product_dict[KEY] += SUM
        self.demand_dict[KEY] += SUM

    def has_quantity(self, KEY:str, 
            QUANTITY:int)->bool:
        """
        Funcion que indica si el mercado
        tiene la cantidad determinada
        del producto.
        """
        PRODUCT_N = self.product_dict[KEY]
        if(PRODUCT_N >= QUANTITY):
            return True
        return False
    
    def sum_product_dict(self, DICT)\
            ->bool:
        v:int = 0
        k:str = ""
        for k in DICT:
            self.sum_product(k, DICT[k])

    def subtract_product_dict(self, DICT)\
            ->bool:
        v:int = 0
        k:str = ""
        for k in DICT:
            self.sum_product(
                k, 
                DICT[k] * -1
            )
    
    def has_product_dict(self, DICT)\
            ->bool:
        v:int = 0
        k:str = ""
        has_product:bool = False
        for k in DICT:
            v = DICT[k]
            has_product = self\
                .has_quantity(k, v)
            if(not has_product):
                return False
        return True