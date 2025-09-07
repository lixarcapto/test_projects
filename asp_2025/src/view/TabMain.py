

from btpy.Btpy import Btpy
import os

class TabMain(Btpy.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.texture_pack:str = ""
        self.model = None
        self.button_box = Btpy.ButtonBox(
            self.widget,
            False,
            "Menu"
        )
        self.button_box.set_components(
            4, 1)
        self.button_box.set_content(
            [
                "new game",
                "load game",
                "guide",
                "exit"
            ]
        )
        self.button_box.pack(
            True, "left")
        self.canvas = Btpy.Canvas(
            self.widget, "main"
        )
        self.canvas.set_size(1000, 600)
        self.canvas.draw_path_image(
            [0, 0],
            "./res/texture_pack/default/main_screen_character.png"
        )
        self.canvas.draw_path_image(
            [0, 400],
            "./res/texture_pack/default/asp_icon.png"
        )
        self.canvas.pack(
            True, "left")
        self.add_new_map_listener()

    def add_new_map_listener(self):
        """
        TODO: quitar esta funcion de 
        aqui.
        """
        def fn(e):
            self.model.new_game()
            print("new game init")
            self.update()
            print("citizen select", 
              self.citizen_id_select
            )
        self.button_box.add_listener_to(
            0, fn)

    def update(self):
        pass