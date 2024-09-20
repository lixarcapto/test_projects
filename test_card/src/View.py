


from btpy.src.btpy.Btpy import Btpy
from Card import Card
from btpy.src.btpy.btpy_maths.mod.vector_sum.vector_sum import*

#def copy(self):

class View:

    def __init__(self):
        self.window = Btpy.Window()
        self.window.set_full_screen()
        self.painter = Btpy.Painter(
            self.window.widget)
        self.size_card_x = 125
        self.size_card_y = 225
        self.values_size = 20
        self.painter.pack_in_axe()
        self.has_event = False
        self.is_on = True
        self.event_buffer = []
        self.painter.set_font("Arial", 20)
        self.__init_functions()

    def __init_functions(self):
        def action(e):
            self.has_event = True
            event = {"event":"click", 
                     "point":[e.x, e.y]}
            self.event_buffer.append(event)
        self.painter.left_click_listener(
            action
        )
        
    def draw_label_name(self,
            TEXT, LOCATION_POINT, 
            REFERENCE_POINT):
        final_point = vector_sum(
            LOCATION_POINT, 
            REFERENCE_POINT
        )
        self.painter.draw_label_text(TEXT,
            final_point)
        
    def receibe(self, MESSAGE):
        self.painter.repaint()
        self.draw_card_field(
            MESSAGE["field_1"], 0)
        self.draw_card_field(
            MESSAGE["field_2"], 
            self.size_card_y * 2)
        self.draw_card_field(
            MESSAGE["deck_1"], 
            self.size_card_y)
        
    def request(self):
        return {
            "events_list":self.event_buffer
        }
        
    def draw_card_field(self, CARD_LIST,
            LOCATION_Y):
        for e in CARD_LIST:
            self.draw_card(
                e, e.get_location())
            print(f"{e} {e.get_location()}")

    def draw_card(self, CARD:Card, location):
        self.painter.draw_image(
            CARD.get_image_layout()[0],
            [location[1], location[0]])
        self.draw_label_name(CARD.name,
            location, [0, 0])
        self.painter.set_brush_color(
            "orange")
        self.draw_label_name(str(CARD.armor),
            [0 , 210], location)
        self.painter.set_brush_color(
            "red")
        self.draw_label_name(str(CARD.attack),
            [0 + self.values_size, 210], 
            location)
        self.painter.set_brush_color(
            "blue")
        self.draw_label_name(str(CARD.magic),
            [0 + self.values_size * 2, 210], 
            location)
        self.painter.set_brush_color(
            "skyblue")
        self.draw_label_name(str(CARD.shield),
            [0 + self.values_size * 3, 210], 
            location)
        self.painter.set_brush_color(
            "yellow")
        self.draw_label_name(str(CARD.cost),
            [0 + self.values_size * 4, 210], 
            location)
        

    def start(self):
        self.window.start()