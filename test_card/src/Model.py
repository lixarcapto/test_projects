

from Player import Player
from btpy.src.btpy.Btpy import Btpy
from Card import Card

class Model:

    CARD_COLLECTION = {}

    def __init__(self):
        self.last_id = 0
        self.player_1 = Player()
        self.player_2 = Player()
        self.phase_key = "COMBAT"
        self.deck_1 = []
        self.deck_2 = []
        self.field_1 = []
        self.field_2 = []
        self.desktop_1 = ""
        self.desktop_2 = ""
        self.size_card_x = 125
        self.size_card_y = 225
        self.scenario = Btpy.Scenario()
        go = None
        self.load_card_collection()
        self.load_desktop_card([
            "princess",
            "peasant",
            "princess"
        ])
        #desktop_1 = self.create_card()
        #self.desktop_1 = desktop_1.get_id()
        self.create_map()

    def update(self):
        self.create_map()

    def create_map(self):
        self.order_in_x(self.deck_1, 1)
        self.order_in_x(self.field_1, 2)

    def order_in_x(self, card_list, 
            field_zone):
        card:Card = None
        x = 0
        y = field_zone * self.size_card_y
        for e in card_list:
            card = self.scenario.get(e)
            card.set_location([x, y])
            self.scenario.set(card)
            x += self.size_card_x

    def create_card(self, KEY):
        card_dict = self.CARD_COLLECTION[KEY]
        card = Card()
        card.set_id(self.last_id)
        self.last_id += 1
        card.load_card_dict(KEY, card_dict)
        self.scenario.__add(card)
        return card

    def load_desktop_card(self, 
            CARD_NAME_LIST):
        card = None
        for e in CARD_NAME_LIST:
            card = self.create_card(e)
            self.deck_1.append(card.get_id())
            card = self.create_card(e)
            self.deck_2.append(card.get_id())

    def load_card_collection(self):
        self.CARD_COLLECTION = Btpy\
            .read_nested_row_xlsx(
                "../res/card_data.xlsx")

    def render_deck_1(self):
        render = []
        card = None
        for id in self.deck_1:
            card = self.scenario.get(id)
            render.append(card)
        return render
    
    def receive(self, MESSAGE:dict):
        events_list = MESSAGE["events_list"]
        for event in events_list:
            if(event["event"] == "click"):
                self.click_effect(event)
        self.update()
    
    def deck_to_field(self, NAME):
        print("deck_to_desktop")
        self.deck_1.remove(NAME)
        self.field_1.append(NAME)

    def click_effect(self, EVENT_DICT):
        name = self.scenario.__object_clicked_id(
            EVENT_DICT["point"]
        )
        print(f"clicked {name}")
        if(name in self.deck_1):
            self.deck_to_field(name)

    def render(self):
        message = {
            "field_1": self.player_1.field_card,
            "field_2": self.player_2.field_card,
            "deck_1": self.render_deck_1()
        }
        return message
        
