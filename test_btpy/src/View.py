


from Model import Model
from btpy.Btpy import Btpy

class View:

    def __init__(self):
        self.model = Model()
        self.flag_duplicate = None
        self.loop_time_seconds = 1
        self.is_started = False
        self.window = Btpy.Window(
            "My first demon")
        self.window.set_size(1000, 700)
        self.label_img = Btpy.SimpleCard(
            self.window, "vertical", False
        )
        self.label_img.grid(0, 1)
        self.card_icon_size = [300, 300]
        self.button_invoke = Btpy.Button(
            self.window, "Invoke")
        self.button_invoke.grid(1, 1)
        self.swiper_magic_circle = Btpy\
            .SwiperImage(self.window, 
                    "magic circle")
        self.swiper_magic_circle.grid(0, 0)
        self.swiper_magic_circle\
            .set_is_cyclical(True)
        self.swiper_magic_circle\
            .set_values_list(
                [
                    "./res/image/magic/magic_circle_1.png",
                    "./res/image/magic/magic_circle_2.png",
                    "./res/image/magic/magic_circle_3.png",
                    "./res/image/magic/magic_circle_4.png",
                    "./res/image/magic/magic_circle_5.png"
                ]
            )
        self.button_invoke.add_listener(
            lambda e:self\
                .react_to_invoke_event()
        )
        self.button_feed = Btpy.Button(
            self.window, "feed")
        self.button_feed.grid(1, 2)
        def fn(e):
            self.model.give_gift()
        self.button_feed.add_listener(fn)
        self.first_update()
        self.init_view_loop()

    def init_view_loop(self):
        def fn(n):
            self.update()
            print("advance_time")
        self.flag_duplicate = Btpy\
            .repeat_each_async(
                self.loop_time_seconds, 
                fn
            )
        
    def react_to_invoke_event(self):
        self.model.random_creature()

    def first_update(self):
        self.label_img.set_title(
            "Laboratorio")
        self.label_img.set_description(
            "Empieza el ritual...")
        self.label_img.set_icon(
            "./res/image/demon/candle_room.png",
            self.card_icon_size
        )
        
    def update(self):
        self.update_creature()

    def update_creature(self):
        if(self.model.creature == None):
            return None
        render = self.model.get_render()
        self.label_img.set_title(
            render["title"])
        self.label_img.set_description(
            render["description"])
        self.label_img.set_icon(
            render["path"],
            self.card_icon_size
        )

    def start(self):
        self.window.start()

