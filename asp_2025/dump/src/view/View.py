

from tkinter import *
from tkinter import ttk

class View:

    def __init__(self):
        self.event = None
        self.frame = Tk()
        self.frame.geometry('1300x720')
        self.frame.configure(bg = 'white')
        self.canvas = Canvas(self.frame, width=500, height=500,
        background="black")
        self.canvas.place(x = 700, y = 0)
        image1 = PhotoImage(file="gas.png")
        self.canvas.create_image(0, 0, image=image1, anchor="nw")
        self.buton = Button(self.frame, text = "pag 2", command = self.clickButton)
        self.buton.place(x = 1000, y = 550, width = 100, height = 50)
        self.text = Text(self.frame, width = 86, height = 30)
        self.text.place(x=0, y=0)
        self.text.insert(END, self.writeText())
        return

    def initLoop(self):
        self.frame.mainloop()

    def writeText(self):
        text = ""
        paragraphCounter = 0
        paragraphLimit = 200
        for i in range(10000):
            if(paragraphLimit == paragraphCounter):
                text += ""
            text += "x"
            paragraphCounter += 1
        return text

    def clickButton(self):
        event = [None] * 2
        event[0] = "advance_time"
        event[1] = ""
        self.event = event
        print("click button")
