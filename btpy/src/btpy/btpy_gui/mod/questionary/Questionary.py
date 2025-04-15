

import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ..frame.Frame import Frame
from ..radio_box.RadioBox import RadioBox
from tkinter import font
from ..label_label.LabelLabel import LabelLabel


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
        font_ = font.Font(
                family="Arial", 
                size=15, 
                weight="bold"
                )
        self.label_symbol = LabelLabel(
            self.widget, 
            "you completed the questionnaire",
        )
        self.label_symbol.set_content(
            " ✔ ")
        self.label_symbol.set_font_content(
            "Arial", 12, True
        )
        self.label_symbol.set_content_color(
            "green",
            "white"
        )
        self.set_title(title)
        self.questionary_list\
            :list[dict] = []
        self.answer_list = []
        self.set_title(title)
        self.callback = None
        self.index = 0

    def show_final_quest(self):
        self.radio_box.pack_forget()
        self.label_symbol.pack()

    def show_radio_box(self):
        self.radio_box.pack()

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
        self.__start_questionary()
        
    def __start_questionary(self):
        self.show_radio_box()
        self.update_question()

    def __is_limit_question(self):
        leng = len(self.questionary_list)
        if(self.index == leng):
            return True
        return False
    
    def has_all_answer(self)->bool:
        len_answer = len(self.answer_list)
        len_question = len(
            self.questionary_list)
        if(len_question == len_answer):
            return True
        return False
    
    def __react_to_selection(self, e):
        if(not self.has_all_answer()):
            self.__add_answer()
        if(not self.__is_limit_question()):
            self.increment_index()
            self.update_question()
        if(self.has_all_answer()):
            if(self.callback != None):
                self.callback(
                self.answer_list
            )
            self.show_final_quest()
        

    def __add_default_listener(self):
        """
        TODO: arreglar este codigo esta
        muy feo.
        """
        self.radio_box.add_listener(
            self.__react_to_selection)
