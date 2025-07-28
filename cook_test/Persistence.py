

from btpy.Btpy import Btpy

class Persistence:

    def get_dish_list():
        dict_ = Btpy.read_json_object(
            "./dish_data_json.json"
        )
        return dict_["DISH_LIST"]
    
    def load_ingredient_data()->dict:
        nested_dict = Btpy\
            .read_xlsx_nested_dict_row(
                "./ingredient_data.xlsx"
            )
        return nested_dict

    def load_nested_dict():
        nested_dict = Btpy\
            .read_xlsx_nested_dict_column(
                "./ingredient_stats.xlsx"
            )
        return nested_dict
    
    def load_dish_data()\
            ->dict[str, dict]:
        nested_dict = Btpy\
            .read_xlsx_nested_dict_row(
                "./dish_data.xlsx"
            )
        return nested_dict
    
    def load_waitress_phrases()\
            ->dict[list]:
        json_dict = Btpy\
            .read_json_object(
                "./waitress_data.json"
            )
        return json_dict