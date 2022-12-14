from random import choice
import time
import pandas as pd
import pyfiglet
from simple_term_menu import TerminalMenu
import clearing
from colorama import init, deinit, Fore
from players import UserPlayer, EasyComputerPlayer, ExpertComputerPlayer
from custom_exceptions import RangeError, OccupiedError
from login import login, name_confirmation
from board import TicTacToeBoard
from asciiart import PANDA_IMG, KOALA_IMG, OCTOPUS_IMG, DOLPHIN_IMG, FIREWORKS_IMG, HAND_GESTURES


def select_difficulty():
    """Collects user input and returns the diffiuclty level they wish to play on"""
    print(Fore.CYAN +
        "To help select the correct player for you, what difficulty level would you like"
        " to play on?")
    print("Menu entries can be selected with the arrow or j/k keys.\n")
    difficulty_options = ["Easy Mode", "Expert Mode"]
    difficulty_terminal_menu = TerminalMenu(difficulty_options, title="Game difficulty level:")
    difficulty_entry_index = difficulty_terminal_menu.show()
    user_difficulty = difficulty_options[difficulty_entry_index]
    print(f"You have chosen to play on {Fore.CYAN}{user_difficulty}.")
    return user_difficulty


def select_opponent():
    """Collects user input and returns the opponent they have selected
    to play against."""
    print(Fore.CYAN +"\nSelect Your Opponent")
    print(
"""Lots of players are around today who would love to play Tic-Tac-Toe with you.
They each have different skill levels and experience.
Here is a table outlining info about each player including their win, tie, and loss history:
"""
        )
    print(Fore.CYAN + pyfiglet.figlet_format("Opponent Player Information", font="digital"))
    df = pd.read_csv("player_scores.csv")
    df_computer_players = df.head(4)
    pd.options.display.float_format = "{:.2%}".format
    print(df_computer_players.to_string(index=False),"\n")
    user_difficulty = select_difficulty()

    if user_difficulty == "Easy Mode":
        print("There are two players who I recommend you challenge to a game.\n")
        print(
            f"Firstly there is the {df.at[0,'personality']} "
            f"{Fore.CYAN}{df.at[0,'player_name']}{Fore.WHITE}. \n"
            f"He has won {df.at[0,'wins']} games out of {df.at[0,'total_games']} and"
            " has still not discovered a reliable strategy to win.\n"
            )
        print(
            f"Secondly there is {Fore.CYAN}{df.at[1,'player_name']}{Fore.WHITE}. \n"
            f"She is {df.at[0,'personality']} but is too busy eating "
            "eucalyptus leaves to focus long enough to consistently win. \n"
            f"She has won {df.at[0,'wins']} games out of {df.at[0,'total_games']}.\n"
            )
        print(Fore.CYAN +
            "You can select any player you like but if you wish to play on easy "
            "mode those are the two I recommend.\n"
            )
    elif user_difficulty == "Expert Mode":
        print("There are two players I recommend you challenge to a game.\n")
        print(
            f"Firstly there is the {df.at[2,'personality']}{Fore.CYAN} "
            f"{df.at[2,'player_name']}{Fore.WHITE}. "
            "He is currently undefeated having never lost a game. He has won "
            f"{df.at[0,'wins']} games out of {df.at[0,'total_games']}."
            )
        print(
            f"Secondly there is {Fore.CYAN}{df.at[3,'player_name']}{Fore.WHITE}. "
            f"She is {df.at[3,'personality']} and also remains undefeated. "
            f"She has won {df.at[3,'wins']} games out of {df.at[3,'total_games']}.\n"
            )
        print(Fore.CYAN +
            "You can select any player that you like but if you wish to play on expert "
            "mode those are the two I recommend to appropriately test your abilities.\n"
            )

    opponent_options = [
        "Pete the Panda (easy mode)",
        "Katie the Koala (easy mode)",
        "Ollie the Octopus (expert mode)",
        "Danni the Dolphin (expert mode)",
        ]
    print("Menu entries can be selected with the arrow or j/k keys.\n")
    opponent_terminal_menu = TerminalMenu(
            opponent_options, title = "Which character would you like to play with today?:"
            )
    opponent_entry_index = opponent_terminal_menu.show()
    opponent_name = opponent_options[opponent_entry_index]
    opponent_name = opponent_name.split()[0]

    if opponent_name == "Pete":
        print(PANDA_IMG)
        print(Fore.CYAN + pyfiglet.figlet_format("Pete the Panda", font="digital"))
        pete_panda = EasyComputerPlayer("O", "Pete the Panda")
        opponent_player = pete_panda
    elif opponent_name == "Katie":
        print(KOALA_IMG)
        print(Fore.CYAN + pyfiglet.figlet_format("Katie the Koala", font="digital"))
        katie_koala = EasyComputerPlayer("O", "Katie the Koala")
        opponent_player = katie_koala
    elif opponent_name == "Ollie":
        print(OCTOPUS_IMG)
        print(Fore.CYAN + pyfiglet.figlet_format("Ollie the Octopus", font="digital"))
        ollie_octopus = ExpertComputerPlayer("O", "Ollie the Octopus")
        opponent_player = ollie_octopus
    else:
        print(DOLPHIN_IMG)
        print(Fore.CYAN + pyfiglet.figlet_format("Danni the Doplphin", font="digital"))
        danni_dolphin = ExpertComputerPlayer("O", "Danni the Dolphin")
        opponent_player = danni_dolphin
    print(
        f"You have selected {opponent_player.name} as your opponent today.  Good choice."
        )
    return opponent_player


