

from ..layout_image.LayoutImage \
    import LayoutImage
from ..motion_image.MotionImage \
    import MotionImage
from .fabric_paint_order import*

class PlayList:

    """
    Clase para definir un tipo de dato 
    personalizado que contiene un array 
    de motion_image.
    """

    _route_image = ""
    _format_image = ""

    def __init__(self):
        self._motion_image_map = {}
        self._location_X = 0
        self._location_Y = 0
        self._key_actual_motion = ""
        # recycled
        self.name_recycled = ""

    def write(self):
        text = ""
        motion = None
        for key in self._motion_image_map:
            motion = self._motion_image_map[key]
            text += motion.write()
        return text

    """
        Funcion que crea un tipo dato layout;
        puede recibir un array de nombres de imagenes.
    """
    # return LayoutImage
    def create_layout_image(self, string_array = []):
        return LayoutImage(string_array)

    """
        Funcion que crea un tipo dato motion;
        puede recibir su nombre y un layout_array.
    """
    # return MotionImage
    def create_motion_image(self,
            name = "",
            layout_array = []):
        return MotionImage(name, layout_array)

    def to_paint_order(self):
        layout = self.get_actual_motion() \
            .get_actual_layout()
        names_array = layout.get_array_of_image_names()
        location_x = self.get_location_x(),
        location_y = self.get_location_y()
        direction = self.get_route_image(),
        format = self.get_format_image(),
        return fabric_paint_order(
                names_array,
                direction,
                format,
                [location_x,
                location_y]
                )


    # ACCESORS -------------------------------------------------

    # return int
    def get_location_y(self):
        return self._location_Y

    def set_location_y(self, integer):
        self._location_Y = integer

    # return int
    def get_location_x(self):
        return self._location_X

    def set_location_x(self, integer):
        self._location_X = integer

    # return string
    def get_format_image(self):
        return PlayList._format_image

    def set_format_image(self, string):
        PlayList._format_image = string

    # return string
    def get_route_image(self):
        return PlayList._route_image

    def set_route_image(self, string):
        PlayList._route_image = string

    def set_key_actual_motion(self, string):
        self._key_actual_motion = string

    # return string
    def get_key_actual_motion(self):
        return self._key_actual_motion

    # return motion
    def get_actual_motion(self):
        return self._motion_image_map[self.get_key_actual_motion()]

    # return motion
    def get_motion_image_array(self):
        return self._motion_image_map

    def set_motion_image_array(self, _motion_image_map):
        self._motion_image_map = _motion_image_map

    def get_motion_image(self, key):
        if(not key in self._motion_image_map):
            raise Exception("invalid key")
        return self._motion_image_map[key]

    def add_motion_image(self, motion_image):
        self.name_recycled = motion_image.get_name()
        self.set_key_actual_motion(self.name_recycled)
        self._motion_image_map[self.name_recycled] = motion_image