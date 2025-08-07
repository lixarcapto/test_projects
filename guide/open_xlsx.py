


import os
import sys
import openpyxl

def open_xlsx(ruta_archivo: str) -> None:
    """
    Abre un archivo con la aplicación 
    predeterminada del sistema operativo.
    
    Esta función es multiplataforma y 
    funciona en Windows, macOS y Linux.
    Args:
        ruta_archivo (str): La ruta completa del archivo que se desea abrir.
    """
    if not os.path.exists(ruta_archivo):
        print(f"❌ Error: El archivo no se encontró en la ruta: '{ruta_archivo}'")
        return

    try:
        if sys.platform == "win32":
            # Para Windows, usamos os.startfile
            os.startfile(ruta_archivo)
        elif sys.platform == "darwin":
            # Para macOS, usamos el comando 'open'
            os.system(f'open "{ruta_archivo}"')
        elif sys.platform.startswith("linux"):
            # Para Linux, usamos el comando 'xdg-open'
            os.system(f'xdg-open "{ruta_archivo}"')
        else:
            print(f"❌ Error: Plataforma no compatible: {sys.platform}")
            return
            
        print(f"✅ Se ha solicitado abrir el archivo '{ruta_archivo}'.")

    except Exception as e:
        print(f"❌ Ocurrió un error al intentar abrir el archivo: {e}")