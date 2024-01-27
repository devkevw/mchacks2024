from typing import Any
import pygame
import math
import sys
from tile import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
game_active = True
NUM_TILES = 36

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snakes and Ladders')
clock = pygame.time.Clock()


# classes
class Tile(pygame.sprite.Sprite): 
    def __init__(self, num, operator, is_snakehead, is_snaketail, is_ladderbottom, is_laddertop):
        """
        Initializes a Tile object 

        """
        num_tiles_in_row = math.sqrt(NUM_TILES)
        size = int(SCREEN_HEIGHT/num_tiles_in_row)
        super().__init__()
        og_image = pygame.image.load('images/tile.png')
        self.image = pygame.transform.scale(og_image, (size, size))

        x_pos = ((num % num_tiles_in_row) - 1) * size + 2
        if x_pos < 0: x_pos = size * (num_tiles_in_row - 1) + 2
        y_pos = (7 - math.ceil(num/num_tiles_in_row)) * size + 2
        self.rect = self.image.get_rect(bottomleft = (x_pos, y_pos))

        self.num = num
        self.operator = operator
        self.is_snakehead = is_snakehead
        self.is_snaketail = is_snaketail
        self.is_laddertop = is_laddertop
        self.is_ladderbottom = is_ladderbottom
         

    


# GROUPS
# tile1 = Tile(1, None, False, False, False, False)
# tile = pygame.sprite.GroupSingle()
# tile.add(tile1)
        
all_tiles = pygame.sprite.Group()
for i in range(1, NUM_TILES + 1):
     tile = Tile(i, None, False, False, False, False)
     all_tiles.add(tile)
        


# display game itself
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    
    if game_active:
         screen.fill((255,255,255))
         all_tiles.draw(screen)
    else: None

    

    pygame.display.update()
    clock.tick(60)
                        

    





