


import os
import sys

def open_docx(PATH: str) -> None:
    """
    Abre un archivo .docx con la 
    aplicación predeterminada 
    del sistema.
    """
    # 1. Verifica si el archivo existe
    if not os.path.exists(PATH):
        print(f"❌ Error: El archivo no se encontró en la ruta: '{PATH}'")
        return

    try:
        # 2. Elige el comando según el sistema operativo
        if sys.platform == "win32":
            # Para Windows, utiliza os.startfile()
            os.startfile(PATH)
        elif sys.platform == "darwin":
            # Para macOS, utiliza el comando 'open'
            os.system(f'open "{PATH}"')
        elif sys.platform.startswith("linux"):
            # Para la mayoría de las distribuciones de Linux, usa 'xdg-open'
            os.system(f'xdg-open "{PATH}"')
        else:
            print(f"❌ Error: Plataforma no compatible: {sys.platform}")
            return
            
        print(f"✅ Se ha solicitado abrir el archivo '{PATH}'.")

    except Exception as e:
        print(f"❌ Ocurrió un error al intentar abrir el archivo: {e}")