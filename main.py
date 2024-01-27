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



while (game.check_if_game_over() == False):
    game.pick_player_turn()
    for player in game.players:
        if (player.is_turn):
            print(player.name + ", it is your turn.")
            current_position = player.occupied_tile.num
            dice_roll = functions.generate_rand_number(1,6)
            print("You rolled a " + str(dice_roll))
            operator = game.tiles[current_position + dice_roll - 1].operator
            num1 = functions.generate_rand_number(1, 10)
            num2 = functions.generate_rand_number(1, 10)
            question_str = "Solve the following: " + str(num1) + " " + operator + " " + str(num2)
            print(question_str)
            ans = int(input("Your Answer: "))
            correct_answer = functions.check_answer(num1, num2, operator, ans)
            if (correct_answer == True): 
                new_tile = game.tiles[current_position + dice_roll - 1]
                player.move_to(game.tiles[current_position + dice_roll - 1])
                print("Succesfully moved to tile " + str(player.occupied_tile.num))
            else:
                print("Incorrect Answer")
            
        
            
            
            
            


