

from basic_things.basic_things import Docutil

class DataBase:

    EXCELS_DIRECTIONS = "../resources/excels/"
    EXCEL_FORMAT = ".xlsx"

    def excel_route(name):
        text = DataBase.EXCELS_DIRECTIONS \
        + name \
        + DataBase.EXCEL_FORMAT
        return text

    # return map_of_string
    def load_female_names():
        route = DataBase.excel_route("name_female_data")
        map_string = Docutil \
            .load_an_excel_file_as_a_string_array_dictionary(
                route
            )
        return map_string

    # return map_of_string
    def load_male_names():
        route = DataBase.excel_route("name_male_data")
        map_string = Docutil \
            .load_an_excel_file_as_a_string_array_dictionary(
                route
            )
        return map_string

    # return map_of_string
    def load_lastnames():
        route = DataBase.excel_route("lastname_data")
        map_string = Docutil \
            .load_an_excel_file_as_a_string_array_dictionary(
                route
            )
        return map_string

    # return map_of_string
    def load_noble_lastnames():
        route = DataBase.excel_route("lastname_noble_data")
        map_string = Docutil \
            .load_an_excel_file_as_a_string_array_dictionary(
                route
            )
        return map_string
