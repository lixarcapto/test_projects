


import sys
import os

def ascends_on_sys_path(LEVELS: int)\
        -> None:
    """
    Añade un directorio ancestro del 
    script actual al sys.path, permitiendo 
    la importación de módulos.
    """
    if not isinstance(LEVELS, int):
        raise TypeError(
            f"The argument LEVELS must be an integer type, but its data is {type(LEVELS)}({LEVELS})"
        )
    if LEVELS < 1:
        raise ValueError(
            f"The argument LEVELS must be greater than or equal to zero, but it is {LEVELS}"
        )
    directorio_actual = os.path.dirname(
        os.path.abspath(__file__))
    directorio_objetivo = directorio_actual
    for _ in range(LEVELS):
        directorio_objetivo = os.path.dirname(directorio_objetivo)
    sys.path.append(directorio_objetivo)