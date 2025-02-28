



import os
import sys

def get_root():
    if getattr(sys, 'frozen', False):
        # Si el script está empaquetado como un ejecutable (usando PyInstaller, etc.)
        return os.path.dirname(sys.executable)
    else:
        # Si el script se ejecuta directamente
        return os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))