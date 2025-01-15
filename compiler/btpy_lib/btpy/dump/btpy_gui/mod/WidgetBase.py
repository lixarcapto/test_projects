

import tkinter
from ...btpy_utilitys.mod.rgb_to_hex.rgb_to_hex import*
from ...btpy_checkers.mod.is_rgb.is_rgb import*

class WidgetBase():

    class RELIEF:
        SUNKEN = "sunken"
        RAISED = "raised"
        FLAT = "flat"
        GROOVE = "groove"
        RIDGE = "ridge"

    def __init__(self):
        self.widget = None

    # BEHAVIOR ------------------------------------

    def set_height(self, height):
        width = self.widget.cget("width")
        self.set_size(height, width)

    def set_width(self, width):
        height = self.widget.cget("height")
        self.set_size(height, width)

    def set_size(self, SIZE_X, SIZE_Y):
        pass

    def set_location(self, point_ar):
        pass

    def destroy(self):
        self.widget.destroy()

    def set_background(self, color):
        final_color = color
        if(is_rgb(color)):
            final_color = rgb_to_hex(color)
        self.widget.config(
            background = final_color)

    def set_relief(self, relief):
        self.widget.config(relief = relief)

    def set_borderwidth(self, integer):
        self.widget.config(
            highlightthickness= integer,
            borderwidth = integer)
        
    def set_border_color(self, COLOR):
        self.widget.config(
            highlightbackground=COLOR
        )

    def set_y(self, y: int):
        x = self.widget.cget("x")
        self.set_location([y, x])

    def set_x(self, x: int):
        y = self.widget.cget("y")
        self.set_location([y, x])

    def listme_fonts(self):
        return tkinter.font.families()
    
    