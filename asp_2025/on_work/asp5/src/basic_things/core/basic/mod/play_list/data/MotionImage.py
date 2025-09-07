


from ..dependences import write_error
from .LayoutImage import LayoutImage

class MotionImage:

    """
        Clase para definir un tipo de dato personalizado
        que contiene arrays de layouts de nombres de imagenes.
    """

    def __init__(self, name = "", layout_array = []):
        self._layout_array = layout_array
        self._name = name
        self._index = 0

    # ACCESORS -----------------------------------------------------

    def set_index(self, integer):
        self._index = integer

    # return int
    def get_index(self):
        return self._index

    def set_name(self, string):
        self._name = string

    # return string
    def get_name(self):
        return self._name

    # return layout
    def get_actual_layout(self):
        return self._layout_array[self.get_index()]

    # return layout_image
    def get_layout_array(self):
        return self._layout_array

    def set_layout_array(self, layout_image_array):
        self._layout_array = layout_image_array

    def add_layout(self, layout_image):
        if(not isinstance(layout_image, LayoutImage)):
            error = write_error(\
                error = "isn't layout",
                file_name = "MotionImage",
                function_name = "add_layout",
                data_error = str(layout_image)
                )
            print(error)
            return None
        self._layout_array.append(layout_image)

    # MODIFIERS -----------------------------------------------

    # return string
    def write(self):
        text = ""
        for e in self._layout_array:
            text += self.get_name() + "\n"
            text += e.write() + "\n"
        return text
