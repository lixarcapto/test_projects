


from btpy.src.btpy.Btpy import Btpy

class PlayerFrame:

    SCAPE_KEY = "\x1b"
    ALLOWED_KEYS = "12345"

    def __init__(self, window) -> None:
        self.frame = Btpy.Frame(window)
        self.frame.pack_in_axe()
        self.size_text_x = 50
        self.size_text_y = 40
        self.size_icon_x = 650
        self.size_icon_y = 650
        self.message = {
            "index_selected":"",
            "event":""
        }
        self.init_calls(window)

    def init_calls(self, window):
        self.init_label(window)
        self.init_text(window)
        self.init_icon(window)
        self.text.widget.focus_set()

    def init_icon(self, window):
        self.icon = Btpy.Label(window)
        """
        self.icon.set_size(
            self.size_icon_x, 
            self.size_icon_y
        )
        """
        self.icon.pack_without_expansion(
            self.icon.SIDE.RIGHT
        )

    def init_text(self, window):
        self.text = Btpy.Input(window)
        self.text.set_text("texto")
        self.text.set_font(
            self.text.FONT.ARIAL, 14)
        self.text.set_line_spacing(10)
        self.text.set_size(
            self.size_text_x, 
            self.size_text_y
        )
        self.text.pack_without_expansion(
            self.text.SIDE.LEFT
        )
        

    def init_label(self, window):
        self.label = Btpy.Label(window)
        self.label.set_background("white")
        self.label.set_font("Arial", 20, 
            self.label.STYLE.BOLD)
        self.label.pack_in_axe(
            self.label.AXE_EXPANSION.X,
            self.label.SIDE.TOP)

    def add_update_listener(self, function):
        def user_action(event):
            key = event.char
            if(key == self.SCAPE_KEY):
                self.launch_turn_off()
            if(not key in self.ALLOWED_KEYS):
                return None
            self.event_triggered = True
            self.message["index_selected"] \
                = key
            function()
        self.add_key_listener(user_action)

    def launch_turn_off(self):
        self.message["event"] = "turn_off"

    def add_key_listener(self, function):
        self.text.widget.bind(
            "<Key>", 
            function
        )
        
    def receive(self, message:dict):
        self.label.set_title(message["title"])
        self.write_in_input(message["text"])
        if(message["route_image"] != ""):
            self.set_image(message["route_image"])
        
    def write_in_input(self, TEXT):
        text = Btpy.sort_text(
            TEXT, self.size_text_x)
        self.text.set_text(text)

    def set_image(self, ROUTE):
        photo = Btpy.read_photoimage(
            ROUTE,
            self.size_icon_x, 
            self.size_icon_y
        )
        self.icon.set_photo(photo)

    def request(self)->dict:
        self.event_triggered = False
        return self.message