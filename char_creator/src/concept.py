


import subprocess
import os

def load_word(DOCX_ROUTE:str):
    absolute_route = os.path.abspath(
        DOCX_ROUTE)
    subprocess.Popen(['start', 
        absolute_route], shell=True)

def main():
    ruta_archivo = os.path.abspath(
        "./character_data.docx")
    subprocess.Popen(['start', 
        ruta_archivo], shell=True)

main()