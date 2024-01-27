import pygame
import sys

pygame.init()

game_active = True

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

test_rect = test_surface.get_rect(bottomright = (600, 300))


# img = pygame.image.load('images/img-name').convert_alpha() # import image as a surface
# .convert_alpha() makes the image a format easier to work with for pygame, .convert() works fine too
# text
test_font = pygame.font.Font(None, 50) # for font
# can import a custom font from a folder (None just uses default font from pygame)
score_surface = test_font.render("Some text", False, 'Green')
score_rect = score_surface.get_rect(center = (400, 50))


# rectangles
box = pygame.Surface((100, 100))
box.fill('Blue')

box_rect = box.get_rect(midbottom = (200, 200))


# keep displaying screen
while True:
    #close window
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

        # another way to get mouse position
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)

        # keyboard input
        if event.type == pygame.KEYDOWN: # or KEYUP for button released
            if event.key == pygame.K_SPACE:
                print ('jump')


    if game_active:
        # move elements
        # test_x_pos -= 4
        # text_x_pos += 4

        # if test_x_pos < - 100: test_x_pos = 800
        # if text_x_pos > 800: text_x_pos = -100

        box_rect.left += 1 # don't move the surface
                        # move the rectangle that contains the surface
        test_rect.x -=4
        if test_rect.right <=0: test_rect.left = 800
        # print(box_rect.left)

        screen.fill((255, 255, 255)) # clear screen with refilling background

        # draw all elements
        screen.blit(test_surface, test_rect)
        # pygame.draw.rect(screen, 'Pink', score_rect) # draw rectangle
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 20) # draw rectangle
        pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos(), 10) # draw line
        screen.blit(score_surface, score_rect)
        screen.blit(box, box_rect)
                
        # check for collision - using rectangles
        test_rect.colliderect(box_rect) # boolean

        # check collision - point
        mouse_pos = pygame.mouse.get_pos()
        if test_rect.collidepoint(mouse_pos):
            print('collision')
            print(pygame.mouse.get_pressed()) # returns tuple of which mouse button
                                            # is being pressed


        # keyboard input 
        keys = pygame.key.get_pressed()
        keys[pygame.K_SPACE] # get space button (see if pressed), returns boolean

    else: # game ends or start screen
        None

    # update everything
    pygame.display.update()
    clock.tick(60) # max frame rate