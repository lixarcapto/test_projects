
import pygame
from PgEntity import PgEntity
from basic.btpy.btpy import*

class PgMovile(PgEntity):

    range_limit_x = [0, 0]
    range_limit_y = [0, 0]

    def __init__(self, name):
        self.point = [0, 0]
        self.image_route = ""
        self.image = None
        self.name = name

    def load(self, screen):
        self.image = pygame.image\
            .load(self.image_route)\
                .convert_alpha()
        screen.blit(self.image, self.point)
        