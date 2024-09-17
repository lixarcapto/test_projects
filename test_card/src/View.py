


from btpy.src.btpy.Btpy import Btpy


#def copy(self):

class View:

    def __init__(self):
        self.window = Btpy.Window()
        self.window.set_full_screen()
        self.painter = Btpy.Painter(
            self.window)
        self.size_card_x = 200
        self.size_card_y = 250
        self.painter.pack_in_axe()
        self.painter.set_font("Arial", 20)

    def draw_rectangle_relate(self,
            LOCATION_POINT, 
            DISPLACE_POINT, 
            COLOR,
            TEXT):
        origen1 = Btpy.vector_sum(
            LOCATION_POINT, DISPLACE_POINT)
        destiny1 = Btpy.vector_sum(
            origen1, [40, 40])
        self.painter.set_brush_color(COLOR)
        self.painter.draw_rectangle(
            origen1,
            destiny1
        )
        self.painter.set_brush_color("WHITE")
        letter_point = Btpy.vector_sum(
            origen1, [20, 20]
        )
        self.painter.draw_text(TEXT, 
            letter_point)
        
    def draw_label_name(self,
            TEXT, LOCATION_POINT):
        origen1 = Btpy.vector_sum(
            LOCATION_POINT, [0, 0])
        destiny1 = Btpy.vector_sum(
            origen1, [self.size_card_x, 30])
        self.painter.set_brush_color("gray")
        self.painter.draw_rectangle(
            origen1,
            destiny1
        )
        self.painter.set_brush_color("black")
        letter_point = Btpy.vector_sum(
            origen1, [40, 15]
        )
        self.painter.draw_text(TEXT, 
            letter_point)
        
    def draw_card_field(self, CARD_LIST):
        x = 0
        for e in CARD_LIST:
            self.draw_card(e, [x, 0])
            x += self.size_card_x

    def draw_card(self, CARD, location):
        self.painter.draw_image(
            CARD.route,
            [location[1], location[0]])
        self.draw_label_name(CARD.name,
            location)
        self.draw_rectangle_relate(
            location,
            [0, 210],
            "orange",
            str(CARD.armor)
        )
        self.draw_rectangle_relate(
            location,
            [40, 210],
            "red",
            str(CARD.attack)
        )
        self.draw_rectangle_relate(
            location,
            [80, 210],
            "blue",
            str(CARD.magic)
        )
        self.draw_rectangle_relate(
            location,
            [120, 210],
            "skyblue",
            str(CARD.shield)
        )
        self.draw_rectangle_relate(
            location,
            [160, 210],
            "yellow",
            str(CARD.cost)
        )
        

    def start(self):
        self.window.start()