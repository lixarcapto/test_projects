

import sys
import os

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)

from btpy.Btpy import Btpy

def main():
    window = Btpy.Window("titulo")
    window.set_is_fullscreen(True)
    file = Btpy.InputFile(window,
            "image", 
            "busca image")
    file.pack()
    file2 = Btpy.InputFile(window,
            "folder", 
            "busca folder")
    file2.pack()
    file3 = Btpy.InputFile(window,
            "text", 
            "busca text")
    file3.pack()
    file4 = Btpy.InputFile(window,
            "any_file", 
            "busca any file")
    file4.pack()
    window.start()

main()