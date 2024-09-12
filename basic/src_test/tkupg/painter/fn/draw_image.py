


import os
from tkinter import PhotoImage

"""
Funcion que dibuja una image en el
canvas usando su direccion y locacion.
"""
def draw_image(painter_data, image_direction, 
            location_x, location_y):
        # si la direccion no es valida 
        # salta al siguiente
        if(not is_valid_direction(image_direction)):
            return None
        # carga un photo image y lo almacena
        photo_image = PhotoImage(
            file = image_direction)
        print(image_direction)
        painter_data.add_image_buffer(photo_image)
        # dibuja el photo_image
        print(str(photo_image))
        painter_data.widget.create_image(\
            location_x,
            location_y,
            image =photo_image,
            anchor="nw"
        )
        return painter_data

"""
        Funcion que valida si la direccion de la imagen
        enviada existe.
    """
    # return boolean
def is_valid_direction(direction_image):
    if (not os.path.exists(direction_image)):
            r = f"direccion invalida {direction_image=}"
            raise Exception(r)
    return True