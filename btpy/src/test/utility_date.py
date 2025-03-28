

import sys
import os

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)
import time

from btpy.Btpy import Btpy

def main():
    time = Btpy.Date(26, 10, 2023)
    time2 = Btpy.Date(1, 1, 1)
    print("numeric date",
        time.get_numeric_british_date())
    print("days", time2.convert_to_days())
    time.sum_date_time(time2)
    print("british date",
        time.get_british_date())
    print("numeric date",
        time.get_numeric_british_date())

main()