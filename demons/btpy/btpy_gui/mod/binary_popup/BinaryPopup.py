

import tkinter as tk
from tkinter import messagebox

class BinaryPopup:

    def __init__(self):
        self.question_text = ""
        self.true_text = ""
        self.false_text = ""
        self.callback = (lambda e:e)

    def launch(self):
        answer = messagebox.askyesno(
            "", 
            self.question_text)
        self.callback(answer)