#Tic Tac Toe Game
# Imported Modules
import math
from random import choice

# Classes
class RangeError(Exception):
    def __init__(self, val):
        super().__init__(f"{val} is not a valid position on the board- The number must be between 0 and 8 and not already taken.")

class Player: # Parent Class used for all players (human and computers)
    def __init__(self, letter, name):  #letter is either X or O  # If time could make this emoji's or a symbol chosen by the player. 
        self.letter = letter
        self.name = name

        # Add features in here to allow players to access their score history from an extra file. 
        # Could have a % of games either won or tied or losses accessed via a txt file. 

class UserPlayer(Player): # If time add a second player so two people could play against each other IRL
    #Can also get them to log in and have a name that you call them. Should this class be assigned a name we can change when the user enters their name? 
    def __init__(self, letter, name):
        super().__init__(letter, name)

    def get_move(self, game):    
        while True:  
            try:
                val = int(input("Enter an integer (0-8) to indicate where you would like to place a cross: "))
                if val not in game.free_spots():
                    raise RangeError(val)
                return val
        # if not user_move in range(0, 9):
        #     raise RangeError(user_move)
        # elif user_move not in game.free_spots():           
            except RangeError as err:
                print(err)
            except ValueError:
                print("That isn't a valid integer.  Please enter a number between 0 and 8.")

if __name__ == '__main__':
    print("Welcome to TicTacToe!")
    player_name = (input("What is your name?: "))
    print("Hello " + player_name.title() + "! So lovely to meet you.\n")
    # returns the winner of the game if there is one. 
    x_player = UserPlayer('X', player_name)
    
    # o_player = GeniusComputerPlayer('O')
    # t = TicTacToe()
    # play(t, x_player, o_player, print_game=True) 