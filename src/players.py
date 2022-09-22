"""A module that contains the player class information.

Classes for each player type are defined with attributes
for their name and the letter they are assigned to play
with (either X or O). Methods are defined allowing players
to select where on the board they should place their letter.
Relevent classes for user input errors are also defined.

Classes:
    RangeError(Exception)- An error raised when an integer is outside of the valid range.
    OccupiedException(Exception)-Error raised when a position is already occupied on the board.
    Player
    UserPlayer(Player)- represent the user/human player.
    EasyComputerPlayer(Player)- represents the easy computer player.
    ExpertComputerPlayer(Player)- represents an unbeatable computer player.
"""
from random import choice

class RangeError(Exception):
    """An error raised when an integer is outside of the valid range."""
    def __init__(self, val):
        super().__init__(
            f"{val} is not a valid position on the board. The number must be between 0 and 8.")


class OccupiedError(Exception):
    """An error raised when a player enters a number that is already occupied on the board."""
    def __init__(self, val):
        super().__init__(
            f"Position {val} is already occupied on the board. Please try again.")


class Player:
    """A parent class used to represent a player.

    Attributes:
        letter (str): the letter/marker the player will be assigned on the board.
        name (str): the player's name.
    """
    def __init__(self, letter, name):
        """Inits Player class with letter and name attributes."""
        self.letter = letter
        self.name = name


class UserPlayer(Player):
    """A class used to represent the user/human player."""
    # def __init__(self, letter, name):
    #     super().__init__(letter, name)

    def get_move(self, game):
        """The player inputs a position to place their letter which is returned by the method.

        Args:
            game: an instance of the TicTacToe class.

        Raises:
            RangeError: if the user selects a position outside the range of 0-8.
            OccupiedError: if the user selects a position that is already occupied.

        Returns:
            int: the position (between 0-8) the player has chosen to move to.
        """
        while True:
            try:
                val = int(
                    input("Based on the board shown above,"
                          " enter an integer (0-8) to indicate where you would like to go: "))
                if val not in range(0, 9):
                    raise RangeError(val)
                if val not in game.free_positions():
                    raise OccupiedError(val)
                return val
            except RangeError as err:
                print(err)
            except OccupiedError as err:
                print(err)
            except ValueError:
                print("That isn't a valid integer. Please enter a number with no decimal places.")


class EasyComputerPlayer(Player):
    """A class used to represent the easy computer player."""

    def get_move(self, game):
        """Randomly returns a free position on the board to position the player's letter.

        Args:
            game: an instance of the TicTacToe class.

        Returns:
            int: the position (between 0-8) the computer will place their marker.
       """
        position = choice(game.free_positions())
        return position


class ExpertComputerPlayer(Player):
    """A class used to represent an Expert Computer Player."""
    # def __init__(self, letter, name):
    #     super().__init__(letter, name)

    def get_move(self, game):
        """Returns the most optimal position on the board to position the player's letter.

        If all of the positions on the board are free it will return a random corner position.
        Otherwise it invokes a recursive minimax function to return the optimal position
        based which position has the highest utility score.

        Args:
            game: an instance of the TicTacToe class.

        Returns:
            int: the position (between 0-8) which is either a randomly selected corner
            or the position with the highest utility score.
        """
        if len(game.free_positions()) == 9:
            return choice([0, 2, 6, 8])
        return self.minimax(game, True)["position"]

    def minimax(self, state, is_maximising):
        """A recursive minimax method used to return a utility score for each possible position.

        The minimax method will continue until one of the following terminal conditions are met:
            1. The maximising player wins
                Returns:
                    dict: showing the position previously determined through recursion
                          and a score of 1 * (the number of empty squares remaining + 1)
            2. The minimising player wins
                Returns:
                    dict: showing the position previously determined through recursion
                          and a score of -1 * (the number of empty squares remaining + 1)
            3. There are no positions left on the board.
                Returns:
                    dict: showing the position previously determined through recursion
                          and a score of 0
        Assumes that the minimising player is also playing optimally.

        Args:
            state: an instance of the TicTacToe class
                shows the current board state in that simulation.
            is_maximising (bool): indicates if it is the maximiser's turn in the simulation.
               when it is the maximiser's turn they are playing to get the highest utility score.
               when it is the minimiser's turn they are playing to get the lowest utility score.

        Returns:
            dict: showing the position (with an int value between 0-8)
                and score (an int value)
        """
        maximising_letter = self.letter
        minimising_letter = "X"
        # Terminal states
        if state.current_winner:
            return {
                "position": None,
                "score": 1 * (state.num_empty_squares() + 1)
                if state.current_winner == maximising_letter
                else -1 * (state.num_empty_squares() + 1)
            }
        if not state.free_positions():
            return {"position": None, "score": 0}

        # When it is the maximisor's turn they are playing to get the highest utility score.
        if is_maximising:
            best_move = {"position": None, "score": -500}
            for possible_move in (state.free_positions()): # Loop through all free moves remaining.
                state.make_move(possible_move, maximising_letter)
                sim_score = self.minimax(state, False) # Method calls itself to test that move.
                # The board is then returned to it's original position as this is only a simulation.
                state.board[possible_move] = " "
                state.current_winner = None
                sim_score["position"] = possible_move
                if sim_score["score"] > best_move["score"]:
                    best_move = sim_score
            return best_move
        # When it is the minimisor's turn in the simulation the following code will be executed:
        # The best move for the maximisor is the lowest utility score.
        best_move = {"position": None, "score": 500}
        for possible_move in state.free_positions():  
            state.make_move(possible_move, minimising_letter)
            sim_score = self.minimax(state, True)
            state.board[possible_move] = " "
            state.current_winner = None  
            sim_score["position"] = possible_move
            if sim_score["score"] < best_move["score"]:
                best_move = sim_score
        return best_move
