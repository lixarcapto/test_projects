

from Persistence import Persistence
from btpy.Btpy import Btpy
from open_xlsx import open_xlsx

class Model:

    def __init__(self):
        self.profile_dict = {}
        self.price_dict = Persistence\
            .get_price_dict()
        self.final_dict = {}

    def calculate_plate_of_food(self):
        main_meal = self.price_dict\
            ["main_meal"]
        light_meal = self.price_dict\
            ["light_meal"]
        drink = self.price_dict\
            ["drink"]
        daily_food = main_meal\
            + light_meal * 2\
            + drink * 3
        month_food = daily_food\
            * 7 * 4
        self.profile_dict["daily_food"]\
            = daily_food
        self.profile_dict["monthly_food"]\
            = month_food
        
    def calcule_balance(self):
        expenses = 0
        expenses += self.profile_dict\
            ["monthly_shower_price"]
        expenses += self.profile_dict\
            ["monthly_food"]
        expenses += self.price_dict\
            ["internet"]
        net_salary = self.profile_dict\
            ["net_salary"]
        result = net_salary - expenses
        self.profile_dict\
            ["balance"] = result

    def calculate_salary(self):
        salary = self.profile_dict\
            ["salary"]
        pension = self.price_dict\
            ["pension_contribution"]
        part = pension * (salary / 100)
        result = salary - part
        self.profile_dict["net_salary"]\
            = result
        
    def calculate_water_price(self):
        price_liter = self.price_dict\
            ["water_liter_price"]
        week_showers = self.profile_dict\
            ["showers_in_week"]
        liter_by_shower = self.price_dict\
            ["liter_by_shower"]
        result = week_showers\
            * liter_by_shower\
            * price_liter\
            * 4
        self.profile_dict\
            ["monthly_shower_price"]\
            = result

    def calculate(self):
        self.calculate_salary()
        self.calculate_plate_of_food()
        self.calculate_water_price()
        self.calcule_balance()
        # -----------------------------
        dict_ = {}
        dict_ |= self.profile_dict
        dict_ |=  self.price_dict
        self.final_dict = dict_
        Btpy.write_xlsx_flat_dict(
            self.final_dict,
            "final_list.xlsx"
        )
        open_xlsx("final_list.xlsx")