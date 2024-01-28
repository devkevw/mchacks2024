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

# game variables
game_paused = False

# classes
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale) ))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

#just a cheeky button creation
start_img = pygame.image.load('images/start_btn.png').convert_alpha()
exit_img = pygame.image.load('images/exit_btn.png').convert_alpha()



class Tile(pygame.sprite.Sprite): 
    def __init__(self, num, operator, is_snakehead, is_snaketail, is_ladderbottom, is_laddertop):
        """
        Initializes a Tile object 

        """
        num_tiles_in_row = math.sqrt(NUM_TILES) # 6
        size = int(SCREEN_HEIGHT/num_tiles_in_row)
        super().__init__()
        og_image = pygame.image.load('images/tile.png').convert_alpha()
        self.image = pygame.transform.scale(og_image, (size, size))

        # tile position
        if (num < 7) or (num > 12 and num < 19) or (num > 24 and num < 31): 
            x_pos = ((num % num_tiles_in_row) - 1) * size + 2
            if x_pos < 0: x_pos = size * (num_tiles_in_row - 1) + 2
        else: 
            x_pos = (6 - (num % num_tiles_in_row)) * size + 2
            if x_pos == 6 * size + 2: x_pos = 2

        y_pos = (7 - math.ceil(num/num_tiles_in_row)) * size + 2
        self.rect = self.image.get_rect(bottomleft = (x_pos, y_pos))

        self.num = num
        self.operator = operator
        self.is_snakehead = is_snakehead
        self.is_snaketail = is_snaketail
        self.is_laddertop = is_laddertop
        self.is_ladderbottom = is_ladderbottom

    def draw_num(self):
        # draw the number
        font = pygame.font.Font(None, 28)
        text_surface = font.render(str(self.num), True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.topright = (self.rect.right - 15, self.rect.top + 15)
        screen.blit(text_surface, text_rect)

        # draw the operator
        op_image = None;
        if self.operator == 'plus': 
            op_image = pygame.image.load('images/ops/add.png').convert_alpha()
        elif self.operator == 'minus': 
            op_image = pygame.image.load('images/ops/minus.png').convert_alpha()
        elif self.operator == 'times':
            op_image = pygame.image.load('images/ops/times.png').convert_alpha()
        elif self.operator == 'divide': 
            op_image = pygame.image.load('images/ops/divide.png').convert_alpha()

        if op_image != None: 
            image = pygame.transform.scale(op_image, (16, 16))
            image_rect = image.get_rect()
            image_rect.bottomright = (self.rect.right - 15, self.rect.bottom - 15)

            screen.blit(image, image_rect)
        



# GROUPS
# tile1 = Tile(1, 'plus', False, False, False, False)
# tile = pygame.sprite.GroupSingle()
# tile.add(tile1)
        
all_tiles = pygame.sprite.Group()
for i in range(1, NUM_TILES + 1):
     tile = Tile(i, 'divide', False, False, False, False)
     all_tiles.add(tile)
        
start_button = Button(800, 200, start_img, 1)
exit_button = Button(800, 400, exit_img, 1)



# display game itself
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
                print("Pause")
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    
    if game_active:
        # all_tiles.update()
        screen.fill((255,255,255))
        # all_tiles.draw(screen)
        start_button.draw()
        exit_button.draw()
        all_tiles.draw(screen)
        for tile in all_tiles.sprites():
            tile.draw_num()


    else: None

    

    pygame.display.update()
    clock.tick(60)
                        

    





