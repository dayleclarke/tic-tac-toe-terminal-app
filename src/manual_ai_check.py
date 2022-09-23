from random import choice
import pandas as pd
from main import EasyComputerPlayer, ExpertComputerPlayer, TicTacToe

def check_update_scores(outcome, player):
    df = pd.read_csv("manual_ai_check_results.csv")
    df.loc[df["player_name"] == player.name, [outcome, "total_games"]] += 1
    df["percentage_loss_ratio"] = df["losses"] / df["total_games"]
    pd.options.display.float_format = "{:.2%}".format
    df.to_csv("manual_ai_check_results.csv", index=False)


def testing_ai(game, x_player, o_player):  
    standard_board.reset_board()
    turn = choice([x_player.name, o_player.name])
    while game.free_positions():
        if turn == x_player.name:
            position = x_player.get_move(game)
            game.make_move(position, "X")
            if game.current_winner:
                check_update_scores("wins", x_player)
                check_update_scores("losses", o_player)
                break
            turn = o_player.name
            continue
        elif turn == o_player.name:
            position = o_player.get_move(game)
            game.make_move(position, "O")
            if game.current_winner:
                check_update_scores("wins", o_player)
                check_update_scores("losses", x_player)
                break
            turn = x_player.name
            continue
    else:
        check_update_scores("ties", o_player)
        check_update_scores("ties", x_player)

standard_board = TicTacToe()
katie_koala = EasyComputerPlayer("O", "Katie the Koala")
ollie_octopus = ExpertComputerPlayer("O", "Ollie the Octopus")

for i in range(100):
    testing_ai(standard_board, katie_koala, ollie_octopus)

df = pd.read_csv("manual_ai_check_results.csv")
print(df)


