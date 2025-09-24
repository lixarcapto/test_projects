


from btpy.Btpy import Btpy
import tkinter as tk
from Model import Model

class FrameExperiences:

    def __init__(self, widget, model):
        self.model:Model = model
        self.frame = tk.Frame(
            widget
        )