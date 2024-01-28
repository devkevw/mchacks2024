from typing import Any
import pygame
import math
import sys
from tile import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
game_active = True
NUM_TILES = 36
OPERATORS = ['+', '-', 'x', '/']
level = 1;
rolldie = False

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
        tiles_in_row = math.sqrt(NUM_TILES) # 6
        size = int(SCREEN_HEIGHT/tiles_in_row)
        super().__init__()
        og_image = pygame.image.load('images/tile.png').convert_alpha()
        self.image = pygame.transform.scale(og_image, (size, size))

        # tile position
        if (num < 7) or (num > 12 and num < 19) or (num > 24 and num < 31): 
            x_pos = ((num % tiles_in_row) - 1) * size + 2
            if x_pos < 0: x_pos = size * (tiles_in_row - 1) + 2
        else: 
            x_pos = (6 - (num % tiles_in_row)) * size + 2
            if x_pos == 6 * size + 2: x_pos = 2

        y_pos = (7 - math.ceil(num/tiles_in_row)) * size + 2
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
        if self.operator == '+': 
            op_image = pygame.image.load('images/ops/add.png').convert_alpha()
        elif self.operator == '-': 
            op_image = pygame.image.load('images/ops/minus.png').convert_alpha()
        elif self.operator == 'x':
            op_image = pygame.image.load('images/ops/times.png').convert_alpha()
        elif self.operator == '/': 
            op_image = pygame.image.load('images/ops/divide.png').convert_alpha()

        if op_image != None: 
            image = pygame.transform.scale(op_image, (16, 16))
            image_rect = image.get_rect()
            image_rect.bottomright = (self.rect.right - 15, self.rect.bottom - 15)

            screen.blit(image, image_rect)
        


class sideDisplay(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()

    def draw_text(self):
        # draw the number
        font = pygame.font.Font(None, 28)
        text_surface = font.render('Turn', True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit(text_surface, text_rect)

        


# GROUPS and FUNCTIONS
        
side_display = pygame.sprite.GroupSingle()
side_display.add(sideDisplay())
       
all_tiles = pygame.sprite.Group()
# generate tiles
def generate_Tiles(level): 
    for i in range (1, 37):
        # levels
        if (level == 1):
            op = OPERATORS[random.randint(0, 1)]
        elif (level == 2): 
            op = OPERATORS[random.randint(0, 2)]
        else: # level 3
            op = OPERATORS[random.randint(0, 3)]

        # tiles
        if i == 1: 
            tile = Tile(i, None, False, False, False, False)
        else: 
            if (i == 2):
                tile = (Tile(i, op, False, True, False, False))
                
            elif (i == 5):
                tile = (Tile(i, op, False, True, False, False))
                 
            elif (i == 6):
                tile = (Tile(i, op, False, False, True, False))  
                
            elif (i == 11):
                tile = (Tile(i, op, False, False, True, False))
                 
            elif (i == 12):
                tile = (Tile(i, op, False, True, False, False))
                 
            elif (i == 14):
                tile = (Tile(i, op, False, False, False, True))
                
            elif (i == 15):
                tile = (Tile(i, op, False, False, True, False))

            elif (i == 16):
                tile = (Tile(i, op, True, False, False, False))
                 
            elif (i == 18):
                tile = (Tile(i, op, False, False, False, True))
                
            elif (i == 20):
                tile = (Tile(i, op, True, True, False, False))
                
            elif (i == 21):
                tile = (Tile(i, op, False, False, True, False))
                
            elif (i == 22):
                tile = (Tile(i, op, False, True, False, True))
                
            elif (i == 23):
                tile = (Tile(i, op, False, False, True, False))
                
            elif (i == 25):
                tile = (Tile(i, op, True, False, False, False))
                
            elif (i == 28):
                tile = (Tile(i, op, False, False, False, True))
                
            elif (i == 31):
                tile = (Tile(i, op, True, False, False, False))
                
            elif (i == 34):
                tile = (Tile(i, op, True, False, False, False))
                
            elif (i == 35):
                tile = (Tile(i, op, False, False, False, True))
                
            else: 
                tile = (Tile(i, op, False, False, False, False))
                   
        all_tiles.add(tile)

generate_Tiles(level)

def draw_ladders(all_tiles): 
     tiles_list = [
         [6, 18],
         [11, 14],
         [15, 22],
         [21, 28],
         [23, 35]
     ]

     for tiles in tiles_list: 
        tile1 = all_tiles.sprites()[tiles[0]-1]
        tile2 = all_tiles.sprites()[tiles[1]-1]
        pygame.draw.line(screen, (139, 69, 19), tile1.rect.center, tile2.rect.center, 5)
    
def draw_snakes(all_tiles): 
    tiles_list = [
         [2, 16],
         [5, 20],
         [20, 31],
         [22, 34],
         [12, 25]
    ]

    dot_size = 3
    dot_spacing = 10

    for tiles in tiles_list:
        tile1 = all_tiles.sprites()[tiles[0] - 1]
        tile2 = all_tiles.sprites()[tiles[1] - 1]

        # Calculate the direction vector and normalized distance
        direction = pygame.math.Vector2(tile2.rect.center[0] - tile1.rect.center[0],
                                         tile2.rect.center[1] - tile1.rect.center[1])
        normalized_direction = direction.normalize()

        # Draw dotted line
        dot_position = pygame.math.Vector2(tile1.rect.center)
        while dot_position.distance_to(tile2.rect.center) >= dot_spacing:
            pygame.draw.circle(screen, (34, 139, 34), (int(dot_position.x), int(dot_position.y)), dot_size)
            dot_position += normalized_direction * dot_spacing
    


    
# display game itself
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    
    if game_active:
        # all_tiles.update()
        screen.fill((255,255,255))
        # all_tiles.draw(screen)
        all_tiles.draw(screen)
        for tile in all_tiles.sprites():
            tile.draw_num()

        side_display.sprites()[0].draw_text()

        # draw ladders and snakes
        draw_ladders(all_tiles)
        draw_snakes(all_tiles)
            


    else: None


    pygame.display.update()
    clock.tick(60)
                        

    





