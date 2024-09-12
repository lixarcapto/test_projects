


from ..view.View import View
from ..model.Model import Model

class Controller:

    def __init__(self) -> None:
        self.view = View()
        self.model = Model()
        self.update_view()

    def update_view(self):
        message = self.model.request()
        self.view.render(message)

    def update_model(self):
        message = self.view.request()
        self.model.receive(message)

    def start(self):
        def action(e):
            self.update_model()
            self.write_character()
        self.view.button.add_click_listener(
            action
        )
        self.view.start()

    def write_character(self):
        selected_dict = self.view\
            .get_selected_dict()
        self.model.write_character(
            selected_dict)