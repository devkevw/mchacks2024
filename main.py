import pygame 
import functions
import tile 
import math 
import random 

num_users = int(input("Please enter the number of players: "))
game_level = int(input("Please select a level of difficulty (1/2/3): "))

game = tile.Game(num_users, game_level)
game.add_players()
game.create_board()
game.add_ladders()
game.add_snakes()



