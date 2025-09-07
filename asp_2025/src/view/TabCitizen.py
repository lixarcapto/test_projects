

from btpy.Btpy import Btpy
import os
from .path_dict import*

class TabCitizen(Btpy.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.texture_pack:str = ""
        self.res_path:str = "./res/"
        self.__id_citizen_list:list[int]\
            = []
        self.model = None
        self.head_panel = None
        self.btn_new_game = None
        self.button_new_character = None
        self.button_new_day = None
        self.button_execute = None
        self.swiper = None
        self.text = None
        self.canvas = None
        self.render_dict:dict = {}
        self.__init_components()
        self.add_listeners()

    def __init_components(self):
        self.__init_head_panel()
        self.__init_text()
        self.__init_canvas()

    def __init_canvas(self):
        self.canvas = Btpy.Canvas(
            self.widget, "canvas"
        )
        self.canvas.set_size(400, 600)
        self.canvas.pack("left")

    def __init_text(self):
        self.text = Btpy.TextArea(
            self.widget, "text")
        self.text.pack("left")
        self.text.set_is_enabled(True)
        font_ = self.text.get_font()
        font_.config(size = 16)
        self.text.text_area.config(
            font=font_
        )
        self.text.set_size(30, 18)

    def __init_head_panel(self):
        self.head_panel = Btpy.Frame(
            self.widget)
        self.head_panel.pack("left")
        self.button_new_character = Btpy\
            .Button(
                self.head_panel, 
                "new character"
        )
        self.button_new_character.grid(0, 1)
        self.button_new_month = Btpy.Button(
            self.head_panel, 
            "1 month more"
        )
        self.button_new_month.grid(0, 2)
        self.button_new_year = Btpy.Button(
            self.head_panel, 
            "1 year more"
        )
        self.button_new_year.grid(0, 3)
        self.button_execute = Btpy.Button(
            self.head_panel,
            "execute"
        )
        self.button_execute.grid(0, 4)
        def fn(e):
            self.model.execute_citizen()
            self.update_character_canvas()
        self.button_execute.add_listener(
            fn
        )
        self.__init_swiper()

    def __init_swiper(self):
        self.swiper = Btpy.SwiperRange(
            self.head_panel,
            "citizen",
            [0, 0]
        )
        self.swiper.grid(0, 5)
        def fn(e):
            idx = self.swiper.get_value()
            id_ = self.render_dict\
                ["citizen_id_list"]\
                [idx]
            self.model\
                .set_citizen_id_selected(
                    id_
                )
            self.update_citizen_graphics()
            print("swiper event value", idx)
        self.swiper.add_listener(fn)

    def add_new_character_listener(self):
        def fn(e):
            self.update()
        self.button_new_character\
            .add_listener(fn)
        
    def update_swiper(self):
        id_list = self\
            .render_dict["citizen_id_list"]
        size = len(id_list)
        self.swiper.set_content(
            [0, size -1]
        )
        id_ = self\
            .render_dict["citizen_id_select"]
        self.model.set_citizen_id_selected(
            id_
        )

    def __add_update_listener(self):
        self.__add_button_new_month_listener()
        self.__add_button_new_year_listener()

    def __add_button_new_month_listener(self):
        def fn(e):
            self.model.advance_months(1)
            self.update()
        self.button_new_month.add_listener(fn)

    def __add_button_new_year_listener(self):
        def fn(e):
            self.model.advance_months(4)
            self.update()
        self.button_new_year.add_listener(fn)

    def update_background_canvas(self):
        list_ = self.model\
            .render_select_region()
        path = ""
        path_list = []
        for k in list_:
            path = self.res_path \
                + self.texture_pack\
                + "region/"\
                + k \
                + ".png"
            if(os.path.exists(path)):
                path_list.append(path)
        
        self.canvas.draw_image_layers(
            [0, 0],
            path_list
        )

    def update_character_canvas(self):
        key_list = self.model\
            .get_citizen_path_list()
        path_list = []
        path = ""
        print("KEY_LIST", key_list)
        for key in key_list:
            if(not self.exist_character_path(key)):
                continue
            path = self\
                .get_character_path_fron_key(
                    key
                )
            if(os.path.exists(path)):
                path_list.append(path)
        print("RESULT_LIST", path_list)
        self.canvas.draw_image_layers(
            [0, 0],
            path_list
        )

    def exist_character_path(self, 
            KEY:str)->bool:
        return KEY in PATH_DICT

    def get_character_path_fron_key(
            self, KEY:str)->str:
        return "" + self.model\
            .get_texture_pack_path()\
            + "character/" + PATH_DICT[KEY]

    def update_canvas(self):
        self.canvas.repaint()
        self.update_background_canvas()
        self.update_character_canvas()
        

    def update_character_text(self):
        id_ = self.model\
            .get_citizen_id_selected()
        print("citizen_select", id_)
        text = self.model\
            .get_citizen_text_by_id(id_)
        text = Btpy.sort_text(text, 30)
        self.text.set_value(text)

    def update_citizen_graphics(self):
        self.update_background_canvas()
        self.update_canvas()
        self.update_character_text()

    def update(self):
        self.render_dict = self.model\
            .get_render_citizen()
        self.update_swiper()
        self.update_citizen_graphics()

    def add_listeners(self):
        self.add_new_character_listener()
        self.__add_update_listener()