def select_starting_player(user_player, computer_player):
    """Returns the starting player based on the outcome of a
    scissors-paper-rock game.

    Args:
        user_player: an instance of the HumanPlayer class.
        computer_player: an instance of the Player class
            based on the opponent previously selected by the user.

    Returns:
        the starting player which will either be the user player or the
            computer player depending on who won scissors-paper-rock.
    """
    print(Fore.CYAN + "We will begin by playing scissors-paper-rock to "
    "determine which player will start.")
    while True:
        print("Menu entries can be selected with the arrow or j/k keys.")
        gesture_options = list(HAND_GESTURES.keys())
        gesture_terminal_menu = TerminalMenu(
            gesture_options,
            title="Please select one of the following hand gestures:")
        gesture_entry_index = gesture_terminal_menu.show()
        user_choice = gesture_options[gesture_entry_index]
        print(Fore.CYAN + HAND_GESTURES[user_choice])
        print(f"{user_player} has chosen to play {user_choice}.")
        time.sleep(0.8)
        opponent_choice = choice(list(HAND_GESTURES.keys()))
        time.sleep(0.8)
        print(Fore.CYAN + HAND_GESTURES[opponent_choice])
        print(f"{computer_player} has chosen to play {opponent_choice}.")
        time.sleep(0.8)
        if user_choice == opponent_choice:
            print(Fore.CYAN + pyfiglet.figlet_format("Draw!"))
            print(
                f"Great minds think alike! You both selected {user_choice}. Please select again."
            )
            continue
        break

    if user_choice == "paper":
        if opponent_choice == "scissors":
            print(Fore.CYAN + pyfiglet.figlet_format("Defeat!"))
            print(
                f"{computer_player}'s scissors cuts {user_player}'s paper. "
                f"{computer_player} wins and will go first!"
                )
            starting_player = computer_player
        else:
            print(Fore.CYAN + pyfiglet.figlet_format("You Win!"))
            print(
                f"{user_player}'s paper covers {computer_player}'s scissors. "
                f"{user_player} wins and will go first!"
                )
            starting_player = user_player

    elif user_choice == "scissors":
        if opponent_choice == "paper":
            print(Fore.CYAN + pyfiglet.figlet_format("You Win!"))
            print(
                f"{user_player}'s scissors cuts {computer_player}'s paper. "
                f"{user_player} wins and will go first!"
                )
            starting_player = user_player
        else:
            print(Fore.CYAN + pyfiglet.figlet_format("Defeat!"))
            print(
                f"{computer_player}'s rock crushes {user_player}'s scissors. "
                f"{computer_player} wins and will go first!"
                )
            starting_player = computer_player

    elif user_choice == "rock":
        if opponent_choice == "paper":
            print(Fore.CYAN + pyfiglet.figlet_format("Defeat!"))
            print(
                f"{computer_player}'s paper covers {user_player}'s rock. "
                f"{computer_player} wins and will go first!"
                )
            starting_player = computer_player
        else:
            print(Fore.CYAN + pyfiglet.figlet_format("Victory!"))
            print(
                f"{user_player}'s rock crushes {computer_player}'s scissors. "
                f"{user_player} wins and will go first!"
                )
            starting_player = user_player
    return starting_player

