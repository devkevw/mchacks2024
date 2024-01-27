import pygame
import sys

pygame.init()

# display screen
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner") # title of screen

# clock
clock = pygame.time.Clock()

# surfaces
test_surface = pygame.Surface((100, 200)) # red box
test_surface.fill('Red')

test_x_pos = 600


# img = pygame.image.load('images/img-name').convert_alpha() # import image as a surface
# .convert_alpha() makes the image a format easier to work with for pygame, .convert() works fine too
# text
test_font = pygame.font.Font(None, 50) # for font
# can import a custom font from a folder (None just uses default font from pygame)
text_surface = test_font.render("Some text", False, 'Green')

text_x_pos = 300

# rectangles


# keep displaying screen
while True:
    #close window
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

    # move elements
    test_x_pos -= 4
    text_x_pos += 4

    if test_x_pos < - 100: test_x_pos = 800
    if text_x_pos > 800: text_x_pos = -100

    screen.fill((255, 255, 255)) # clear screen with refilling background

    # draw all elements
    screen.blit(test_surface, (test_x_pos, 100))
    screen.blit(text_surface, (text_x_pos, 50))
            
    


    # update everything
    pygame.display.update()
    clock.tick(60) # max frame rate