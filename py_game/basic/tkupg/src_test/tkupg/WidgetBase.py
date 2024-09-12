

import tkinter

class WidgetBase:

    def __init__(self):
        self.widget = None

    # BEHAVIOR ------------------------------------

    def set_height(self, height):
        width = self.widget.cget("width")
        self.set_size([height, width])

    def set_width(self, width):
        height = self.widget.cget("height")
        self.set_size([height, width])

    def set_size(self, range):
        pass

    def set_location(self, point_ar):
        pass

    def destroy(self):
        self.widget.destroy()

    def set_background(self, color):
        color = self.get_color(color)
        self.widget.config(background = color)

    def get_color(self, color_name):
        return color_name

    def set_relief(self, relief):
        self.widget.config(relief = relief)

    def set_borderwidth(self, integer):
        self.widget.config(borderwidth = integer)

    def set_y(self, y: int):
        x = self.widget.cget("x")
        self.set_location([y, x])

    def set_x(self, x: int):
        y = self.widget.cget("y")
        self.set_location([y, x])

    def listme_fonts(self):
        return tkinter.font.families()
    
    