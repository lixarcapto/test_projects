

"""
    Funcion para fusionar dos arrays
    en uno solo.
"""

def fuse(array_a, array_b) -> list:
    for i in range(len(array_a)):
        array_b.append(array_a[i])
    return array_b