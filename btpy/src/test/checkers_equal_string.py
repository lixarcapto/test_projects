

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
    r = Btpy.equal_string(
        "lizard", "LiZard")
    print(r == True)
    try:
        r = Btpy.equal_string(
            5, "LiZard")
    except Exception as e:
        print(e)
    try:
        r = Btpy.equal_string(
            "lizard", 5)
    except Exception as e:
        print(e)

main()