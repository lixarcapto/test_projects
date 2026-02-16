
import sys
import os

# Obtiene la ruta absoluta del directorio del script actual.
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Sube dos niveles en la jerarquía de directorios.
directorio_padre = os.path.dirname(directorio_actual)
directorio_abuelo = os.path.dirname(directorio_padre)

# Añade el directorio abuelo al sys.path.
sys.path.append(directorio_abuelo)

from btpy.Btpy import Btpy

def main():
    mi_diccionario = {
        "USR_001": {"Nombre": "Carlos", "Email": "carlos@mail.com", "Edad": 28},
        "USR_002": {"Nombre": "Marta", "Email": "marta@mail.com", "Ciudad": "Madrid"}, # Falta 'Edad', tiene 'Ciudad'
        "USR_003": {"Nombre": "Elena", "Edad": 32}
    }
    Btpy.write_xlsx_nested_dict_row(
        "./nested_dict_writed.xlsx",
        mi_diccionario
    )

main()