



import subprocess
import os

def load_word(DOCX_ROUTE:str)->None:
    """
     Función que obtiene la ruta 
     absoluta de un documento docx para  
     ejecutarlo en el programa Word 
     en windows.
    """
    absolute_route = os.path.abspath(
        DOCX_ROUTE)
    subprocess.Popen(['start', 
        absolute_route], shell=True)