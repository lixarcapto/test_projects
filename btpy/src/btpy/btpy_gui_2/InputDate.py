
from tkinter import ttk
import tkinter.font as tkFont
import tkinter as tk
from btpy.btpy_utilitys.mod.date.Date import Date
from tkinter import ttk

class InputDate:

    MONTH_NUMBER = 12
    DAYS_BY_MONTH = {
        "january":31,
        "february":29,
        "march":31,
        "april":30,
        "may":31,
        "june":30,
        "july":31,
        "august":31,
        "september":30,
        "october":31,
        "november":30,
        "december":31
    }

    def __init__(self, widget, 
            TEXT = ""):
        self.widget = tk.Frame(
            widget
        )
        self.widget.pack()
        self.year_range_arr__:list = [0, 1]
        self.combo_day = ttk.Combobox(
            self.widget, 
            values=[], 
            state="readonly",
            width=4
        )
        self.combo_month = ttk.Combobox(
            self.widget, 
            values=[], 
            state="readonly",
            width=10
        )
        self.combo_year = ttk.Combobox(
            self.widget, 
            values=[], 
            state="readonly",
            width=5
        )
        self.combo_day.grid(
            row=0, column=0)
        self.combo_month.grid(
            row=0, column=1)
        self.combo_year.grid(
            row=0, column=2)
        # listener
        def fn(e):
            self.update_day()
        self.combo_month.bind(
            "<<ComboboxSelected>>",
            fn
        )
        self.update_month()
        self.update_day()
        self.update_year()

    def set_range_year(self, RANGE_LIST):
        self.year_range_arr__ = RANGE_LIST
        self.update_year()

    def update_year(self):
        list_ = []
        range_ = self.year_range_arr__
        for i in range(range_[0], range_[1]):
            list_.append(str(i))
        self.combo_year.config(
            values=list_
        )
        self.combo_year.set(list_[0])
        
    def update_month(self):
        month_key_arr = list(
            InputDate.DAYS_BY_MONTH.keys())
        self.combo_month.config(
            values=month_key_arr)
        self.combo_month.set(
            month_key_arr[0])

    def update_day(self):
        month = self.combo_month.get()
        day_list = self.get_day_list(
            month)
        self.combo_day.config(
            values=day_list)
        self.combo_day.set(day_list[0])
        
    def get_day_list(self, MONTH_NAME):
        days_number = InputDate\
            .DAYS_BY_MONTH[MONTH_NAME]
        list_ = []
        for i in range(1, days_number +1):
            list_.append(str(i))
        return list_

