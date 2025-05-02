

import numpy as np

"""
Creates a 3D NumPy array representing a white image.
Args:
    width (int): The width of the image 
    in pixels.
    height (int): The height of the image 
    in pixels.
Returns:
    numpy.ndarray: A 3D NumPy array 
    representing the white image.
"""
# return numpy image RGB.
def create_numpy_image_RGB(width, height):
    # Create an array filled with 
    # [255, 255, 255] (white)
    white_color = [255, 255, 255]
    numpy_image_RGB = np.full(
        (height, width, 3),
        white_color, 
        dtype=np.uint8 # valida la imagen
    )
    return numpy_image_RGB