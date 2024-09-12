

from .fn.create_numpy_image_RGB import*
from .fn.numpy_image_RGB_to_photoimage import*
from .fn.draw_box import*

class Mig:

    # return numpy image RGB.
    def create_numpy_image_RGB(width, height):
        return create_numpy_image_RGB(width, 
            height)
    
    def numpy_image_RGB_to_photoimage(
        numpy_image_RGB):
        return numpy_image_RGB_to_photoimage(
            numpy_image_RGB)
    
    def draw_box(image, point, size, color):
        return draw_box(image, 
            point, size, color)