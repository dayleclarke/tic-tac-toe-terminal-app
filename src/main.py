from random import choice  #Ensure you place any built-in modules first.
import time
import pyfiglet
from simple_term_menu import TerminalMenu
import clearing
import pandas as pd
from players import UserPlayer, EasyComputerPlayer, ExpertComputerPlayer, RangeError, OccupiedError

class TicTacToe:
    def __init__(self):
        self.board = [
            " " for i in range(9)
        ]  # we will use a singe list to rep 3x3 board
        self.current_winner = None  # Keep track of the winner

    @staticmethod
    def board_number_indices():
        # 0 | 1 | 2 | (this tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        print("-------------")
        for row in number_board:
            print("| " + " | ".join(row) + " |")
        print("-------------\n")

    def print_board(self):
        # The calaculates the rows
        print("-------------")
        for row in [
            self.board[i * 3 : (i + 1) * 3] for i in range(3)
        ]:  # If time try and change this to match the num pad on the key board.
            print("| " + " | ".join(row) + " |")
        print("-------------")

    def free_positions(self):
        return [
            i for i, position in enumerate(self.board) if position == " "
        ]  # List comprehension outlining all the free spots available on the board.

    def empty_squares(self,):  
    # This will return true if there are empty squares on the board. False means all the positions are taken.
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, position, letter):
        if self.board[position] == " ":
            self.board[position] = letter
            if self.winner(position, letter):
                self.current_winner = letter

    def test_move(self, possible_move, player_letter):
        if self.board[possible_move] == " ":
            self.board[possible_move] = player_letter
        if self.winner(possible_move, player_letter):
            return True
        else:
            return False

    def winner(self, position, letter):
        # winner if 3 in a row anywhere. Must check row, column and both diagonals
        # row check
        row_index = (
            position // 3
        )  # how many times is the position index divisable by 3?  This will indicate its row (either 0, 1 or 2).
        row = self.board[
            row_index * 3 : (row_index + 1) * 3
        ]  # This selects the entire row that the position is in.
        if all([square == letter for square in row]):
            return True

        # column check
        col_index = (
            position % 3
        )  # When you divide the position by 3 what is left over? (Position modu 3 will indicate its column index (either 0, 1 or 2))
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all([square == letter for square in column]):
            return True

        # diagonal check
        # diagonals left to right are on (0, 4, 8)
        # diagonals right to left are on (2, 4, 6)
        if position % 2 == 0:  # Only even numbers run along the diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([square == letter for square in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([square == letter for square in diagonal2]):
                return True

        # If all checks fail there is no winner return False
        return False

    def reset_board(self):
        self.board = [
            " " for i in range(9)
        ]  # we will use a singe list to rep 3x3 board
        self.current_winner = None

