

from btpy.Btpy import Btpy
from find_nearest_mayor_key import*
from names_female_list import*
from names_male_list import*
from lastnames_list import*

class Minion:

    max_happiness = 1
    probability_emigrating = 20
    age_of_independence = 16
    taxes_range = [18, 70]
    age_range = {
        "child":[0, 12],
        "teen":[13, 18],
        "young":[19, 30],
        "middle":[31, 50],
        "senior":[51, 70],
        "elderly":[71, 100],
        "dying":[101, 150]
    }
    probability_death_dict = {
        "child":0,
        "teen":0,
        "young":0,
        "middle":0,
        "senior":10,
        "elderly":60,
        "dying":95
    }
    fertility_by_age = {
        "child":0,
        "teen":50,
        "young":80,
        "middle":10,
        "senior":1,
        "elderly":0,
        "dying":0
    }
    last_code = 0
    cause_death_list = [
        "starvation",
        "natural"
    ]

    def __init__(self):
        self.code = 0
        self.is_male = True
        self.age = 0
        self.profession = "none"
        self.sexual_orientation\
            = "hetero"
        self.productivity = 1
        self.wants_to_emigrate = False
        self.child_list = []
        self.is_fertile = True
        self.name_idx = 0
        self.lastname_idx = 0
        self.happiness = 0
        self.is_happy = False
        self.is_alive = True
        self.is_pregnant = False
        self.have_dead_of_blood = False
        self.have_dead_foretold = False
        self.create_code()
        self.has_food = False
        self.has_building = False
        self.cause_death = ""

    def calculate_happiness(self):
        pass

    def run_happiness_system(self):
        if(self.happiness == 0):
            self.make_decision_to_migrate()

    def make_decision_to_migrate(self):
        will_it_migrate = Btpy\
            .random_probability(
                Minion.probability_emigrating
            )
        if(will_it_migrate):
            self.wants_to_emigrate = True

    def create_code(self):
        self.code = Minion.last_code
        Minion.last_code += 1

    def get_gender_key(self):
        if(self.is_male):
            return "male"
        return "female"
    
    def get_name_key(self):
        if(self.is_male):
            return names_male_list\
                [self.name_idx]
        else:
            return names_female_list\
                [self.name_idx]
        
    def get_lastname_key(self):
        return lastnames_list\
            [self.lastname_idx]

    def write(self):
        txt = ""
        txt += f"{self.get_name_key()} "
        txt += f"{self.get_lastname_key()}"
        txt += f" ({self.code}) "
        txt += self.get_gender_key() + " "
        txt += str(self.age) + " years "
        txt += self.profession + " "
        if(self.is_mom()):
            txt += "mother of:\n"
            for child in self.child_list:
                txt += "   " \
                    + child.write() + "\n"
        return txt 
    
    def socialize(self, minion):
        if(self.is_male 
                and not minion.is_male
        or not self.is_male
                and minion.is_male):
            self.have_sex(minion)

    def have_sex(self, minion):
        if(not self.is_fertile):
            return None
        fertility = 0
        if(not self.is_male):
            if(self.is_pregnant):
                return None
            age_k = Btpy.whats_range(
                Minion.age_range,
                minion.age
            )[0]
            fertility = Minion\
                .fertility_by_age[age_k]
            is_pregnant = Btpy\
                .random_probability(
                    fertility)
            if(is_pregnant):
                self.get_pregnant(minion)

    def get_pregnant(self, minion):
        died_in_childbirth = Btpy\
            .random_probability(1)
        if(died_in_childbirth):
            self.cause_death\
                = "fatal birth"
            self.is_alive = False
            return None
        self.is_pregnant = True
        has_twins = Btpy\
            .random_probability(1)
        twins_number = Btpy\
            .rand_range([1, 9])
        if(has_twins):
            for i in range(twins_number):
                self.create_child(minion)
        else:
            self.create_child(minion)

    def create_child(self, dad_minion):
        minion = Minion()
        dad_lastname = ""
        if(dad_minion.is_male):
            dad_lastname = dad_minion\
                .lastname_idx
        else:
            dad_lastname = self\
                .lastname_idx
        minion.lastname_idx = dad_lastname
        minion.be_born()
        self.child_list.append(minion)

    def has_adult(self):
        for child in self.child_list:
            if(child.age \
               >= Minion.age_of_independence):
                return True
        return False
    
    def is_mom(self):
        if(len(self.child_list) > 0):
            return True
        return False
    
    def get_child_quantity(self):
        return len(self.child_list)

    def get_adult_list(self):
        adult_list = []
        to_delete_index_arr = []
        i = 0
        for child in self.child_list:
            if(child.age 
               >= Minion.age_of_independence):
                adult_list.append(child)
                to_delete_index_arr\
                    .append(i)
            i += 1
        to_delete_index_arr.sort(
            reverse=True)
        for i in to_delete_index_arr:
            del(self.child_list[i])
        return adult_list


    def advance_one_year(self):
        self.age += 1
        self.is_pregnant = False
        if(len(self.child_list) > 0):
            for child in self.child_list:
                child.advance_one_year()
        self.apply_aging()
        self.apply_dead_foretold()
        self.run_happiness_system()

    def apply_aging(self):
        key = Btpy.whats_range(
            Minion.age_range,
            self.age
        )[0]
        prob = Minion\
            .probability_death_dict[key]
        will_die = Btpy\
            .random_probability(prob)
        if(will_die):
            self.is_alive = False

    def randomize_sickness(self):
        if(Btpy.random_probability(5)):
            self.is_fertile = False
        if(Btpy.random_probability(3)):
            self.have_dead_foretold\
                = True
            
    def apply_dead_foretold(self):
        will_die = Btpy\
            .random_probability(5)
        if(will_die):
            self.is_alive = False
            self.cause_death\
                = "dead_foretold"
            
    def randomize_age(self, AGE_RANGE):
        self.age = Btpy.rand_range(
            AGE_RANGE
        )

    def randomize(self, AGE_RANGE):
        self.randomize_sickness()
        self.randomize_gender()
        self.randomize_name()
        self.randomize_lastname()
        self.randomize_age(AGE_RANGE)

    def be_born(self):
        self.randomize_name()
        self.randomize_gender()

    def randomize_gender(self):
        if(Btpy.random_bool()):
            self.is_male = True
        else:
            self.is_male = False
        
    def randomize_name(self):
        if(self.is_male):
            leng = len(names_male_list)
            self.name_idx = Btpy\
                .rand_range([0, leng -1])
        else:
            leng = len(names_female_list)
            self.name_idx = Btpy\
                .rand_range([0, leng -1])
    
    def randomize_lastname(self):
        leng = len(lastnames_list)
        self.lastname_idx = Btpy\
            .rand_range([0, leng -1])

