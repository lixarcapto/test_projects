
import pygame
from basic.btpy.btpy import*

class PgEntity:

    range_limit_x = [0, 0]
    range_limit_y = [0, 0]

    def __init__(self) -> None:
        self.point = [0, 0]
        self.image_route = ""
        self.image = None

    def write(self):
        txt = f"{PgEntity.range_limit_x=}\n"
        txt += f"{PgEntity.range_limit_y=}\n"
        txt += f"{self.point=}\n"
        return txt

    def set_size_map(range_arr:list[int]):
        PgEntity\
            .range_limit_x = [0, range_arr[0]]
        PgEntity\
            .range_limit_y = [0, range_arr[1]]

    def load(self, screen):
        self.image = pygame.image\
            .load(self.image_route)\
                .convert()
        screen.blit(self.image, self.point)

    def set_image(self, route:str):
        self.image_route = route

    def repaint(self, screen):
        screen.blit(self.image, 
            (self.point[0], self.point[1]))
        
    def center(self):
        self.point[0] = PgEntity\
            .range_limit_x[1] / 2
        self.point[1] = PgEntity\
            .range_limit_y[1] / 2

    """
    TODO: añadir este algoritmo de mover 
    puntos a basic things.
    """
    def move(self, screen, 
               range_arr:list[int]):
        # suma las locaciones con el movimiento
        # para encontrar si esta en el limite
        x = range_arr[0] + self.point[0] 
        limit_x = PgEntity.range_limit_x
        y = range_arr[1] + self.point[1] 
        limit_y = PgEntity.range_limit_y
        if(Btpy.in_range(x, limit_x)):
            self.point[0] += range_arr[0]
        if(Btpy.in_range(y, limit_y)):
            self.point[1] += range_arr[1]
        self.repaint(screen)