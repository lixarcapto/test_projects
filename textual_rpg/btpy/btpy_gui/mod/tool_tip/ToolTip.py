


import tkinter as tk

class ToolTip:
    """
    Crea una burbuja de información 
    para un widget de Tkinter.
    TODO: arreglar esto, lo creo GEMINI
    y no se que hace, y esta muy raro.
    """
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self.size_font = 12
        self.background_color = "white"
        self.foreground_color = "black"
        def showtip(event):
            """Muestra la burbuja de información"""
            self.x, self.y = event.x_root, event.y_root
            self.showtip()

        def hidetip(event):
            """Esconde la burbuja de información"""
            self.hidetip()

        self.widget.bind("<Enter>", showtip)
        self.widget.bind("<Leave>", hidetip)

    def showtip(self):
        """Muestra la burbuja de información"""
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("anchor")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # Crea una ventana emergente
        self.tipwindow = tw = tk.Toplevel(self.widget)
        # Quita la decoración de la ventana
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(
            tw, 
            text=self.text, 
            justify=tk.LEFT,
            background="#ffffe0", 
            relief=tk.SOLID, 
            borderwidth=1,
            bg = self.background_color,
            fg = self.foreground_color,
            font=(
                "tahoma", 
                self.size_font, 
                "normal")
            )
        label.pack(ipadx=1)

    def hidetip(self):
        """Esconde la burbuja de información"""
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()