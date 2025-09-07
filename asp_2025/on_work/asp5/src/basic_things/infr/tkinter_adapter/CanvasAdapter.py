


from tkinter import Canvas

class CanvasAdapter:

    """
        Clase adaptadora del Canvas de Tkinter
        para mejorar su funcionalidad y aislar
        la libreria Tkinter.
    """

    def __init__(self, tk_widget):
        self._canvas = Canvas(tk_widget)

    def set_background(self, color):
        self._canvas.config(background = color)

    def set_size(self, width_size, height_size):
        self._canvas.config(\
            width = width_size,
            height = height_size)

    def pack(self):
        self._canvas.pack()

    def create_line(self, \
        location_1_x,
        location_1_y,
        location_2_x,
        location_2_y,
        color_key
        ):
        self._canvas.create_line( \
            location_1_x,
            location_1_y,
            location_2_x,
            location_2_y,
            fill = color_key
            )

    def create_image(self,
            location_x,
            location_y,
            photo_image,
            anchor_string
            ):
        self._canvas.create_image(
            location_x,
            location_y,
            image = photo_image,
            anchor = anchor_string
            )
