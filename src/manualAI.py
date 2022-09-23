from main import EasyComputerPlayer, ExpertComputerPlayer, TicTacToe

def testing_ai(game, x_player, o_player):
    while game.free_positions():
        if turn == x_player.name:
            position = x_player.get_move(game)
            game.make_move(position, "X")
            game.print_board()
            if game.current_winner:
                print(x_player.name, "wins")
                print(x_player.update_scores("wins"))
                print(o_player.update_scores("losses"))
                break
            turn = o_player.name
            continue
        elif turn == o_player.name:
            position = o_player.get_move(game)
            game.make_move(position, "O")
            game.print_board()
            if game.current_winner:
                print(f"Better luck next time! {o_player.name} won the game this time.")
                print(o_player.update_scores("wins"))
                break
            turn = x_player.name
            continue
    else:
        print("It's a tie!")
        print(o_player.update_scores("ties"))

standard_board = TicTacToe()
katie_koala = EasyComputerPlayer("O", "Katie the Koala")
ollie_octopus = ExpertComputerPlayer("O", "Ollie the Octopus")

testing_ai(standard_board, katie_koala, ollie_octopus)