def select_opponent():
    """Collects user input and returns the opponent they have selected to play against."""
    print(
"""Lots of players are around today who would love to play Tic-Tac-Toe with you.
They each have different skill levels and experience.
Here is a table outlining some info about each player including their win and loss history:\n"""
        )
    time.sleep(0.8)
    df = pd.read_csv("player_scores.csv")
    pd.options.display.float_format = "{:.2%}".format
    print(df,"\n")
    print(
        "To help select the correct player for you, what difficulty level would you like"
        " to play on? \nMenu entries can be selected with the arrow or j/k keys.\n"
        )
    difficulty_options= ["easy mode", "expert mode"]
    difficulty_terminal_menu = TerminalMenu(difficulty_options, title="Game difficulty level:")
    difficulty_entry_index = difficulty_terminal_menu.show()
    user_difficulty = difficulty_options[difficulty_entry_index]
    print(f"You have chosen to play on {user_difficulty}.")
    time.sleep(0.8)

    if user_difficulty == "easy mode":
        print("There are two players who I recommend you challenge to a game.\n")
        print(
            f"Firstly there is the {df.at[0,'personality']} {df.at[0,'player_name']}. "
            f"He has won {df.at[0,'wins']} games out of {df.at[0,'total_games']} and"
            " has still not discovered a reliable strategy to win.\n"
            )
        print(
            f"Secondly there is {df.at[1,'player_name']}. "
            f"She is {df.at[0,'personality']} but is too focused on eating "
            "eucalyptus leaves to focus long enough to consistently win. "
            f"She has won {df.at[0,'wins']} games out of {df.at[0,'total_games']}.\n"
            )
        print(
            "You can select any player that you like but if you wish to play on easy "
            "mode those are the two I recommend.\n"
            )
    elif user_difficulty == "expert mode":
        print("There are two players who I recommend you challenge to a game.\n")
        print(
            f"Firstly there is the {df.at[2,'personality']} {df.at[2,'player_name']}. "
            "He is currently undefeated having never lost a game. He he has won "
            f"{df.at[0,'wins']} games out of {df.at[0,'total_games']}."
            )
        print(
            f"Secondly there is {df.at[1,'player_name']}. "
            f"She is {df.at[0,'personality']} and also remains undefeated. "
            f"She has won {df.at[0,'wins']} games out of {df.at[0,'total_games']}.\n"
            )
        print(
            "You can select any player that you like but if you wish to play on expert "
            "mode those are the two I recommend to appropriately test your abilities.\n"
            )

    opponent_options= [
        "Pete the Panda (easy mode)",
        "Katie the Koala (easy mode)",
        "Ollie the Octopus (expert Mode)",
        "Danni the Dolphin (expert Mode)",
        ]
    print("Menu entries can be selected with the arrow or j/k keys.\n")
    opponent_terminal_menu = TerminalMenu(
            opponent_options, title = "Which character would you like to play with today?:"
            )
    opponent_entry_index = opponent_terminal_menu.show()
    opponent_player = opponent_options[opponent_entry_index]
    opponent_player = opponent_player.split()[0]

    if opponent_player == "Pete":
        print(
            """⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣦⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⠟⠋⠉⠀⠀⠀⠀⠉⠑⠢⣄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣦⡀
⠀⣀⠀⠀⢀⡏⠀⢀⣴⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⠇
⣾⣿⣿⣦⣼⡀⠀⢺⣿⣿⡿⠃⠀⠀⠀⠀⣠⣤⣄⠀⠀⠈⡿⠋⠀
⢿⣿⣿⣿⣿⣇⠀⠤⠌⠁⠀⡀⢲⡶⠄⢸⣏⣿⣿⠀⠀⠀⡇⠀⠀
⠈⢿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠈⠉⠓⠂⠀⠙⠛⠛⠠⠀⡸⠁⠀⠀
⠀⠀⠻⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⠀⠀⠀⠀⠑⠀⣠⠞⠁⠀⠀⠀
⠀⠀⠀⢸⡏⠉⠛⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⢿⣿⣿⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⡀⠀⠀⠀
⠀⠀⠀⢸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⢸⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠻⠿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣶⠶⠤⠤⢤⣶⣾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠹⣿⣿⣿⠏⠀⠀⠀⠈⢿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
        )
        print(pyfiglet.figlet_format("Pete the Panda", font="digital"))
        return pete_panda
    if opponent_player == "Katie":
        print(
            """
⢀⠔⠊⠉⠑⢄⠀⠀⣀⣀⠤⠤⠤⢀⣀⠀⠀⣀⠔⠋⠉⠒⡄⠀
⡎⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠘⡄
⣧⢢⠀⠀⠀⠀⠀⠀⠀⠀⣀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣆⡗
⠘⡇⠀⢀⠆⠀⠀⣀⠀⢰⣿⣿⣧⠀⢀⡀⠀⠀⠘⡆⠀⠈⡏⠀
⠀⠑⠤⡜⠀⠀⠈⠋⠀⢸⣿⣿⣿⠀⠈⠃⠀⠀⠀⠸⡤⠜⠀⠀
⠀⠀⠀⣇⠀⠀⠀⠀⠀⠢⣉⢏⣡⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀
⠀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢨⠃⠀⢀⠀⢀⠔⡆⠀⠀⠀⠀⠻⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡎⠀⠀⠧⠬⢾⠊⠀⠀⢀⡇⠀⠀⠟⢆⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡇⠀⠀⡞⠀⠀⢣⣀⡠⠊⠀⠀⠀⢸⠈⣆⡀⠀⠀
⠀⠀⡠⠒⢸⠀⠀⠀⡇⡠⢤⣯⠅⠀⠀⠀⢀⡴⠃⠀⢸⠘⢤⠀
⠀⢰⠁⠀⢸⠀⠀⠀⣿⠁⠀⠙⡟⠒⠒⠉⠀⠀⠀⠀⠀⡇⡎⠀
⠀⠘⣄⠀⠸⡆⠀⠀⣿⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⢀⠟⠁⠀
⠀⠀⠘⠦⣀⣷⣀⡼⠽⢦⡀⠀⠀⢀⣀⣀⣀⠤⠄⠒⠁⠀⠀⠀
"""
        )
        print(pyfiglet.figlet_format("Katie the Koala", font="digital"))
        return katie_koala
    if opponent_player == "Ollie":
        print("""
                        ___
                     .-'   `'.
                    /         \\ 
                    |         ;
                    |         |           ___.--,
           _.._     |0) ~ (0) |    _.---'`__.-( (_.
    __.--'`_.. '.__.\\    '     \\_.-' ,.--'`     `""`
   ( ,.--'`   ',__ /./;   ;, '.__.'`    __
   _`) )  .---.__.' / |   |\\   \\__..--""  ""--.,_
  `---' .'.''-._.-'`_./  /\\ '.  \\ _.-~~~````~~~-._`-.__.'
        | |  .' _.-' |  |  \\  \\  '.               `~---`
         \\ \\/ .'     \\  \\   '. '-._)
          \\/ /        \\  \\    `=.__`~-.
          / /\\         `) )    / / `"".`
    , _.-'.'\\ \\        / /    ( (     / /
     `--~`   ) )    .-'.'      '.'.  | (
            (/`    ( (`          ) )  '-;
             `      '-;         (-'
        """
        )
        print(pyfiglet.figlet_format("Ollie the Octopus", font="digital"))
        return ollie_octopus
    print(
            """
⠀⠀⠀⠐⢿⣿⣿⣿⣿⣿⣶⣤⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠟⠃
⠀⠀⢸⣿⣿⣿⣿⡿⠛⠉⠁⠀⢸⣿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣾⣿⣿⣿⣷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣾⣿⣿⣿⠿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡿⠛⠉⠀⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
        )
    print(pyfiglet.figlet_format("Danni the Doplphin", font="digital"))
    return danni_dolphin

def select_starting_player(user_player, computer_player):
    """Returns the starting player

    A function used to determine the starting player based on the
    outcome of a scissors-paper-rock game.

    Args:
        user_player: an instance of the HumanPlayer class.
        computer_player: an instance of the Player class
            based on the opponent previously selected by the user.

    Returns:
        the starting player which will either be the user player or the
            computer player depending on who won scissors-paper-rock.
    """
    hand_gestures = {
        "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
        "paper": """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
        "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
}
    print("We will begin by playing scissors-paper-rock to determine which player will start.")

    while True:
        print("Menu entries can be selected with the arrow or j/k keys.")
        gesture_options = list(hand_gestures.keys())
        gesture_terminal_menu = TerminalMenu(
            gesture_options,
            title="Please select one of the following hand gestures:")
        gesture_entry_index = gesture_terminal_menu.show()
        user_choice = gesture_options[gesture_entry_index]
        print(hand_gestures[user_choice])
        print(f"{user_player} has chosen to play {user_choice}.")
        time.sleep(0.8)
        opponent_choice = choice(list(hand_gestures.keys()))
        time.sleep(0.8)
        print(hand_gestures[opponent_choice])
        print(f"{computer_player} has chosen to play {opponent_choice}.")
        time.sleep(0.8)
        if user_choice == opponent_choice:
            print(pyfiglet.figlet_format("Draw!"))
            print(
                f"Great minds think alike! You both selected {user_choice}. Please select again."
            )
            continue
        break

    if user_choice == "paper":
        if opponent_choice == "scissors":
            print(pyfiglet.figlet_format("Defeat!"))
            print(
                f"{computer_player}'s scissors cuts {user_player}'s paper. "
                f"{computer_player} wins and will go first!"
                )
            return computer_player
        print(pyfiglet.figlet_format("You Win!"))
        print(
            f"{user_player}'s paper covers {computer_player}'s scissors. "
            f"{user_player} wins and will go first!"
            )
        return user_player

    if user_choice == "scissors":
        if opponent_choice == "paper":
            print(pyfiglet.figlet_format("You Win!"))
            print(
                f"{user_player}'s scissors cuts {computer_player}'s paper. "
                f"{user_player} wins and will go first!"
                )
            return user_player
        print(pyfiglet.figlet_format("Defeat!"))
        print(
            f"{computer_player}'s rock crushes {user_player}'s scissors. "
            f"{computer_player} wins and will go first!"
            )
        return computer_player

    if user_choice == "rock":
        if opponent_choice == "paper":
            print(pyfiglet.figlet_format("Defeat!"))
            print(
                f"{computer_player}'s paper covers {user_player}'s rock. "
                f"{computer_player} wins and will go first!"
                )
            return computer_player
        print(pyfiglet.figlet_format("Victory!"))
        print(
            f"{user_player}'s rock crushes {computer_player}'s scissors. "
            f"{user_player} wins and will go first!"
            )
        return user_player


def play(game, x_player, o_player):
    turn = select_starting_player(user_player_1.name, opponent.name)
    print("Our game will be played on a 3 by 3 board using the following positions.\n")
    standard_board.board_number_indices()
    print("Commencing game....")
    # Add in option here to play scissor, paper rock to decide who goes first.
    while game.free_positions():
        if turn == x_player.name:
            while True:
                try:
                    position = x_player.get_move(game)
                    break
                    # val = int(
                    #     input("Based on the board shown above,"
                    #           " enter an integer (0-8) to indicate where you would like to go: "))
                    # if val not in range(0, 9):
                    #     raise RangeError(val)
                    # if val not in game.free_positions():
                    #     raise OccupiedError(val)
                    # return val
                except RangeError as err:
                    print(err)
                except OccupiedError as err:
                    print(err)
                except ValueError:
                    print("That isn't a valid integer. Please enter a number with no decimal places.")

            
            game.make_move(position, "X")
            print(f"{x_player.name} makes a move to position {position}")
            game.print_board()
            if game.current_winner:
                print("Congratulations!!!")
                print(pyfiglet.figlet_format("You Win!"))
                print(
                    """
                                   .''.
       .''.      .        *''*    :_\\/_:     .
      :_\\/_:   _\\(/_  .:.*_\\/_*   : /\\ :  .'.:.'.
  .''.: /\\ :   ./)\\   ':'* /\\ * :  '..'.  -=:o:=-
 :_\\/_:'.:::.    ' *''*    * '.\'/.' _\\(/_'.':'.'
 : /\\ : :::::     *_\\/_*     -= o =-  /)\\    '  *
  '..'  ':::'     * /\\ *     .'/.\\'.   '
      *            *..*         :
        *
        """)
                print(o_player.update_scores("losses"))
                break
            turn = o_player.name
            continue
        elif turn == o_player.name:
            time.sleep(1)
            position = o_player.get_move(game)
            game.make_move(position, "O")
            print(f"{o_player.name} makes a move to position {position}")
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



if __name__ == "__main__":
    clearing.clear()
    pete_panda = EasyComputerPlayer("O", "Pete the Panda")
    katie_koala = EasyComputerPlayer("O", "Katie the Koala")
    ollie_octopus = ExpertComputerPlayer("O", "Ollie the Octopus")
    danni_dolphin = ExpertComputerPlayer("O", "Danni the Dolphin")
    standard_board = TicTacToe()
    print("Welcome to ...\n")
    print(pyfiglet.figlet_format("Tic Tac Toe"))
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    while True:
        player_name = input("What is your name?: ")
        print(
            "Hello "
            + player_name.title()
            + "! So lovely to meet you. That's a great name. "
            "Can you please confirm I have your name spelt correctly? "
            "Menu entries can be selected with the arrow or j/k keys.\n"
            )
        user_options= [f"Yes, my name is {player_name.title()}",
                        "No, I wish to enter my name again."]
        terminal_menu = TerminalMenu(user_options)
        menu_entry_index = terminal_menu.show()
        name_confirmation = user_options[menu_entry_index]
        print("This is your", name_confirmation)
        if name_confirmation == "No, I wish to enter my name again.":
            continue
        break
    print("Thank you for confirming that for me. I would hate to call you by the wrong name.")
    time.sleep(0.8)
    user_player_1 = UserPlayer("X", player_name)

    while True:
        standard_board.reset_board()  # Resets the board to commence a new game
        opponent = select_opponent()  # User selects difficulty level and choses an
        print(
            f"You have selected {opponent.name} as your opponent today.  Good choice."
        )
        play(standard_board, user_player_1, opponent)
        play_again = input(
            "Thanks for playing today. Would you like to play again? (yes/no): "
        )
        if play_again.lower().strip().startswith("y"):
            continue
        break
