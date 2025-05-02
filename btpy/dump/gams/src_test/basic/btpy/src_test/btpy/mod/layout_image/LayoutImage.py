
class LayoutImage:

    """
        Clase para definir un tipo de dato 
        personalizado que contiene un 
        array de nombres de imagenes.
    """

    def __init__(self, 
            name_image_arr:list[str] = []):
        self.__image_names_arr = []
        self.set_name_image_arr(name_image_arr)

    # ACCESORS ---------------------------------------------------

    def get_name_image_arr(self)->list[str]:
        return self.__image_names_arr

    def set_name_image_arr(self, 
            name_image_arr:list[str])->None:
        self.__image_names_arr = name_image_arr

    def add_name_image(self, name:str):
        self.__image_names_arr\
            .append(name)

    # MODIFIERS -----------------------------------------------

    """
        Funcion que escribe los atributos de layout_image
        como texto.
    """
    def write(self)->str:
        text = ""
        array = self.__image_names_arr
        for i, e in enumerate(array):
            text += f"{i}.{array[i]}\n"
        return text