def clear_screen(game, x_player, o_player):
    clearing.clear()
    print(Fore.CYAN + pyfiglet.figlet_format("Tic Tac Toe"))
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    print(Fore.CYAN +f"{x_player.name} vs. {o_player.name}\n")
    standard_board.board_number_indices()
    game.print_board()


def play(game, x_player, o_player):
    """A function used to play one complete game of TicTacToe.

    This function calls the select_starting_player() function to
    determine which player will go first. While there are free
    positions on the board players will alternate turns and placing
    their marker in one of the 9 positions on the board. The game will
    continue until a player places 3 markers in a row
    horizontally, vertically or diagonally or the board fills up.
    The win status is checked in the make_method() after each player
    places their marker. Instructions are printed to the terminal to
    guide the user how to place the game.

    At the end of the game the outcome is printed to the terminal and
    both player's score history is updated in a seperate player_scores
    csv file.

    Args:
        game: an instance of the TicTacToeBoard class.
        x_player: an instance of the HumanPlayer class.
        o_player: an instance of the Player class.
            based on the opponent previously selected by the user.
    """
    # Envoke function to determine which player will go first based on
    # a scissors-paper-rock game.

    turn = select_starting_player(user_player_1.name, opponent.name)
    print("Our game will be played on a 3 by 3 board based on the following positions:\n")
    standard_board.board_number_indices()
    input("Press the ENTER key when you are ready to begin.")
    # Game play will continue while there are free positions remaining
    while game.free_positions():
        clear_screen(game, x_player, o_player)
        if turn == x_player.name: # if it is player x's turn then:
            while True:
                try:
                    position = x_player.get_move(game)
                    break
                except RangeError as err:
                    print(err)
                except OccupiedError as err:
                    print(err)
                except ValueError:
                    print("That isn't a valid integer."
                    " Please enter a number with no decimal places.")
            game.make_move(position, "X")
            if game.current_winner: # If that move made the X player the winner then:
                clear_screen(game, x_player, o_player)
                print("Congratulations!!!")
                print(Fore.CYAN + pyfiglet.figlet_format("You Win!"))
                print(Fore.CYAN + FIREWORKS_IMG)
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
                # Update the opponent's scores in the player_scores.csv file.
                o_player.update_scores("losses")
                print(Fore.CYAN + pyfiglet.figlet_format("Top 10 Players", font="digital"))
                # Update the user player's scores in the player_scores.csv file.
                print(x_player.update_scores("wins"))
                break
            # Swap the player whose turn it currently is to the "O" player.
            turn = o_player.name
            continue
        if turn == o_player.name:
            position = o_player.get_move(game)
            time.sleep(1.5)
            game.make_move(position, "O")              
            if game.current_winner:
                clear_screen(game, x_player, o_player)
                print(f"Better luck next time! {o_player.name} won the game.\n")
                o_player.update_scores("wins")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
                print(Fore.CYAN + pyfiglet.figlet_format("Top 10 Players", font="digital"))
                print(x_player.update_scores("losses"))
                break
            turn = x_player.name
            continue
    else:
        clear_screen(game, x_player, o_player)
        print(Fore.CYAN + "It's a tie!")
        o_player.update_scores("ties")
        print(Fore.CYAN + pyfiglet.figlet_format("Top 10 Players", font="digital"))
        print(x_player.update_scores("ties"))


if __name__ == "__main__":
    clearing.clear()
    init(autoreset=True)
    standard_board = TicTacToeBoard()
    print("Welcome to ...\n")
    print(Fore.CYAN + pyfiglet.figlet_format("Tic Tac Toe"))
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")

    print(Fore.CYAN + "How would you like to begin today?\n")
    print("Menu entries can be selected with the arrow or j/k keys.\n")
    user_details = login()
    player_name = name_confirmation()
    user_player_1 = UserPlayer("X", player_name, user_details["username"])

    while True:
        standard_board.reset_board()  # Resets the board to commence a new game
        opponent = select_opponent()  # User selects difficulty level and choses an opponent
        play(standard_board, user_player_1, opponent)
        play_again = input(Fore.CYAN +
            "\nThanks for playing today. Would you like to play again? (yes/no): "
        )
        if play_again.lower().strip().startswith("y"):
            continue
        deinit()
        break
