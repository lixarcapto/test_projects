

import pygame
from pygame.locals import *
import sys
from PgEntity import PgEntity
from PgMovile import PgMovile
from PgBack import PgBack
from basic.btpy.btpy import*

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
range_size = [SCREEN_WIDTH, SCREEN_HEIGHT]

class PgMap:

    def __init__(self, screen, 
            range_size) -> None:
        self.screen = screen
        self.name = ""
        self.back = None
        self.entity_arr = []
        self.range_size = range_size
        PgEntity.set_size_map(self.range_size)

    def new_back(self):
        self.back = PgBack()
        return self.back
    
    def new_entity(self, key:str):
        entity = PgMovile(key)
        self.entity_arr.append(entity)
        return entity
    
    def load(self):
        self.back.load(self.screen)
        for i in range(len(self.entity_arr)):
            self.entity_arr[i].load(self.screen)
    
    def main_loop(self, pg_map):
        def wrapper(function):
            pg_map.load()
            pygame.display.flip()
            def loop():
                pg_map.back\
                    .repaint(pg_map.screen)
                function()
                pygame.display.flip()
                # Posibles entradas del teclado 
                # y mouse
                for event in pygame.event\
                    .get():
                    if event.type == pygame.QUIT:
                        sys.exit()
            Btpy.repeat(10, 1, loop)
        return wrapper



def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT)
    )
    pygame.display.set_caption("tutorial pygame parte 2")

    pgmap = PgMap(screen, [1200, 700])
    pj = pgmap.new_entity("main")
    pj.set_image("star_icon.png")
    print(pj.write())
    pj.center()
    background = pgmap.new_back()
    background.set_image("star_and_galaxis.png")
    background.point = [0, 0]

    @pgmap.main_loop(pgmap)
    def start():
        pj.move(screen, [0, -5])
    """
    def main_loop():
        background.repaint(screen)
        pj.move(screen, [0, -5])
        print(pj.write())
        pygame.display.flip()
        # Posibles entradas del teclado 
        # y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    Basic.repeat(10, 1, main_loop)
    """

    """
    # el bucle principal del juego
    while True:
        pj.move(screen, [0, -1])
        pygame.display.flip()
        # Posibles entradas del teclado 
        # y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    """

main()