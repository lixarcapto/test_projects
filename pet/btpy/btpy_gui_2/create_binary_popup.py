

import tkinter as tk
from tkinter import messagebox

def create_binary_popup(question_text):
    answer = messagebox.askyesno(
            "", 
            question_text
    )
    return answer