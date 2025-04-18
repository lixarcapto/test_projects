

from btpy.Btpy import Btpy
from .CharCard import CharCard

class BattleTab:

    def __init__(self, widget, model):
        self.main_frame = Btpy.Frame(
            widget)
        self.frame = Btpy.Frame(
            widget)
        self.model = model
        self.frame.pack(False, "top")
        self.char_card_1 = CharCard(
            self.frame
        )
        self.char_card_1.pack(
            False, "left"
        )
        self.char_card_1\
            .set_background_color("blue")
        self.char_card_2 = CharCard(
            self.frame
        )
        self.char_card_2.pack(
            False, "left"
        )
        self.char_card_1\
            .set_background_color("red")
        self.btn_advance = Btpy.Button(
            widget, "new turn..."
        )
        self.btn_advance.pack(
            False, "top")
        self.btn_new_match = Btpy.Button(
            widget, "new match"
        )
        self.btn_new_match.pack(
            False, "top")
        self.btn_new_match.add_listener(
            lambda e:self.new_match()
        )
        self.btn_advance.add_listener(
            lambda e:self.advance())
    
    def pack(self):
        self.main_frame.pack()
        
    def new_match(self):
        self.model.new_match()
        self.update()

    def advance(self):
        self.model.advance_turn()
        self.update()

    def update(self):
        render_list = self.model.get_render()
        render_1 = render_list[0]
        self.char_card_1.set_render_dict(
            render_1
        )
        #
        render_2 = render_list[1]
        self.char_card_2.set_render_dict(
            render_2
        )