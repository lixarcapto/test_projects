


from .dependences import tkinter

class Quicktk:

    def __init__(self):
        self.window = tkinter.Tk()
        self.frame = None
        #self.init()

    def init(self):
        self.init_window()
        self.init_frame()
        self.window.mainloop()

    def add_keyboard_event(self, function):
        self.window.bind("<Key>",
            function)

    def init_window(self):
        # window
        self.window.geometry( "1300x750" )
        self.window.attributes( "-fullscreen", True )
        self.window.bind( "<F11>", self.toggle_full_screen )
        self.window.bind( "<Escape>", self.quit_full_screen )

    def toggle_full_screen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quit_full_screen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def init_frame(self):
        self.frame = tkinter.Frame(\
                           self.window,
                           width = 1300,
                           height = 750
                           )
        self.frame.pack()
        """
        self.frame.place(\
                        x = 0,
                        y = 0
                        )
        """

    def destroy(self):
        self.window.destroy()

    # ACCESORS ---------------------------------------------

    def get_window(self):
        return self.window

    def set_background(self, color):
        self.window.config(background = color)
        self.frame.config(background = color)
