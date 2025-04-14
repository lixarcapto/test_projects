

import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ..frame.Frame import Frame
from ..radio_box.RadioBox import RadioBox

class Questionary(WidgetComposite):

    def __init__(self, widget, 
            title):
        super().__init__(widget, False)
        self.radio_box = RadioBox(
            self.widget,
            ""
        )
        self.radio_box.label_title.config(
            bg = "#FFFFFF")
        self.radio_box.pack()
        self.set_title(title)
        self.questionary_list\
            :list[dict] = []
        self.answer_list = []
        self.set_title(title)
        self.callback = None
        self.index = 0

    def get_value(self)->list[str]:
        return self.answer_list

    def __add_answer(self):
        value = self.radio_box.get_value()
        self.answer_list.append(value)

    def add_listener(self, CALLBACK):
        self.callback = CALLBACK

    def increment_index(self):
        leng = len(self.questionary_list)
        print(f"index {self.index}, leng {leng}")
        if(self.index < leng -1):
            self.index += 1

    def update_question(self):
        question_dict = self\
            .questionary_list[self.index]
        self.radio_box.set_title(
            question_dict["question"]
        )
        self.radio_box.set_content(
            question_dict["option_list"]
        )
        self.__add_default_listener()

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

    def __is_limit_question(self):
        leng = len(self.questionary_list)
        if(self.index == leng):
            return True
        return False

    def __add_default_listener(self):
        """
        TODO: arreglar este codigo esta
        muy feo.
        """
        def fn(e):
            if(len(self.questionary_list) \
                != len(self.answer_list)):
                self.__add_answer()
            if(not self.__is_limit_question()):
                self.increment_index()
                self.update_question()
            if((self.callback != None)
            and len(self.questionary_list) \
                == len(self.answer_list)):
                self.callback(
                    self.answer_list
                )
        self.radio_box.add_listener(fn)
