



from btpy.src.btpy.Btpy import Btpy

class Persistence:

    ROUTE_NAMES_TABLE = ""

    def __init__(self) -> None:
        pass

    # para basic things
    def read_nested_tables(route_dict):
        nested_dict = {}
        route = ""
        for k in route_dict:
            route = route_dict[k]
            nested_dict[k] = Btpy\
                .read_xlsx_nested(route)
        return nested_dict
    
    def read_city_names()->dict:
        result = Btpy.read_excel_dict(
            "../res/tables/region_names.xlsx"
        )
        return result

    def read_names():
        route_tables = {
            "extreme_north":"../res/tables/names_nordic_male.xlsx",
        }
        nested_dict = Persistence\
            .read_nested_tables(route_tables)
        return nested_dict
    
    def read_female_names():
        route_tables = {
            "extreme_north":"../res/tables/names_female_nordic.xlsx",
        }
        nested_dict = Persistence\
            .read_nested_tables(route_tables)
        return nested_dict
    
    def read_races():
        route = "../res/tables/race_propertys.xlsx"
        dict = Btpy.read_xlsx_nested(route)
        dict = Persistence.normalize(dict)
        return dict
    
    def read_races_names():
        route = "../res/tables/race_propertys.xlsx"
        dict = Btpy.read_xlsx_nested(route)
        dict = Persistence.normalize(dict)
        return dict.keys()
    
    def normalize_excel_dict(dict):
        v = None
        for k in dict:
            if("[" in str(dict[k])):
                v = dict[k]
                v = v.replace("[", "")
                v = v.replace("]", "")
                v = v.split(",")
                dict[k] = v
        return dict
    
    def normalize(nested_dict):
        inner_dict = {}
        for k in nested_dict:
            inner_dict = nested_dict[k]
            inner_dict = Persistence.normalize_excel_dict(
                inner_dict)
            nested_dict[k] = inner_dict
        return nested_dict

    
