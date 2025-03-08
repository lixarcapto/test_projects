

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
    r = Btpy.LimitNumber(4, [0, 10])
    def fn(n):
        r.sum(3)
        print("funciona " + str(r.get()))
        if(n == 5): return True
    Btpy.repeat_each(0.7, fn)

main()