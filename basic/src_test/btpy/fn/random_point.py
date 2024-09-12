


from ..out_deps import random

"""
Función que genera un punto Aleatorio en el 
rango enviado. El formato de punto es un 
array numerico 2x.
"""
def random_point(range_ar:list[int])\
            ->list[int]:
        return [
            random.randint(range_ar[0], 
                        range_ar[1]),
            random.randint(range_ar[0], 
                        range_ar[1]),
        ]