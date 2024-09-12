

from ...mod.mix_operation.abs_sum import*

class SpiralGen:

    """
    Clase que permite generar índices 
    para una matriz de dos dimensiones 
    que se recorre en espiral del interior 
    hacia afuera.
    TODO: añadir que pueda iniciar el 
    espiral desde afuera.
    """

    def __init__(self,
                 point,
                 size_x, 
                 size_y) -> None:
        self.x_symbol = -1
        self.y_symbol = 1
        self.point_sum_x = 0
        self.point_sum_y = 0
        self.counter_x = 0
        self.counter_y = 0
        self.reach_limit_x = False
        self.reach_limit_y = False
        self.size_x = size_x -1
        self.size_y = size_y -1
        self.point = point.copy()
    
    def get_x(self):
        return self.point[0]
    
    def get_y(self):
        return self.point[1]
        
    def next(self):
        # operaciones para calcular indices
        # es una suma absoluta
        self.point_sum_x = abs_sum(
            self.x_symbol, 
            self.counter_x
        )
        self.point_sum_y = abs_sum(
            self.y_symbol, 
            self.counter_y
        )
        # invierte los signos de la 
        # operacion para calcular indices
        self.x_symbol *= -1
        self.y_symbol *= -1
        # calcula el indice final 
        # los otros solo son puntos para 
        # sumar
        self.point[0] += self.point_sum_x
        self.point[1] += self.point_sum_y
        # impresion
        print(f"{self.point[0]}/{self.point[1]}")
        # analiza si llego al limite 
        if(self.point[0] >= self.size_x
        or self.point[0] < 0):
            self.reach_limit_x = True
        if(self.point[1] >= self.size_y
        or self.point[1] < 0):
            self.reach_limit_y = True
        # avansa los contadores
        if(not self.reach_limit_x):
            self.counter_x += 1
        if(not self.reach_limit_y):
            self.counter_y += 1
        # termina el iterador al llegar 
        # al limite
        if((self.reach_limit_x)
        and (self.reach_limit_y)):
            return False
        return True
        

    def write(self):
        return f"{self.point[0]=}\
        /{self.point[1]=}"

    def __str__(self):
        return self.write()