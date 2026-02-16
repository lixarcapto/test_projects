


import shutil
import os

def copy_file(
        source_path: str, 
        destination_path: str)\
        -> bool:
    """
    Copies a file from the source_path 
    to the destination_path.
    Returns:
    bool: True if the file was copied 
    successfully, False otherwise.
    """
    try:
        # Check if the source file exists
        if not os.path.exists(source_path):
            print(f"❌ Error: El archivo de origen no existe: '{source_path}'")
            return False

        # If the destination is an existing directory, append the source filename
        if os.path.isdir(destination_path):
            destination_path = os.path.join(destination_path, os.path.basename(source_path))

        shutil.copy(source_path, destination_path)
        print(f"✅ Archivo copiado exitosamente de '{source_path}' a '{destination_path}'")
        return True
    except FileNotFoundError:
        print(f"❌ Error: La ruta de origen o destino no es válida.")
        return False
    except PermissionError:
        print(f"❌ Error: Permiso denegado para copiar el archivo. Revise los permisos de acceso.")
        return False
    except shutil.SameFileError:
        print(f"❌ Error: Los archivos de origen y destino son el mismo.")
        return False
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado al copiar el archivo: {e}")
        return False