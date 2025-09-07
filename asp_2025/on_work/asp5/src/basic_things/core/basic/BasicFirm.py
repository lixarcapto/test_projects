


class BasicFirm:

    """
        Clase firma que contiene un conjunto de herramientas
        de uso basico y general.
    """

    def __init__(self):
        None

    """
        Funcion que crea un objeto Probability
        que sirve para la generacion de probabilidades.
    """
    # return Probability
    def create_probability():
        pass

    """
        Funcion que crea una matriz vacia.
    """
    # return matrix_2D_none
    def create_matrix(size_x, size_y, size_z = -1,
            type = "none"):
        pass


    """
        Funcion que convierte un array string a
        un solo string
    """
    # return string
    def write_array_string_as_array(\
        map_of_string_array):
        pass

    """
        Funcion que randomiza booleanos
    """
    # return bool
    def random_bool():
        pass

    """
        Funcion que elige aleatoriamente un elemento
        de un array.
    """
    # return array_variable
    def random_element(array):
        pass

    """
        Funcion que toma un array de elementos aleatorios
        sin repetir de un array.
    """
    # return array
    def random_elements_without_repeat(\
        array, quantity):
        pass

    """
        Funcion que genera un array de numeros
        aleatorios en un rango minimo y maximo.
    """
    # return int_array
    def random_numbers_array_in_range(\
        quantity,
        minimum,
        maximum
        ):
        pass

    """
        Funcion que escribe un array string como una
        lista punteada en formato string
    """
    # return string
    def write_a_string_array_as_a_dotted_list(\
        array,
        type = "",
        dot_symbol = ">",
        margin_size = 3
        ):
        pass

    """
        Funcion que escribe el texto entre los
        simbolos indicados
    """
    # return string
    def quote(text):
        pass

    """

    """
    # return string
    def get_key_by_index(map, index):
        pass

    """
        Funcion que escribe un array de string como
        una descripcion con comas.
    """
    # return string
    def join_as_string(string_array,
            divisor_symbol = ","):
        pass


    """
        Funcion que remplaza mayuculas y tildes por minusculas
    """
    # return text
    def converts_uppercase_and_accent_letters_to_lowercase(texto):
        pass

    """
        Funcion que elimina los caracteres indicados
        de un string, remplaza al replace(string, "")
    """
    # return text
    def remove_string(string, string_to_remove):
        pass


    """
        Funcion que corta el string despues de cierto string
        del array
    """
    # return text
    def cuts_text_from_character(string, caracter):
        pass

    """
        Funcion que convierte un texto a negritas.
    """
    #return string
    def blackens_the_text(string):
        pass

    """
        Funcion que crea un array lleno de elementos numericos
        o string. Para numeros recibe la key number y para
        letras la key letter.
    """
    # return string_array
    def create_array(size = 27, type = "number"):
        pass

    """
        Funcion que recorre una matriz aplicando la lambda
        enviada a cada elemento.
    """
    # return matrix
    def map_in_matrix(function, matrix):
        pass

    """
        Funcion que escribe un error de forma ordenada
        y limpia.
    """
    # return string
    def write_error(\
            error,
            file_name,
            function_name,
            data_error = ""
            ):
        pass

    """
        Funcion que crea un objeto playlist.
    """
    # return PlayList
    def create_play_list():
        pass

    def clean_console():
        pass

    # return DateManager
    def create_date_manager():
        pass

    """
        Función que crea un objeto menú, que sirve como
        un creador de menús de texto.
        este contiene las funciones:
        * write()
        * mimic_menu_map(menu_map)
        * get_margin_size()
        * set_margin_size(integer)
        * get_options_array()
        * set_options_array(string_array)
        * get_title()
        * set_title(string)
        * get_dot_symbol()
        * set_dot_symbol(string)
        * get_format()
        * set_format(string)
    """
    # return Menu
    def create_menu():
        pass

    """
        Función que entrega un código de color HEX
        según la Key enviada.
    """
    # return string
    def hex_color(key):
        pass

    # return boolean
    def is_string(string):
        pass

    # return boolean
    def is_int(integer):
        pass

    # return boolean
    def is_float(float):
        pass

    # return boolean
    def is_list(list):
        pass

    # return boolean
    def is_dict(dict):
        pass

    # return boolean
    def is_matrix(matrix):
        pass

    # return boolean
    def is_matrix3d(matrix3d):
        pass

    # return string
    def take_string_between(\
            texto, delimitador_inicio,
            delimitador_fin
            ):
        pass

    """
        Funcion que crea un reporte ordenado en string
        para escribir en consola; segun el tamaño de los
        datos los escribira en una linea o varias.
    """
    # return string
    def write_a_report(report_name, data_string, file_name,
            function_name):
        pass

    # return Coordiante
    def create_coordinate():
        pass

    # string_array
    def get_abc_array():
        pass

    # integer_array
    def get_number_array():
        pass

    """
        Funcion que extrae una letra del string en
        una posicion especifica usando slicing.
    """
    # char
    def charat(string, index):
        pass

    """
        Funcion que busca un string similar al enviado en
        un array, map o matriz 2D.
    """
    # return string
    def get_similar_string(collection, searched_value):
        pass

    # return float
    def calcule_part_from_percent(percent, total):
        pass

    # return float
    def calcule_percent_from_part(part, total):
        pass

    # return float
    def calcule_total_from_part(percent, part):
        pass

    """
        Funcion que compara cuantas letras de un string
        existen en el otro string retornando un
        porcentaje de similitud
    """
    # return integer
    def calculate_similes_chars(string_base,
            string_to_compare):
        pass

    """
        Funcion que busca una clave en un diccionario de
        arrays usando un elemento de sus arrays.
    """
    # return string
    def search_key_by_element(map, searched_element):
        pass

    """
        Funcion para crear map_of_string_array prediseñados
        para pruebas de codigo y funciones.
    """
    # map_of_string_array
    def create_map_of_array_premade(topic):
        pass

    """
        Funcion que escribe una matriz 2D como una matrix
        en formato texto.
    """
    # return string
    def write_matrix_as_matrix(matrix):
        pass

    """
        Funcion que busca la siguiente palabra al
        string enviado en el texto
    """
    # return string
    def find_next_word(text, searched_string):
        pass

    """
        Funcion que divide un string por los string
        enviados en el array. Utiliza la libreria re
    """
    # return string_array
    def split_text_by_strings(text, delimiters):
        pass

    # return string_array
    def convert_description_to_array(string,
            name_list, init_string, separator_string,
            end_string):
        pass

    """
        Funcion que genera un boolean aleatorio
        basado en el porcentaje enviado.
    """
    # return int
    def random_probability(porcentage):
        pass

    """
        Funcion que genera numeros aleatorios que no se
        encuentran en la lista enviada y en el rango
        maximo enviado, usando random libreria.
    """
    # return int
    def random_int_different_from(number_list, maximum):
        pass

    """
        Funcion que calcula todos los numeros que faltan
        en una lista hasta el numero mas alto, y retorna
        una lista de rangos array con esos numeros faltantes.
    """
    # return int_array
    def generates_missing_numbers(number_list):
        pass

    # return Quicktk
    def create_quicktk():
        pass

    # return Painter
    def create_painter(window_tk):
        pass

    """
        Funcion que busca una palabra similar basado en
        su letras similares y el porcentage enviado.
    """
    # return string
    def simil_search(array, element, required_percent):
        pass

    """
        función que calcule Cuántos caracteres de un string se
        encuentran en el mismo índice de un string enviado,
        y retorna un porcentaje entero de esa cantidad
    """
    # return int
    def char_in_same_index(string_primal,
            string_to_compare):
        pass

    # return float
    def calculate_mid(array):
        pass

    """
        Funcion que calcula las similitudes entre dos
        strings a partir de sus caracteres similares
        y su posicion en la cadena; despues hace
        una media entre ambos porcentajes.
    """
    # return int
    def compare_strings(strig_primal, string_to_compare):
        pass

    # return int
    def search_index_different(array_to_analize,
            array_reference):
        pass

    """
        Funcion que elimina los string indicados en el
        different_array enviado del string enviado.
    """
    # return string_array
    def remove_diferent(string,
            different_array):
        pass

    """
        Funcion map mejorada, para evitar usar list(map()) y
        ademas permite escribir una lambda despues mas
        ordenada.
    """
    # return array
    def forf(array, function):
        pass

    """
        Funcion que separa y obtiene las palabras de
        un texto a pesar de otros simbolos.
    """
    # return string_array
    def separate_the_words(text):
        pass

    def map_to_array(map):
        pass

    """
        Funcion que obtiene la clave de un element en
        un diccionario
    """
    def key_by_value(self, map, value):
        pass

    """
        Funcion que devuele un boolean si el int
        enviado esta entre el rango enviado en un array
    """
    def between_range(integer, limits_array):
        pass

    def is_error(value):
        pass

    def is_key_value(array):
        pass

    def is_map_of_arrays(array):
        pass

    """
        Funcion que crea un Tipo de dato personalizado
        para crear numeros int con limites marcados.
            * sum(number): suma un numero
            * set(number): ajusta un numero
            * get(): obtiene el numero
    """
    def limit_int(number, min = -1, max = -1):
        pass

    """
        Funcion que revisa si un numero esta en un rango
        array.
    """
    def in_range(number, range):
        pass

    def randindex(array):
        pass

    def randrange(range):
        pass
