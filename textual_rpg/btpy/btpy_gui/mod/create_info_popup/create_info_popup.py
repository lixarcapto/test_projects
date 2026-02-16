

import tkinter as tk
from tkinter import messagebox

def create_info_popup(TITLE:str, 
        CONTENT:str):
    messagebox.showinfo(
        title= TITLE,
        message= CONTENT
    )