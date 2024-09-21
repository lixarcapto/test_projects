

from .WidgetElement import WidgetElement
import tkinter
from .WidgetButton import WidgetButton
from ...btpy_list.mod.fit_list.fit_list import*

class WidgetPanelButton(WidgetElement):

    def __init__(self, widget, 
            QUANTITY_X, QUANTITY_Y) -> None:
        self.widget = tkinter.Frame(widget)
        self.button_clicked = 0
        self.quantity_x = QUANTITY_X
        self.quantity_y = QUANTITY_Y
        self.total = self.quantity_x \
            * self.quantity_y
        self.button_list = []
        self.init_button_list()

    def get_button_press(self)->int:
        return self.button_clicked

    def init_button_list(self):
        button = None
        self.limit_button_x \
            = self.quantity_y
        x = 0
        y = 0
        for i in range(self.total):
            button = WidgetButton(
                self.widget)
            button.widget.grid(
                row=y, 
                column=x
            )
            x += 1
            if(x >= self.quantity_x):
                y += 1
                x = 0
            def aux(i):
                def action(e):
                    print(i)
                    self.button_clicked = i
                return action
            button.add_click_listener(aux(i))
            self.button_list.append(button)

    def set_image(self, route):
        for i, button in enumerate(\
                self.button_list):
            button.set_image(route)

    def set_image_list(self, ROUTE_LIST):
        route_list = fit_list(ROUTE_LIST,
            self.total)
        for i, button in enumerate(\
                self.button_list):
            button.set_image(route_list[i])

    def set_text(self, text):
        for i, button in enumerate(\
                self.button_list):
            button.set_text(text)

    def set_text_list(self, TEXT_LIST):
        text_list = fit_list(TEXT_LIST,
            self.total)
        for i, button in enumerate(\
                self.button_list):
            button.set_text(text_list[i])