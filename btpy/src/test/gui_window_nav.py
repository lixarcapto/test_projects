

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
    window = Btpy.WindowNav("titulo")
    window.set_is_fullscreen(True)
    frame = Btpy.FrameSectioned(window)
    btn = Btpy.Button(frame.head, "frame1")
    btn.pack(True)
    window.add_frame("main", frame)
    frame2 = Btpy.FrameSectioned(window)
    btn2 = Btpy.Button(frame2.head, "frame2")
    btn2.pack(True)
    window.add_frame("second", frame2)
    window.select_frame("main")
    window.start()
    

main()