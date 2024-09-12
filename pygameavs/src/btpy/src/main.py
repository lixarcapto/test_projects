

from btpy.Btpy import Btpy
import tkinter as tk
import time

def get_type_base(TYPE_CLASS):
    if(TYPE_CLASS == int): return 0
    elif(TYPE_CLASS == str): return ""
    elif(TYPE_CLASS == float): return 0.0
    elif(TYPE_CLASS == list): return []
    elif(TYPE_CLASS == dict): return {}

def main():

    r = ""
    #--------------------------------
        

    


    

    """
    window = Btpy.Window()
    window.set_full_screen()
    label = Btpy.Label(window)
    label.pack_without_expansion()
    text_box = Btpy.Input(window)
    text_box.pack_without_expansion()
    def action(e):
        text = text_box.extract_text()
        text = Btpy.remove_char(text, 
            len(text) -1)
        label.set_text(text)
    text_box.add_enter_listener(action)
    window.start()
    """

    #------------------------------
    print(r)

main()