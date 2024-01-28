import functions
import tile 


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

            if ((current_position + dice_roll) > 36):
                print("You went over the limit! Remain at your Tile")
                continue

            operator = game.tiles[current_position + dice_roll - 1].operator
            num1 = functions.generate_rand_number(1, 10)
            num2 = functions.generate_rand_number(1, 10)
            question_str = "Solve the following: " + str(num1) + " " + operator + " " + str(num2)
            print(question_str)
            ans = int(input("Your Answer: "))
            correct_answer = functions.check_answer(num1, num2, operator, ans)

            if (correct_answer == True): 
                print("Correct Answer!")
                new_tile = game.tiles[current_position + dice_roll - 1]

                if (new_tile.is_ladderbottom == True):

                    for ladder in game.ladders:
                        if ladder.bottom_tile == new_tile:
                            print("Congrats! You're moving up the ladder.")
                            player.move_to(ladder.top_tile)
                            print("Succesfully moved to tile " + str(player.occupied_tile.num))

                elif (new_tile.is_snakehead == True):
                    print("Good job! You escaped the snake.")
                    print("Returning to tile " + str(current_position))

                else: 
                    player.move_to(game.tiles[current_position + dice_roll - 1])
                    print("Succesfully moved to tile " + str(player.occupied_tile.num))

            else:
                new_tile = game.tiles[current_position + dice_roll - 1]

                if (new_tile.is_snakehead == True):

                    for snake in game.snakes:
                        if snake.head_tile == new_tile:
                            print("Uh oh! You're sliding down the snake...")
                            player.move_to(snake.tail_tile)
                            print("You are now at tile " + str(player.occupied_tile.num))
                
                else: 
                    print("Incorrect Answer. You will remain at the same tile.")
            
for player in game.players: 
    if (player.occupied_tile.num == 36):
        print(player.name + " wins! Congratulations!") 


     
            


