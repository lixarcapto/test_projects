





import tkinter as tk

class ClickTrainer:

    def __init__(self):
        self.click_list = []
        self.root = tk.Tk()
        self.root.attributes('-alpha', 0.5)  # Establece la transparencia a 0.5 (semitransparente)
        self.root.overrideredirect(True)
        self.canvas = tk.Canvas(
            self.root, 
            bg='white', 
            highlightthickness=0
        )
        self.canvas.pack(
            fill=tk.BOTH, 
            expand=True
        )
        self.screen_width = self.root\
            .winfo_screenwidth()
        self.screen_height = self.root\
            .winfo_screenheight()
        self.root.geometry(
            f"{self.screen_width}x{self.screen_height}+0+0")  
        # Establece el tamaño y la 
        # posición de la ventana
        def cerrar_ventana(event):
            """Cierra la ventana Tkinter."""
            self.root.destroy()
            print(self.click_list)
        # Vincula la tecla Esc a la función cerrar_ventana
        self.root.bind('<Escape>', 
                cerrar_ventana)
        def click_listener(event):
            x, y = event.x_root, event.y_root
            self.click_list.append([x, y])
        # Vincula el evento de clic del botón izquierdo a la función on_click
        self.root.bind("<Button-1>", 
          click_listener)
        self.root.mainloop()



