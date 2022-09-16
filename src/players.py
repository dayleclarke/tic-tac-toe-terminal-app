#Tic Tac Toe Game
# Imported Modules
import math
from random import choice

# Classes
class RangeError(Exception):
    def __init__(self, val):
        super().__init__(f"{val} does not represent a valid position on the board. The number you enter must be between 0 and 8 inclusive.")

class OccupiedError(Exception):
    def __init__(self, val):
        super().__init__(f"Sorry. Position {val} is already occupied on the board. Please select a position (between 0 and 8) not already taken.")


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

    def get_move(self):    
        while True:  
            try:
                val = int(input("Enter an integer (0-8) to indicate where you would like to place a cross: "))
                if not val in range(0, 9): # While this error would be picked up by the next raised error it is helpful for users to know why their number isn't valid.  
                    raise RangeError(val)
                elif val not in (3, 4, 5, 7):  #game.free_spots():
                    raise OccupiedError(val)
                return val           
            except RangeError as err:
                print(err)
            except OccupiedError as err:
                print(err)
            except ValueError:
                print("That isn't a valid integer.  Please enter a number between 0 and 8 (inclusive) with no decimal places.")

class EasyComputerPlayer(Player):
    def __init__(self, letter, name):
        super().__init__(letter, name)

    def get_move(self, game): 
        square = choice(game.free_spots()) #Will select a random square on the board from those that are free. 
        return square

# Add another computer player medium difficulty with less logic. 
# Add an extreme computer player with difficult minimax logic. 
class GeniusComputerPlayer(Player):
    def __init__(self, letter, name):
        super().__init__(letter, name)
    
    def get_move(self, game):
        pass

