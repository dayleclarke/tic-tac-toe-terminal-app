"""A module that contains player class information.

Classes for each player type are defined with attributes
for their name and the letter they are assigned to play
with (either X or O). Methods are defined allowing players
to select where on the board they should place their letter.
Relevent classes for user input errors are also defined.

Classes:
    RangeError(Exception)- An error raised when an integer is outside
        of the valid range.
    OccupiedException(Exception)-Error raised when a position is
        already occupied on the board.
    Player-A parent class used to represent a player.
    UserPlayer(Player)- represents a user/human player.
    EasyComputerPlayer(Player)- represents an easy computer player.
    ExpertComputerPlayer(Player)- represents an unbeatable computer player.
"""

from random import choice
import pandas as pd
from custom_exceptions import RangeError, OccupiedError


class Player:
    """A parent class used to represent a player.

    Attributes:
        letter (str): the letter/marker the player will be assigned on
            the board.
        name (str): the player's name.
    """
    def __init__(self, letter, name):
        """Inits Player class with letter and name attributes."""
        self.letter = letter
        self.name = name

    def update_scores(self, outcome):
        """Updates the player's win/tie/loss records.

        Increases either the player's total wins, ties or losses by 1
        in the player_scores.csv file, depending on the outcome of the
        game. Also increases the total games played by one and updates
        the percentage_loss_ratio.

        Args:
            outcome(str): the column title that needs to be updated
                to reflect the outcome of the game: either "wins",
                "ties", or "losses".

        Returns:
            dataframe: a dataframe showing the updated
                player_score.csv file.
        """
        df = pd.read_csv("player_scores.csv")
        df.loc[df["player_name"] == self.name, [outcome, "total_games"]] += 1
        df["percentage_loss_ratio"] = df["losses"] / df["total_games"]
        # pd.options.display.float_format = "{:.2%}".format
        df.to_csv("player_scores.csv", index=False)
        return df

    def __repr__(self):
        return f"An instance of the Player class with the name {self.name}."

    def __str__(self):
        return f"A player named: {self.name}."



class UserPlayer(Player):
    """A class used to represent the user/human player."""
    def __init__(self, letter, name, username):
        super().__init__(letter, name)
        self.username = username
    
    def update_scores(self, outcome):
        """Updates the player's win/tie/loss records.

        Increases either the player's total wins, ties or losses by 1
        in the player_scores.csv file, depending on the outcome of the
        game. Also increases the total games played by one and updates
        the percentage_loss_ratio.

        Args:
            outcome(str): the column title that needs to be updated
                to reflect the outcome of the game: either "wins",
                "ties", or "losses".

        Returns:
            dataframe: a dataframe showing the updated
                player_score.csv file.
        """
        df = pd.read_csv("player_scores.csv")
        df.loc[df["player_name"] == self.username, [outcome, "total_games"]] += 1
        df["percentage_loss_ratio"] = df["losses"] / df["total_games"]
        pd.options.display.float_format = "{:.2%}".format
        df.to_csv("player_scores.csv", index=False)
        df = df.sort_values(by=["wins", 'total_games'], ascending=False).head(11)
        df = df[["player_name", "wins", "ties", "losses", "total_games", "percentage_loss_ratio"]]
        df = df.to_string(index=False)
        return df


    def get_move(self, game):
        """The player inputs a position to place their letter which is
            returned by the method.

        Args:
            game: an instance of the TicTacToe class.

        Raises:
            RangeError: if the user selects a position outside the
                range of 1-9.
            OccupiedError: if the user selects a position that is already occupied.

        Returns:
            int: the position (between 1-9) the player has chosen to move to.
        """
        val = (int(input("Based on the board shown above,"
                  " enter an integer (1-9) to indicate where you would like to go: ")))- 1
        if val not in range(0, 9):
            raise RangeError(val)
        if val not in game.free_positions():
            raise OccupiedError(val)
        return val
    # def update_scores(self, outcome):
    #     """Updates the player's win/tie/loss records.

    #     Increases either the player's total wins, ties or losses by 1
    #     in the player_scores.csv file, depending on the outcome of the
    #     game. Also increases the total games played by one and updates
    #     the percentage_loss_ratio.

    #     Args:
    #         outcome(str): the column title that needs to be updated
    #             to reflect the outcome of the game: either "wins",
    #             "ties", or "losses".

    #     Returns:
    #         dataframe: a dataframe showing the updated
    #             player_score.csv file.
    #     """
    #     df = pd.read_csv("player_scores.csv")
    #     df.loc[df["player_name"] == self.username, [outcome, "total_games"]] += 1
    #     df["percentage_loss_ratio"] = df["losses"] / df["total_games"]
    #     pd.options.display.float_format = "{:.2%}".format
    #     df.to_csv("player_scores.csv", index=False)
    #     return df


class EasyComputerPlayer(Player):
    """A class used to represent the easy computer player."""
    def get_move(self, game):
        """Randomly returns a free position on the board to position
        the player's letter.

        Args:
            game(any): an instance of the TicTacToe class.

        Returns:
            int: the position (between 0-8) the computer will place
                their marker.
       """
        position = choice(game.free_positions())
        return position


class ExpertComputerPlayer(Player):
    """A class used to represent an Expert Computer Player."""
    def get_move(self, game):
        """Returns the optimal position on the board to place the
        player's letter.

        If all the positions on the board are free it will return a
        random corner position. Otherwise it invokes a recursive
        minimax function to return the optimal position based on which
        position has the highest utility score.

        Args:
            game(any): an instance of the TicTacToe class.

        Returns:
            int: the position (between 0-8) which is either a randomly
                selected corner or the position with the highest
                utility score.
        """
        if len(game.free_positions()) == 9:
            return choice([0, 2, 6, 8])
        return self.minimax(game, True)["position"]

    def minimax(self, state, is_maximising):
        """A recursive minimax method used to return a utility score
        for each possible position.

        The minimax method will continue until one of the following
        terminal conditions are met:
            1. The maximising player wins:
                Returns:
                    dict: showing the position previously determined
                        through recursion and a score of 1 * (the
                        number of empty squares remaining + 1).
            2. The minimising player wins:
                Returns:
                    dict: showing the position previously determined
                        through recursion and a score of -1 * (the
                        number of empty squares remaining + 1).
            3. There are no positions left on the board:
                Returns:
                    dict: showing the position previously determined
                        through recursion and a score of 0
        Assumes that the minimising player is also playing optimally.

        Args:
            state(any): an instance of the TicTacToe class
                shows the current board state in that simulation.
            is_maximising(bool): indicates if it is the maximiser's turn in the simulation.
               when it is the maximiser's turn they are playing to get the highest utility score.
               when it is the minimiser's turn they are playing to get the lowest utility score.

        Returns:
            dict: showing the position (with an int value between 0-8)
                and score (an int value) see terminal conditions above.
        """
        maximising_letter = self.letter
        minimising_letter = "X" if maximising_letter == "O" else "O"
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

        # When it is the maximisor's turn they are playing to get the
        # highest utility score.
        if is_maximising:
            best_move = {"position": None, "score": -500}
            # Loop through all free moves remaining.
            for possible_move in (state.free_positions()):
                state.make_move(possible_move, maximising_letter)
                # Method calls itself to test that move.
                sim_score = self.minimax(state, False)
                # The board is then returned to it's original position
                state.board[possible_move] = " "
                state.current_winner = None
                sim_score["position"] = possible_move
                if sim_score["score"] > best_move["score"]:
                    best_move = sim_score
            return best_move
        # When it is the minimisor's turn in the simulation the
        # following code will be executed:
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
        