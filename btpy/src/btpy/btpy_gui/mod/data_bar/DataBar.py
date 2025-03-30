



import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ...mod.create_photo_image.create_photo_image import*
from ....btpy_maths.mod.sum_in_range.sum_in_range import*
from ....btpy_maths.mod.set_in_range.set_in_range import*
from ....btpy_maths.mod.percent.part_from_percent import*
from ....btpy_maths.mod.percent.percent_from_part import*
from ...mod.frame.Frame import Frame

class DataBar(WidgetStandard):

    def __init__(self, window, title = ""):
        super().__init__()
        # Crear el Canvas
        self.widget = Frame(window)
        self.widget.set_border(1)
        self.canvas = tk.Canvas(
            self.widget.widget,
            bg="gray")
        self.label_title = tk.Label(
            self.widget.widget
        )
        self.bar_color = "red"
        self.is_horizontal:bool = True
        self.is_graduated:bool = False
        self.graduation_number:int = 0
        self.range_list:list[int] = [0, 0]
        self.set_size(100, 20)
        self.set_title(title)

    def set_is_horizontal(self, BOOL:bool):
        self.is_horizontal = BOOL


    def set_title(self, TEXT:str):
        self.label_title.config(text = TEXT)

    def get_title(self)->str:
        return self.label_title.cget("text")

    def draw_value(self, WIDTH, HEIGHT):
        text_ = f"{self.range_list[0]}"\
            + f"/ {self.range_list[1]}"
        if(not self.is_horizontal):
            text_ = text_.replace(" ", "\n")
        self.canvas.create_text(
            WIDTH / 2, 
            HEIGHT / 2, 
            text=text_,
            fill="white"
        )


    def set_value(self, 
            RANGE_LIST:list[int]):
        self.range_list = RANGE_LIST
        self.draw_bar()

    def set_size(self, WIDTH:int, 
            HEIGHT:int):
        self.canvas.config(width=WIDTH, 
            height=HEIGHT)
        
    def get_height(self)->int:
        return int(self.canvas.cget(
            "height"))

    def get_width(self)->int:
        return int(self.canvas.cget(
            "width"))
    
    def draw_bar(self):
        self.canvas.delete("all")
        if(self.is_horizontal):
            self.__draw_bar_X(
                self.get_width(),
                self.get_height()
            )
        else:
            self.__draw_bar_Y(
                self.get_height(),
                self.get_width()
            )
        
    def __draw_bar_X(self,
            WIDTH, HEIGHT):
        WIDTH = self.get_width()
        HEIGHT = self.get_height()
        percent = percent_from_part(
            self.range_list[0],
            self.range_list[1]
        )
        print("percent", percent)
        part = part_from_percent(
            percent, WIDTH)
        print("part", part)
        self.draw_rectangle(
            part,
            HEIGHT
        )
        if(self.is_graduated):
            self.draw_graduation_x(
                WIDTH,
                HEIGHT,
                self.graduation_number
            )
        self.draw_margin(
            WIDTH,
            HEIGHT
        )
        self.draw_value(
            WIDTH,
            HEIGHT
        )

    def __draw_bar_Y(self,
            WIDTH, HEIGHT):
        WIDTH = self.get_width()
        HEIGHT = self.get_height()
        percent = percent_from_part(
            self.range_list[0],
            self.range_list[1]
        )
        print("percent", percent)
        part = part_from_percent(
            percent, HEIGHT)
        print("part", part)
        self.draw_rectangle(
            WIDTH,
            part
        )
        if(self.is_graduated):
            self.draw_graduation_y(
                WIDTH,
                HEIGHT,
                self.graduation_number
            )
        self.draw_margin(
            WIDTH,
            HEIGHT
        )
        self.draw_value(
            WIDTH,
            HEIGHT
        )

    def pack(self, MARGIN:int = 0):
        self.widget.pack(MARGIN)
        if(self.is_horizontal):
            self.label_title.grid(
                row=0, column=0
            )
            self.canvas.grid(
                row=0, column=1
            )
        else:
            self.label_title.grid(
                row=0, column=0
            )
            self.canvas.grid(
                row=1, column=0
            )
    
    def draw_margin(self, WIDTH:int, 
            HEIGHT:int):
        self.canvas.create_rectangle(
            2, 2, 
            WIDTH +1, 
            HEIGHT +1, 
            outline="black", 
            width=1
        )
        
    def draw_rectangle(self, 
            WIDTH:int, HEIGHT:int):
        self.canvas.create_rectangle(
            0, 0, 
            WIDTH + 1, 
            HEIGHT +1, 
            fill=self.bar_color,
            width=0
        )

    def draw_graduation_x(self, WIDTH, 
            HEIGHT, DIVISION):
        step = round(WIDTH / DIVISION)
        for i in range(0, WIDTH, step):
            self.canvas.create_line(
                i, 0, 
                i, HEIGHT + 1, 
                fill="black"
            )

    def draw_graduation_y(self, WIDTH, 
            HEIGHT, DIVISION):
        step = round(HEIGHT / DIVISION)
        for i in range(0, HEIGHT, step):
            self.canvas.create_line(
                0, i, 
                WIDTH + 1, i,
                fill="black"
            )