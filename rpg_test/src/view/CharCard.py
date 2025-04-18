

from btpy.Btpy import Btpy

class CharCard:

    def __init__(self,widget):
        self.frame = Btpy.Frame(
            widget)
        self.card = Btpy.SimpleCard(
            self.frame,
            "vertical",
            False
        )
        self.card.label_title.config(
            bg = "blue")
        self.card.label_icon.config(
            bg = "white")
        self.card.pack(False, "left")
        self.stat_frame = Btpy.Frame(
            self.frame
        )
        self.stat_frame.pack(
            False, "left"
        )
        self.attack_label = Btpy.Label(
            self.stat_frame
        )
        self.attack_label\
            .set_foreground_color("white")
        self.attack_label\
            .set_background_color("red")
        self.attack_label.pack(
            False, "top"
        )
        self.load_bar = Btpy.DataBar(
            self.stat_frame, "life"
        )
        self.load_bar.pack(False, "top")

    def set_background_color(self, COLOR):
        self.card.label_title.config(
            bg = COLOR)

    def pack(self, is_expandable, side):
        self.frame.pack(
            is_expandable, side)

    def set_render_dict(self, render_dict):
        self.card.set_title(
            render_dict["title_text"]
        )
        self.card.set_description(
            render_dict["character_text"]
        )
        self.card.set_icon(
            render_dict["path_image"]
        )
        text = render_dict["attack"]
        self.attack_label.set_title(
            f"Attack:  {text}  "
        )
        self.load_bar.set_value(
            render_dict["range_bar"]
        )