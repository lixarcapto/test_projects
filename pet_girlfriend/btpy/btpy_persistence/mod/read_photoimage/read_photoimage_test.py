


import tkinter as tk
from PIL import Image, ImageTk
from read_photoimage import*

def read_photoimage_test():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Visual Test")
    photo = read_photoimage(
        "./res/teacher3.png",
        300, 300)
    # Crear un label para mostrar la imagen
    label = tk.Label(root, image=photo)
    label.pack()
    # Mantener la ventana abierta
    root.mainloop()

read_photoimage_test()