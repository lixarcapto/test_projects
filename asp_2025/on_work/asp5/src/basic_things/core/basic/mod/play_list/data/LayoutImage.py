



class LayoutImage:

    """
        Clase para definir un tipo de dato personalizado
        que contiene un array de nombres de imagenes.
    """

    def __init__(self, string_array = []):
        self._array_of_image_names = []
        self.set_array_of_image_names(string_array)

    # ACCESORS ---------------------------------------------------

    def get_array_of_image_names(self):
        return self._array_of_image_names

    def set_array_of_image_names(self, array_string):
        self._array_of_image_names = array_string

    def add_image_name(self, string):
        self._array_of_image_names.append(string)

    # MODIFIERS -----------------------------------------------

    """
        Funcion que escribe los atributos de layout_image
        como texto.
    """
    # return string
    def write(self):
        text = ""
        for i in range(len(self._array_of_image_names)):
            text += "    " + str(i) + ". " \
            + self._array_of_image_names[i] + "\n"
        return text
