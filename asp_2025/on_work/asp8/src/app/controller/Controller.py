

from btpy.src.btpy.Btpy import Btpy

class Controller:

    def __init__(self, view, model) -> None:
        self.view = view
        self.model = model

    def new_map(self):
        self.model.create_map()

    def create_user(self):
        nickname = input("user name:")
        self.model.create_user(nickname)
        self.view.nickname = nickname

    def start(self):
        self.new_map()
        self.create_user()
        self.new_game()
        text_on_wait = ""
        user_input = ""
        while(True):
            Btpy.clean_console()
            user_input = input(text_on_wait)
            if(user_input == "f"):
                break
            self.model.update()
            text_on_wait = self.render()


    def new_game(self):
        self.model.select_new_person(
            self.view.nickname)

    def take_desition(self, key):
        self.model.take_desition(
            self.view.nickname, 
            key
        )

    def render(self):
        txt = self.model.render(
            self.view.nickname)
        return txt

    def write_all(self):
        print(self.model.write())