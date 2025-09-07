

from ..recipe.RecipeCollection import RecipeCollection
from ..recipe.Recipe import Recipe
from ..market.Market import Market
from btpy.Btpy import Btpy
from ..structure_blueprint_depot.StructBlueprintDepot import StructBlueprintDepot

class Structure:

    structure_bp_depot = StructBlueprintDepot()
    recipe_collection = RecipeCollection()

    def __init__(self, TYPE_KEY:str):
        self.__type:str = ""
        self.recipe_key:str = ""
        self.life_time:int = 0
        self.build_type(TYPE_KEY)

    def build_type(self, TYPE_KEY):
        struct_bp = Structure\
            .structure_bp_depot\
                .get_struct_bp(TYPE_KEY)
        self.__type = TYPE_KEY
        self.recipe_key = struct_bp\
            .get_recipe_key()
        self.life_time = struct_bp\
            .get_life_time()

    def has_life_time(self, NUMBER)->bool:
        if(self.life_time >= NUMBER):
            return True
        return False

    def sum_life_time(self, NUMBER):
        self.life_time = Btpy\
            .sum_in_range(
                self.life_time,
                NUMBER,
                [0, 9999]
            )

    def get_type(self)->str:
        """
        Funcion que obtiene una clave 
        de la categoria que identifica
        a la estructura.
        """
        return self.__type

    def set_type(self, TYPE_KEY:str):
        self.__type = TYPE_KEY

    def get_recipe(self)->Recipe:
        KEY:str = self.recipe_key
        return Structure.recipe_collection\
            .get_recipe(KEY)
    
    def get_recipe_key(self)->str:
        return self.recipe_key
    
    def get_has_recipe(self)->bool:
        if(self.recipe_key == ""):
            return False
        return True
    
    def get_source_dict_request(self):
        recipe = self.get_recipe()
        return recipe.get_sources_dict()
    
    def produce_resources(self, 
            market:Market):
        # -------------------------------
        # Obtiene la receta de la 
        # estructura de la coleccion
        # de recetas.
        recipe = self.get_recipe()
        # ---------------------------------
        # verifica si el mercado tiene
        # los ingredientes para craftear
        # la receta correspondiente.        
        ingredient_dict = recipe\
            .get_ingredient_dict()
        if(not market.has_product_dict(
                ingredient_dict)):
            return market
        # ------------------------------------
        # resta los ingredientes 
        # correspondientes del mercado
        # indicados por la receta.
        market.subtract_product_dict(
            ingredient_dict
        )
        # ---------------------------------
        # Agrega los ingredientes
        # resultante de lar receta
        # crafteada al mercado.
        product_dict = recipe\
            .get_product_dict()
        market.sum_product_dict(
            product_dict
        )
        # -------------------------------
        return market