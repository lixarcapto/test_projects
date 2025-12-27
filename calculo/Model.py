
from btpy.Btpy import Btpy
from Minion import Minion
from RecipeDict import RecipeDict
from Recipe import Recipe

class Model:

    recipe_dict = RecipeDict()
    professions_list = [
        "farmer",
        "miner",
        "builder",
        "manager",
        "soldier",
        "carrier"
    ]
    resources_by_profession = {
        "farmer":"food",
        "miner":"metal",
        "builder": "building",
        "manager": "job"
    }

    def __init__(self):
        self.minion_list = []
        self.populate(10)
        self.population = 0
        self.money = 0
        self.woman_population = 0
        self.man_population = 0
        self.moms_population = 0
        self.childs_population = 0
        self.year_deaths = 0
        self.total_deaths = 0
        self.natural_deaths = 0
        self.starvation_deaths = 0
        self.subsidized_sector_list = []
        self.resources_dict\
        = {
            "farmer":0,
            "miner":0,
            "builder":0,
            "manager":0,
            "food":500,
            "metal":100,
            "fuel":100,
            "building":100,
            "soldier":0,
            "carrier":0
        }

    def collect_taxes(self):
        minion:Minion = None
        for minion in self.minion_list:
            if(Btpy.in_range(
                    minion.age, 
                    Minion.taxes_range)):
                self.money\
                    += minion.productivity

    def craft_resources(self):
        recipe:Recipe = None
        for recipe in Model.recipe_dict.recipe_list:
            while(self.has_resources_dict(
                    recipe.raw_materials_dict)):
                self.use_resources_dict(
                    recipe.raw_materials_dict
                )
                self.create_resources_dict(
                    recipe.product_dict
                )
            
    def create_resources_dict(self, DICT):
        for resource_k in DICT:
            self.resources_dict\
                [resource_k] \
                    += DICT[resource_k]

    def use_resources_dict(self, DICT):
        for resource_k in DICT:
            self.resources_dict\
                [resource_k] \
                    -= DICT[resource_k]

    def has_resources_dict(self, DICT):
        value = 0
        for resource_k in DICT:
            value = self.resources_dict\
                [resource_k]
            if(value < DICT[resource_k]):
                return False
        return True

    def produce_resources(self):
        res_key = ""
        for minion in self.minion_list:
            if(minion.profession == "none"):
                continue
            self.resources_dict\
                [minion.profession]\
                    += minion.productivity

    def assign_professions(self):
        key = ""
        is_subsidized = False
        if(self.subsidized_sector_list 
                == []):
            is_subsidized = False
        else:
            is_subsidized = True
        for minion in self.minion_list:
            if(minion.profession == "none"):
                if(is_subsidized):
                    if(Btpy.random_probability(
                            70)):
                        key = Btpy.random_choice(
                            self.subsidized_sector_list)
                    else:
                        key = Btpy.random_choice(
                            Model.professions_list)
                else:
                    key = Btpy.random_choice(
                            Model.professions_list)
                minion.profession = key

    def write_minions(self):
        txt = ""
        for i in range(50):
            txt += "-"
        txt += "\n"
        for minion in self.minion_list:
            txt += minion.write() + "\n"
        return txt

    def collect_dead_minions(self):
        minion_idx_arr = []
        i = 0
        minion:Minion = None
        self.year_deaths = 0
        for minion in self.minion_list:
            if(minion.is_alive == False):
                minion_idx_arr.append(i)
                self.total_deaths += 1
                self.year_deaths += 1
                if(minion.cause_death 
                   == "starvation"):
                    self.starvation_deaths\
                        += 1
                elif(minion.cause_death 
                   == "natural"):
                    self.natural_deaths\
                        += 1
            i += 1
        minion_idx_arr.sort(reverse=True)
        for i in minion_idx_arr:
            print(i)
            del(self.minion_list[i])

    def relate_minion(self):
        minion_idx = 0
        i = 0
        minions_to_meet = 4
        if(not len(self.minion_list) > 2):
            return None
        for minion_main in self.minion_list:
            for n in range(minions_to_meet):
                minion_idx = Btpy\
                .rand_range([
                    0, 
                    len(self.minion_list) -1
                ])
                while(minion_idx == i):
                    minion_idx = Btpy\
                    .rand_range([
                        0, 
                        len(self.minion_list) -1
                    ])
                self.minion_list[i].have_sex(
                    self.minion_list\
                        [minion_idx]
                )
            i += 1

    def calcule_stats(self):
        self.population = len(
            self.minion_list)
        self.woman_population = 0
        self.man_population = 0
        self.childs_population = 0
        self.moms_population = 0
        minion:Minion = None
        for minion in self.minion_list:
            if(minion.is_male):
                self.man_population += 1
            else:
                self.woman_population += 1
            if(minion.is_mom()):
                self.moms_population += 1
                childs = minion\
                    .get_child_quantity()
                self.childs_population\
                    += childs
                self.population\
                    += childs
                


    def has_resource(self, KEY, QUANTITY):
        dict_ = self.resources_dict
        if(dict_[KEY] >= QUANTITY):
            return True
        return False
                
    def use_resource(self, KEY,
            QUANTITY):
        self.resources_dict[KEY]\
            -= QUANTITY

    def consume_for_all(self):
        minion:Minion = None
        for minion in self.minion_list:
            minion.has_food = False
            if(self.has_resource("food", 1)):
                self.use_resource(
                    "food", 1
                )
                minion.has_food = True
            else:
                minion.has_food = False
                minion.is_alive = False
                minion.cause_death \
                    = "starvation"
    
    def populate(self, SIZE):
        minion = None
        range_age = [0, 1]
        range_age[0] = Minion.age_range\
            ["young"][0]
        range_age[1] = Minion.age_range\
            ["senior"][1]
        for i in range(SIZE):
            minion = Minion()
            minion.age = Btpy\
                .rand_range(range_age)
            minion.randomize()
            self.minion_list\
                .append(minion)

    def advance_one_year(self):
        minion:Minion = None
        for minion in self.minion_list:
            minion.advance_one_year()
        self.assign_professions()
        self.produce_resources()
        self.collect_taxes()
        self.calcule_stats()
        # relacionamiento
        self.relate_minion()
        # crecimiento
        self.become_independent_minions()
        self.craft_resources()
        self.consume_for_all()
        self.collect_dead_minions()
        Btpy.clean_console()
        print(self.write_minions())

    def become_independent_minions(self):
        leng = len(self.minion_list)
        minion_list = []
        for i in range(leng):
            minion = self.minion_list[i]
            if(minion.has_adult()):
                minion_list = minion\
                    .get_adult_list()
                self.minion_list \
                    = self.minion_list \
                    + minion_list