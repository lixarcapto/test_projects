


from .dependences import write_a_string_array_as_a_dotted_list, \
    write_a_string_array_as_a_dotted_list

class Menu:

    """
        Clase para almacenar datos para la escritura de menus
        de texto. el formato puede ser void, number o letter.
    """
    def __init__(self):
        self.margin_size = 3
        self.options_array = []
        self.title = ""
        self.dot_symbol = ""
        self.format = ""

    # MODIFIERS --------------------------------------------------

    def write(self):
        text = self.title + "\n"
        text += write_a_string_array_as_a_dotted_list(\
            array = self.options_array,
            type = self.format,
            dot_symbol = self.dot_symbol,
            margin_size = self.margin_size
        )
        return text

    """
        Funcion que imita el menu map enviado.
        menu map = {\
            "margin_size" : 3,
            "options_array" : [],
            "title" : "",
            "dot_symbol" : "",
            "format" : ""
        }
    """
    def mimic_menu_map(self, menu_map):
        self.set_options_array(menu_map["options_array"])
        self.set_title(menu_map["title"])
        self.set_format(menu_map["format"])
        self.set_dot_symbol(menu_map["dot_symbol"])
        self.set_margin_size(menu_map["margin_size"])

    #  ACCESORS --------------------------------------------------

    def get_margin_size(self):
        return self.margin_size

    def set_margin_size(self, integer):
        self.margin_size = integer

    def get_options_array(self):
        return self.options_array

    def set_options_array(self, string_array):
        self.options_array = string_array

    def get_title(self):
        return self.title

    def set_title(self, string):
        self.title = string

    def get_dot_symbol(self):
        return self.dot_symbol

    def set_dot_symbol(self, string):
        self.dot_symbol = string

    def get_format(self):
        return self.format

    def set_format(self, string):
        self.format = string
