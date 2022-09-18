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

    def get_move(self, game):    
        while True:  
            try:
                val = int(input("Based on the board shown above, enter an integer (0-8) to indicate where you would like to place a cross: "))
                if not val in range(0, 9): # While this error would be picked up by the next raised error it is helpful for users to know why their number isn't valid.  
                    raise RangeError(val)
                elif val not in game.free_positions():
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
        position = choice(game.free_positions()) #Will select a random square on the board from those that are free. 
        return position

# Add another computer player medium difficulty with less logic. 
# Add an extreme computer player with difficult minimax logic. 
# Utility function = (the remaining squares on the board + 1) * by either + 1 or -1 depending on if you won. If the tree ends in a draw there is a zero.   The more empty squares the more ideal the position. 

    # place a marker on the board in every possible position. 
class ExpertComputerPlayer(Player):
    def __init__(self, letter, name):
        super().__init__(letter, name)
       
    def get_move(self, game):
        if len(game.free_positions()) == 9:
            square = choice(0, 2, 6, 8) # If O is going first it will select one of the courners
        else:
            # get the square based off the minimax algorithm called in the function below.
            square = self.minimax(game, self.letter)['position']
        return square
    # Utility function = (the remaining squares on the board + 1) * by either + 1 or -1 depending on if you won. If the tree ends in a draw there is a zero.   The more empty squares the more ideal the position. 

    # place a marker on the board in every possible position. 
    def minimax(self, state, current_player_letter): # Three parameters: self(the Hardcomputerplayer), state is the current state of the board in the simulation and current_player is the player who's turn it currently is. 
        maximiser = self.letter # The ExpectComputerPlay is always wanting to achieve the highest possible utility value. 
        waiting_player_letter = "O" if current_player_letter == "X" else "X" 
        # first we want to check if the previous move is a winner
        # this is our base case
        if state.current_winner == waiting_player_letter:
            #we return position and score to keep track of the score
            # for minimax to work
            return {"position": None,
                    "score": 1 * (state.num_empty_squares() + 1) if waiting_player_letter == maximiser else -1 *(
                        state.num_empty_squares() + 1)
                    }
        elif not state.empty_squares(): 
            return {"position": None, "score": 0}

        # initialise some dictionaries
        if current_player_letter == maximiser: 
            best = {"position": None, "score": -math.inf}   # The maximiser will beat this super low score each time until the highest utility score is achieved. As the maximiser we want the highest utility score possible. 
        else:
            best = {"position": None, "score": math.inf} # This will allow the mimimiser to try and minimise this value. (Becuase they want to win the minimisor will chose the value with the lowest utility score)  
        
        for possible_move in state.free_positions():  # loop through all the possible moves in the blank spaces that are free
            state.make_move(possible_move, current_player_letter) #make a move and see what score it is.  
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, waiting_player_letter)  # This calls the minimax function on each of the positions. 
            
            # step 3: Undo the move
            state.board[possible_move] = ' ' #Return the position to be empty as we are just testing it. 
            state.current_winner = None  # Return the current winner back to none in case there was one. 
            sim_score['position'] = possible_move

            # step 4: updates the dictionaries if necessary
            if current_player_letter == maximiser:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best