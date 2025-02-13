

from btpy_lib.btpy.src.btpy.Btpy import Btpy
from compile_file import*
import os

"""
Inicia una consola que pide la URL
de la carpeta javascript.
"""
def start_console():
    user_input = ""
    while(True):
        user_input = input("write path")
        if(user_input == ""):
            break
        compile_file(user_input)
        #Btpy.clean_console()
 
if __name__ == "__main__":
    start_console()


