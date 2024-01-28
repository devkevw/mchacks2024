import pygame
import math
import sys
from game import *


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
black = (0, 0, 0)
green = (0, 255, 0)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snakes and Ladders')
clock = pygame.time.Clock()
game_active = True

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale) ))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        mouse_position = pygame.mouse.get_pos()

        #check collision
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

#just a cheeky button creation
start_img = pygame.image.load('images/start_btn.png').convert_alpha()
exit_img = pygame.image.load('images/exit_btn.png').convert_alpha()

start_button = Button(400, 400, start_img, 1)
exit_button = Button(800, 400, exit_img, 1)

#font stuff
font = pygame.font.Font('fonts/Sixtyfour-Regular.ttf', 64)
subtitle_font = pygame.font.Font('fonts/Sixtyfour-Regular.ttf', 48)

title_text = font.render('Learn & Climb', True, black, green)
subtitle_text = subtitle_font.render('Snake Scholars', True, black)

text_rect = title_text.get_rect()
subtitle_text_rect = subtitle_text.get_rect()

text_rect.center = (600, 100)
subtitle_text_rect.center = (600, 175)

# display game itself
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
                print("Pause")
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_active:

        screen.fill((255, 255, 255))
        screen.blit(title_text, text_rect)
        screen.blit(subtitle_text, subtitle_text_rect)


        if start_button.draw():
            print("Start")

        if exit_button.draw():
            pygame.quit()
            sys.exit()
            print("Exit")

    else:
        None

    pygame.display.update()
    clock.tick(60)
