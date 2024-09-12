
import pygame
from PgEntity import PgEntity

class PgBack(PgEntity):

    range_limit_x = [0, 0]
    range_limit_y = [0, 0]

    def __init__(self):
        super().__init__()
        self.point = [0, 0]
        self.image_route = ""
        self.image = None

    def load(self, screen):
        self.image = pygame.image\
            .load(self.image_route)\
                .convert_alpha()
        screen.blit(self.image, self.point)