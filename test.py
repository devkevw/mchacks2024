import pygame
import sys
import random
import math
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 10, 10
TILE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snakes and Ladders")

# Player class
class Player:
    def __init__(self):
        self.position = 0

    def move(self, steps):
        self.position += steps
        if self.position in snakes:
            print("Oops! Snakes got you!")
            self.position = snakes[self.position]
        elif self.position in ladders:
            print("Yay! You found a ladder!")
            self.position = ladders[self.position]

        if self.position >= ROWS * COLS:
            print("Congratulations! You reached the end!")
            pygame.quit()
            sys.exit()

# Snakes and Ladders positions
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Initialize players
player1 = Player()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get a random dice roll between 1 and 6
    dice_roll = random.randint(1, 6)

    # Move the player
    player1.move(dice_roll)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the board
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, BLACK, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), 2)

    # Draw the player
    player_row = player1.position // COLS
    player_col = player1.position % COLS
    pygame.draw.circle(screen, RED, (player_col * TILE_SIZE + TILE_SIZE // 2, player_row * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 3)

    # Update the display
    pygame.display.flip()

    # Pause for a short duration to make the movement visible
    pygame.time.delay(500)

# This code will keep running until the user closes the window. The player moves on the board based on the dice roll, and if they encounter a snake or a ladder, the position is updated accordingly. The game will print messages in the console about whether a snake got the player or if they found a ladder. The game continues until the player reaches the last tile.
