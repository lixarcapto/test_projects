

import tkinter as tk
import io
from PIL import Image, ImageDraw
from ..btpy_dict.mod.max_key.max_key import*
from ..btpy_maths.mod.percent.percent_from_part import*
from ..btpy_maths.mod.percent.part_from_percent import*
from ..btpy_maths.mod.percent.total_from_part import*

class Graphic:

    def __init__(self, widget):
        self.widget = tk.Canvas(
            widget, 
            bg="white"
        )
        self.width_bar:int = 70
        self.distant_bar:int = 10
        self.height = 300
        self.width = 300
        self.set_size(300, 300)

    def calculate_width_bar(self,
            bars_quantity):
        space_bar = self.width\
            / bars_quantity
        self.distant_bar = part_from_percent(
            10, space_bar
        )
        self.width_bar = space_bar\
            - self.distant_bar

    def find_height_bar(self, 
            value, max_value):
        percent = percent_from_part(
            value,
            max_value
        )
        return part_from_percent(
            percent,
            self.height
        )

    def draw_graphic_dict(self, 
            DICT_NUMBER:dict[int]):
        k = max_key(DICT_NUMBER)
        max_value = DICT_NUMBER[k]
        bar_height = 0
        p = [0, 0]
        y_location = 0
        self.calculate_width_bar(
            len(DICT_NUMBER)
        )
        p[0] += self.distant_bar
        for k in DICT_NUMBER:
            bar_height = self.find_height_bar(
                DICT_NUMBER[k],
                max_value
            )
            y_location = self.height \
                - bar_height
            print(k, bar_height,
                    "y_location", y_location)
            p[1] = y_location
            self.draw_rectangle(
                p,
                self.width_bar,
                bar_height,
                "blue"
            )
            p[0] += self.distant_bar\
                + self.width_bar


    def draw_rectangle(self, POINT, 
            WIDTH:int, HEIGHT:int,
            COLOR):
        self.widget.create_rectangle(
            POINT[0], POINT[1], 
            POINT[0] + WIDTH, 
            POINT[1] + HEIGHT, 
            fill=COLOR, 
            outline=COLOR, 
            width=1
        )

    def set_size(self, WIDTH, HEIGHT):
        self.widget.config(
            width=WIDTH, height=HEIGHT)
        self.height = HEIGHT
        self.width = WIDTH

    def grid(self, ROW, COLUMN, 
             STICKY = ""):
        self.widget.grid(
            row = ROW, column= COLUMN,
            sticky= STICKY,
            ipadx=5, ipady=5
        )

    def place(self, 
            LOCATION_X:int, 
            LOCATION_Y:int):
        self.widget.place(
            x=LOCATION_X,
            y=LOCATION_Y
        )

    def pack(self, 
            IS_EXPANDABLE:bool = False,
            SIDE_KEY:str = "left"):
        """
        SIDE_KEY:
        * left
        * top
        * right
        * bottom
        """
        if(IS_EXPANDABLE):
            self.widget.pack(
                fill=tk.BOTH, 
                expand=True,
                side = SIDE_KEY
            )
        else:
            self.widget.pack(
                side = SIDE_KEY
            )