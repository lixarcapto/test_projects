

import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ..frame.Frame import Frame
from ..radio_box.RadioBox import RadioBox

class Questionary(WidgetComposite):

    def __init__(self, widget, 
            title):
        super().__init__(widget, False)
        self.widget = RadioBox(self.widget,
            "")
        self.questionary_list\
            :list[dict] = []
        self.answer_list = []
        self.set_title(title)
        self.index = 0
        self.__add_default_listener()

    def save_answer(self):
        value = self.widget.get_value()
        self.answer_list.append(value)

    def increment_index(self):
        leng = len(self.questionary_list)
        if(self.index < leng):
            self.index += 1

    def update_question(self):
        question_dict = self\
            .questionary_list[self.index]
        self.widget.set_title(
            question_dict["question"]
        )
        self.widget.set_content(
            question_dict["option_list"]
        )

    def set_questionary_list(self, LIST):
        """
        Questionary:
        [
            {
                "question":"",
                "option_list":[""]
            }
        ]
        """
        self.questionary_list = LIST
        self.update_question()

    def __add_default_listener(self):
        def fn(e):
            self.save_answer()
            self.increment_index()
            self.update_question()
        self.widget.add_listener(fn)
