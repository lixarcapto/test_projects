

from .Structure import Structure

class Territory:

    def __init__(self):
        self.__structure_list:list = []
        self.randomize_structures()

    def render_structures(self)->list:
        struct:Structure = None
        list_:list[str] = []
        for struct in self.__structure_list:
            list_.append(struct.get_type())
        return list_

    def write(self)->str:
        txt = ""
        struct:Structure = None
        for struct in self.__structure_list:
            print(
                struct.get_type(),
                "life_time" , struct.life_time
            )

    def randomize_structures(self):
        pass
        list_ = [
            "aquifer", 
            "aquifer",
            "fountain",
            "forest",
            "farm"
        ]
        for k in list_:
            self.create_structure(k)

    def create_structure(self, 
                TYPE_KEY:str)->None:
        structure = Structure(TYPE_KEY)
        self.__structure_list.append(
            structure
        )

    def has_sources_dict(self, dict_):
        v = None
        if(dict_ == {}): return True
        for k in dict_:
            v = dict_[k]
            if(not self.has_source(k, v)):
                return False
        return True
    
    def has_source(self, KEY_SOURCE:str,
            QUANTITY:int):
        struct:Structure = None
        key = ""
        for struct in self.__structure_list:
            key = struct.get_type()
            if(key == KEY_SOURCE
            and struct.has_life_time(
                    QUANTITY)):
                return True
        return False

    def consume_source_dict(self, dict_):
        v = None
        for k in dict_:
            v = dict_[k]
            self.consume_source(k, v)
    
    def consume_source(self, KEY_SOURCE:str,
            QUANTITY:int):
        struct:Structure = None
        key = ""
        leng = len(self.__structure_list)
        for i in range(leng):
            struct = self.__structure_list[i]
            key = struct.get_type()
            if(key == KEY_SOURCE
            and struct.has_life_time(
                    QUANTITY)):
                struct.sum_life_time(
                    QUANTITY * -1)
                self.__structure_list[i] = struct
                break

    def produce_resources(self, market):
        """
        Funcion que produce productos
        para el mercado enviado ejecutando
        las recetas de crafteo de cada
        structura en el territory ya
        creada.
        """
        size = len(self.__structure_list)
        struct:Structure = None
        source_dict = {}
        for i in range(size):
            struct = self\
                .__structure_list[i]
            # si la estructura no 
            # tiene una receta continua
            # a la siguiente.
            if(not struct.get_has_recipe()):
                continue
            # obtiene los requisitos de 
            # fuentes de recursos.
            source_dict = struct\
                .get_source_dict_request()
            has_sources:bool = self\
                .has_sources_dict(
                    source_dict)
            # si no tiene las fuentes
            # continua al siguiente struct
            if(not has_sources): 
                continue
            # si tiene las fuentes consume
            # las fuentes indicadas.
            self.consume_source_dict(
                source_dict
            )
            # si tiene las fuentes produce 
            # los productos indicados.
            market = struct\
                .produce_resources(market)
            self.__structure_list[i] \
                = struct
        return market
            

        