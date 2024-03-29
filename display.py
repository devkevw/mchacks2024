import pygame
import math
import sys
import random


# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
NUM_TILES = 36
OPERATORS = ['+', '-', 'x', '/']
game_active = True
level = 3


# initialize screen
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Learn & Climb: Snake Scholars')
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

        # attributes
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

    def draw_circles(self, colors):
        # draw circles in the middle of the tile
        circle_radius = 15
        circle_colors = colors

        center_x = self.rect.centerx
        center_y = self.rect.centery

        for i, color in enumerate(circle_colors):
            # calculate the position for each circle
            angle = i * (2 * math.pi / len(circle_colors))
            circle_x = center_x + int(circle_radius * math.cos(angle))
            circle_y = center_y + int(circle_radius * math.sin(angle))

            pygame.draw.circle(screen, color, (circle_x, circle_y), circle_radius)

        
class Player:
    def __init__(self, occupied_tile, color):
        """
        Initializes a Player object

        """
        self.occupied_tile = occupied_tile
        self.is_turn = False
        self.color = color

    def move_to(self, tile):
        self.occupied_tile = tile


class SideDisplay(pygame.sprite.Sprite):
    def __init__(self, player):
        """
        Initializes a SideDisplay object

        """
        super().__init__()
        self.player = player

    def draw_text(self, die_num): 
        x_pos = 6 * 116 + 2 + ((SCREEN_WIDTH - 6 * 116 + 2) // 2)

        # turn
        font = pygame.font.Font(None, 50)
        text_surface = font.render("Player's Turn:", True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x_pos, SCREEN_HEIGHT // 4)
        screen.blit(text_surface, text_rect)

        # player
        pygame.draw.circle(screen, self.player.color, (x_pos, SCREEN_HEIGHT / 2.8), 24)

        # roll die
        die_surface = font.render("Roll Die", True, (0, 0, 0))
        die_rect = die_surface.get_rect()
        die_rect.center = (x_pos, SCREEN_HEIGHT // 1.8)

        # rectangle for die button
        pygame.draw.rect(screen, (192, 192, 192), die_rect.inflate(20, 10))
        screen.blit(die_surface, die_rect)

        if die_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (192, 192, 192), die_rect.inflate(20, 10), 2)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.draw.rect(screen, (192, 192, 192), die_rect.inflate(20, 10), 2)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # die number
        num_surface = font.render(str(die_num), True, (0, 0, 0))
        num_rect = num_surface.get_rect()
        num_rect.center = (x_pos, SCREEN_HEIGHT // 1.5)
        screen.blit(num_surface, num_rect)
            

# groups and functions
player1 = Player(None, 'Red')
side_display = pygame.sprite.GroupSingle()
side_display.add(SideDisplay(player1))
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
        elif i == 2:
            tile = (Tile(i, op, False, True, False, False))
        elif i == 5:
            tile = (Tile(i, op, False, True, False, False))
        elif i == 6:
            tile = (Tile(i, op, False, False, True, False))  
        elif i == 11:
            tile = (Tile(i, op, False, False, True, False))     
        elif i == 12:
            tile = (Tile(i, op, False, True, False, False))     
        elif i == 14:
            tile = (Tile(i, op, False, False, False, True)) 
        elif i == 15:
            tile = (Tile(i, op, False, False, True, False))
        elif i == 16:
            tile = (Tile(i, op, True, False, False, False))      
        elif i == 18:
            tile = (Tile(i, op, False, False, False, True))
        elif i == 20:
            tile = (Tile(i, op, True, True, False, False))
        elif i == 21:
            tile = (Tile(i, op, False, False, True, False)) 
        elif i == 22:
            tile = (Tile(i, op, False, True, False, True))
        elif i == 23:
            tile = (Tile(i, op, False, False, True, False)) 
        elif i == 25:
            tile = (Tile(i, op, True, False, False, False))
        elif i == 28:
            tile = (Tile(i, op, False, False, False, True))  
        elif i == 31:
            tile = (Tile(i, op, True, False, False, False))
        elif i == 34:
            tile = (Tile(i, op, True, False, False, False))  
        elif i == 35:
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

        # calculate the direction vector and normalized distance
        direction = pygame.math.Vector2(tile2.rect.center[0] - tile1.rect.center[0],
                                         tile2.rect.center[1] - tile1.rect.center[1])
        normalized_direction = direction.normalize()

        # draw dotted line
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
        screen.fill((255,255,255))

        # draw board
        all_tiles.draw(screen)

        for tile in all_tiles.sprites():
            tile.draw_num()
            if tile.num == 1:
                tile.draw_circles([(0, 255, 0), (0, 0, 255), (255, 255, 0)])
            elif tile.num == 5: 
                tile.draw_circles([(255, 0, 0)])

        side_display.sprites()[0].draw_text(5)

        draw_ladders(all_tiles)
        draw_snakes(all_tiles)
            
    else: None # to fill with menu screen, or end game screen

    pygame.display.update()
    clock.tick(60)
                        
