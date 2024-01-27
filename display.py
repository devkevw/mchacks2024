import pygame
import sys
from tile import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snakes and Ladders')
clock = pygame.time.Clock()
game_active = False


# display game itself
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    
    if game_active: None
    else: None

    

    pygame.display.update()
    clock.tick(60)
                        

    





