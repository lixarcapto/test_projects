
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
        "carrier",
        "electrician",
        "plumbers",
        "chemical",
        "driller"
    ]
    resources_by_profession = {
        "farmer":"food",
        "miner":"metal",
        "builder": "building",
        "manager": "job"
    }

    def __init__(self):
        self.minion_list = []
        self.population = 0
        self.initial_population = 20
        self.annual_entry_permits = 1
        self.money = 0
        self.number_immigrants = 0
        self.number_emigrants = 0
        self.unhappy_years = 0
        self.total_happiness = 0
        self.max_happiness = 0
        self.woman_population = 0
        self.man_population = 0
        self.moms_population = 0
        self.childs_population = 0
        self.year_deaths = 0
        self.total_deaths = 0
        self.natural_deaths = 0
        self.fatal_birth_deaths = 0
        self.starvation_deaths = 0
        self.subsidized_sector_list = []
        self.record_resources_dict = {}
        self.resources_dict\
        = {
            "farmer":0,
            "miner":0,
            "builder":0,
            "manager":0,
            "food":5000,
            "metal":100,
            "fuel":100,
            "transport":100,
            "vehicles":100,
            "building":100,
            "soldier":0,
            "carrier":0,
            "electricity": 0,
            "water":0,
            "homes":0,
            "sand":0,
            "concrete":0,
            "chemical":0,
            "plumbers":0,
            "electrician":0,
            "driller":0,
            "oil":0
        }
        self.populate(
            self.initial_population
        )

    def execute_emigration(self):
        minion:Minion = None
        idx_list = []
        i = 0
        for minion in self.minion_list:
            if(minion.wants_to_emigrate):
                idx_list.append(i)
            i += 1
        idx_list.sort(reverse=True)
        for i in idx_list:
            del(self.minion_list[i])

    def execute_immigration(self):
        migrants_number = Btpy.rand_range(
            [0, self.annual_entry_permits]
        )
        for i in range(migrants_number):
            self.receive_migrant()

    def receive_migrant(self):
        minion:Minion = Minion()
        range_age = [0, 1]
        range_age[0] = Minion.age_range\
            ["young"][0]
        range_age[1] = Minion.age_range\
            ["senior"][1]
        minion.randomize(range_age)
        minion.profession = self\
            .get_random_profession()
        self.minion_list.append(minion)

    def get_random_profession(self):
        return Btpy.random_choice(
            Model.professions_list
        )

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
        craftable_recipes = 1
        while(craftable_recipes != 0):
            craftable_recipes = 0
            for recipe in Model.recipe_dict.recipe_list:
                if(self.can_craft_recipe(
                    recipe)):
                    self.craft_recipe(recipe)
                if(self.can_craft_recipe(
                    recipe)):
                    craftable_recipes += 1

    def can_craft_recipe(self, recipe):
        return self.has_resources_dict(
            recipe.raw_materials_dict
        )

    def craft_recipe(self, recipe):
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
                if(minion.cause_death 
                   == "fatal birth"):
                    self.fatal_birth_deaths\
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
                self.minion_list[i].socialize(
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
        self.total_happiness = 0
        self.max_happiness = 0
        self.number_emigrants = 0
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
            if(minion.happiness >= 1):
                self.total_happiness += 1
            self.max_happiness += 1
            if(minion.wants_to_emigrate):
                self.number_emigrants += 1
                


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
            minion.happiness = 0
            # food
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
            # homes
            if(self.has_resource("homes", 1)):
                self.use_resource(
                    "homes", 1
                )
                minion.happiness += 1
    
    def populate(self, SIZE):
        minion = None
        range_age = [0, 1]
        range_age[0] = Minion.age_range\
            ["young"][0]
        range_age[1] = Minion.age_range\
            ["senior"][1]
        for i in range(SIZE):
            minion = Minion()
            minion.randomize(range_age)
            self.minion_list\
                .append(minion)
            
    def write_resources_table(self):
        txt = ""
        r = 0
        for k in self.resources_dict:
            r = self.resources_dict[k] - self.record_resources_dict[k]
            txt += f"{k} : {self.resources_dict[k]}"
            if(r > 0):
                txt += f"(+{r})\n"
            else:
                txt += f"({r})\n"
        return txt 
    
    def save_record_resources_dict(self):
        for k in self.resources_dict:
            self.record_resources_dict[k]\
                = self.resources_dict[k]

    def advance_one_year(self):
        self.save_record_resources_dict()
        self.execute_immigration()
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
        self.execute_emigration()
        #Btpy.clean_console()
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