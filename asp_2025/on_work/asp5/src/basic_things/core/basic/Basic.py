


from .index import*
import os

class Basic(BasicFirm):

    """
        Clase fachada que contiene un conjunto de herramientas
        de uso basico y general.
    """

    def __init__(self):
        None

    def create_matrix(size_x, size_y, size_z = -1,
            type = "none"):
        return create_matrix(size_x, size_y, size_z,
                type)

    def create_probability():
        return Probability()

    def write_array_string_as_array(\
        map_of_string_array):
        return write_array_string_as_array(\
            map_of_string_array)

    def random_bool():
        return random_bool()

    def random_element(array):
        return random_element(array)

    def random_elements_without_repeat(\
        array, quantity):
        return random_elements_without_repeat(\
            array, quantity)

    def random_numbers_array_in_range(\
            quantity,
            minimum,
            maximum
            ):
        return random_numbers_array_in_range(\
            quantity,
            minimum,
            maximum
            )

    def write_a_string_array_as_a_dotted_list(\
            string_array,
            type = "",
            dot_symbol = ">",
            margin_size = 3
            ):
        return write_a_string_array_as_a_dotted_list(\
                string_array,
                type,
                dot_symbol,
                margin_size
                )

    # return string
    def quote(text):
        return "\"" + text + "\""

    # return string
    def get_key_by_index(map, index):
        return get_key_by_index(map, index)

    # return string
    def join_as_string(string_array,
            divisor_symbol = ","):
        return join_as_string(string_array,
                divisor_symbol = ",")

    # return text
    def remove_capitals_and_accents(texto):
        return remove_capitals_and_accents(\
        texto)

    # return text
    def remove_string(string, string_to_remove):
        return remove_string(string, string_to_remove)

    # return text
    def cuts_text_from_character(string, caracter):
        return cuts_text_from_character(string, caracter)

    # return string
    def blackens_the_text(string):
        return blackens_the_text(string)

    # return string_array
    def create_array(size = 27, type = "none"):
        return create_array(size, type)

    # return matrix
    def map_in_matrix(function, matrix):
        return map_in_matrix(function, matrix)

    # return string
    def write_error(\
            error,
            file_name,
            function_name,
            data_error = ""
            ):
        return write_error(\
                error,
                file_name,
                function_name,
                data_error
                )

    # return PlayList
    def create_play_list():
        return PlayList()

    def clean_console():
        os.system ("cls")

    # return DateManager
    def create_date_manager():
        return DateManager()

    # return Menu
    def create_menu():
        return Menu()

    # return string
    def hex_color(key):
        return hex_color(key)

    # return boolean
    def is_string(string):
        if(type("") == type(string)):
            return True
        return False

    # return boolean
    def is_int(integer):
        if(type(0) == type(integer)):
            return True
        return False

    # return boolean
    def is_float(float):
        if(type(0.1) == type(float)):
            return True
        return False

    # return boolean
    def is_list(list):
        if(type([]) == type(list)):
            return True
        return False

    # return boolean
    def is_dict(dict):
        if(type({}) == type(dict)):
            return True
        return False

    # return boolean
    def is_matrix(matrix):
        if(type([]) == type(matrix)\
        and type([]) == type(matrix[0])):
            return True
        return False

    # return boolean
    def is_matrix3d(matrix3d):
        if(type([]) == type(matrix3d)\
        and type([]) == type(matrix3d[0])\
        and type([]) == type(matrix3d[0][0])):
            return True
        return False

    # return string
    def take_string_between(\
            texto, delimitador_inicio,
            delimitador_fin
            ):
        return take_string_between(\
                texto, delimitador_inicio,
                delimitador_fin
                )

    # return string
    def write_a_report(report_name, data_string, file_name,
            function_name):
        return write_a_report(report_name, data_string,
            file_name, function_name)

    # return Coordiante
    def create_coordinate():
        return Coordinate()

    # string_array
    def get_abc_array():
        return ABC_ARRAY

    # integer_array
    def get_number_array():
        return NUMBER_ARRAY

    # return char
    def charat(string, index):
        return charat(string, index)

    # return string
    def get_similar_string(collection, searched_value):
        return get_similar_string(collection,
            searched_value)

    # return float
    def calcule_part_from_percent(percent, total):
        return percent * (total / 100)

    # return float
    def calcule_percent_from_part(part, total):
        return part * (100 / total)

    # return float
    def calcule_total_from_part(percent, part):
        return (part * percent) / 100

    # return integer
    def calculate_similes_chars(string_base,
            string_to_compare):
        return calculate_similes_chars(string_base,
                string_to_compare)

    # return string
    def search_key_by_element(map, searched_element):
        return search_key_by_element(map, searched_element)

    # map_of_string_array
    def create_map_of_array_premade(topic):
        return create_map_of_array_premade(topic)

    # return string
    def write_matrix_as_matrix(matrix):
        return write_matrix_as_matrix(matrix)

    # return string
    def find_next_word(text, searched_string):
        return find_next_word(text, searched_string)

    # return string
    def get_test_string(format = "none"):
        text = "el gato desperto temprano"
        text += " y fue a comer croquetas"
        if(format == "none"):
            return text

    """
        Funcion que divide un string por los string
        enviados en el array. Utiliza la libreria re
    """
    # return string_array
    def split_text_by_strings(text, delimiters):
        return split_text_by_strings(text, delimiters)

    """
        Funcion que busca en un string una descripcion
        iniciada por un punto y coma, y separada por comas,
        obtiene la descripcion y separada cada palabra entre
        comas para formar un array de elementos.
    """
    # return string_array
    def convert_description_to_array(\
            string,
            name_list,
            init_string,
            separator_string,
            end_string
        ):
        pass

    """
        Funcion que genera un boolean aleatorio
        basado en el porcentaje enviado.
    """
    # return int
    def random_probability(porcentage):
      numero = random.randint(0, 100 - porcentage)
      result = False
      if(numero == 1):
        result = True
      return result

    # return int
    def random_int_different_from(number_list, maximum):
        return random_int_different_from(number_list,
            maximum)

    # return int_array
    def generates_missing_numbers(number_list):
        return generates_missing_numbers(number_list)

    # return Quicktk
    def create_quicktk():
        return Quicktk()

    # return Painter
    def create_painter(window_tk):
        return Painter(window_tk)

    # return string
    def simil_search(array, element, required_percent):
        return simil_search(array, element,
            required_percent)

    # return float
    def char_in_same_index(string_primal,
        string_to_compare):
        return char_in_same_index(string_primal,
            string_to_compare)

    # return float
    def calculate_mid(array):
        sum_number = 0
        for e in array:
            sum_number += e
        result = sum_number / len(array)
        return result

    # return int
    def compare_strings(strig_primal, string_to_compare):
        return compare_strings(strig_primal,
            string_to_compare)

    """
        Funcion que comprueba si existe algo diferente
        al array de referencia enviado en el array
        enviado.
    """
    # return int
    def search_index_different(array_to_analize,
            array_reference):
        return search_index_different(array_to_analize,
                array_reference)

    # return string_array
    def remove_diferent(string, different_array):
        return remove_diferent(string, different_array)

    # return array
    def forf(array, function):
        # si es un array
        if(type(array) == type([])):
            return list(map(function, array))
        # si es un map
        if(type(array) == type({})):
            e = None
            for k in array:
                e = array[k]
                break
            if(not type(e) == type([])):
                return list(map(function, array))
            elif(type(e) == type([])):
                for k in array:
                    for i in range(len(array[k])):
                        array[k][i] = function(array[k][i])
                return array

    # return string_array
    def separate_the_words(text):
        return separate_the_words(text)

    def map_to_array(map):
        array = []
        for k in map:
            array.append(map[k])
        return array

    def key_by_value(map, value):
        return list(map.values()).index(value)

    def between_range(integer, limits_array):
        if((limits_array[0])
        and (limits_array[1])):
            return True
        return False

    def is_error(value):
        if value == -1: return True
        elif value == None: return True
        elif type(value) == type(""): return True
        return False

    def is_key_value(array):
        e = None
        for k in array:
            e = array[k]
            break
        if(not type(e) == type([])):
            return True
        return False

    def is_map_of_arrays(array):
        e = None
        for k in array:
            e = array[k]
            break
        if(type(e) == type([])):
            return True
        return False

    def limit_int(number, min = -1, max = -1):
        return LimitedInt(number, min, max)

    def in_range(number, range):
        if(number >= range[0]
        and number <= range[1]):
            return True
        return False

    def randindex(array):
        return random.randint(0,
            len(array) -1)

    def randrange(range):
        return random.randint(range[0], range[1])
