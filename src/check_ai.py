"""A test run to check the accuracy of the ExpertComputerPlayer AI.

This will set up a game where an instance of the ExpertComputerPlayer
will play against an instance of the RandomComputerPlayer.  This is
used to check that the get_move() method and the minimax() method of
the ExpertComputerPlayer are working properly. The term "check" is used
instead of "test" as this is not a test run through pytest.  If it runs
successfully the ExpertComputerPlayer will win or tie all games.

Test Limitations: The minimax algorithm is written assuming that the
minimising player will play optimally.  The random player will chose
randomly rather than playing to win. This part of the algorithm will
not be able to be tested here.

Functions:
    check_updates_scores()-Reads and updates player's scores in a
        separate csv file.
    game_testing_ai()-Sets up a simulation game between two players
        and calls the check_updates_scores() function to update
        the results of the game to a separate csv file.
"""
from random import choice
import pandas as pd
from main import EasyComputerPlayer, ExpertComputerPlayer, TicTacToeBoard

def check_update_scores(outcome, player):
    """Reads and updates player's scores in a separate csv file.

    This will update the player's scores based on the outcome of the
    game. It will increase either their win, loss, or tie tally,
    increase their total games played and update their overall
    percentage_loss_ratio.

    Args:
        outcome (str): The outcome (win, loss, or tie) of the game
            played in the simulation this indicates which column in the
            df should be increased by 1.
        player (any): an instance of either the ExpertComputerPlayer or the
            EasyComputerPlayer depending on which score is being
            updated.
    """
    df = pd.read_csv("check_ai_results.csv")
    df.loc[df["player_name"] == player.name, [outcome, "total_games"]] += 1
    df["percentage_loss_ratio"] = df["loss"] / df["total_games"]
    pd.options.display.float_format = "{:.2%}".format
    df.to_csv("check_ai_results.csv", index=False)


def game_testing_ai(game, x_player, o_player):
    """Sets up a simulation game between two players and updates the
    results of the game to a separate csv file.

    Args:
        game(any): An instance of the TicTacToeBoard class.
        x_player(any): an instance of either the ExpertComputerPlayer or the
                EasyComputerPlayer
        o_player(any): an instance of either the ExpertComputerPlayer or the
                EasyComputerPlayer

    """
    standard_board.reset_board()
    turn = choice([x_player.name, o_player.name])
    while game.free_positions():
        if turn == x_player.name:
            position = x_player.get_move(game)
            game.make_move(position, "X")
            if game.current_winner:
                check_update_scores("win", x_player)
                check_update_scores("loss", o_player)
                break
            turn = o_player.name
            continue
        if turn == o_player.name:
            position = o_player.get_move(game)
            game.make_move(position, "O")
            if game.current_winner:
                check_update_scores("win", o_player)
                check_update_scores("loss", x_player)
                break
            turn = x_player.name
            continue
    else:
        check_update_scores("tie", o_player)
        check_update_scores("tie", x_player)

standard_board = TicTacToeBoard()
katie_koala = EasyComputerPlayer("O", "Katie the Koala")
ollie_octopus = ExpertComputerPlayer("O", "Ollie the Octopus")

for i in range(100):
    game_testing_ai(standard_board, katie_koala, ollie_octopus)

df = pd.read_csv("check_ai_results.csv")
print(df)
