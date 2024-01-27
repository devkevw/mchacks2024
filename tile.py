import pygame
import math
import random 



class Tile: 
    def __init__(self, num, operator, is_snakehead, is_snaketail, is_ladderbottom, is_laddertop):
        """
        Initializes a Tile object 

        """
        self.num = num
        self.operator = operator
        self.is_snakehead = is_snakehead
        self.is_snaketail = is_snaketail
        self.is_laddertop = is_laddertop
        self.is_ladderbottom = is_ladderbottom
        
OPERATORS_G1 = ["+", "-"]
OPERATORS_G2 = ["+", "-", "x"] 
OPERATORS_G3 = ["+", "-", "x", "/"] 
 

class Player: 
    def __init__(self, occupied_tile, name):
        """
        Initializes a Player object 

        """

        self.occupied_tile = occupied_tile
        is_turn = False
        self.name = name

    def move_to(self,tile):
        self.occupied_tile = tile

class Snake: 
    def __init__(self, head_tile, tail_tile):
        """
        Initializes a Snake object 

        """

        self.head = head_tile
        self.tail_tile = tail_tile


class Ladder: 
    def __init__(self, top_tile, bottom_tile):
        """
        Initializes a Ladder object 

        """

        self.top_tile = top_tile
        self.bottom_tile = bottom_tile 

class Game: 
    def __init__(self, num_players, level):
        """

        Initializes a Game object 

        """
        self.num_players = num_players 
        self.level = level
        self.players = []
        self.tiles = []
        self.snakes = []
        self.ladders = []

        
    def add_players(self):

        i = 0
        player_number = 1
        while (i < self.num_players):
            name_str = "Player " + str(player_number)
            new_player = Player(Tile(1,None, False, False, False, False), name_str)
            self.players.append(new_player)
            i += 1
            player_number += 1

    def pick_player_turn(self):
        
        num_turn = -1
        i = 0
        while (i < self.num_players):
            if (self.players[i].is_turn == True): 
                num_turn = i

        if (num_turn == -1):
            self.players[0].is_turn = True
        
        elif (num_turn == (self.num_players - 1)):
            self.players[num_turn].is_turn = False
            self.players[0].is_turn = True
        else:
            self.players[num_turn].is_turn = False 
            self.players[num_turn + 1] = True 

    
    def create_board(self):
        self.tiles.append(Tile(1,None, False, False, False, False))
        i = 1
        num_tile = 2
        
        while (i <= 36):
            if (self.level == 1):
                op = OPERATORS_G1[random.randint(0, 1)]
            elif (self.level == 2): 
                op = OPERATORS_G2[random.randint(0, 2)]
            elif (self.level == 3): 
                op = OPERATORS_G3[random.randint(0, 3)]

            if (i == 2):
                self.tiles.append(Tile(num_tile, op, False, True, False, False))
                num_tile += 1 
                
            elif (i == 5):
                self.tiles.append(Tile(num_tile, op, False, True, False, False))
                num_tile += 1 

            elif (i == 6):
                self.tiles.append(Tile(num_tile, op, False, False, True, False))
                num_tile += 1 
                
            elif (i == 11):
                self.tiles.append(Tile(num_tile, op, False, False, True, False))
                num_tile += 1 

            elif (i == 12):
                self.tiles.append(Tile(num_tile, op, False, True, False, False))
                num_tile += 1 
                
            elif (i == 14):
                self.tiles.append(Tile(num_tile, op, False, False, False, True))
                num_tile += 1

            elif (i == 15):
                self.tiles.append(Tile(num_tile, op, False, False, True, False))
                num_tile += 1 

            elif (i == 16):
                self.tiles.append(Tile(num_tile, op, True, False, False, False))
                num_tile += 1 
            
            elif (i == 18):
                self.tiles.append(Tile(num_tile, op, False, False, False, True))
                num_tile += 1
            
            elif (i == 20):
                self.tiles.append(Tile(num_tile, op, True, True, False, False))
                num_tile += 1
            
            elif (i == 21):
                self.tiles.append(Tile(num_tile, op, False, False, True, False))
                num_tile += 1
            
            elif (i == 22):
                self.tiles.append(Tile(num_tile, op, False, True, False, True))
                num_tile += 1
            
            elif (i == 23):
                self.tiles.append(Tile(num_tile, op, False, False, True, False))
                num_tile += 1
            
            elif (i == 25):
                self.tiles.append(Tile(num_tile, op, True, False, False, False))
                num_tile += 1
            
            elif (i == 28):
                self.tiles.append(Tile(num_tile, op, False, False, False, True))
                num_tile += 1

            elif (i == 31):
                self.tiles.append(Tile(num_tile, op, True, False, False, False))
                num_tile += 1
            
            elif (i == 34):
                self.tiles.append(Tile(num_tile, op, True, False, False, False))
                num_tile += 1
            
            elif (i == 35):
                self.tiles.append(Tile(num_tile, op, False, False, False, True))
                num_tile += 1

            else: 
                self.tiles.append(Tile(num_tile, op, False, False, False, False))
                num_tile += 1   

            i += 1

    def add_snakes(self):
        self.snakes.append(Snake(self.tiles[15], self.tiles[1]))
        self.snakes.append(Snake(self.tiles[19], self.tiles[4]))
        self.snakes.append(Snake(self.tiles[30], self.tiles[19]))
        self.snakes.append(Snake(self.tiles[33], self.tiles[21]))
    
    def add_ladders(self): 
        self.ladders.append(Ladder(self.tiles[17], self.tiles[5]))
        self.ladders.append(Ladder(self.tiles[13], self.tiles[10]))
        self.ladders.append(Ladder(self.tiles[21], self.tiles[14]))
        self.ladders.append(Ladder(self.tiles[27], self.tiles[20]))
        self.ladders.append(Ladder(self.tiles[34], self.tiles[22]))
    











        

    





    
